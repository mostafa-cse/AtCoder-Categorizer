import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 6 PART 3A: ABC / ARC CURATED LADDER (2301 - 2309)")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/part5_part3a_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 5 Part 3A.")

COMPLEXITIES = {
    "abc314_g": {
        "key_idea": "Given $N$ monsters each with type $A_i$ and attack $B_i$, and $M$ amulet slots, find the maximum prefix of monsters that can be defeated when using $k$ amulets for each $k = 0, \\dots, M$.",
        "time_complexity": "O((N + M) \\log M)",
        "space_complexity": "O(N + M)"
    },
    "arc211_d": {
        "key_idea": "Given an undirected graph of $N$ vertices and $M$ edges, place blue and yellow signposts at each vertex directed towards 1 and 2 respectively, such that following blue leads to 1, following yellow leads to 2, and no vertex has identical signpost orientations.",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)"
    },
    "arc229_f": {
        "key_idea": "In a card game with $N$ vertices and $N$ edge cards of weights $C_i$, find a subgraph where every connected component has size at least 3 or is an edge without isolated single edges, minimizing total edge cost.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)"
    },
    "abc281_g": {
        "key_idea": "Count the number of connected undirected graphs with $N$ labeled vertices where vertex $N$ has strictly greater shortest path distance from vertex 1 than any other vertex, modulo $M$.",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)"
    },
    "abc379_g": {
        "key_idea": "Given an $H \\times W$ grid ($HW \\le 200$) with characters in $\\{1, 2, 3, ?\\}$, count valid 3-colorings where adjacent cells differ, modulo 998244353.",
        "time_complexity": "O(HW \\cdot 3 \\cdot 2^{W-1})",
        "space_complexity": "O(2^W)"
    },
    "arc159_c": {
        "key_idea": "Given array $A$ of length $N \\le 50$, repeatedly add permutations of $(1, \\dots, N)$ in at most $10^4$ operations to equalize all elements, or determine impossible.",
        "time_complexity": "O(N \\sum |A_i|)",
        "space_complexity": "O(N)"
    },
    "abc234_g": {
        "key_idea": "Given array $A$, compute $\\sum \\prod (\\max(B_i) - \\min(B_i))$ over all $2^{N-1}$ compositions of $A$ into contiguous blocks, modulo 998244353.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "abc258_f": {
        "key_idea": "On an integer grid where lines $x = Bn$ and $y = Bn$ are highways (cost 1/unit) and other lines cost $K$/unit, find the minimum time to travel from $(S_x, S_y)$ to $(G_x, G_y)$.",
        "time_complexity": "O(T)",
        "space_complexity": "O(1)"
    },
    "abc295_f": {
        "key_idea": "Given digit string $S$ of length $\\le 16$, compute the total occurrences of $S$ as substrings among all integers in $[L, R]$ for $T$ queries.",
        "time_complexity": "O(T (\\log_{10} R)^2)",
        "space_complexity": "O(1)"
    },
    "abc209_f": {
        "key_idea": "In a line of $N$ trees with heights $H_i$, cutting tree $P_i$ costs $H_{P_i-1} + H_{P_i} + H_{P_i+1}$. Count permutations minimizing the total cost, modulo $10^9+7$.",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)"
    },
    "agc024_d": {
        "key_idea": "Expand a tree $G$ by adding leaves so that all vertices in each color class have isomorphic rooted trees. Minimize colorfulness, and secondarily minimize the number of leaves.",
        "time_complexity": "O(N^2)",
        "space_complexity": "O(N)"
    },
    "arc068_c": {
        "key_idea": "Given $N$ souvenir intervals $[l_i, r_i] \\subseteq [1, M]$, for each train interval $d = 1, \\dots, M$, find the number of souvenir intervals containing at least one multiple of $d$.",
        "time_complexity": "O(N \\log M + M \\log^2 M)",
        "space_complexity": "O(N + M)"
    },
    "arc049_c": {
        "key_idea": "Given directed dependency constraints of Type 1 ($y$ must be painted before $x$) and Type 2 ($v$ must not be painted when painting $u$), find the maximum number of paintable vertices.",
        "time_complexity": "O(2^B (N + A + B))",
        "space_complexity": "O(N + A + B)"
    },
    "arc044_c": {
        "key_idea": "In a $W \\times H$ grid with $Q$ horizontal and vertical beams appearing at integer times, find the minimum number of steps to avoid all beams or report -1.",
        "time_complexity": "O(W + H + Q \\log Q)",
        "space_complexity": "O(W + H + Q)"
    },
    "exawizards2019_e": {
        "key_idea": "Given $B$ black and $W$ white chocolates, repeatedly choose Black or White with equal probability and eat one if available. Find the probability that the $i$-th chocolate eaten is Black for all $i = 1, \\dots, B+W$.",
        "time_complexity": "O(B + W)",
        "space_complexity": "O(B + W)"
    },
    "panasonic2020_e": {
        "key_idea": "Given three strings $a, b, c$ with wildcards '?', find the minimum length of a string containing all three as substrings.",
        "time_complexity": "O(|a||b| + |a||c| + |b||c| + L^2)",
        "space_complexity": "O(L)"
    }
}

