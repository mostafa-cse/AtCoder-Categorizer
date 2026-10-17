import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Read C++ codes from scratch test files or embedded strings
code_arc047_c = open('scratch/test_arc047_c.cpp', 'r', encoding='utf-8').read()
code_abc400_f = open('scratch/test_abc400_f.cpp', 'r', encoding='utf-8').read()
code_abc311_g = open('scratch/test_abc311_g.cpp', 'r', encoding='utf-8').read()

# For arc154_d, ensure LOCAL_TEST is NOT defined for standard interactive submission
code_arc154_d = """#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool query(int i, int j, int k) {
    cout << "? " << i << " " << j << " " << k << endl;
    string res;
    if (!(cin >> res) || res == "-1") exit(0);
    return res == "Yes";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    // Step 1: Find index of 1
    int one_idx = 1;
    for (int i = 2; i <= n; ++i) {
        if (!query(i, i, one_idx)) {
            one_idx = i;
        }
    }

    // Step 2: Compare elements using query(b, one_idx, a)
    // P_b + 1 > P_a <=> P_a < P_b
    auto comp = [&](int a, int b) {
        if (a == b) return false;
        return query(b, one_idx, a);
    };

    vector<int> a;
    for (int i = 1; i <= n; ++i) {
        if (i != one_idx) a.push_back(i);
    }

    vector<int> tmp(a.size());
    auto merge_sort = [&](auto self, int l, int r) -> void {
        if (r - l <= 1) return;
        int m = l + (r - l) / 2;
        self(self, l, m);
        self(self, m, r);
        int i = l, j = m, k = l;
        while (i < m && j < r) {
            if (comp(a[i], a[j])) {
                tmp[k++] = a[i++];
            } else {
                tmp[k++] = a[j++];
            }
        }
        while (i < m) tmp[k++] = a[i++];
        while (j < r) tmp[k++] = a[j++];
        for (int p = l; p < r; ++p) a[p] = tmp[p];
    };

    merge_sort(merge_sort, 0, (int)a.size());

    vector<int> ans(n + 1);
    ans[one_idx] = 1;
    for (size_t i = 0; i < a.size(); ++i) {
        ans[a[i]] = (int)(i + 2);
    }

    cout << "!";
    for (int i = 1; i <= n; ++i) {
        cout << " " << ans[i];
    }
    cout << endl;

    return 0;
}
"""

code_agc014_d = open('scratch/test_agc014_d.cpp', 'r', encoding='utf-8').read()
code_discovery_2016_final_c = open('scratch/test_discovery_2016_final_c.cpp', 'r', encoding='utf-8').read()
code_arc004_4 = open('scratch/test_arc004_4.cpp', 'r', encoding='utf-8').read()
code_arc231_c = open('scratch/test_arc231_c.cpp', 'r', encoding='utf-8').read()
code_abc242_f = open('scratch/test_abc242_f.cpp', 'r', encoding='utf-8').read()
code_abc443_g = open('scratch/test_abc443_g.cpp', 'r', encoding='utf-8').read()
code_m_solutions2020_e = open('scratch/test_m_solutions2020_e.cpp', 'r', encoding='utf-8').read()
code_abc245_g = open('scratch/test_abc245_g.cpp', 'r', encoding='utf-8').read()
code_arc131_d = open('scratch/test_arc131_d.cpp', 'r', encoding='utf-8').read()
code_abc432_f = open('scratch/test_abc432_f.cpp', 'r', encoding='utf-8').read()
code_arc190_b = open('scratch/test_arc190_b.cpp', 'r', encoding='utf-8').read()
code_abc196_f = open('scratch/test_abc196_f.cpp', 'r', encoding='utf-8').read()

