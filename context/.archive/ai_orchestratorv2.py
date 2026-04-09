#!/usr/bin/env python3
"""
Single-Agent JSON Pipeline (Local Ollama / Gemma 4 Edition)
===========================================================
Prompt inputs are limited to schema paths under ``product_data`` (see
``PROMPT_INPUT_SOURCES``). Optional ``text.specifications`` is passed verbatim
as canonical facts; ``filters.filter_options`` is secondary (purchase choices).

``load_output_file`` passes the inner ``product_data`` dict — paths are
``core.*``, ``text.*``, ``filters.*`` (not ``product_data.core.*``).

Usage:
  python ai_orchestratorv2.py --product 10002 --dry-run
  python ai_orchestratorv2.py --limit 100 --concurrency 2
"""
from __future__ import annotations

import argparse
import json
import os
import re
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

try:
    from tqdm import tqdm
except ImportError:
    print("❌ Error: 'tqdm' is required. Run 'pip install tqdm' first.")
    exit(1)

# --- INHERIT LEGACY PARSERS ---
# Note: Ensure these are available in your environment
from step1c_ai_enhance import (
    AI_CONTENT_FOLDER,
    OUTPUT_FOLDER,
    group_spec_sections,
    filter_resource_link_specs,
    merge_parsed_specs_with_ul,
    merge_parsed_specs_append_unique,
    clean_description_html,
    extract_spec_resources_from_html,
    extract_specifications_block_html,
    extract_also_available_html,
    extract_img_tags_from_html,
    extract_available_sizes_section,
    available_sizes_table_to_parsed_specs,
    remove_substrings_once,
    strip_html,
    assemble_verbatim_description_parts,
    ai_content_path,
    load_output_file,
    _pd_compat,
    _pd_get,
    _resolve_focus_keyword,
)

# --- CONFIGURATION ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_CORE = "gemma4:latest"
DIR_REVIEW = Path("output_needs_review")
DIR_REVIEW.mkdir(exist_ok=True)

FORBIDDEN_WORDS = ["amazing", "luxurious", "perfect", "beautiful", "cheap", "stunning", "game-changer"]

GLOBAL_GUIDELINES = """
1. TONE: Authoritative, technical, and plainspoken.
2. NO HYPE: Write like a senior architectural hardware consultant.
3. FORMATTING: Use standard US Inch formatting (e.g., 2-3/8" or 1-1/4").
4. ACCURACY: Rely ONLY on the provided product data. Do not hallucinate features.
5. SOURCE PRIORITY: Keep prose and SEO aligned with the Core identity and Description plain text. When Canonical specifications (verbatim) are present, treat them as authoritative for facts and dimensions. Use Filter options only as secondary context for purchase/configuration choices; do not invent finishes, trims, or keying not implied there.
"""

# Prompt uses only these logical sources (paths relative to the product_data root from output_*.json).
PROMPT_INPUT_SOURCES = """
- product_data.core.sku, product_data.core.title, product_data.core.vendor
- product_data.text.description_html (plain text below: same as v1 — only <p> body copy after removing spec blocks, also-available, sizes, and images)
- product_data.text.seo.keywords
- product_data.filters.filter_options (secondary reference for purchasable choices)
- Optional: product_data.text.specifications — when present, passed verbatim; authoritative for core facts
"""

def _format_verbatim_specifications(specs: list | None) -> str:
    if not specs:
        return ""
    lines = []
    for s in specs:
        if isinstance(s, dict):
            k = str(s.get("key", "")).strip()
            v = str(s.get("value", "")).strip()
            lines.append(f"- {k}: {v}" if k else f"- {v}")
    return "\n".join(lines)


def _format_filter_options(opts: list | None) -> str:
    if not opts:
        return "(none listed)"
    return "\n".join(f"- {line}" for line in opts if str(line).strip())


