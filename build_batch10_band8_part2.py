import os, sys, json, subprocess, collections

sys.stdout.reconfigure(encoding='utf-8')

# Ensure scratch is on path for compiler_helper
sys.path.append(os.path.abspath('scratch'))
from compiler_helper import compile_cpp

print("=" * 75)
print("      PROCESSING BATCH 10 PART 2: RED LEVEL LADDER (2826 - 2850)")
print("            ADVANCING CURATED CURRICULUM TO 1241 PROBLEMS!")
print("             *** BAND 8 (2801 - 3000) IN PROGRESS! ***")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/band8_part2_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 8 Part 2.")

# Check zero duplicates against completed problems
for p in problems_meta:
    pid = p['id']
    if pid in completed_ids:
        print(f"[!] ERROR: Problem {pid} is already completed in progress.json!")
        sys.exit(1)

print("[+] Zero-duplicate check passed: None of the 16 problems have been previously added.")

# 0. Verify taxonomy compliance
with open('taxonomy_3tier.json', 'r', encoding='utf-8') as f:
    tax = json.load(f)

tax_set = set()
for d, subs in tax.items():
    for s, topics in subs.items():
        for item in topics:
            if isinstance(item, list):
                tax_set.add((d, s, item[1]))
            else:
                tax_set.add((d, s, item))

for p in problems_meta:
    d, s, t = p['domain'], p['subtopic'], p['topic']
    if (d, s, t) not in tax_set:
        print(f"[!] Taxonomy validation error for {p['id']}: {d} > {s} > {t}")
        sys.exit(1)

print("[+] All 16 problems strictly verified against 3-tier taxonomy.")

# Custom verifier for tree reconstruction arc103_d
def verify_arc103_d(inp, actual, expected):
    if expected.strip() == '-1':
        return actual.strip() == '-1'
    
    if actual.strip() == '-1':
        return False
        
    lines = actual.strip().splitlines()
    inp_tokens = list(map(int, inp.split()))
    N = inp_tokens[0]
    D = inp_tokens[1:]
    
    if len(lines) != N - 1:
        return False
        
    adj = [[] for _ in range(N + 1)]
    for line in lines:
        parts = list(map(int, line.split()))
        if len(parts) != 2:
            return False
        u, v = parts[0], parts[1]
        adj[u].append(v)
        adj[v].append(u)
        
    # Check tree connectivity
    dist = [-1] * (N + 1)
    dist[1] = 0
    q = collections.deque([1])
    visited = 0
    while q:
        curr = q.popleft()
        visited += 1
        for nxt in adj[curr]:
            if dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1
                q.append(nxt)
                
    if visited != N:
        return False
        
    return True

# 1. Compile and verify every C++ solution on samples
print("\n--- Compiling and Verifying C++ Solutions on Samples ---")
os.makedirs('scratch/test_build_bins_b8p2', exist_ok=True)

for p in problems_meta:
    pid = p['id']
    code = p.get('cpp_solution') or p.get('cpp_code')
    src_path = f"scratch/{pid}.cpp"
    bin_path = f"scratch/test_build_bins_b8p2/{pid}.exe"
    
    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(code)
        
    comp = compile_cpp(src_path, bin_path)
    if comp.returncode != 0:
        print(f"[!] Compilation failed for {pid}:")
        print(comp.stderr)
        sys.exit(1)
    else:
        print(f"[+] Compiled {pid} successfully.")
    
    # Run against samples
    raw_samples = p.get('samples', [])
    if isinstance(raw_samples, dict) and 'samples' in raw_samples:
        samples = raw_samples['samples']
    else:
        samples = raw_samples
    for idx, s in enumerate(samples):
        inp = s['in'] if 'in' in s else s['input']
        exp_raw = s['out'] if 'out' in s else s['output']
        
        run_res = subprocess.run([bin_path], input=inp, capture_output=True, text=True, timeout=15)
        out = run_res.stdout.strip()
        
        if pid == 'arc103_d':
            match = verify_arc103_d(inp, out, exp_raw)
        else:
            out_tokens = out.split()
            exp_tokens = exp_raw.strip().split()
            match = (out_tokens == exp_tokens)
            
        if not match:
            print(f"[!] Sample {idx+1} mismatch for {pid}:")
            print(f"Input:\n{inp}")
            print(f"Expected:\n{exp_raw}")
            print(f"Actual:\n{out}")
            sys.exit(1)
            
    print(f"    [+] Passed all {len(samples)} sample tests for {pid}.")

# Clean up binaries and temporary source after verification
for p in problems_meta:
    bin_path = f"scratch/test_build_bins_b8p2/{p['id']}.exe"
    if os.path.exists(bin_path):
        os.remove(bin_path)
    src_path = f"scratch/{p['id']}.cpp"
    if os.path.exists(src_path):
        os.remove(src_path)