meta = [
    {
        "id": "arc047_c",
        "contest_id": "arc047",
        "title": "C. N!÷K番目の単語",
        "rating": 2262,
        "domain": "Miscellaneous",
        "subtopic": "General",
        "topic": "Factorial Number System",
        "cat_file": "categories/miscellaneous/factorial_number_system_rank_fenwick.md",
        "key_idea": "We are given integers $N$ ($1 \\le N \\le 10^5$) and $K$ ($1 \\le K \\le N$). All $N!$ permutations of $(1, 2, \\dots, N)$ are arranged in lexicographical order. We must find the $1$-based $\\frac{N!}{K}$-th permutation.",
        "observation": "Because $N!$ is astronomical, we represent the rank in the factorial number system (factoradic). At each step with $m$ remaining unchosen elements, the block size of permutations for the current position is $(m-1)!$. The fraction of remaining permutations we seek is maintained as $\\frac{rem}{K}$ where $rem < K$. Multiplying by $m$ gives $\\frac{rem \\times m}{K}$. Its quotient $q = \\lfloor \\frac{rem \\times m}{K} \\rfloor$ determines the 0-based choice index among currently available numbers, and the new remainder is $r = (rem \\times m) \\bmod K$. If $r = 0$, this step lands exactly at the end of block $q-1$, so the current digit is $q-1$ and all subsequent remaining digits take their maximal values $(m-2, m-3, \\dots, 0)$. Available numbers are retrieved and removed using a Fenwick Tree with binary lifting in $O(\\log N)$.",
        "algorithm": "Initialize a Fenwick Tree over $[1, N]$ with all elements marked present.\nSet $rem = 1$ (representing the initial fraction $\\frac{1}{K}$ of $N!$).\nFor $m = N, N-1, \\dots, 1$:\nCompute $val = rem \\times m, q = val / K, r = val \\% K$.\nIf $r == 0$, append digit $q-1$, then append all remaining maximal digits $(m-2, m-3, \\dots, 0)$ and break.\nOtherwise, append digit $q$ and update $rem = r$.\nFor each factoradic digit $d$, query the Fenwick tree using binary lifting for the $d$-th available element, print it, and remove it from the tree.",
        "time_complexity": "O(N \\log N)",
        "space_complexity": "O(N)",
        "code": code_arc047_c
    },
    {
        "id": "abc400_f",
        "contest_id": "abc400",
        "title": "F. Happy Birthday! 3",
        "rating": 2263,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Classic DP",
        "topic": "Interval DP / Range DP / Matrix Chain Multiplication (MCM)",
        "cat_file": "categories/dynamic_programming_dp/interval_dp_circular_cake_coloring.md",
        "key_idea": "A circular cake has $N$ equal slices ($N \\le 400$). Slices initially have color 0 and must end with color $C_i \\in [1, N]$. An operation paints $b$ contiguous slices starting at $a$ with color $c$ for cost $b + X_c$. Find the minimum total cost to reach the target configuration.",
        "observation": "Reverse the process: start with the target colors $C_i$ and repaint contiguous intervals to color 0. A final operation on interval $[l, r)$ costs $(r - l) + X_c$, where endpoints $l$ and $r-1$ must originally have color $c$. Operations form a non-crossing laminar family, reducing the problem to Interval DP. Unroll the circular cake into an array of length $2N$. Let $dp[l][r]$ be the minimum cost to clear $[l, r)$ to color 0, and $ep[l][r]$ be the minimum cost to make all elements in $[l, r)$ either color 0 or color $C_l$. For $m \\in (l, r)$, transitions split via $dp[l][m] + dp[m][r]$ and $ep[l][m] + dp[m][r]$. When $C_l == C_{r-1}$, we transition $ep[l][r] = \\min(ep[l][r], ep[l][r-1])$ and $dp[l][r] = \\min(dp[l][r], ep[l][r] + (r - l) + X_{C_l})$. The answer is $\\min_{0 \\le i < N} dp[i][i + N]$.",
        "algorithm": "Duplicate the color array to size $2N$.\nInitialize $dp[i][i] = 0$ and $ep[i][i] = 0$ for all $i \\le 2N$.\nIterate interval length $len = 1 \\dots N$ and starting left endpoint $l = 0 \\dots 2N - len$ ($r = l + len$).\nSplit over midpoint $m \\in (l, r)$: update $dp[l][r] = \\min(dp[l][r], dp[l][m] + dp[m][r])$ and $ep[l][r] = \\min(ep[l][r], ep[l][m] + dp[m][r])$.\nIf $C_l == C_{r-1}$, update $ep[l][r] = \\min(ep[l][r], ep[l][r-1])$ and $dp[l][r] = \\min(dp[l][r], ep[l][r] + (r - l) + X_{C_l})$.\nCompute answer as $\\min_{0 \\le i < N} dp[i][i + N]$.",
        "time_complexity": "O(N^3)",
        "space_complexity": "O(N^2)",
        "code": code_abc400_f
    },
    {
        "id": "abc311_g",
        "contest_id": "abc311",
        "title": "G. One More Grid Task",
        "rating": 2265,
        "domain": "Data Structures (DS)",
        "subtopic": "Monotonic Data Structures",
        "topic": "Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum",
        "cat_file": "categories/data_structures_ds/monotonic_stack_2d_grid_min_sum.md",
        "key_idea": "Given an $N \\times M$ grid of non-negative integers ($N, M \\le 300, A_{i,j} \\le 300$), select a rectangular subgrid $R$ to maximize $(\\sum_{(i,j) \\in R} A_{i,j}) \\times \\min_{(i,j) \\in R} A_{i,j}$.",
        "observation": "Iterate over all $O(N^2)$ row boundary pairs $[u, d]$. For a fixed pair $[u, d]$, collapse columns into two 1D arrays: column sum $S_j = \\sum_{i=u}^d A_{i, j}$ and column minimum $B_j = \\min_{i=u}^d A_{i, j}$. Any subsegment of columns $[l, r]$ has subgrid sum $\\sum_{j=l}^r S_j$ and minimum $\\min_{j=l}^r B_j$. Because all entries $A_{i,j} \\ge 1 > 0$, column sums are strictly positive; thus, for a column $k$ acting as the minimum, extending the column range as far left and right as possible while $B_j \\ge B_k$ strictly maximizes the sum. Using a monotonic stack, we find the maximal span $[L_k, R_k]$ for each column $k$ in $O(M)$ time.",
        "algorithm": "Loop over row upper bound $u$ from $0$ to $N-1$.\nMaintain column sum array $S$ and column minimum array $B$, resetting $S_j = 0, B_j = \\infty$.\nLoop over lower row bound $d$ from $u$ to $N-1$:\nAccumulate $S_j += A_{d, j}$ and $B_j = \\min(B_j, A_{d, j})$, and compute prefix sums of $S$.\nUse a monotonic stack to compute the left bound $L_j$ (furthest index with elements $\\ge B_j$) for all columns in $O(M)$.\nUse a monotonic stack to compute the right bound $R_j$ (furthest index with elements $\\ge B_j$) for all columns in $O(M)$.\nFor each column $j$, update global maximum with $(\\text{pref}[R_j + 1] - \\text{pref}[L_j]) \\times B_j$.\nOutput the maximum result.",
        "time_complexity": "O(N^2 M)",
        "space_complexity": "O(N M)",
        "code": code_abc311_g
    },
    {
        "id": "arc154_d",
        "contest_id": "arc154",
        "title": "D. A + B > C ?",
        "rating": 2265,
        "domain": "Miscellaneous",
        "subtopic": "Interactive Problems",
        "topic": "Interactive Problems",
        "cat_file": "categories/miscellaneous/interactive_permutation_comparator_merge_sort.md",
        "key_idea": "An unknown permutation $P$ of length $N \\le 2000$ is hidden. We can ask at most 25,000 queries of the form '? i j k', asking if $P_i + P_j > P_k$. Recover the entire permutation $P$.",
        "observation": "First, locate the index $x$ where $P_x = 1$ in $N-1$ queries. Start with candidate $x = 1$. For $i = 2 \\dots N$, query '? i i x' ($P_i + P_i > P_x$). If 'No', then $2 P_i \\le P_x \\implies P_i < P_x$, so update candidate $x \\leftarrow i$. When $i$ hits the true position of $1$, $2(1) \\le P_x$ is 'No' (since $P_x \\ge 2$), so $x$ switches to the position of $1$, and never changes again since $2 P_k > 1$ for all other elements.\nOnce the index $x$ with $P_x = 1$ is known, querying '? b x a' tests $P_b + 1 > P_a \\iff P_b \\ge P_a$. Since all elements are distinct, this provides a strict comparison oracle between any two elements $P_a$ and $P_b$. Using standard merge sort on the remaining $N-1$ elements takes at most $(N-1) \\lceil \\log_2 (N-1) \\rceil \\le 22,000$ queries, well within the 25,000 query limit.",
        "algorithm": "Set $one\\_idx = 1$.\nFor $i = 2 \\dots N$, ask '? i i one_idx'. If response is 'No', set $one\\_idx = i$.\nDefine comparator $comp(a, b)$: query '? b one_idx a'. Returns true if $P_a < P_b$.\nSort all indices $\{1, \\dots, N\} \\setminus \\{one\\_idx\\}$ using in-place merge sort with comparator $comp$.\nAssign $P[one\\_idx] = 1$, and for sorted indices assign values $2, 3, \\dots, N$ in increasing order.\nFlush answer '! P_1 P_2 ... P_N'.",
        "time_complexity": "O(N \\log N) \\text{ queries}",
        "space_complexity": "O(N)",
        "code": code_arc154_d
    },
    {
        "id": "agc014_d",
        "contest_id": "agc014",
        "title": "D. Black and White Tree",
        "rating": 2266,
        "domain": "Game Theory",
        "subtopic": "Graph Games",
        "topic": "[Problem] Matching Game On A Graph",
        "cat_file": "categories/game_theory/matching_game_on_tree_perfect_matching.md",
        "key_idea": "Takahashi (white) and Aoki (black) alternately color uncolored vertices of a tree of $N$ vertices ($N \\le 10^5$), Takahashi going first. At the end, every white vertex adjacent to at least one black vertex is repainted black. Takahashi wins if any white vertex remains; Aoki wins if all vertices turn black. Determine the winner with optimal play.",
        "observation": "A white vertex survives repainting if and only if all of its neighbors are white. If the tree possesses a perfect matching $M$ of size $N/2$, Aoki adopts a symmetric mirror strategy: whenever Takahashi colors vertex $u$, Aoki immediately colors the matched vertex $v$ where $(u, v) \\in M$. At the end, every white vertex has an adjacent matched partner colored black, so every white vertex is repainted black and Aoki (Second) wins.\nConversely, if the tree lacks a perfect matching, Takahashi can force a win by repeatedly identifying an unmatched leaf and securing its parent, guaranteeing at least one white vertex with all-white neighbors. Hence, Aoki (Second) wins if and only if the tree has a perfect matching (which requires $N$ even and greedy leaf-parent matching covering all $N$ vertices).",
        "algorithm": "If $N$ is odd, output 'First' immediately.\nRun a bottom-up post-order DFS on the tree from root 1.\nFor each node $u$, after visiting its children: if $u$ is unmatched and its parent $p \\neq 0$ is unmatched, match $u$ with $p$ and increment match count.\nIf the total matching size equals $N / 2$, output 'Second'; otherwise output 'First'.",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "code": code_agc014_d
    },
    {
        "id": "discovery_2016_final_c",
        "contest_id": "discovery_2016_final",
        "title": "C. 特別講演「括弧列と塗り分け」",
        "rating": 2266,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Dp on Different Structures",
        "topic": "DP on Trees and DAGs",
        "cat_file": "categories/dynamic_programming_dp/dp_on_trees_bracket_nesting_coloring.md",
        "key_idea": "Given a balanced bracket sequence $S$ ($|S| \\le 3000$) and an integer $K$. Color each bracket Red or Blue such that for every matched pair of brackets $(i, j)$, the substring $S[i \\dots j]$ satisfies $|R - B| \\le K$. Find the number of valid colorings modulo $10^9 + 7$.",
        "observation": "A balanced bracket sequence naturally represents a forest of nested interval nodes. For each node $u$ corresponding to pair $(i, j)$, the substring $S[i \\dots j]$ consists of the two outer brackets $i$ and $j$, plus the disjoint subtrees of its direct children $v \\in children(u)$. The difference $\\Delta = R - B$ is additive: $\\Delta_u = (c_i + c_j) + \\sum_{v} \\Delta_v$. The outer brackets $(i, j)$ contribute $+2$ (1 way), $0$ (2 ways: RB or BR), or $-2$ (1 way). Since each child $v$ independently enforces $|\\Delta_v| \\le K$, node $u$ combines its children's $\\Delta$ distributions via tree knapsack DP. The maximum value of $|\\Delta|$ for a subtree is bounded by its size and by $K$, yielding an overall $O(|S|^2)$ tree DP.",
        "algorithm": "Parse $S$ into a tree structure using a stack, creating nodes for each '(' and recording direct children.\nDefine recursive tree DP function $dfs(u)$ returning array $dp$, where $dp[d]$ is the number of colorings of subtree $u$ yielding difference $d$.\nInitialize combined state with single value $\\Delta = 0$ (1 way).\nMerge children sequentially: convolve the current difference polynomial with child's difference polynomial, bounding $|\\Delta| \\le \\min(\\text{size}, K + 2)$.\nApply outer bracket transitions: $\\Delta \\pm 2$ (1 way each) and $\\Delta + 0$ (2 ways), discarding any states with $|\\Delta| > K$.\nMultiply total valid ways across all top-level trees in the forest modulo $10^9 + 7$.",
        "time_complexity": "O(|S|^2)",
        "space_complexity": "O(|S| \\min(|S|, K))",
        "code": code_discovery_2016_final_c
    },
    {
        "id": "arc004_4",
        "contest_id": "arc004",
        "title": "D. 表現の自由 ( Freedom of expression )",
        "rating": 2267,
        "domain": "Basics",
        "subtopic": "Basic Counting",
        "topic": "Stars and Bars",
        "cat_file": "categories/basics/stars_and_bars_signed_factor_partition.md",
        "key_idea": "Given integers $N$ ($1 \\le |N| \\le 10^9$) and $M$ ($1 \\le M \\le 10^5$). Count the number of ways to express $N$ as the product of $M$ integers: $N = a_1 \\times a_2 \\times \\dots \\times a_M$, with $a_i \\in \\mathbb{Z}$. Output the result modulo $10^9 + 7$.",
        "observation": "Decompose the problem into magnitudes and signs independently:\n1. Magnitudes: Factorize $|N| = \\prod_{i=1}^k p_i^{e_i}$. Each prime factor $p_i$ has its exponent $e_i$ partitioned among $M$ factors ($e_{i, 1} + \\dots + e_{i, M} = e_i$). By stars and bars, the number of ways is $\\binom{e_i + M - 1}{M - 1}$.\n2. Signs: Exactly $M$ factors each have a sign $\\in \\{+1, -1\\}$. If $N > 0$, an even number of factors must be negative; if $N < 0$, an odd number of factors must be negative. In either case, the number of valid sign assignments is precisely $\\sum \\binom{M}{s} = 2^{M - 1}$.\nThe total answer is $2^{M - 1} \\times \\prod_{i=1}^k \\binom{e_i + M - 1}{M - 1} \\pmod{10^9 + 7}$.",
        "algorithm": "Precompute factorials and modular inverse factorials up to $M + 100$.\nFactorize $|N|$ by trial division up to $\\sqrt{|N|}$ into prime powers $(p_i, e_i)$.\nCompute base answer as $2^{M - 1} \\pmod{10^9 + 7}$.\nFor each prime exponent $e_i$, multiply answer by $\\binom{e_i + M - 1}{M - 1} \\pmod{10^9 + 7}$.\nOutput the final product.",
        "time_complexity": "O(\\sqrt{|N|} + M)",
        "space_complexity": "O(M)",
        "code": code_arc004_4
    },
    {
        "id": "arc231_c",
        "contest_id": "arc231",
        "title": "C. One Sky, Many Stars",
        "rating": 2267,
        "domain": "Geometry",
        "subtopic": "Euclidean Geometry",
        "topic": "Euclidean Geometry",
        "cat_file": "categories/geometry/euclidean_geometry_1d_stargazing_intervals.md",
        "key_idea": "There are $N$ people on a 1D line at coordinates $x_1 < x_2 < \\dots < x_N$. Each person claims the distance to their nearest star is $d_i$. Stars can be placed at any coordinates. We must determine if a valid star configuration exists, supported under $Q$ point updates on $d_i$.",
        "observation": "Each person $i$'s claim implies that at least one star must be placed at $x_i - d_i$ or $x_i + d_i$, and NO star may be placed strictly inside the open interval $(x_i - d_i, x_i + d_i)$.\nA coordinate $pos \\in \\{x_i - d_i, x_i + d_i\\}$ is valid if it does not fall into any other person's forbidden interval. Crucially, by monotonicity of $x_i$, checking validity against the immediately adjacent neighbors $i-1$ and $i+1$ is both necessary and sufficient! Person $i$ is valid if at least one of $x_i - d_i$ or $x_i + d_i$ is not strictly inside $(x_{i-1} - d_{i-1}, x_{i-1} + d_{i-1})$ and not strictly inside $(x_{i+1} - d_{i+1}, x_{i+1} + d_{i+1})$. Maintaining the count of invalid people allows $O(1)$ updates per query affecting only $P-1, P, P+1$.",
        "algorithm": "Define helper `check_person(i)` checking if $x_i - d_i$ or $x_i + d_i$ avoids the open intervals of neighbors $i-1$ and $i+1$.\nInitialize an array `bad` of size $N+2$ and count total invalid people `bad_count`.\nFor each of the $Q$ queries $(P, S)$:\nUpdate $d_P = S$.\nRe-evaluate validity for indices in $\{P - 1, P, P + 1\}$, updating `bad` and `bad_count` accordingly.\nOutput 'Yes' if `bad_count == 0`, else 'No'.",
        "time_complexity": "O(N + Q)",
        "space_complexity": "O(N)",
        "code": code_arc231_c
    },
    {
        "id": "abc242_f",
        "contest_id": "abc242",
        "title": "F. Black and White Rooks",
        "rating": 2268,
        "domain": "Combinatorics",
        "subtopic": "Inclusion Exclusion",
        "topic": "Principle of Inclusion and Exclusion (PIE)",
        "cat_file": "categories/combinatorics/pie_2d_chess_rook_placement.md",
        "key_idea": "Place $B$ black rooks and $W$ white rooks on an $N \\times M$ grid ($N, M \\le 50$) such that no black rook attacks any white rook (rooks attack horizontally/vertically unobstructed). Find the number of valid placements modulo 998244353.",
        "observation": "Because rooks of different colors attack along unobstructed lines, no row or column can contain both black and white rooks. Thus, black rooks occupy a subgrid of $r_1$ rows and $c_1$ columns, and white rooks occupy a subgrid of $r_2$ rows and $c_2$ columns, where the row subsets and column subsets are mutually disjoint: $r_1 + r_2 \\le N$ and $c_1 + c_2 \\le M$.\nLet $f(R, C, K)$ denote the number of ways to place $K$ rooks on an $R \\times C$ board such that every row and column has at least one rook. By 2D Principle of Inclusion and Exclusion (PIE): $f(R, C, K) = \\sum_{i=0}^R \\sum_{j=0}^C (-1)^{i+j} \\binom{R}{i} \\binom{C}{j} \\binom{(R - i)(C - j)}{K}$. Precomputing $f$ and summing over disjoint row/col choices gives the total count.",
        "algorithm": "Precompute factorials and combinations up to $N \\times M$.\nCompute $f(r, c, B)$ and $f(r, c, W)$ for all $1 \\le r \\le N, 1 \\le c \\le M$ using 2D PIE over empty rows $i$ and empty columns $j$.\nIterate all row partition pairs $1 \\le r_1, r_2$ with $r_1 + r_2 \\le N$: compute row selection ways $\\binom{N}{r_1} \\binom{N - r_1}{r_2}$.\nIterate all column partition pairs $1 \\le c_1, c_2$ with $c_1 + c_2 \\le M$: compute column selection ways $\\binom{M}{c_1} \\binom{M - c_1}{c_2}$.\nAccumulate product $\\text{ways}_r \\times \\text{ways}_c \\times f(r_1, c_1, B) \\times f(r_2, c_2, W) \\pmod{998244353}$.\nOutput the total sum.",
        "time_complexity": "O(N^2 M^2)",
        "space_complexity": "O(N M)",
        "code": code_abc242_f
    },
    {
        "id": "abc443_g",
        "contest_id": "abc443",
        "title": "G. Another Mod of Linear Problem",
        "rating": 2268,
        "domain": "Number Theory",
        "subtopic": "Floor Sum",
        "topic": "Floor Sum and Mod Sum of Arithmetic Progression",
        "cat_file": "categories/number_theory/floor_sum_linear_modulo_inequality.md",
        "key_idea": "Given integers $N, M, A, B$ with $1 \\le N \\le M \\le 10^9$ and $0 \\le A, B < M$. Across $T \\le 3 \\times 10^5$ test cases, find the number of integers $0 \\le k < N$ such that $(Ak + B) \\bmod M > k$.",
        "observation": "Rewrite the inequality algebraically:\n$(Ak + B) \\bmod M > k \\iff k + 1 \\le Ak + B - M \\lfloor \\frac{Ak + B}{M} \\rfloor \\iff \\lfloor \\frac{Ak + B}{M} \\rfloor \\le \\frac{(A - 1)k + (B - 1)}{M}$.\nSince the LHS is an integer, this is equivalent to $\\lfloor \\frac{Ak + B}{M} \\rfloor \\le \\lfloor \\frac{(A - 1)k + (B - 1)}{M} \\rfloor$.\nFurthermore, the difference $\\Delta(k) = \\lfloor \\frac{Ak + B}{M} \\rfloor - \\lfloor \\frac{(A - 1)k + (B - 1)}{M} \\rfloor$ only ever takes values in $\\{0, 1\\}$. The condition $\\Delta(k) \\le 0$ means $\\Delta(k) = 0$. Hence, the number of valid $k$ is precisely $N - \\sum_{k=0}^{N-1} \\Delta(k) = N - \\text{floor\\_sum}(N, M, A, B) + \\text{floor\\_sum}(N, M, A - 1, B - 1)$. Using generalized floor division and Euclidean floor sum computes each query in $O(\\log M)$ time.",
        "algorithm": "Implement generalized `floor_sum(n, m, a, b)` using Euclidean-like recursion supporting arbitrary integer $a, b$ via floor division.\nFor each testcase $(N, M, A, B)$:\nCompute $ans = N - \\text{floor\\_sum}(N, M, A, B) + \\text{floor\\_sum}(N, M, A - 1, B - 1)$.\nOutput $ans$.",
        "time_complexity": "O(T \\log M)",
        "space_complexity": "O(1)",
        "code": code_abc443_g
    },
    {
        "id": "m_solutions2020_e",
        "contest_id": "m-solutions2020",
        "title": "E. M's Solution",
        "rating": 2268,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Bitmask DP",
        "cat_file": "categories/dynamic_programming_dp/bitmask_dp_ternary_state_railway.md",
        "key_idea": "A grid city has initial railways along $x=0$ and $y=0$. There are $N \\le 15$ towns with positions $(X_i, Y_i)$ and populations $P_i$. For each $K = 0, 1, \\dots, N$, find the minimum weighted walking distance to railways if we build $K$ new horizontal or vertical railways.",
        "observation": "Any optimal railway line passes directly through at least one town ($x = X_i$ or $y = Y_i$). Moreover, among at most $N$ lines, each chosen line can be injectively associated with a distinct town. Hence, each town $i$ is assigned one of 3 states: (1) build vertical line $x = X_i$, (2) build horizontal line $y = Y_i$, or (0) build no line. There are $3^N = 3^{15} \\approx 1.43 \\times 10^7$ assignments. A ternary branch-and-bound DFS maintaining running distances for all $N$ towns evaluates all combinations in $\\approx 140$ ms.",
        "algorithm": "Store town coordinates and populations in fixed arrays.\nInitialize answer array `ans[K] = inf` for $0 \\le K \\le N$.\nRun ternary DFS `dfs(idx, count_lines, d0, ..., d14)` from `idx = 0`.\nBranch 0: town `idx` builds no line, passing distances unchanged.\nBranch 1: town `idx` builds $x = X_{idx}$, updating each $d_j = \\min(d_j, |X_j - X_{idx}|)$ and incrementing `count_lines`.\nBranch 2: town `idx` builds $y = Y_{idx}$, updating each $d_j = \\min(d_j, |Y_j - Y_{idx}|)$ and incrementing `count_lines`.\nAt leaf `idx == N`, sum $P_j \\times d_j$ and update `ans[count_lines]`.\nApply prefix minima `ans[K] = min(ans[K], ans[K-1])` and print answers.",
        "time_complexity": "O(3^N)",
        "space_complexity": "O(N)",
        "code": code_m_solutions2020_e
    },
    {
        "id": "abc245_g",
        "contest_id": "abc245",
        "title": "G. Foreign Friends",
        "rating": 2270,
        "domain": "Graph Theory",
        "subtopic": "Shortest Paths",
        "topic": "Dijkstra's Algorithm",
        "cat_file": "categories/graph_theory/dijkstra_top2_distinct_origin_countries.md",
        "key_idea": "In a graph of $N$ people and $M$ weighted edges, each person belongs to a country $A_i \\in [1, K]$. There are $L$ popular people. For each person $i$, find the minimum cost path to any popular person belonging to a different country ($A_{popular} \\neq A_i$), or -1 if impossible.",
        "observation": "Standard multi-source Dijkstra from all popular people would only find the single shortest path, which might originate from the same country $A_i$. Because each person $i$ has only one forbidden country $A_i$, tracking the **top 2 shortest distances to popular people originating from distinct countries** at every vertex guarantees that for any vertex $i$, at least one of the top 2 shortest sources has country $\\neq A_i$. Maintaining $(dist_1, country_1)$ and $(dist_2, country_2)$ with $country_1 \\neq country_2$ in priority queue relaxation runs in $O((N + M) \\log N)$.",
        "algorithm": "Initialize `dist1[u] = inf, dist2[u] = inf, c1[u] = -1, c2[u] = -1` for all $u$.\nPush all popular vertices $u \\in B$ with $dist=0$ and country $A_u$ into min-priority queue.\nWhile priority queue is not empty, pop $(d, u, c)$:\nSkip if $d > dist1[u]$ (when $c == c1[u]$) or $d > dist2[u]$ (when $c == c2[u]$).\nFor each neighbor $(v, w)$ with new distance $nd = d + w$:\nIf $c == c1[v]$, relax $dist1[v]$.\nElse if $c == c2[v]$, relax $dist2[v]$.\nElse if $nd < dist1[v]$, shift 1 to 2 and set 1 to $(nd, c)$, pushing into PQ.\nElse if $nd < dist2[v]$, set 2 to $(nd, c)$, pushing into PQ.\nFor each vertex $i$, output $dist1[i]$ if $c1[i] \\neq A_i$, else $dist2[i]$ if $c2[i] \\neq A_i$, else -1.",
        "time_complexity": "O((N + M) \\log N)",
        "space_complexity": "O(N + M)",
        "code": code_abc245_g
    },
    {
        "id": "arc131_d",
        "contest_id": "arc131",
        "title": "D. AtArcher",
        "rating": 2271,
        "domain": "Basics",
        "subtopic": "More Techniques",
        "topic": "Difference Array",
        "cat_file": "categories/basics/difference_array_concentric_score_bands.md",
        "key_idea": "Shoot $N$ arrows into concentric scoring bands $[-r_i, r_i]$ with scores $s_i$ centered at 0. Any two arrows must be separated by distance $\\ge D$ ($D \\le 10^6$). Find the maximum total score obtainable.",
        "observation": "Arrows should be placed at exact intervals of $D$ to remain as close to 0 as possible: $x_j(k) = A + k + j D$ for $j = 0, \\dots, N-1$, where $A = -\\lfloor \\frac{ND}{2} \\rfloor$ and shift $k \\in [0, D-1]$.\nAs the shift $k$ increases from $k$ to $k+1$, all arrows shift right by $+1$. An arrow's score only changes when it crosses a concentric ring boundary $\\pm r_i$. For each boundary point $B$, at most one arrow $j = \\lfloor \\frac{B - A - rem}{D} \\rfloor$ crosses $B$ at $k = (B - A) \\bmod D$. Using a difference array of size $D$, we add score changes for all $2M$ boundaries in $O(M)$ time, and find the maximum total score in $O(M + D)$ time via prefix sums.",
        "algorithm": "Set $A = -\\lfloor \\frac{ND}{2} \\rfloor$.\nInitialize difference array `diff` of size $D+1$.\nFor negative boundaries $B = -r_i$, compute $\\Delta = s_{i-1} - s_i$ (score increases moving right into ring); find $rem = (B - A) \\bmod D$ and check if $j = (B - A - rem) / D \\in [0, N-1]$; add $\\Delta$ to `diff[rem]`.\nFor positive boundaries $B = r_i + 1$, compute $\\Delta = s_i - s_{i-1}$ (score decreases moving right out of ring); find $rem$ and $j$; add $\\Delta$ to `diff[rem]`.\nCompute base score at $k = 0$ for arrows within $[-r_M, r_M]$.\nIterate $k = 1 \\dots D-1$, accumulating `cur_score += diff[k]` and tracking the maximum score.",
        "time_complexity": "O(M + D)",
        "space_complexity": "O(D)",
        "code": code_arc131_d
    },
    {
        "id": "abc432_f",
        "contest_id": "abc432",
        "title": "F. Candy Redistribution",
        "rating": 2273,
        "domain": "Dynamic Programming (DP)",
        "subtopic": "Bit Related DP",
        "topic": "Bitmask DP",
        "cat_file": "categories/dynamic_programming_dp/bitmask_dp_zero_sum_partition_reconstruction.md",
        "key_idea": "$N \\le 20$ children have candies $A_i$. In one operation, child $x$ can give $z \\le A_x$ candies to child $y$. Find the minimum operations to make all children have equal candies, and reconstruct the sequence of transfers.",
        "observation": "Let target $T = \\frac{\\sum A_i}{N}$ (if total not divisible by $N$, impossible). Define net deficits $D_i = A_i - T$. Any valid redistribution partitions children into disjoint zero-sum subsets $\\sum_{i \\in S_j} D_i = 0$. In each connected component $S_j$, $|S_j| - 1$ operations suffice to balance candies using a star graph rooted at an arbitrary child $r \\in S_j$: children with excess first send to $r$, then $r$ sends to children with deficits. Total operations is $\\sum (|S_j| - 1) = N - k$, where $k$ is the number of zero-sum subsets. Minimizing operations is equivalent to maximizing $k$. Since $N \\le 20$, `dp[mask]` = max zero-sum subsets in `mask` can be computed in $O(N 2^N)$.",
        "algorithm": "Check if $\\sum A_i$ is divisible by $N$; if not, output -1.\nCompute $D_i = A_i - T$ for all $i$.\nCompute `sum_d[mask]` and `dp[mask]` for $mask = 1 \\dots 2^N - 1$: $dp[mask] = \\max_{i \\in mask} dp[mask \\setminus \\{i\\}] + (sum_d[mask] == 0 ? 1 : 0)$.\nReconstruct disjoint components $C_1, \\dots, C_k$ by backtracking from full mask $(1 \\ll N) - 1$.\nFor each component $C$: pick root $r$; send candies from all children with $A_i > T$ to $r$; then send from $r$ to all children with $A_j < T$.\nOutput total operations and each triple $(x, y, z)$.",
        "time_complexity": "O(N 2^N)",
        "space_complexity": "O(2^N)",
        "code": code_abc432_f
    },
    {
        "id": "arc190_b",
        "contest_id": "arc190",
        "title": "B. L Partition",
        "rating": 2273,
        "domain": "Combinatorics",
        "subtopic": "Factorials and Binomial Coefficients (nCr)",
        "topic": "Prefix Sum Queries of Binomial Coefficients",
        "cat_file": "categories/combinatorics/prefix_sum_binomial_l_partition_bijection.md",
        "key_idea": "Partition an $N \\times N$ grid ($N \\le 10^7$) into $N$ L-shapes, one of each level $1, \\dots, N$. For $Q \\le 200,000$ queries $k_i$, count the partitions where a given cell $(a, b)$ belongs to the level $k_i$ L-shape, modulo 998244353.",
        "observation": "Level $k$ or smaller L-shapes always occupy a square subgrid $I_k \\times J_k$ of size $k \\times k$, where $[1, N] = I_N \\supsetneq \\dots \\supsetneq I_1$ and $[1, N] = J_N \\supsetneq \\dots \\supsetneq J_1$ are shrinking intervals. Cell $(a, b)$ belongs to level $\\le k$ iff $a \\in I_k$ and $b \\in J_k$. The row and column choices are completely independent! For a 1D sequence of intervals, starting at $[1, N]$ and shrinking by 1 at each step to $[1+x, k+x]$ after $m = N - k$ steps has $\\binom{m}{x}$ paths. The condition $a \\in [1+x, k+x]$ gives $x \\in [\\max(0, a-k), \\min(N-k, a-1)]$. Hence $F(a, k) = 2^{k-1} \\sum_{x} \\binom{N-k}{x}$. As $m = N-k$ increments, $\\sum \\binom{m+1}{x}$ updates in $O(1)$ from $\\sum \\binom{m}{x}$. The exact level $k$ answer is $F(a, k) F(b, k) - F(a, k-1) F(b, k-1)$.",
        "algorithm": "Precompute factorials and powers of 2 up to $N$.\nCompute array $F(a, k)$ for $k = N$ down to $1$ ($m = N-k$ from 0 to $N-1$) by updating binomial coefficient prefix sums in $O(1)$ per step.\nCompute array $F(b, k)$ similarly for coordinate $b$.\nFor each query $k$, output $(F(a, k) F(b, k) - F(a, k-1) F(b, k-1)) \\pmod{998244353}$.",
        "time_complexity": "O(N + Q)",
        "space_complexity": "O(N)",
        "code": code_arc190_b
    },
    {
        "id": "abc196_f",
        "contest_id": "abc196",
        "title": "F. Substring 2",
        "rating": 2274,
        "domain": "Math",
        "subtopic": "Convolution",
        "topic": "Number Theoretic Transform (NTT)",
        "cat_file": "categories/math/ntt_binary_string_hamming_distance.md",
        "key_idea": "Given binary strings $S$ and $T$ ($|T| \\le |S| \\le 10^6$). Choose a substring of $S$ of length $|T|$ to minimize the Hamming distance (number of differing characters) from $T$.",
        "observation": "The mismatch count at offset $i$ is $\\sum_{j=0}^{|T|-1} [S[i+j] \\neq T[j]] = \\sum [S[i+j] == 0 \\land T[j] == 1] + \\sum [S[i+j] == 1 \\land T[j] == 0]$.\nLet $T^R$ be the reversal of $T$. Then $\\sum_{j=0}^{|T|-1} S_1[i+j] T_0^R[|T|-1-j]$ is precisely the convolution of indicator array $S_1$ with $T_0^R$, evaluated at index $i + |T| - 1$. Similarly, the other term is the convolution of $S_0$ with $T_1^R$. Using NTT modulo 998244353, both convolutions are computed in $O(|S| \\log |S|)$ time.",
        "algorithm": "Construct binary indicator vectors $S_0, S_1$ of size $|S|$ and reversed indicator vectors $T_0^R, T_1^R$ of size $|T|$.\nConvolve $S_0$ with $T_1^R$ using NTT.\nConvolve $S_1$ with $T_0^R$ using NTT.\nFor each starting index $i \\in [0, |S| - |T|]$, the mismatch count is $conv_1[i + |T| - 1] + conv_2[i + |T| - 1]$.\nFind and output the minimum mismatch count.",
        "time_complexity": "O(|S| \\log |S|)",
        "space_complexity": "O(|S|)",
        "code": code_abc196_f
    }
]

with open('scratch/part5_part2b_meta.json', 'w', encoding='utf-8') as f:
    json.dump(meta, f, indent=2, ensure_ascii=False)

print(f"Successfully generated scratch/part5_part2b_meta.json with {len(meta)} problems!")
