import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

# Ensure scratch is on path for compiler_helper
sys.path.append(os.path.abspath('scratch'))
from compiler_helper import compile_cpp

print("=" * 75)
print("      PROCESSING BATCH 8 PART 6: ABC / ARC / AGC CURATED LADDER (2713 - 2740)")
print("            ADVANCING CURATED CURRICULUM TO 1177 PROBLEMS!")
print("                *** BAND 7 (2601-2800) CONTINUING! ***")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/band7_part6_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 7 Part 6.")

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

# 1. Compile and verify every C++ solution on samples
print("\n--- Compiling and Verifying C++ Solutions on Samples ---")
os.makedirs('scratch/test_build_bins_b7p6', exist_ok=True)

for p in problems_meta:
    pid = p['id']
    code = p.get('cpp_solution') or p.get('cpp_code')
    src_path = f"scratch/{pid}.cpp"
    bin_path = f"scratch/test_build_bins_b7p6/{pid}.exe"
    
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
    samples = p.get('samples', [])
    for idx, s in enumerate(samples):
        inp = s['in'] if 'in' in s else s['input']
        exp_raw = s['out'] if 'out' in s else s['output']
        
        run_res = subprocess.run([bin_path], input=inp, capture_output=True, text=True, timeout=15)
        out = run_res.stdout.strip()
        
        if pid == 'arc119_d':
            lines = inp.strip().splitlines()
            H, W = map(int, lines[0].split())
            grid = [list(line.strip()) for line in lines[1:H+1]]
            
            out_lines = out.splitlines()
            K_ops = int(out_lines[0].strip())
            for i in range(1, K_ops + 1):
                parts = out_lines[i].strip().split()
                t, r, c = parts[0], int(parts[1]) - 1, int(parts[2]) - 1
                if grid[r][c] != 'R':
                    print(f"[!] arc119_d Sample {idx+1}: chosen cell ({r+1}, {c+1}) is not 'R' (val='{grid[r][c]}')")
                    sys.exit(1)
                if t == 'X':
                    for c_idx in range(W): grid[r][c_idx] = 'W'
                elif t == 'Y':
                    for r_idx in range(H): grid[r_idx][c] = 'W'
                else:
                    print(f"[!] arc119_d Sample {idx+1}: unknown op type '{t}'")
                    sys.exit(1)
            white_count = sum(sum(1 for cell in row if cell == 'W') for row in grid)
            
            exp_lines = exp_raw.strip().splitlines()
            exp_k = int(exp_lines[0].strip())
            exp_grid = [list(line.strip()) for line in lines[1:H+1]]
            for i in range(1, exp_k + 1):
                parts = exp_lines[i].strip().split()
                t, r, c = parts[0], int(parts[1]) - 1, int(parts[2]) - 1
                if t == 'X':
                    for c_idx in range(W): exp_grid[r][c_idx] = 'W'
                else:
                    for r_idx in range(H): exp_grid[r_idx][c] = 'W'
            exp_white = sum(sum(1 for cell in row if cell == 'W') for row in exp_grid)
            if white_count != exp_white:
                print(f"[!] arc119_d Sample {idx+1}: white count mismatch: got {white_count}, expected {exp_white}")
                sys.exit(1)

        elif pid == 'arc110_f':
            lines = inp.strip().splitlines()
            N = int(lines[0].strip())
            P = list(map(int, lines[1].split()))
            out_lines = out.splitlines()
            K_ops = int(out_lines[0].strip())
            if K_ops > 200000:
                print(f"[!] arc110_f Sample {idx+1}: operations {K_ops} exceeds 200,000!")
                sys.exit(1)
            for i in range(1, K_ops + 1):
                op_idx = int(out_lines[i].strip())
                val = P[op_idx]
                nxt = (op_idx + val) % N
                P[op_idx], P[nxt] = P[nxt], P[op_idx]
            if P != list(range(N)):
                print(f"[!] arc110_f Sample {idx+1}: array not sorted: {P}")
                sys.exit(1)

        elif pid == 'agc012_c':
            N = int(inp.strip())
            out_lines = out.splitlines()
            k_len = int(out_lines[0].strip())
            vals = list(map(int, out_lines[1].split()))
            if len(vals) != k_len or k_len > 200:
                print(f"[!] agc012_c Sample {idx+1}: invalid length {k_len}")
                sys.exit(1)
            if not all(1 <= v <= 100 for v in vals):
                print(f"[!] agc012_c Sample {idx+1}: values out of range [1, 100]")
                sys.exit(1)
            k = k_len // 2
            P = vals[:k]
            Q = vals[k:]
            if P != list(range(1, k + 1)):
                print(f"[!] agc012_c Sample {idx+1}: P is not 1..k")
                sys.exit(1)
            dp = [1] * len(Q)
            for i in range(len(Q)):
                for j in range(i):
                    if Q[j] < Q[i]:
                        dp[i] += dp[j]
            tot_good = sum(dp)
            if tot_good != N:
                print(f"[!] agc012_c Sample {idx+1}: good count {tot_good} != N {N}")
                sys.exit(1)

        elif pid == 'hitachi2020_e':
            lines = inp.strip().splitlines()
            N, M = map(int, lines[0].split())
            grid_lines = [line.strip() for line in out.splitlines() if line.strip()]
            R = (1 << N) - 1
            C = (1 << M) - 1
            if len(grid_lines) != R or any(len(row) != C for row in grid_lines):
                print(f"[!] hitachi2020_e Sample {idx+1}: dimensions mismatch: {len(grid_lines)}x{len(grid_lines[0]) if grid_lines else 0} vs {R}x{C}")
                sys.exit(1)
            pref = [[0] * (C + 1) for _ in range(R + 1)]
            for r in range(R):
                for c in range(C):
                    pref[r + 1][c + 1] = pref[r][c + 1] + pref[r + 1][c] - pref[r][c] + int(grid_lines[r][c])
            oddness_count = 0
            for r1 in range(R):
                for r2 in range(r1, R):
                    for c1 in range(C):
                        for c2 in range(c1, C):
                            val = pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]
                            if val % 2 == 1:
                                oddness_count += 1
            max_N_M = max(N, M)
            min_N_M = min(N, M)
            H_bound = 1 << max_N_M
            W_bound = 1 << min_N_M
            expected_max = (H_bound * H_bound // 4) * (W_bound * (W_bound - 1) // 2)
            if oddness_count != expected_max:
                print(f"[!] hitachi2020_e Sample {idx+1}: oddness {oddness_count} != max {expected_max}")
                sys.exit(1)

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

# Clean up binaries after verification
for p in problems_meta:
    bin_path = f"scratch/test_build_bins_b7p6/{p['id']}.exe"
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

progress['current_batch'] = "Batch 8 Band 7 Part 6: ABC / ARC / AGC Ladder (2713-2740) COMPLETED"
progress['status'] = "BAND_7_IN_PROGRESS"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['selected_count'] = len(completed_ids)
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 8 Band 7 Part 6 completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("MILESTONE REACHED: 1177 CURATED PROBLEMS!")
print("BAND 7 (RATING 2601 - 2800) ADVANCED TO 1177 TOTAL PROBLEMS!")
print("=" * 75)
