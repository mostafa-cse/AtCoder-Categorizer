#!/usr/bin/env python3
"""
Master Synchronizer for AtCoder Categorizer
==========================================
Synchronizes:
1. categories/README.md
2. categories/dp/README.md
3. state/progress.json
4. Audits consistency across analysis/, categories/, SELECTION_LOG.md, and QUALITY_PROBLEMS_BY_TOPIC.md
"""

import os
import re
from typing import Dict, List

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CATEGORIES_DIR = os.path.join(BASE_DIR, "categories")
ANALYSIS_DIR = os.path.join(BASE_DIR, "analysis")

DOMAIN_NAMES = {
    "dp": "Dynamic Programming (DP)",
    "graph_theory": "Graph Theory",
    "data_structures": "Data Structures (DS)",
    "basics": "Basics & Search",
    "game_theory": "Game Theory",
    "number_theory": "Number Theory",
    "strings": "Strings",
    "geometry": "Geometry",
    "combinatorics": "Combinatorics",
    "math": "Math"
}

def update_master_categories_readme():
    subdirs = [d for d in os.listdir(CATEGORIES_DIR) if os.path.isdir(os.path.join(CATEGORIES_DIR, d))]
    
    rows = []
    total_all_problems = 0
    for d in sorted(subdirs):
        d_path = os.path.join(CATEGORIES_DIR, d)
        files = [f for f in os.listdir(d_path) if f.endswith(".md") and f != "README.md"]
        total_probs = 0
        file_links = []
        for f in sorted(files):
            with open(os.path.join(d_path, f), encoding="utf-8") as fp:
                content = fp.read()
            cnt = len(re.findall(r"\[problem:AtCoder-[^\]]+\]", content))
            total_probs += cnt
            file_links.append(f"[`{f}`]({d}/{f})")
        
        total_all_problems += total_probs
        d_name = DOMAIN_NAMES.get(d, d.capitalize())
        links_str = "<br>".join(file_links)
        rows.append(f"| **{d_name}** | [`{d}/`]({d}/) | {links_str} | {total_probs} |")

    table_content = "\n".join(rows)

    readme_content = f"""# 📚 AtCoder Problem Categories Directory

This directory organizes curated AtCoder problems into dedicated domain folders and skill-specific `.md` files.
All problems inside these files teach **reusable competitive programming techniques and algorithms**, completely filtering out trivial logic-building and syntax simulations.

---

## 📁 Category Folders & Topic Markdown Files

| Tag / Domain | Directory | Topic `.md` Files | Total Curated Problems |
|---|---|---|---|
{table_content}

---

## 🔬 Problem Evaluation Methodology
Every problem categorized across these `.md` files is evaluated under the strict 7-step pipeline:
1. **Read**: Statement, limits, types, and constraints.
2. **Analyze**: Identify hidden mathematical observations, monotonicity, subproblem independence.
3. **Solve Independently**: Formulate an optimal algorithm with proven time and space complexity before reading editorial.
4. **Read Editorial**: Verify against official and community approaches.
5. **Classify Tag & Topics**: Map to canonical 3-tier taxonomy.
6. **Quality & Anti-Redundancy Filter**: Reject basic logic building and duplicate problems.
7. **Document**: Archive in dedicated topic `.md` file, update selection log, and provide individual analysis with verified C++ solution.

[Back to Main Repository](../../README.md)
"""
    readme_path = os.path.join(CATEGORIES_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"[+] Master categories README updated with {len(subdirs)} domains and {total_all_problems} problem references.")


def update_dp_readme():
    dp_dir = os.path.join(CATEGORIES_DIR, "dp")
    files = [f for f in os.listdir(dp_dir) if f.endswith(".md") and f != "README.md"]
    
    rows = []
    for f in sorted(files):
        f_path = os.path.join(dp_dir, f)
        with open(f_path, encoding="utf-8") as fp:
            content = fp.read()
        cnt = len(re.findall(r"\[problem:AtCoder-[^\]]+\]", content))
        
        # Extract title and subtopic from file
        m_title = re.search(r"# 📖 (.*?)\n", content)
        title = m_title.group(1).strip() if m_title else f
        
        m_sub = re.search(r"- \*\*Subtopic\*\*: `(.*?)`", content)
        subtopic = m_sub.group(1).strip() if m_sub else "DP Technique"

        rows.append(f"| [`{f}`]({f}) | {subtopic} | **{title}** | {cnt} |")

    table_str = "\n".join(rows)
    dp_readme = f"""# Dynamic Programming (DP) Category Index

Curated collection of high-value problems in **Dynamic Programming (DP)** partitioned into modular, skill-specific topic Markdown files.

## 📂 Topic Markdown Files

| Topic File | Subtopic | Topic / Skill | Problems Count |
|---|---|---|---|
{table_str}

---

[Back to Categories Directory](../README.md) | [Back to Main Repository](../../README.md)
"""
    with open(os.path.join(dp_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(dp_readme)
    print(f"[+] categories/dp/README.md updated with {len(files)} topic files.")


def audit_status():
    with open(os.path.join(BASE_DIR, "SELECTION_LOG.md"), encoding="utf-8") as f:
        sel_log = f.read()
    with open(os.path.join(BASE_DIR, "QUALITY_PROBLEMS_BY_TOPIC.md"), encoding="utf-8") as f:
        quality = f.read()

    selected_in_log = re.findall(r"\[problem:AtCoder-([^\]]+)\].*?\*\*SELECTED\*\*", sel_log)
    rejected_in_log = re.findall(r"\[problem:AtCoder-([^\]]+)\].*?\*\*REJECTED.*?\*\*", sel_log)
    in_quality = re.findall(r"\[problem:AtCoder-([^\]]+)\]", quality)
    analysis_files = [f[8:-3] for f in os.listdir(ANALYSIS_DIR) if f.startswith("AtCoder-") and f.endswith(".md")]

    print("\n" + "=" * 60)
    print("                 CURRICULUM AUDIT REPORT")
    print("=" * 60)
    print(f"Total Selected in SELECTION_LOG.md: {len(selected_in_log)} (Unique: {len(set(selected_in_log))})")
    print(f"Total Rejected in SELECTION_LOG.md: {len(rejected_in_log)} (Unique: {len(set(rejected_in_log))})")
    print(f"Total in QUALITY_PROBLEMS_BY_TOPIC.md: {len(in_quality)} (Unique: {len(set(in_quality))})")
    print(f"Total Analysis Markdown Files in analysis/: {len(analysis_files)}")
    
    # Check for missing analysis files
    missing_analysis = set(selected_in_log) - set(analysis_files)
    if missing_analysis:
        print(f"WARNING: Missing analysis files for: {missing_analysis}")
    else:
        print("[OK] All selected problems have corresponding analysis files in analysis/!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    update_master_categories_readme()
    update_dp_readme()
    audit_status()