def validate_arc211_d(inp, actual, expected):
    lines = actual.strip().split()
    if not lines:
        return False
    if expected.strip().split()[0] == "No":
        return lines[0] == "No"
    if lines[0] != "Yes":
        return False
    
    inp_lines = inp.strip().split()
    N = int(inp_lines[0])
    M = int(inp_lines[1])
    edges = set()
    for i in range(M):
        u = int(inp_lines[2 + 2*i])
        v = int(inp_lines[3 + 2*i])
        edges.add((u, v))
        edges.add((v, u))
        
    if len(lines) != 1 + 2 + 2 * (N - 2):
        return False
        
    y1 = int(lines[1])
    b2 = int(lines[2])
    if (1, y1) not in edges or (2, b2) not in edges:
        return False
        
    bpar = {2: b2}
    ypar = {1: y1}
    for i in range(3, N + 1):
        bi = int(lines[3 + 2 * (i - 3)])
        yi = int(lines[4 + 2 * (i - 3)])
        if bi == yi or (i, bi) not in edges or (i, yi) not in edges:
            return False
        bpar[i] = bi
        ypar[i] = yi
        
    for start in range(2, N + 1):
        curr = start
        vis = {curr}
        while curr != 1:
            curr = bpar.get(curr, 0)
            if curr == 0 or curr in vis:
                return False
            vis.add(curr)
            
    for start in range(1, N + 1):
        if start == 2: continue
        curr = start
        vis = {curr}
        while curr != 2:
            curr = ypar.get(curr, 0)
            if curr == 0 or curr in vis:
                return False
            vis.add(curr)
            
    return True

def validate_arc159_c(inp, actual, expected):
    lines = actual.split()
    if not lines:
        return False
    if expected.split()[0] == "No":
        return lines[0] == "No"
    if lines[0] != "Yes":
        return False
    
    inp_lines = inp.strip().split()
    N = int(inp_lines[0])
    A = [int(x) for x in inp_lines[1:N+1]]
    
    K = int(lines[1])
    if K > 10000:
        return False
    
    tokens = lines[2:]
    if len(tokens) != K * N:
        return False
    
    for k in range(K):
        perm = [int(x) for x in tokens[k*N:(k+1)*N]]
        if sorted(perm) != list(range(1, N + 1)):
            return False
        for i in range(N):
            A[i] += perm[i]
            
    return len(set(A)) == 1

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
        
        if pid == 'arc211_d':
            if not validate_arc211_d(inp, actual, expected):
                print(f"[!] Validation failed for {pid} on sample {idx+1}")
                sys.exit(1)
            continue

        if pid == 'arc159_c':
            if not validate_arc159_c(inp, actual, expected):
                print(f"[!] Validation failed for {pid} on sample {idx+1}")
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

progress['current_batch'] = "Batch 6 Band 5 Part 3A: ABC / ARC Ladder (2301-2309) COMPLETED"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 6 Band 5 Part 3A completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("=" * 75)