# --- 🤖 SINGLE AGENT PROMPT & API ---
def call_agent(model, prompt, temperature=0.3):
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": model, 
            "prompt": prompt, 
            "stream": False,
            "format": "json", 
            "options": {
                "temperature": temperature, 
                "num_predict": 1024,
                "num_ctx": 32768
            }
        }, timeout=600)
        response.raise_for_status()
        raw_text = response.json().get('response', '{}').strip()
        return json.loads(raw_text)
    except Exception as e:
        return {"error": str(e), "raw": raw_text if 'raw_text' in locals() else ""}

def build_json_prompt(
    sku: str,
    title: str,
    vendor: str,
    description_plain: str,
    seo_keywords: str,
    filter_options_text: str,
    verbatim_specs_text: str,
) -> str:
    specs_block = verbatim_specs_text.strip() if verbatim_specs_text.strip() else "(not provided — derive facts only from description and filter options; do not invent dimensions.)"
    return f"""<persona>You are a senior door hardware copywriter and technical SEO expert. Your writing is authoritative, highly technical, and plainspoken. You write for architects, contractors, and informed homeowners. Do not use marketing fluff.</persona>

<input_schema>
{PROMPT_INPUT_SOURCES.strip()}
</input_schema>

<global_rules>
{GLOBAL_GUIDELINES.strip()}
</global_rules>

<seo_rules>
1. SEO TITLE: Must strictly follow this format: "[Brand] [Series/Model] [Product Type] - [SKU]". (Maximum 65 characters).
2. SEO DESCRIPTION: Must be 140-160 characters. Must include the main keyword, the SKU, and end with a technical specification or call to action.
3. SEO KEYWORD: Select the most search-relevant, high-intent keyword from the provided list.
</seo_rules>

<json_schema_instructions>
Analyze the product data and output a strictly valid JSON object.
- NO markdown formatting (do not wrap in ```json).
- NO conversational text before or after the JSON.
- DO NOT include HTML tags (like <p> or <br>) in your paragraphs.
- "technical_features" must be split into a short "benefit" and a "detail".

{{
  "prose_paragraphs": [
    "Paragraph 1: Core product introduction, material, and primary function.",
    "Paragraph 2: Technical and installation detail grounded in verbatim specifications (when provided) and description."
  ],
  "technical_features": [
    {{
      "benefit": "Grade 1 Security Rating",
      "detail": "Meets ANSI/BHMA A156.5 standards for maximum residential protection against forced entry."
    }},
    {{
      "benefit": "Adjustable Backset",
      "detail": "Accommodates standard residential door preps of 2-3/8 inch or 2-3/4 inch without modification."
    }}
  ],
  "seo_title": "Kwikset Arlington Double Cylinder Handleset - KWI-801AN",
  "seo_description": "Upgrade your front door with the Kwikset Arlington Double Cylinder Handleset (KWI-801AN). Solid brass, Grade 1 security, adjustable backset.",
  "seo_keyword": "arlington double cylinder handlesets"
}}
</json_schema_instructions>

<product_data>
product_data.core.sku: {sku}
product_data.core.title: {title}
product_data.core.vendor: {vendor}

product_data.text.description_html (plain text from paragraph copy only — specifications / also-available / size sections stripped like ai_orchestratorv1; keep meaning and tone similar):
{description_plain}

product_data.text.seo.keywords:
{seo_keywords}

product_data.filters.filter_options (secondary — purchase/configuration choices; do not contradict verbatim specs when both exist):
{filter_options_text}

product_data.text.specifications (VERBATIM — authoritative core facts when provided; reproduce accurately in prose and features):
{specs_block}
</product_data>

OUTPUT ONLY VALID JSON:"""

def qa_manager_check(prose, title):
    reasons = []
    if len(prose) < 200: reasons.append("Prose too short (under 200 chars).")
    if "<p>" not in prose: reasons.append("Missing <p> tags in prose.")
    prose_lower = prose.lower()
    for word in FORBIDDEN_WORDS:
        if re.search(r'\b' + word + r'\b', prose_lower):
            reasons.append(f"Used forbidden marketing word: '{word}'.")
    title_len = len(title)
    if title_len > 75 or title_len < 30:
        reasons.append(f"SEO Title length out of bounds ({title_len} chars).")
    return reasons


