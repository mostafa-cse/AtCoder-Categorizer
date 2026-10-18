import os, sys, json, subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 75)
print("      PROCESSING BATCH 6 PART 3F-1: ABC / ARC CURATED LADDER (2377 - 2388)")
print("=" * 75)

# Load existing progress
with open('state/progress.json', 'r', encoding='utf-8') as f:
    progress = json.load(f)

completed_ids = set(progress.get('completed_problem_ids', []))
evaluated_ids = set(progress.get('evaluated_problems', []))

with open('scratch/part5_part3f1_meta.json', 'r', encoding='utf-8') as f:
    problems_meta = json.load(f)

print(f"Loaded {len(problems_meta)} selected problems for Band 5 Part 3F-1.")

COMPLEXITIES = {
    "abc227_e": {
        "key_idea": "Count distinct strings reachable from a ternary string of characters 'K', 'E', 'Y' (|S| <= 30) using at most K adjacent swaps. Since each distinct string corresponds uniquely to the permutation preserving identical characters' relative order, state dp[cK][cE][cY][inv] tracks minimum inversions to place prefixes, running in O(|S|^5) time.",
        "time_complexity": "O(|S|^5)",
        "space_complexity": "O(|S|^4)"
    },
    "abc373_g": {
        "key_idea": "Given N red and N blue points with no three collinear, find a non-crossing bipartite matching. By the triangle inequality, any crossing pair of segments can be uncrossed to strictly decrease total Euclidean length; thus, the minimum Euclidean distance matching guarantees zero crossings, solved via the Hungarian algorithm in O(N^3) time.",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)"
    },
    "arc171_d": {
        "key_idea": "Determine if a sequence A exists such that M rolling hash subsegments are all non-zero mod prime P. Inverting powers of base B reduces hash(L..R) != 0 to y_R != y_{L-1} mod P on prefix hashes, which is graph coloring on N+1 <= 17 vertices. Testing if chromatic number chi(G) <= P via Fast Zeta Transform and inclusion-exclusion runs in O(N 2^N) time.",
        "time_complexity": "O(N 2^N)",
        "space_complexity": "O(2^N)"
    },
    "arc188_c": {
        "key_idea": "Determine confusion statuses D_i for N villagers under M statements. A statement A -> (B, C) holds iff H_A ^ H_B = D_A ^ C; since D_A only affects statements made by A, all outgoing targets of A must satisfy H_{B_1} ^ H_{B_j} = C_1 ^ C_j. Finding a 2-coloring of this component system and setting D_A = H_A ^ H_B ^ C solves the problem in O(N + M) time.",
        "time_complexity": "O(N + M)",
        "space_complexity": "O(N + M)"
    },
    "agc039_c": {
        "key_idea": "Compute the sum of return periods under negated cyclic bit shifts for all integers k <= X. Any state has period 2d dividing 2N with N/d odd, uniquely determined by its length-d prefix. Counting valid prefixes <= X in O(N) per divisor and applying inclusion-exclusion over odd-quotient divisors solves the problem in O(N d(N)) time.",
        "time_complexity": "O(N d(N))",
        "space_complexity": "O(N)"
    },
    "abc303_f": {
        "key_idea": "Find the earliest turn T to defeat a monster of health H given N spells dealing d_i damage for t_i turns. Binary searching on T allows greedy damage evaluation at each remaining turn k as max(max_{t_i <= k}(t_i d_i), k * max_{t_i > k} d_i); summing over piecewise linear segments in O(N) per test evaluates in O(N log(H)) time.",
        "time_complexity": "O(N \\log(H))",
        "space_complexity": "O(N)"
    },
    "arc152_d": {
        "key_idea": "Add (N-1)/2 edges to an empty graph such that shifting every edge by +K mod N forms a tree. Impossible iff N is even. For odd N, arranging vertices in an n x g grid (n = N/g, g = gcd(N, K)) and placing vertical edges in odd columns, horizontal edges from odd columns, and bottom horizontal edges from even columns constructs a valid spanning tree in O(N) time.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "donuts_2015_4": {
        "key_idea": "Pack K donuts into N nested boxes, minimizing total buffer material C_i - C_j across Q box crush events. Nesting into K chains equates to partitioning sorted active boxes into K intervals, minimizing span minus the sum of the K-1 largest adjacent differences. Maintaining differences with two multisets answers each query in O(log N) time.",
        "time_complexity": "O((N + Q) \\log N)",
        "space_complexity": "O(N)"
    },
    "dwango2016qual_c": {
        "key_idea": "Find the path from src to dst minimizing worst-case travel time when falling asleep carries the commuter to the terminus. After computing baseline distances d_{normal} to dst, each line edge e = (u -> v) carries risk P(e) = dist(u, T) + d_{normal}(T). Reverse Dijkstra solving dp(u) = min_e max(w(e) + dp(v), P(e)) runs in O((N + \\sum L_i) \\log N) time.",
        "time_complexity": "O((N + \\sum L_i) \\log N)",
        "space_complexity": "O(N + \\sum L_i)"
    },
    "abc337_f": {
        "key_idea": "For all N cyclic rotations of balls into M boxes of capacity K, find total stored balls. A box is allocated when a color reaches 1, K+1, 2K+1, ... balls in the active prefix until M boxes are full, accepting min(total_count[c], b_c * K) balls per color. A two-pointer sliding window maintaining allocated boxes evaluates all shifts in O(N) amortized time.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)"
    },
    "abc479_g": {
        "key_idea": "Given points (A_i, B_i), minimize sum of Manhattan perturbations |c_i| + |d_i| such that all points become collinear through the origin. The Manhattan distance to line Y = s X (|s| <= 1) is |B_i - s A_i|, and to X = t Y (|t| <= 1) is |A_i - t B_i|. Both reduce to weighted median problems on rational slopes, solved with __int128 exact arithmetic in O(N log N) time.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)"
    },
    "abc135_f": {
        "key_idea": "Find maximum repetitions of string t inside s^infinity. Repeating s to length >= |t| + |s| and finding match positions via KMP builds a functional graph on starting positions 0 .. |s|-1 with edge p -> (p + |t|) mod |s|. Detecting cycles (outputting -1) or finding the DAG longest path takes O(|s| + |t|) time.",
        "time_complexity": "O(|s| + |t|)",
        "space_complexity": "O(|s| + |t|)"
    },
    "abc325_g": {
        "key_idea": "Minimize remaining length of string S under operations deleting 'of' plus up to K subsequent characters (|S| <= 300). Interval DP dp[l][r] considers splitting at mid, and whenever S[l]=='o' pairs with S[m]=='f' with dp[l+1][m-1]==0, the operation consumes up to K remaining characters from S[m+1..r], yielding transitions in O(|S|^3) time.",
        "time_complexity": "O(|S|^3)",
        "space_complexity": "O(|S|^2)"
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

        if pid == "abc373_g":
            # Verify valid non-crossing matching
            lines = inp.strip().split()
            N = int(lines[0])
            P = []
            pos = 1
            for _ in range(N):
                P.append((int(lines[pos]), int(lines[pos+1])))
                pos += 2
            Q = []
            for _ in range(N):
                Q.append((int(lines[pos]), int(lines[pos+1])))
                pos += 2
            
            # Check actual is a valid permutation of 1..N
            act_tokens = [int(x) for x in actual.split()]
            if sorted(act_tokens) != list(range(1, N + 1)):
                print(f"[!] Sample {idx+1} not a valid permutation for {pid}: {actual}")
                sys.exit(1)
            # Check segments do not cross
            def ccw(A, B, C):
                return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
            def intersect(A, B, C, D):
                cp1 = ccw(A, B, C)
                cp2 = ccw(A, B, D)
                cp3 = ccw(C, D, A)
                cp4 = ccw(C, D, B)
                return ((cp1 > 0 and cp2 < 0) or (cp1 < 0 and cp2 > 0)) and \
                       ((cp3 > 0 and cp4 < 0) or (cp3 < 0 and cp4 > 0))
            has_cross = False
            for i in range(N):
                for j in range(i + 1, N):
                    p_i = P[i]
                    q_i = Q[act_tokens[i] - 1]
                    p_j = P[j]
                    q_j = Q[act_tokens[j] - 1]
                    if intersect(p_i, q_i, p_j, q_j):
                        has_cross = True
                        break
                if has_cross: break
            if has_cross:
                print(f"[!] Sample {idx+1} has crossing segments for {pid}!")
                sys.exit(1)

        elif pid == "arc152_d":
            lines = inp.strip().split()
            N = int(lines[0])
            K = int(lines[1])
            if expected == "-1":
                if actual != "-1":
                    print(f"[!] Sample {idx+1} mismatch for {pid}: expected -1, got {actual}")
                    sys.exit(1)
            else:
                act_lines = actual.strip().split('\n')
                M = int(act_lines[0].strip())
                if M != (N - 1) // 2:
                    print(f"[!] Sample {idx+1} invalid edge count for {pid}: {M}")
                    sys.exit(1)
                edges = []
                for line in act_lines[1:1+M]:
                    u, v = map(int, line.split())
                    edges.append((u, v))
                shifted = [((u + K) % N, (v + K) % N) for u, v in edges]
                all_e = edges + shifted
                adj_t = [[] for _ in range(N)]
                for u, v in all_e:
                    adj_t[u].append(v)
                    adj_t[v].append(u)
                visited = [False] * N
                q = [0]
                visited[0] = True
                cnt = 0
                while q:
                    curr = q.pop()
                    cnt += 1
                    for nxt in adj_t[curr]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)
                if cnt != N:
                    print(f"[!] Sample {idx+1} graph is not a tree on {N} vertices for {pid}")
                    sys.exit(1)

        elif pid == "arc188_c":
            if expected == "-1":
                if actual != "-1":
                    print(f"[!] Sample {idx+1} mismatch for {pid}: expected -1, got {actual}")
                    sys.exit(1)
            else:
                lines = inp.strip().split()
                N = int(lines[0])
                M = int(lines[1])
                pos = 2
                statements = []
                for _ in range(M):
                    statements.append((int(lines[pos]), int(lines[pos+1]), int(lines[pos+2])))
                    pos += 3
                D = [int(c) for c in actual.strip()]
                # Check if there exists H satisfying all statements
                adj_h = [[] for _ in range(N + 1)]
                for u, v, c in statements:
                    w = D[u - 1] ^ c
                    adj_h[u].append((v, w))
                    adj_h[v].append((u, w))
                H = [-1] * (N + 1)
                valid = True
                for i in range(1, N + 1):
                    if H[i] != -1: continue
                    H[i] = 0
                    q = [i]
                    for curr in q:
                        for nxt, w in adj_h[curr]:
                            req = H[curr] ^ w
                            if H[nxt] == -1:
                                H[nxt] = req
                                q.append(nxt)
                            elif H[nxt] != req:
                                valid = False
                                break
                        if not valid: break
                    if not valid: break
                if not valid:
                    print(f"[!] Sample {idx+1} invalid D string for {pid}: {actual}")
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

progress['current_batch'] = "Batch 6 Band 5 Part 3F-1: ABC / ARC Ladder (2377-2388) COMPLETED"
progress['completed_problem_ids'] = sorted(list(completed_ids))
progress['evaluated_problems'] = sorted(list(evaluated_ids))
progress['total_evaluated_in_curriculum'] = len(evaluated_ids)

with open('state/progress.json', 'w', encoding='utf-8') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)
print("[+] Updated progress checkpoint: state/progress.json")

print("=" * 75)
print(f"Batch 6 Band 5 Part 3F-1 completed successfully! Total selected in curriculum: {len(completed_ids)}")
print("=" * 75)
