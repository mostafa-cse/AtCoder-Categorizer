import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 6 PART 3D: ABC / ARC CURATED LADDER (2341 - 2351)")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/part5_part3d_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 5 Part 3D.")

COMPLEXITIES = {
    "tenka1_2014_qualA_d": {
        "key_idea": "Line obstacles subtend angular intervals on the circle. Fixing the rightmost endpoint of an obstacle as the first ray reduces the circular stabbing problem to linear greedy interval stabbing in $O(N^2 \\log N)$.",
        "time_complexity": "O(N^2 \\log N)",
        "space_complexity": "O(N)"
    },
    "abc141_f": {
        "key_idea": "Maximize the sum of two disjoint subset XOR sums. Bits with odd total counts contribute $2^b$ regardless; bits with even total counts can both be made 1 by finding the maximum subset XOR sum on masked elements via Gaussian elimination in $O(N \\log (\\max A))$.",
        "time_complexity": "O(N \\log (\\max A))",
        "space_complexity": "O(N)"
    },
    "agc030_b": {
        "key_idea": "Find the maximum distance to burn all trees along a circular walk. The optimal path alternates visiting the leftmost and rightmost unburned trees, evaluated over all $N$ split points using prefix sums in $O(N)$.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "arc141_c": {
        "key_idea": "Reconstruct a valid bracket sequence from its lexicographically smallest and largest permutations. Adjacent inversions force bracket types, with greedy validation in $O(N)$.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "abc300_g": {
        "key_idea": "Count $P$-smooth numbers $\\le N$ ($P \\le 100, N \\le 10^{16}$). Splitting the 25 primes into small primes $\\le 19$ (8 primes) and large primes in $[23, 97]$ (17 primes) balances search spaces at $\\approx 3 \\times 10^6$, solved via meet-in-the-middle in $O(M_1 \\log M_1 + M_2 \\log M_2)$.",
        "time_complexity": "O(M_1 \\log M_1 + M_2 \\log M_2)",
        "space_complexity": "O(M_1 + M_2)"
    },
    "abc384_g": {
        "key_idea": "Answer $K$ prefix queries $\\sum_{i=1}^X \\sum_{j=1}^Y |A_i - B_j|$ on arrays of size $N$. Maintaining two Fenwick trees over coordinate-compressed values under 2D Mo's algorithm with block size $N/\\sqrt{K}$ yields $O((N + K)\\sqrt{K} \\log N)$.",
        "time_complexity": "O((N + K)\\sqrt{K} \\log N)",
        "space_complexity": "O(N + K)"
    },
    "agc004_d": {
        "key_idea": "Given a teleporter graph, find the minimum changes so every town reaches town 1 in exactly $K$ steps. Forces $a_1=1$ and prunes subtrees exceeding height $K-1$ greedily bottom-up in $O(N)$.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "agc010_c": {
        "key_idea": "Determine if all stones on tree vertices can be removed by subtracting 1 along leaf-to-leaf paths. Rooted tree DP computes the required upward path capacity $c_v = 2 A_v - \\sum c_w$ and verifies internal pairability in $O(N)$.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "arc216_c": {
        "key_idea": "Count subarrays whose power-of-two sum $\\sum_{i=l}^r 2^{A_i}$ is a single power of 2. Divide and conquer on range maximums checks the smaller half against $O(\\log N)$ candidate powers of 2 via rolling hashes in $O(N \\log^2 N)$.",
        "time_complexity": "O(N \\log^2 N)",
        "space_complexity": "O(N)"
    },
    "abc442_g": {
        "key_idea": "Bounded knapsack with small weights $W_i \\in \\{1, 2, 3\\}$ and capacity $C \\le 2 \\times 10^9$. Since $\\text{lcm}(1, 2, 3) = 6$, all items are grouped into weight-6 super-items, leaving only 36 remainder combinations solved greedily in $O(N \\log N)$.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)"
    },
    "abc264_g": {
        "key_idea": "Find the maximum beauty of a string scored by matches of patterns of length $\\le 3$. Construct a de Bruijn graph on 703 2-letter states; detect positive cycles and find the longest path via SPFA / Bellman-Ford in $O(V \\cdot E)$.",
        "time_complexity": "O(V \\cdot E)",
        "space_complexity": "O(V + E)"
    },
    "abc371_g": {
        "key_idea": "Find the lexicographically smallest permutation $A_{P^k(i)}$. Permutation cycle decomposition and greedy shift selection sequentially constrain $k$ across distinct cycle lengths via CRT and extended GCD in $O(N + D^2 \\log N)$.",
        "time_complexity": "O(N + D^2 \\log N)",
        "space_complexity": "O(N)"
    },
    "abc299_f": {
        "key_idea": "Count non-empty strings $T$ such that $T T$ is a subsequence of $S$. Fixing the canonical starting position of the second copy of $T$ eliminates duplicate counting, solved via subsequence automaton DP in $O(N^3 \\cdot 26)$.",
        "time_complexity": "O(N^3 \\cdot 26)",
        "space_complexity": "O(N^2)"
    },
    "abc211_f": {
        "key_idea": "Answer point location queries in $N$ rectilinear polygons. CCW orientation determines whether vertical edges enter (+1) or exit (-1) the interior, evaluated by sweeping $x$ with a difference-array Fenwick tree in $O((M + Q) \\log (\\max Y))$.",
        "time_complexity": "O((M + Q) \\log (\\max Y))",
        "space_complexity": "O(M + Q + \\max Y)"
    },
    "arc221_b": {
        "key_idea": "Count reachable arrays formed by subset bitwise operations $A_i = \\sum_{j \\in S} 2^{j-1}$. Reversing the overwrite dependency DAG uniquely layers newly exposed elements, computed via Stirling numbers and $O(N^3)$ layer DP.",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)"
    },
    "abc223_g": {
        "key_idea": "Count vertices whose deletion does not decrease the tree's maximum matching size. A vertex can be left unmatched iff all its neighbors are matched in their subtrees when rooted at $u$, solved via 2-pass rerooting DP in $O(N)$.",
        "time_complexity": "O(N)",
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

progress['current_batch'] = "Batch 6 Band 5 Part 3D: ABC / ARC Ladder (2341-2351) COMPLETED"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 6 Band 5 Part 3D completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("=" * 75)
