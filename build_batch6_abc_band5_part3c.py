import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 6 PART 3C: ABC / ARC CURATED LADDER (2331 - 2350)")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/part5_part3c_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 5 Part 3C.")

COMPLEXITIES = {
    "arc122_d": {
        "key_idea": "In a game where Alice and Bob pair up $2N$ integers to minimize/maximize the maximum pair XOR, bitwise divide-and-conquer partitions elements by MSB. If both subsets are even, they decouple; if odd, a crossover pair is forced and found via binary Trie in $O(N \\log (\\max A))$.",
        "time_complexity": "O(N \\log (\\max A))",
        "space_complexity": "O(N \\log (\\max A))"
    },
    "arc232_a": {
        "key_idea": "Given intervals $[L_j, R_j]$, find whether there exists a permutation visiting elements such that consecutive steps adhere to interval constraints. Adding sentinels and tracking valid predecessor ranges via 1D monotone reachability DP solves in $O((N + M) \\log N)$.",
        "time_complexity": "O((N + M) \\log N)",
        "space_complexity": "O(N + M)"
    },
    "abc212_f": {
        "key_idea": "Buses connect cities deterministically at discrete times. Each bus departure transitions to a unique subsequent bus, forming a functional graph. Binary lifting over bus transitions answers position queries at time $Z$ in $O(\\log M)$ time.",
        "time_complexity": "O((M + Q) \\log M)",
        "space_complexity": "O(M \\log M)"
    },
    "agc035_c": {
        "key_idea": "Construct a tree of $2N$ vertices with weights $1 \\dots N, 1 \\dots N$ where the path between $i$ and $N+i$ has XOR sum $i$. Star topology around 1 with pairs $(2k, 2k+1)$ and 3-basis decomposition solves for all non-powers of 2 in $O(N)$.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "arc126_d": {
        "key_idea": "Find the minimum operations to form a contiguous subsegment containing a permutation of $1 \\dots K$. Bitmask DP over subset of chosen elements adds inversion counts and median clustering costs in $O(N 2^K)$.",
        "time_complexity": "O(N 2^K)",
        "space_complexity": "O(2^K)"
    },
    "abc191_f": {
        "key_idea": "Repeatedly replacing $(x, y)$ with $\\gcd(x, y)$ or $\\min(x, y)$ can achieve any divisor $d \\le \\min(A)$ if and only if the GCD of all array elements divisible by $d$ is exactly $d$. Evaluated by factorizing all elements in $O(N \\sqrt{\\max A})$.",
        "time_complexity": "O(N \\sqrt{\\max A})",
        "space_complexity": "O(N \\cdot d(\\max A))"
    },
    "abc136_f": {
        "key_idea": "Sum the number of points enclosed in bounding boxes over all non-empty subsets. By quadrant complementary counting, a point $P$ is enclosed unless all chosen points lie in a single half-plane, computed via Fenwick sweep in $O(N \\log N)$.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)"
    },
    "abc262_f": {
        "key_idea": "Find the lexicographically smallest permutation achievable by at most $K$ operations of deleting the first element or rotating the last element to the front. Evaluates 0 rotations vs optimal suffix minimum rotation via monotonic stack in $O(N)$.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "arc044_d": {
        "key_idea": "Invert a given suffix array $A$ into the lexicographically smallest uppercase string $S$. Characters are determined greedily by comparing next-suffix ranks $rank[A_i + 1] < rank[A_{i+1} + 1]$ in $O(N)$ time.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "arc071_d": {
        "key_idea": "Count valid infinite sequences where each value $a_i$ forces the next $a_i$ elements to be identical and stabilizes at step $n$. Two consecutive values $\\ge 2$ lock the sequence, yielding a linear DP solved with prefix sums in $O(n)$.",
        "time_complexity": "O(n)",
        "space_complexity": "O(n)"
    },
    "arc174_e": {
        "key_idea": "For each $t \\in [1, N]$, count permutations $b \\le P$ of length $K$ containing $t$. Decomposing by the first diverging position and counting occurrences of $t$ via an offline Fenwick tree sweep solves in $O(N \\log N)$.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)"
    },
    "abc260_g": {
        "key_idea": "Count how many pieces cover each query square in a scalene triangle region. Triangular coverage regions have vertical and slope-2 diagonal boundaries, computed via 2D imos difference arrays in $O(N(N + M) + Q)$.",
        "time_complexity": "O(N(N + M) + Q)",
        "space_complexity": "O(N(N + M))"
    },
    "abc274_g": {
        "key_idea": "Find the minimum number of surveillance cameras to monitor all empty cells in a grid with obstacles. Each camera covers a maximal row or column segment, reducing by König's theorem to maximum bipartite matching via Hopcroft-Karp in $O(HW \\sqrt{HW})$.",
        "time_complexity": "O(HW \\sqrt{HW})",
        "space_complexity": "O(HW)"
    },
    "abc292_g": {
        "key_idea": "Given $N$ strings of length $M$ with digits and `?`, count completions such that $S_1 < S_2 < \\dots < S_N$ as integers. Equal string lengths equate integer order with lexicographical order, solved by interval DP partitioning into non-decreasing digit blocks in $O(N^3 M \\cdot 10)$.",
        "time_complexity": "O(N^3 M \\cdot 10)",
        "space_complexity": "O(N^2 M)"
    },
    "arc202_b": {
        "key_idea": "Count the number of tours visiting every cell of an $H \\times W$ torus chessboard under knight moves $(i-2, j \\pm 1)$. If $H$ is even, answer is 0. If $H$ is odd, row visits are periodic and column shifts must be coprime to $W$ or $W/2$, solved in $O(H \\log W)$.",
        "time_complexity": "O(H \\log W)",
        "space_complexity": "O(H)"
    },
    "keyence2020_e": {
        "key_idea": "Color vertices Black and White and assign edge weights so that the shortest path from each vertex $v$ to an opposite color equals $D_v$. Greedy processing in ascending order of $D_v$ pairs each vertex with a neighbor $u$ having $D_u \\le D_v$ in $O(N \\log N + M)$.",
        "time_complexity": "O(N \\log N + M)",
        "space_complexity": "O(N + M)"
    }
}

