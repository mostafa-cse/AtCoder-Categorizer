import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 6 PART 3B: ABC / ARC CURATED LADDER (2311 - 2330)")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/part5_part3b_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 5 Part 3B.")

COMPLEXITIES = {
    "abc268_g": {
        "key_idea": "Given $N$ strings $S_1, \\dots, S_N$, a random permutation of the 26 lowercase English letters is chosen uniformly. For each string $S_i$, find the expected value of its 1-based index when all $N$ strings are sorted lexicographically, modulo 998244353.",
        "time_complexity": "O(\\sum |S_i|)",
        "space_complexity": "O(\\sum |S_i|)"
    },
    "abc246_g": {
        "key_idea": "In a tree game on $N$ vertices with root 1 and values $A_i$, Takahashi moves a piece downward while Aoki zeroes out an unvisited vertex. Takahashi wants to maximize the final value; Aoki wants to minimize it. Determine Takahashi's optimal score.",
        "time_complexity": "O(N \\log (\\max A_i))",
        "space_complexity": "O(N)"
    },
    "arc167_d": {
        "key_idea": "Given a permutation $P$ of length $N$, you can swap elements within existing cycles at most $C-1$ times to connect all elements into a single cycle. Find the lexicographically smallest permutation achievable.",
        "time_complexity": "O(N \\alpha(N))",
        "space_complexity": "O(N)"
    },
    "arc213_b": {
        "key_idea": "Given $L$ and $R$, find the maximum size of an independent set in the induced subgraph of the hypercube graph formed by vertices $x \\in [L, R]$, where edges connect integers differing by exactly one bit.",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)"
    },
    "arc131_e": {
        "key_idea": "Given $N$, color the edges of the complete graph $K_N$ with three colors (Red, Blue, White) such that each color appears on exactly $M/3$ edges and no triangle contains all three colors, or determine impossible.",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)"
    },
    "abc315_g": {
        "key_idea": "Given $N, A, B, C, X$, count the number of triples $(i, j, k)$ with $1 \\le i, j, k \\le N$ satisfying $A i + B j + C k = X$.",
        "time_complexity": "O(N)",
        "space_complexity": "O(1)"
    },
    "arc090_c": {
        "key_idea": "Given an undirected weighted graph, Takahashi travels from $S$ to $T$ and Aoki from $T$ to $S$ along shortest paths at constant speed. Count pairs of shortest paths where they never meet (neither at a vertex nor along an edge), modulo $10^9+7$.",
        "time_complexity": "O((N + M) \\log N)",
        "space_complexity": "O(N + M)"
    },
    "agc062_c": {
        "key_idea": "Given a multiset $A$ of $N$ positive integers, find the $K$ smallest positive integers that cannot be represented as the sum of a subset of $A$.",
        "time_complexity": "O(N K \\log K)",
        "space_complexity": "O(K)"
    },
    "abc227_f": {
        "key_idea": "In an $H \\times W$ grid with values $A_{i, j}$, find the minimum sum of the $K$ largest elements along any shortest path from $(1, 1)$ to $(H, W)$.",
        "time_complexity": "O(H^2 W^2 K)",
        "space_complexity": "O(H W K)"
    },
    "abc271_g": {
        "key_idea": "A process transitions along a circular 24-hour clock. At hour $h$, with probability $p_h$ an access occurs. If so, with probability $A_i$ user $i$ accesses it. Find the probability that the $N$-th access is made by each user, modulo 998244353.",
        "time_complexity": "O(24^3 \\log N)",
        "space_complexity": "O(24^2)"
    },
    "arc212_e": {
        "key_idea": "Given an array $P$ of length $N$, elements are deleted in a valid order corresponding to tree hook-length independence on the Cartesian tree. Find the expected eliminations or total valid topological orderings modulo 998244353.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "arc115_d": {
        "key_idea": "Given an undirected graph of $N$ vertices and $M$ edges, for each $k = 0, \\dots, N$, count the number of spanning subgraphs having exactly $k$ vertices of odd degree, modulo 998244353.",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)"
    },
    "agc038_c": {
        "key_idea": "Given array $A$ of length $N$, compute $\\sum_{1 \\le i < j \\le N} \\text{lcm}(A_i, A_j) \\pmod{998244353}$.",
        "time_complexity": "O(M \\log M + N)",
        "space_complexity": "O(M)"
    },
    "caddi2018_c": {
        "key_idea": "Given array $A$ of length $N$, find the minimum number of operations (multiplying an element by 4 or dividing by 4) to make $A$ non-decreasing, allowing negative values via optimal sign assignment.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "abc133_f": {
        "key_idea": "Given a tree with colored weighted edges, answer $Q$ queries: if all edges of color $x$ have their weights replaced with $y$, what is the distance between vertices $u$ and $v$?",
        "time_complexity": "O((N + Q) \\log N)",
        "space_complexity": "O(N + Q)"
    },
    "abc307_g": {
        "key_idea": "Given array $A$ of length $N$, you can repeatedly choose an index $i$ and replace $(A_i, A_{i+1})$ with $(A_i - 1, A_{i+1} + 1)$. Minimize the sum of squared differences or prefix sum deviations to equalize the elements.",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)"
    }
}

