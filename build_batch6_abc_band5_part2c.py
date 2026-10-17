import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 6 PART 2C: ABC / ARC CURATED LADDER (2274 - 2284)")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/part5_part2c_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 5 Part 2C.")

COMPLEXITIES = {
    "arc202_c": {
        "key_idea": "Given an array of indices $A_1, \\dots, A_N$, find the least common multiple of repunits $R_{A_1}, \\dots, R_{A_k}$ modulo 998244353 for every prefix $k = 1, \\dots, N$.",
        "time_complexity": "O(M \\log M + N \\cdot d(M)) where M = \\max(A_i) \\le 2 \\times 10^5",
        "space_complexity": "O(M)"
    },
    "abc215_g": {
        "key_idea": "Given $N$ colored candies with color frequencies $c_1, \\dots, c_m$, for each $k = 1, \\dots, N$, compute the expected number of distinct colors when choosing $k$ candies uniformly at random modulo 998244353.",
        "time_complexity": "O(N \\sqrt{N})",
        "space_complexity": "O(N)"
    },
    "arc175_d": {
        "key_idea": "Given a tree of $N$ vertices and a target integer $K$, construct a permutation $P$ of $1, \\dots, N$ such that the sum of lengths of longest increasing subsequences over all simple paths starting from the root equals $K$, or determine it is impossible.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "abc143_f": {
        "key_idea": "Given $N$ integers, for each $K = 1, \\dots, N$, find the maximum number of operations possible where each operation chooses $K$ pairwise distinct integers and removes them.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)"
    },
    "abc273_f": {
        "key_idea": "Given a coordinate line with start at 0, target at $X$, $N$ walls, and $N$ hammers required to break corresponding walls, find the minimum total travel distance to reach $X$, or -1 if unreachable.",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)"
    },
    "arc052_c": {
        "key_idea": "In a graph with Type A edges (cost 1) and Type B edges (the $k$-th traversed Type B edge costs $k$), find the minimum cost path from vertex 0 to all other vertices.",
        "time_complexity": "O((N + M) \\log(N B)) where B = \\min(N, 150)",
        "space_complexity": "O(N B + M)"
    },
    "arc080_c": {
        "key_idea": "Given a permutation $P$ of length $2N$, repeatedly select an adjacent pair $(P_i, P_{i+1})$ in the current sequence to place at the front of a new sequence, prioritizing lexicographically smallest sequences. Find the resulting permutation.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)"
    },
    "arc227_d": {
        "key_idea": "Given $N$ vectors of length $M$ over $\\{0, 1, 2\\}$, determine if the set of vectors is closed under componentwise majority operation $m(x, y, z)$.",
        "time_complexity": "O(M^2 N / 64 + M^2)",
        "space_complexity": "O(M N / 64 + M^2)"
    },
    "abc276_g": {
        "key_idea": "Count the number of non-decreasing sequences $0 \\le A_1 \\le A_2 \\le \\dots \\le A_N \\le M$ such that $A_{i+1} - A_i \\not\\equiv 0 \\pmod 3$ for all $1 \\le i < N$, modulo 998244353.",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)"
    },
    "arc170_d": {
        "key_idea": "Alice chooses a card $A_i$, then Bob chooses $B_j$, then Alice chooses $A_k$ ($k \\neq i$). Alice wins if the three lengths form a non-degenerate triangle. Determine if Alice can guarantee a win with optimal play.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)"
    },
    "abc474_g": {
        "key_idea": "Construct an $N \\times N$ matrix filled with integers from 1 to $N^2$ such that each row and each column contains exactly $K$ adjacent pairs whose difference is 1 in absolute value, or report impossible.",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)"
    },
    "abc150_f": {
        "key_idea": "Given two sequences $a$ and $b$ of length $N$, find all pairs $(k, x)$ with $0 \\le k < N$ and $0 \\le x < 2^{30}$ such that cyclically shifting $a$ left by $k$ positions and bitwise XORing with $x$ yields $b$.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "arc223_d": {
        "key_idea": "A grid walk starts at $(0, 0)$ and makes $A$ horizontal steps and $B$ vertical steps. Compute the number of paths that reach $(A, B)$ without the number of vertical steps ever exceeding horizontal steps by $K$ or more, modulo 998244353.",
        "time_complexity": "O(A + B)",
        "space_complexity": "O(A + B)"
    },
    "arc151_d": {
        "key_idea": "Given an array of size $2^N$ and $Q$ operations of the form $(x_i, y_i)$ which add $A_u$ to $A_v$ for indices whose $x_i$-th bit differs, compute the final array modulo 998244353.",
        "time_complexity": "O(Q + 2^N \\log(2^N))",
        "space_complexity": "O(2^N)"
    },
    "codefestival_2016_qualC_d": {
        "key_idea": "Given an $H \\times W$ grid of colored blocks, repeatedly choose a column and lower it by one cell. Whenever two horizontally adjacent blocks share the same color, 1 point of friction cost is incurred. Find the minimum total friction cost to sink all blocks.",
        "time_complexity": "O(W \\cdot H^2)",
        "space_complexity": "O(H^2)"
    },
    "agc032_c": {
        "key_idea": "Given a connected undirected graph where every vertex has even degree, determine if the edges can be partitioned into three or more simple cycles.",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)"
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
    samples = p.get('sample_tests', [])
    for idx, s in enumerate(samples):
        inp = s['input']
        expected = s['output'].strip()
        run_res = subprocess.run([bin_path], input=inp, capture_output=True, text=True, timeout=10)
        actual = run_res.stdout.strip()
        
        if pid in ['arc175_d', 'abc474_g']:
            # Constructive problem with multiple valid answers
            first_line = actual.split('\n')[0].strip()
            exp_first_line = expected.split('\n')[0].strip()
            if first_line != exp_first_line:
                print(f"[!] Constructive feasibility mismatch for {pid} sample {idx+1}:")
                print(f"Expected: {exp_first_line}, Actual: {first_line}")
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

progress['current_batch'] = "Batch 6 Band 5 Part 2C: ABC / ARC Ladder (2274-2284) COMPLETED"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 6 Band 5 Part 2C completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("=" * 75)