# Custom validator for agc035_c
def validate_agc035_c(inp, out_str):
    tokens = out_str.strip().split()
    if not tokens:
        return False
    ans = tokens[0]
    n = int(inp.strip().split()[0])
    
    # Check if n is power of 2
    if (n & (n - 1)) == 0:
        return ans.lower() == "no"
    
    if ans.lower() != "yes":
        return False
    
    num_edges = 2 * n - 1
    if len(tokens) != 1 + 2 * num_edges:
        return False
    
    edges = []
    tokens = [int(x) for x in tokens[1:]]
    adj = [[] for _ in range(2 * n + 1)]
    for i in range(2 * n - 1):
        u = tokens[2 * i]
        v = tokens[2 * i + 1]
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        
    weights = [0] * (2 * n + 1)
    for i in range(1, n + 1):
        weights[i] = i
        weights[n + i] = i
        
    for i in range(1, n + 1):
        parent = {i: -1}
        queue = [i]
        found = False
        for cur in queue:
            if cur == n + i:
                found = True
                break
            for nxt in adj[cur]:
                if nxt not in parent:
                    parent[nxt] = cur
                    queue.append(nxt)
        if not found:
            return False
        curr = n + i
        xor_sum = 0
        while curr != -1:
            xor_sum ^= weights[curr]
            curr = parent[curr]
        if xor_sum != i:
            return False
            
    return True

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

        if pid == "agc035_c":
            if not validate_agc035_c(inp, run_res.stdout):
                print(f"[!] Sample {idx+1} failed custom validator for agc035_c!")
                sys.exit(1)
            continue

        if pid == "keyence2020_e":
            exp_tokens = expected.split()
            act_tokens = actual.split()
            if exp_tokens[0] == "-1":
                if act_tokens[0] != "-1":
                    print(f"[!] Sample {idx+1} failed for keyence2020_e (expected -1, got {act_tokens[0]})")
                    sys.exit(1)
            else:
                if act_tokens[0] == "-1" or len(act_tokens) != len(exp_tokens):
                    print(f"[!] Sample {idx+1} failed for keyence2020_e (invalid constructive output)")
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

progress['current_batch'] = "Batch 6 Band 5 Part 3C: ABC / ARC Ladder (2331-2350) COMPLETED"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 6 Band 5 Part 3C completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("=" * 75)
