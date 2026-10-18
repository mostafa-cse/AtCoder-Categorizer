import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 7 PART 1: ABC / ARC CURATED LADDER (2401 - 2410)")
print("                     FIRST SUB-BATCH OF BAND 6!")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/band6_part1_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 6 Part 1.")

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

print("[+] All 15 problems strictly verified against 3-tier taxonomy.")

# 1. Compile and verify every C++ solution on samples
print("\n--- Compiling and Verifying C++ Solutions on Samples ---")
os.makedirs('scratch/test_build_bins', exist_ok=True)

for p in problems_meta:
    pid = p['id']
    code = p.get('cpp_solution')
    src_path = f"scratch/{pid}.cpp"
    bin_path = f"scratch/test_build_bins/{pid}.exe"
    
    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(code)
        
    cmd = ["g++", "-std=c++17", "-O2", src_path, "-o", bin_path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[!] Compilation failed for {pid}:")
        print(res.stderr)
        sys.exit(1)
    else:
        print(f"[+] Compiled {pid} successfully.")
    
    # Run against samples
    samples = p.get('samples', [])
    for idx, s in enumerate(samples):
        inp = s['input']
        expected = s['output'].strip()
        
        run_res = subprocess.run([bin_path], input=inp, capture_output=True, text=True, timeout=15)
        actual = run_res.stdout.strip()

        if pid == 'arc139_c':
            # arc139_c is construction: verify validity
            lines = actual.splitlines()
            if not lines:
                print(f"[!] Empty output for arc139_c sample {idx+1}")
                sys.exit(1)
            K = int(lines[0].strip())
            s_pts = []
            s1, s2 = set(), set()
            for line in lines[1:]:
                parts = line.strip().split()
                if len(parts) >= 2:
                    x, y = int(parts[0]), int(parts[1])
                    s_pts.append((x, y))
                    v1 = x + 3 * y
                    v2 = 3 * x + y
                    if v1 in s1 or v2 in s2:
                        print(f"[!] arc139_c duplicate invariant for sample {idx+1}")
                        sys.exit(1)
                    s1.add(v1)
                    s2.add(v2)
            if len(s_pts) != K:
                print(f"[!] arc139_c count mismatch: K={K}, pts={len(s_pts)}")
                sys.exit(1)
        elif pid == 'abc366_g':
            # abc366_g can have multiple Yes configurations
            act_tokens = actual.split()
            exp_tokens = expected.split()
            if act_tokens[0] != exp_tokens[0]:
                print(f"[!] abc366_g status mismatch for sample {idx+1}: got {act_tokens[0]}, exp {exp_tokens[0]}")
                sys.exit(1)
            if act_tokens[0] == 'Yes':
                vals = [int(x) for x in act_tokens[1:]]
                inp_lines = inp.strip().split()
                n = int(inp_lines[0])
                m = int(inp_lines[1])
                deg = [0] * n
                adj = [0] * n
                line_idx = 2
                for _ in range(m):
                    u = int(inp_lines[line_idx]) - 1
                    v = int(inp_lines[line_idx + 1]) - 1
                    line_idx += 2
                    adj[u] |= (1 << v)
                    adj[v] |= (1 << u)
                    deg[u] += 1
                    deg[v] += 1
                for u in range(n):
                    if vals[u] <= 0 or vals[u] >= (1 << 60):
                        print(f"[!] abc366_g value out of range for sample {idx+1}")
                        sys.exit(1)
                    if deg[u] >= 1:
                        xor_sum = 0
                        for v in range(n):
                            if (adj[u] >> v) & 1:
                                xor_sum ^= vals[v]
                        if xor_sum != 0:
                            print(f"[!] abc366_g neighbor XOR != 0 for vertex {u+1}")
                            sys.exit(1)
        elif pid == 'arc043_c':
            act_tokens = actual.split()
            exp_tokens = expected.split()
            if exp_tokens[0] == '-1':
                if act_tokens[0] != '-1':
                    print(f"[!] arc043_c expected -1, got {actual}")
                    sys.exit(1)
            else:
                C = [int(x) for x in act_tokens]
                inp_tokens = inp.strip().split()
                N = int(inp_tokens[0])
                A = [int(x) for x in inp_tokens[1:N+1]]
                B = [int(x) for x in inp_tokens[N+1:2*N+1]]
                posC = {v: i for i, v in enumerate(C)}
                distA = sum(1 for i in range(N) for j in range(i+1, N) if posC[A[i]] > posC[A[j]])
                distB = sum(1 for i in range(N) for j in range(i+1, N) if posC[B[i]] > posC[B[j]])
                if distA != distB:
                    print(f"[!] arc043_c distA ({distA}) != distB ({distB}) for sample {idx+1}")
                    sys.exit(1)
        else:
            actual_tokens = actual.split()
            expected_tokens = expected.split()
            if actual_tokens != expected_tokens:
                print(f"[!] Sample {idx+1} mismatch for {pid}:")
                print(f"Input:\n{inp}")
                print(f"Expected:\n{expected}")
                print(f"Actual:\n{actual}")
                sys.exit(1)
            
    print(f"    [+] Passed all {len(samples)} sample tests for {pid}.")

# Clean up binaries after verification
for p in problems_meta:
    bin_path = f"scratch/test_build_bins/{p['id']}.exe"
    if os.path.exists(bin_path):
        os.remove(bin_path)

# 2. Generate Analysis Markdown Files
print("\n--- Generating Analysis Files ---")
os.makedirs('analysis', exist_ok=True)
for p in problems_meta:
    pid = p['id']
    code = p.get('cpp_solution')
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

progress['current_batch'] = "Batch 7 Band 6 Part 1: ABC / ARC Ladder (2401-2410) COMPLETED"
progress['status'] = "BAND_6_IN_PROGRESS"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['selected_count'] = len(completed_ids)
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 7 Band 6 Part 1 completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("BAND 6 (RATING 2401 - 2600) PART 1 IS 100% COMPLETE!")
print("=" * 75)