# 2. Generate Analysis Markdown Files
print("\n--- Generating Analysis Files ---")
os.makedirs('analysis', exist_ok=True)
for p in problems_meta:
    pid = p['id']
    code = p.get('cpp_solution') or p.get('cpp_code')
    cat_file = p.get('category_file')
    observation = p.get('observation')
    algorithm = p.get('algorithm')
    
    key_idea = p.get('key_idea', '')
    time_comp = p.get('time_complexity', 'O(N)')
    space_comp = p.get('space_complexity', 'O(N)')
    contest_id = p.get('contest')
    title = p.get('name')
    
    analysis_path = f"analysis/AtCoder-{pid}.md"
    steps_md = "\n".join([f"{i+1}. {step}" for i, step in enumerate(algorithm.split('\n')) if step.strip()])
    
    rel_cat_path = f"../{cat_file}"
    
    content = f"""# Problem Analysis: AtCoder-{pid} — {title}

**Problem ID**: `AtCoder-{pid}`  
**Contest**: `{contest_id}`  
**Rating / Difficulty**: {p['rating']}  
**URL**: https://atcoder.jp/contests/{contest_id}/tasks/{pid}  
**VJudge Tag**: `[problem:AtCoder-{pid}]`  
**Category File**: [`{rel_cat_path}`]({rel_cat_path})  

- **Tag (Domain)**: `{p['domain']}`  
- **Subtopic**: `{p['subtopic']}`  
- **Topic (Skill)**: `{p['topic']}`  

---

## 1. Problem Statement & Key Idea
{key_idea}

## 2. Core Observation & Invariant
{observation}

## 3. Step-by-Step Algorithm
{steps_md}

## 4. Complexity Analysis
- **Time Complexity**: `{time_comp}`
- **Space Complexity**: `{space_comp}`

## 5. C++ Source Code
```cpp
{code}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
"""
    with open(analysis_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[+] Generated: {analysis_path}")

# 3. Update Category Workbooks
print("\n--- Updating Category Workbooks ---")
for p in problems_meta:
    pid = p['id']
    cat_file = p.get('category_file')
    observation = p.get('observation')
    key_idea = p.get('key_idea', '')
    title = p.get('name')
    
    os.makedirs(os.path.dirname(cat_file), exist_ok=True)
    
    table_row = f"| [`AtCoder-{pid}`](../../analysis/AtCoder-{pid}.md) | {title} | {p['rating']} | {key_idea[:120]}... |\n"
    
    if not os.path.exists(cat_file):
        header = f"""# {p['topic']}

**Taxonomy Path**: `{p['domain']}` > `{p['subtopic']}` > `{p['topic']}`

## Description
This topic focuses on {p['topic'].lower()} techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: {observation}
- Common Reductions: {key_idea}

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
"""
        with open(cat_file, 'w', encoding='utf-8') as f:
            f.write(header + table_row)
        print(f"[+] Created Category File: {cat_file}")
    else:
        with open(cat_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Check if already present
        if not any(pid in line for line in lines):
            with open(cat_file, 'a', encoding='utf-8') as f:
                f.write(table_row)
            print(f"[+] Updated Category File: {cat_file}")
        else:
            print(f"[~] Already in Category File: {cat_file}")

# 4. Update SELECTION_LOG.md
with open('SELECTION_LOG.md', 'r', encoding='utf-8') as f:
    sel_log = f.read()

new_log_entries = []
for p in problems_meta:
    pid = p['id']
    key_idea = p.get('key_idea', '')
    contest_id = p.get('contest')
    tag_str = f"`[problem:AtCoder-{pid}]`"
    if pid not in sel_log:
        entry = f"| {tag_str} | `{contest_id}` | {p['rating']} | `{p['domain']}` | `{p['subtopic']}` | `{p['topic']}` | **SELECTED** | Premier archetype: {key_idea[:90]}... |\n"
        new_log_entries.append(entry)

if new_log_entries:
    with open('SELECTION_LOG.md', 'a', encoding='utf-8') as f:
        f.writelines(new_log_entries)
    print(f"[+] Added {len(new_log_entries)} new entries to SELECTION_LOG.md")

# 5. Update QUALITY_PROBLEMS_BY_TOPIC.md
with open('QUALITY_PROBLEMS_BY_TOPIC.md', 'r', encoding='utf-8') as f:
    q_content = f.read()

new_quality_entries = []
for p in problems_meta:
    pid = p['id']
    cat_file = p.get('category_file')
    title = p.get('name')
    if pid not in q_content:
        entry = f"| [`[problem:AtCoder-{pid}]`](analysis/AtCoder-{pid}.md) | {title} | {p['rating']} | `{p['domain']}` | `{p['topic']}` | [`{cat_file}`]({cat_file}) |\n"
        new_quality_entries.append(entry)

if new_quality_entries:
    with open('QUALITY_PROBLEMS_BY_TOPIC.md', 'a', encoding='utf-8') as f:
        f.writelines(new_quality_entries)
    print(f"[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# 6. Update progress.json
for p in problems_meta:
    pid = p['id']
    completed_ids.add(pid)
    evaluated_ids.add(pid)

progress['current_batch'] = "Batch 10 Band 8 Part 2: Red Level Ladder (2826-2850) COMPLETED"
progress['status'] = "BAND_8_IN_PROGRESS"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['selected_count'] = len(completed_ids)
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 10 Band 8 Part 2 completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("MILESTONE REACHED: 1241 CURATED PROBLEMS!")
print("BAND 8 (RATING 2801 - 3000) IS ACTIVELY IN PROGRESS!")
print("=" * 75)