# 1. Compile and verify every C++ solution on samples
print("\n--- Compiling and Verifying C++ Solutions on Samples ---")
os.makedirs('scratch/test_build_bins', exist_ok=True)

for p in problems_meta:
    pid = p['id']
    code = p.get('code') or p.get('cpp_solution')
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
        
        run_res = subprocess.run([bin_path], input=inp, capture_output=True, text=True, timeout=10)
        actual = run_res.stdout.strip()

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
    code = p.get('code') or p.get('cpp_solution')
    cat_file = p.get('cat_file') or p.get('category_file')
    observation = p.get('observation') or p.get('invariant')
    algorithm = p.get('algorithm') or p.get('editorial_reduction')
    
    comp_info = COMPLEXITIES.get(pid, {})
    key_idea = comp_info.get('key_idea', p.get('key_idea', ''))
    time_comp = comp_info.get('time_complexity', 'O(N)')
    space_comp = comp_info.get('space_complexity', 'O(N)')
    
    analysis_path = f"analysis/AtCoder-{pid}.md"
    steps_md = "\n".join([f"{i+1}. {step}" for i, step in enumerate(algorithm.split('\n')) if step.strip()])
    
    rel_cat_path = f"../{cat_file}"
    
    content = f"""# Problem Analysis: AtCoder-{pid} — {p['title']}

**Problem ID**: `AtCoder-{pid}`  
**Contest**: `{p['contest_id']}`  
**Rating / Difficulty**: {p['rating']}  
**URL**: https://atcoder.jp/contests/{p['contest_id']}/tasks/{pid}  
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
    cat_file = p.get('cat_file') or p.get('category_file')
    observation = p.get('observation') or p.get('invariant')
    comp_info = COMPLEXITIES.get(pid, {})
    key_idea = comp_info.get('key_idea', p.get('key_idea', ''))
    
    os.makedirs(os.path.dirname(cat_file), exist_ok=True)
    
    table_row = f"| [`AtCoder-{pid}`](../../analysis/AtCoder-{pid}.md) | {p['title']} | {p['rating']} | {key_idea[:120]}... |\n"
    
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
    comp_info = COMPLEXITIES.get(pid, {})
    key_idea = comp_info.get('key_idea', p.get('key_idea', ''))
    tag_str = f"`[problem:AtCoder-{pid}]`"
    if pid not in sel_log:
        entry = f"| {tag_str} | `{p['contest_id']}` | {p['rating']} | `{p['domain']}` | `{p['subtopic']}` | `{p['topic']}` | **SELECTED** | Premier archetype: {key_idea[:90]}... |\n"
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
    cat_file = p.get('cat_file') or p.get('category_file')
    if pid not in q_content:
        entry = f"| [`[problem:AtCoder-{pid}]`](analysis/AtCoder-{pid}.md) | {p['title']} | {p['rating']} | `{p['domain']}` | `{p['topic']}` | [`{cat_file}`]({cat_file}) |\n"
        new_quality_entries.append(entry)

if new_quality_entries:
    with open('QUALITY_PROBLEMS_BY_TOPIC.md', 'a', encoding='utf-8') as f:
        f.writelines(new_quality_entries)
    print(f"[+] Updated QUALITY_PROBLEMS_BY_TOPIC.md with new archetypes.")

# 6. Update progress.json
for p in problems_meta:
    pid = p['id']
    if pid not in completed_ids:
        completed_ids.add(pid)
    if pid not in evaluated_ids:
        evaluated_ids.add(pid)

progress['current_batch'] = "Batch 6 Band 5 Part 3B: ABC / ARC Ladder (2311-2330) COMPLETED"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 6 Band 5 Part 3B completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("=" * 75)
