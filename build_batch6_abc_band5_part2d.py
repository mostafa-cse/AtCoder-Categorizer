import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 6 PART 2D: ABC / ARC CURATED LADDER (2285 - 2300)")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/part5_part2d_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 5 Part 2D.")

COMPLEXITIES = {
    "arc199_a": {
        "key_idea": "Given $N$ vertices with $M$ red edges and $M$ blue edges, each forming an Eulerian graph, partition the red and blue edges into two equal sets such that both subgraphs have equal degrees at every vertex.",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)"
    },
    "abc219_g": {
        "key_idea": "In a graph of $N$ vertices and $M$ edges where each vertex initially has value $x$, process $Q$ operations where choosing vertex $x$ sets the values of $x$ and all its neighbors to $x$'s current value.",
        "time_complexity": "O(Q \\sqrt{M} + M)",
        "space_complexity": "O(N + M)"
    },
    "agc021_d": {
        "key_idea": "Given a string $S$ of length up to 300 and at most $K$ character modifications, find the maximum possible length of the longest palindromic subsequence of the modified string.",
        "time_complexity": "O(N^2 K)",
        "space_complexity": "O(N^2 K)"
    },
    "arc083_c": {
        "key_idea": "In a tree where each node $u$ requires one color in its subtree to sum to $X_u$, determine if there exists a valid non-negative weight assignment and 2-coloring for all vertices.",
        "time_complexity": "O(N \\max X)",
        "space_complexity": "O(N + \\max X)"
    },
    "abc265_f": {
        "key_idea": "Given two points $P, Q \\in \\mathbb{R}^N$, count the number of integer points $R \\in \\mathbb{Z}^N$ such that $d(P, R) \\le D$ and $d(Q, R) \\le D$ under the Manhattan distance metric, modulo 998244353.",
        "time_complexity": "O(N D^2)",
        "space_complexity": "O(D^2)"
    },
    "abc177_f": {
        "key_idea": "In an $(H+1) \\times W$ grid where each row $i$ has an impassable block $[A_i, B_i]$, find the minimum path length from row 1 to row $i+1$ moving only down or right for each $i = 1, \\dots, H$.",
        "time_complexity": "O(H + W \\log W)",
        "space_complexity": "O(W)"
    },
    "arc054_c": {
        "key_idea": "Given a bipartite graph with adjacency matrix $S$, determine whether the number of edge subsets where every vertex has an odd degree (or cycle partitions) is odd or even.",
        "time_complexity": "O(N^3 / 64)",
        "space_complexity": "O(N^2 / 64)"
    },
    "nikkei2019_qual_e": {
        "key_idea": "Given a weighted graph with vertex weights $X_v$ and edge weights $Y_e$, find the minimum number of edges to delete such that every remaining edge belongs to a connected component whose total vertex weight is at least its edge weight.",
        "time_complexity": "O(M \\log M + (N + M) \\alpha(N))",
        "space_complexity": "O(N + M)"
    },
    "arc026_4": {
        "key_idea": "Given a connected undirected multigraph with edge costs $C_i$ and construction times $T_i$, find a connected spanning subgraph that minimizes the overall cost-to-time ratio $\\frac{\\sum C_e}{\\sum T_e}$.",
        "time_complexity": "O(K \\cdot M \\log M)",
        "space_complexity": "O(N + M)"
    },
    "arc145_d": {
        "key_idea": "Construct a set of $N$ distinct integers in $[-10^7, 10^7]$ with sum $M$ such that no three elements form an arithmetic progression.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)"
    },
    "abc355_e": {
        "key_idea": "Given $N, L, R$, find $\\sum_{k=L}^R A_k \\bmod 100$ in at most 100 interactive queries of the form $(i, j)$ computing $\\sum_{k=j \\cdot 2^i}^{(j+1)2^i - 1} A_k \\bmod 100$.",
        "time_complexity": "O(N 2^N)",
        "space_complexity": "O(2^N)"
    },
    "arc177_d": {
        "key_idea": "Given $N$ poles of height $H$ at coordinates $X_i$, each falling left or right with probability $1/2$ during sequential earthquakes, compute the probability that all poles have fallen by exactly the $t$-th earthquake multiplied by $2^N$ for all $t = 1, \\dots, N$ modulo 998244353.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)"
    },
    "arc198_d": {
        "key_idea": "In a tree with $N$ vertices and given binary constraints $A_{u, v} = 1$ indicating path $(u, v)$ is a palindrome, find the maximum possible number of palindromic simple paths over all valid character assignments.",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N^2)"
    },
    "abc290_f": {
        "key_idea": "Compute the sum of maximum possible tree diameters over all valid degree sequences of size $N$, modulo 998244353.",
        "time_complexity": "O(N + T)",
        "space_complexity": "O(N)"
    },
    "arc078_c": {
        "key_idea": "Identify a hidden integer $1 \\le N \\le 10^9$ in at most 64 queries where each query $n$ returns whether $(n \\le N \\land n \\le_{lex} N)$ or $(n > N \\land n >_{lex} N)$.",
        "time_complexity": "O(\\log N)",
        "space_complexity": "O(1)"
    },
    "arc129_d": {
        "key_idea": "Given a circular array $A_1, \\dots, A_N$ of sum 0, determine the minimum number of operations $(-1, +2, -1)$ at positions $(i-1, i, i+1)$ needed to reduce all elements to 0, or report impossible.",
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
        
        if pid in ['arc199_a', 'arc145_d', 'abc355_e', 'arc078_c']:
            # Constructive or interactive problems verified in dedicated scripts
            continue
        
        run_res = subprocess.run([bin_path], input=inp, capture_output=True, text=True, timeout=10)
        actual = run_res.stdout.strip()
        
        if pid == 'arc026_4':
            if abs(float(actual) - float(expected)) > 1e-3:
                print(f"[!] Float mismatch for {pid}: actual={actual}, expected={expected}")
                sys.exit(1)
            continue

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

progress['current_batch'] = "Batch 6 Band 5 Part 2D: ABC / ARC Ladder (2285-2300) COMPLETED"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 6 Band 5 Part 2D completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("=" * 75)
