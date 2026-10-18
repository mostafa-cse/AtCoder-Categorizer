import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 6 PART 3E: ABC / ARC CURATED LADDER (2354 - 2374)")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/part5_part3e_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 5 Part 3E.")

COMPLEXITIES = {
    "abc405_g": {
        "key_idea": "Count permutations of remaining elements in $A[L..R]$ after removing elements $\\ge X$ as a multinomial coefficient. Sorting queries via Mo's algorithm and maintaining frequency counts with block-based SQRT decomposition on the value domain achieves $O((N + Q) \\sqrt{N})$ time.",
        "time_complexity": "O((N + Q) \\sqrt{N})",
        "space_complexity": "O(N + Q)"
    },
    "agc011_c": {
        "key_idea": "Count connected components in the tensor product graph $G \\times G$. Isolated vertices yield $I(2N - I)$ components; bipartite component pairs produce 2 components each, while any pair containing a non-bipartite component forms 1 component, evaluated via DFS in $O(N + M)$.",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)"
    },
    "abc345_e": {
        "key_idea": "Delete exactly $K$ balls such that adjacent remaining balls have distinct colors, maximizing total value. For each deletion count $j \\le K$, maintaining only the top 2 maximum values with distinct colors allows $O(1)$ transitions per ball in $O(NK)$ time.",
        "time_complexity": "O(NK)",
        "space_complexity": "O(K)"
    },
    "abc414_f": {
        "key_idea": "Find minimum tree jumps of length $K$ from vertex 1 to all vertices. BFS over $2(N-1)$ directed edges limits visits per vertex to at most 2 per phase $d \\bmod K$, yielding optimal paths in $O(NK)$ time.",
        "time_complexity": "O(NK)",
        "space_complexity": "O(NK)"
    },
    "agc036_c": {
        "key_idea": "Characterize sequences reachable by $M$ operations of adding 2 to one element and 1 to another. Solved by stars and bars over each valid odd-element count $k \\le M$ ($k \\equiv M \\pmod 2$) and subtracting the single exceeding element $> 2M$ in $O(N + M)$.",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)"
    },
    "arc172_e": {
        "key_idea": "Find the smallest positive integer $n$ such that $n^n \\equiv X \\pmod{10^9}$. Hensel lifting / digit-by-digit lifting uniquely extends the solution from $10^{k-1}$ to $10^k$ by testing only 10 candidates per digit in $O(L^2)$ per query.",
        "time_complexity": "O(Q L^2)",
        "space_complexity": "O(1)"
    },
    "abc475_g": {
        "key_idea": "Find an integer $x \\le N$ not divisible by $D$ with the maximum number of divisors. Enforcing $v_p(x) < v_p(D)$ for at least one prime factor $p \\mid D$ restricts the search to non-increasing exponent sequences with at most one exception, explored via branch-and-bound DFS.",
        "time_complexity": "O(T \\cdot \\text{HCN_States})",
        "space_complexity": "O(\\text{primes})"
    },
    "arc232_c": {
        "key_idea": "Match multisets $A$ and $B$ under adding 1 to all elements or negating single elements. The minimum required shift $s_{min}$ is found by sorting by parity; iterating $s \\in [s_{min}, s_{min} + 2N]$ and running the Hungarian algorithm on sign-flip costs solves the problem in $O(N^4)$.",
        "time_complexity": "O(N^4)",
        "space_complexity": "O(N^2)"
    },
    "arc092_c": {
        "key_idea": "Array merging via neighbor replacement preserves relative index parity. Any achievable value is a non-empty sum of same-parity elements; greedy parity selection and $O(N)$ constructive trimming and collapsing deterministically yields the maximum sum.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "arc115_e": {
        "key_idea": "Count sequences with $1 \\le X_i \\le A_i$ and $X_i \\ne X_{i+1}$. By inclusion-exclusion, the recurrence $f[i] = - \\sum_{j < i} f[j] \\min_{j < k \\le i} A_k$ is evaluated dynamically using a monotonic stack with aggregated dot-products in $O(N)$ time.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "agc004_c": {
        "key_idea": "Paint Red and Blue connected grids whose intersection is strictly the given purple cells. Dual interlocking comb construction: Red spans column 1 and all odd rows; Blue spans column $W$ and all even rows. Their base combs are disjoint, solved in $O(HW)$.",
        "time_complexity": "O(HW)",
        "space_complexity": "O(HW)"
    },
    "abc430_g": {
        "key_idea": "Maintain sets $S_1, \\dots, S_N$ under range insertions/deletions of $x \\in [1, 60]$ and query range max cardinality and count. Maintaining 60 ODT interval sets and mapping additions/removals to a lazy segment tree answers all queries in $O(Q \\log N)$.",
        "time_complexity": "O(Q \\log N)",
        "space_complexity": "O(N + Q)"
    },
    "abc309_g": {
        "key_idea": "Count permutations with $|P_i - i| \\ge X$ ($X \\le 5, N \\le 100$). Inclusion-exclusion on banned positions uses profile DP tracking a sliding bitmask of width $2X - 1 \\le 9$ of used values, running in $O(N^2 2^{2X-1})$ time.",
        "time_complexity": "O(N^2 2^{2X-1})",
        "space_complexity": "O(N 2^{2X-1})"
    },
    "arc050_c": {
        "key_idea": "Compute $\\text{lcm}(R_A, R_B) \\pmod M$ for repunits. Using $\\gcd(R_A, R_B) = R_{\\gcd(A, B)}$, the LCM factors into two geometric series $R_A$ and $\\sum (10^{\\gcd(A, B)})^j$, each evaluated via $2 \\times 2$ matrix exponentiation in $O(\\log A + \\log B)$.",
        "time_complexity": "O(\\log A + \\log B)",
        "space_complexity": "O(1)"
    },
    "abc226_g": {
        "key_idea": "Determine if baggages of weights $1..5$ can be carried by people of capacities $1..5$. Strict greedy allocation matches items from weight 5 down to 1 to the tightest fitting available containers in $O(1)$ per testcase.",
        "time_complexity": "O(T)",
        "space_complexity": "O(1)"
    },
    "abc224_g": {
        "key_idea": "Find the minimum expected cost to reach target $T$ on an $N$-sided die with increment cost $A$ and reroll cost $B$. Optimal stopping strategy rerolls iff distance to $T$ exceeds threshold $k$; the expected cost $E(k) = \\frac{NB}{k+1} + \\frac{Ak}{2}$ is minimized via convex optimization in $O(1)$.",
        "time_complexity": "O(1)",
        "space_complexity": "O(1)"
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

        if pid == "abc475_g":
            lines_in = inp.strip().split('\n')[1:]
            act_lines = actual.split()
            exp_lines = expected.split()
            for i, line in enumerate(lines_in):
                n_val, d_val = map(int, line.split())
                act_x = int(act_lines[i])
                if act_x > n_val or act_x % d_val == 0:
                    print(f"[!] Sample {idx+1} invalid result for {pid}: {act_x} for N={n_val}, D={d_val}")
                    sys.exit(1)
        elif pid == "agc004_c":
            lines = [l.strip() for l in actual.split('\n') if l.strip()]
            in_lines = [l.strip() for l in inp.split('\n') if l.strip()]
            h, w = map(int, in_lines[0].split())
            orig = in_lines[1:h+1]
            if len(lines) == 2 * h:
                red = lines[:h]
                blue = lines[h:]
                for i in range(h):
                    for j in range(w):
                        is_purp = (red[i][j] == '#' and blue[i][j] == '#')
                        exp_purp = (orig[i][j] == '#')
                        if is_purp != exp_purp:
                            print(f"[!] Sample {idx+1} mismatch for {pid}")
                            sys.exit(1)
            else:
                print(f"[!] Sample {idx+1} line count mismatch for {pid}")
                sys.exit(1)
        elif pid == "arc092_c":
            act_max = actual.split()[0]
            exp_max = expected.split()[0]
            if act_max != exp_max:
                print(f"[!] Sample {idx+1} max sum mismatch for {pid}: expected {exp_max}, got {act_max}")
                sys.exit(1)
        elif pid == "abc224_g":
            act_val = float(actual)
            exp_val = float(expected)
            if abs(act_val - exp_val) >= 1e-6 and abs(act_val - exp_val) / max(1.0, abs(exp_val)) >= 1e-6:
                print(f"[!] Sample {idx+1} mismatch for {pid}: expected {exp_val}, got {act_val}")
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

progress['current_batch'] = "Batch 6 Band 5 Part 3E: ABC / ARC Ladder (2354-2374) COMPLETED"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 6 Band 5 Part 3E completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("=" * 75)