# --- 🚀 PIPELINE EXECUTION ---
def process_product_orchestrator(legacy_id: str, local_data: dict, *, force: bool, dry_run: bool) -> tuple[str, list[str]]:
    out_path = ai_content_path(legacy_id)
    if not force and os.path.exists(out_path):
        return "skipped", []

    # 1. Prepare Data (local_data is the inner product_data object from output_*.json)
    compat = _pd_compat(local_data)
    sku = (_pd_get(local_data, "core.sku", "") or compat.get("sku", "")).strip()
    title = (_pd_get(local_data, "core.title", "") or compat.get("title", "")).strip()
    vendor = (_pd_get(local_data, "core.vendor", "") or compat.get("vendor", "")).strip()
    raw_description_html = _pd_get(local_data, "text.description_html", "") or compat.get("descriptionHtml") or ""
    seo_keywords = _pd_get(local_data, "text.seo.keywords", "") or compat.get("seo_keywords", "")
    description_html = clean_description_html(raw_description_html)
    strip_sizes, _, size_table = extract_available_sizes_section(description_html)
    html_for_prompt = remove_substrings_once(description_html, [
        extract_specifications_block_html(description_html),
        extract_also_available_html(description_html),
        strip_sizes,
    ] + extract_img_tags_from_html(description_html))
    description_plain = strip_html(html_for_prompt)

    filter_options = _pd_get(local_data, "filters.filter_options", default=None)
    if not isinstance(filter_options, list):
        filter_options = []
    filter_options_text = _format_filter_options(filter_options)

    structured_specs = _pd_get(local_data, "text.specifications", default=None)
    if not isinstance(structured_specs, list):
        structured_specs = []
    verbatim_specs_text = _format_verbatim_specifications(structured_specs)

    # Persisted specifications: prefer structured text.specifications; else merge from description HTML
    if len(structured_specs) > 0:
        merged_specs = filter_resource_link_specs(structured_specs)
    else:
        raw_specs = _pd_get(local_data, "text.specifications", default=[]) or []
        parsed_specs = filter_resource_link_specs(compat.get("parsed_specs") or raw_specs)
        table_specs = available_sizes_table_to_parsed_specs(size_table)
        merged_specs = filter_resource_link_specs(merge_parsed_specs_append_unique(
            merge_parsed_specs_with_ul(parsed_specs, description_html), table_specs
        ))

    prompt_json = build_json_prompt(
        sku,
        title,
        vendor,
        description_plain,
        seo_keywords,
        filter_options_text,
        verbatim_specs_text,
    )
    
    if dry_run:
        print(f"\n{'='*50}\n🔍 DRY RUN: PROMPT PIPELINE FOR {sku}\n{'='*50}")
        print(f"\n[AGENT: CORE JSON ({MODEL_CORE})]\n{prompt_json}")
        return "dry_run", []

    try:
        # Phase 1: LLM Generates Raw Data
        llm_data = call_agent(MODEL_CORE, prompt_json, temperature=0.2)
        if "error" in llm_data: raise Exception(f"JSON Generation failed: {llm_data.get('error')}")

        # Phase 2: Python Handles Final Text Transformations
        prose_paragraphs = llm_data.get("prose_paragraphs", [])
        prose_text = "".join([f"<p>{p.strip()}</p>" for p in prose_paragraphs if p.strip()])
        
        features_list = []
        for feat_obj in llm_data.get("technical_features", []):
            benefit = feat_obj.get("benefit", "").strip()
            detail = feat_obj.get("detail", "").strip()
            if benefit and detail:
                features_list.append(f"{benefit}: {detail}")
            elif benefit or detail:
                features_list.append(benefit or detail)
                
        if not features_list:
            raise Exception("LLM returned zero features in JSON array.")

        seo_title_ai = llm_data.get("seo_title", "").strip()
        seo_description_ai = llm_data.get("seo_description", "").strip()
        seo_focus_keyword = llm_data.get("seo_keyword", "").strip()

        # 3. QA Validation
        flag_reasons = qa_manager_check(prose_text, seo_title_ai)

        # 4. Assemble Final Payload
        also_raw = extract_also_available_html(description_html)
        legacy_imgs = extract_img_tags_from_html(description_html)
        final_html = assemble_verbatim_description_parts(prose_text, also_raw, legacy_imgs)
        
        result_json = {
            "schema_version": 2,
            "legacy_product_id": legacy_id,
            "sku": sku,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "model": "gemma4-single-agent-json",
            "description_prose": prose_text,
            "features": features_list,
            "text": {
                 "description_html": final_html,
                 "features": features_list,
                 "seo_title_ai": seo_title_ai,
                 "seo_description_ai": seo_description_ai,
                 "seo_focus_keyword": _resolve_focus_keyword(seo_focus_keyword, seo_keywords),
                 "specifications": merged_specs,
                 "spec_sections": group_spec_sections(merged_specs),
                 "resources": extract_spec_resources_from_html(raw_description_html)
            },
            "text_raw": {
                "description_html_input": raw_description_html,
                "seo_title_input": compat.get("seo_title", ""),
                "seo_description_input": compat.get("seo_description", ""),
                "seo_keywords_input_csv": seo_keywords,
            },
            "parsed_specs": merged_specs,
            "spec_sections": group_spec_sections(merged_specs),
            "resources": extract_spec_resources_from_html(raw_description_html)
        }

        # Save and Route
        if flag_reasons:
            result_json["_review_notes"] = flag_reasons
            target_path = DIR_REVIEW / f"ai_{legacy_id}.json"
            status = "needs_review"
        else:
            os.makedirs(AI_CONTENT_FOLDER, exist_ok=True)
            target_path = Path(AI_CONTENT_FOLDER) / f"ai_{legacy_id}.json"
            status = "success"

        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(result_json, f, indent=2, ensure_ascii=False)
            
        return status, flag_reasons

    except Exception as e:
        return "error", [str(e)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", type=str)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--concurrency", type=int, default=1)
    args = parser.parse_args()

    products = []
    if args.product:
        p = load_output_file(os.path.join(OUTPUT_FOLDER, f"output_{args.product}.json"))
        if p: products.append(p)
    else:
        for fname in sorted(os.listdir(OUTPUT_FOLDER)):
            if fname.startswith("output_") and fname.endswith(".json"):
                products.append(load_output_file(os.path.join(OUTPUT_FOLDER, fname)))
                if args.limit and len(products) >= args.limit: break
    
    products = [p for p in products if p]
    if not products:
        print("❌ No products found.")
        return

    if args.dry_run:
        process_product_orchestrator(products[0][0], products[0][1], force=True, dry_run=True)
        return

    print("🔥 Warming up Gemma 4 model...")
    try:
        requests.post(OLLAMA_URL, json={"model": MODEL_CORE, "prompt": "hi", "keep_alive": "60m"}, timeout=120)
    except Exception as e:
        print(f"⚠️ Failed to warmup model: {e}. Check if Ollama is running.")

    results = {"success": 0, "needs_review": 0, "skipped": 0, "error": 0}
    
    print(f"\n🚀 Starting Single-Agent JSON Orchestration ({len(products)} products, {args.concurrency} workers)")
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futures = {pool.submit(process_product_orchestrator, lid, pdata, force=args.force, dry_run=False): lid for lid, pdata in products}
        
        for future in tqdm(as_completed(futures), total=len(products), desc="Processing"):
            lid = futures[future]
            status, notes = future.result()
            results[status] += 1
            
            if status == "needs_review":
                tqdm.write(f"⚠️  [REVIEW] SKU {lid}: {notes[0]}")
            elif status == "error":
                tqdm.write(f"❌  [ERROR] SKU {lid}: {notes[0]}")

    print(f"\n{'='*40}\n🏁 BATCH COMPLETE\n✅ Approved: {results['success']}\n⚠️ Review:   {results['needs_review']}\n↩️ Skipped:  {results['skipped']}\n❌ Errors:   {results['error']}\n{'='*40}\n")

if __name__ == "__main__":
    main()