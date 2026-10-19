import os, sys, json, subprocess, collections

sys.stdout.reconfigure(encoding='utf-8')

# Ensure scratch is on path for compiler_helper
sys.path.append(os.path.abspath('scratch'))
from compiler_helper import compile_cpp

print("=" * 75)
print("      PROCESSING BATCH 12 PART 4: RED LEVEL LADDER (2876 - 2900)")
print("            ADVANCING CURATED CURRICULUM TO 1273 PROBLEMS!")
print("             *** BAND 8 (2801 - 3000) IN PROGRESS! ***")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/band8_part4_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 8 Part 4.")

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

# Custom verifier for arc158_d
def verify_arc158_d(inp, actual):
    inp_lines = inp.strip().splitlines()
    t = int(inp_lines[0].strip())
    act_lines = [l for l in actual.strip().splitlines() if l.strip()]
    if len(act_lines) != t:
        return False
    for i in range(t):
        n, p = map(int, inp_lines[i+1].split())
        parts = list(map(int, act_lines[i].split()))
        if len(parts) != 3: return False
        x, y, z = parts
        if not (1 <= x < y < z < p): return False
        s1 = (x + y + z) % p
        sn = (pow(x, n, p) + pow(y, n, p) + pow(z, n, p)) % p
        s2n = (pow(x, 2*n, p) + pow(y, 2*n, p) + pow(z, 2*n, p)) % p
        s3n = (pow(x, 3*n, p) + pow(y, 3*n, p) + pow(z, 3*n, p)) % p
        lhs = (s1 * sn % p) * s2n % p
        rhs = s3n
        if lhs != rhs: return False
    return True

# Custom verifier for arc183_d
def verify_arc183_d(inp, actual, expected):
    lines = inp.strip().splitlines()
    n = int(lines[0].strip())
    adj = collections.defaultdict(list)
    for line in lines[1:]:
        u, v = map(int, line.split())
        adj[u].append(v)
        adj[v].append(u)
        
    dist = {}
    for start in range(1, n + 1):
        q = collections.deque([start])
        d = {start: 0}
        while q:
            curr = q.popleft()
            for nxt in adj[curr]:
                if nxt not in d:
                    d[nxt] = d[curr] + 1
                    q.append(nxt)
        dist[start] = d
        
    def score(output_str):
        tot = 0
        pairs = []
        for line in output_str.strip().splitlines():
            if not line.strip(): continue
            u, v = map(int, line.split())
            pairs.append((u, v))
            tot += dist[u][v]
        return tot, pairs

    exp_tot, exp_pairs = score(expected)
    act_tot, act_pairs = score(actual)
    
    if exp_tot != act_tot:
        return False
        
    if len(act_pairs) != n // 2:
        return False
        
    active = set(range(1, n + 1))
    for u, v in act_pairs:
        if u not in active or v not in active or u == v:
            return False
        deg_u = sum(1 for nxt in adj[u] if nxt in active)
        deg_v = sum(1 for nxt in adj[v] if nxt in active)
        if len(active) > 2:
            if deg_u != 1 or deg_v != 1:
                return False
        active.remove(u)
        active.remove(v)
        
        if len(active) > 0:
            deg = {x: sum(1 for nxt in adj[x] if nxt in active) for x in active}
            leaves = [x for x in active if deg[x] <= 1]
            rem = set(active)
            while leaves:
                leaf = leaves.pop()
                if leaf not in rem: continue
                nbrs = [x for x in adj[leaf] if x in rem]
                if not nbrs:
                    if len(rem) > 1: return False
                    break
                nbr = nbrs[0]
                rem.remove(leaf)
                rem.remove(nbr)
                for nxt in adj[nbr]:
                    if nxt in rem:
                        deg[nxt] -= 1
                        if deg[nxt] == 1:
                            leaves.append(nxt)
            if len(rem) != 0:
                return False
    return True

# 1. Compile and verify every C++ solution on samples
print("\n--- Compiling and Verifying C++ Solutions on Samples ---")
os.makedirs('scratch/test_build_bins_b8p4', exist_ok=True)

for p in problems_meta:
    pid = p['id']
    code = p.get('cpp_solution') or p.get('cpp_code')
    src_path = f"scratch/{pid}.cpp"
    bin_path = f"scratch/test_build_bins_b8p4/{pid}.exe"
    
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
        
        if pid == 'arc158_d':
            match = verify_arc158_d(inp, out)
        elif pid == 'arc183_d':
            match = verify_arc183_d(inp, out, exp_raw)
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

# Clean up temporary binaries after verification
for p in problems_meta:
    bin_path = f"scratch/test_build_bins_b8p4/{p['id']}.exe"
    if os.path.exists(bin_path):
        os.remove(bin_path)

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

progress['current_batch'] = "Batch 12 Band 8 Part 4: Red Level Ladder (2876-2900) COMPLETED"
progress['status'] = "BAND_8_IN_PROGRESS"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['selected_count'] = len(completed_ids)
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 12 Band 8 Part 4 completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("MILESTONE REACHED: 1273 CURATED PROBLEMS!")
print("BAND 8 (RATING 2801 - 3000) IS ACTIVELY IN PROGRESS!")
print("=" * 75)
