# Problem Analysis: AtCoder-arc186_a — A - Underclued

**Problem ID**: `AtCoder-arc186_a`  
**Contest**: `arc186`  
**Rating / Difficulty**: 2511  
**URL**: https://atcoder.jp/contests/arc186/tasks/arc186_a  
**VJudge Tag**: `[problem:AtCoder-arc186_a]`  
**Category File**: [`../categories/combinatorics/underclued_tournament_bipartite_scc.md`](../categories/combinatorics/underclued_tournament_bipartite_scc.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
Determine whether there exists an $N \times N$ grid of directed edges matching row/column constraints with exactly $K$ non-fixed entries.

## 2. Core Observation & Invariant
In a bipartite directed tournament graph between $N$ row vertices and $N$ column vertices, an edge is uniquely determined iff it is not part of any directed alternating cycle. Therefore, the set of non-fixed entries corresponds to the union of non-trivial strongly connected components (SCCs) of size $(u_i, v_i)$ with $u_i \ge 2, v_i \ge 2$. Each such component contributes $u_i \times v_i$ non-fixed cells. The problem reduces to a 2D knapsack DP determining all achievable values of $\sum u_i v_i$ subject to $\sum u_i \le N$ and $\sum v_i \le N$.

## 3. Step-by-Step Algorithm
1. 1. Define a 3D bitset DP: $dp[u][v]$ storing reachable sums of $u_i v_i$ using $u$ row vertices and $v$ column vertices.
2. 2. Initialize $dp[0][0][0] = 1$.
3. 3. Iterate over all possible SCC sizes $a \in [2, N]$ and $b \in [2, N]$:
4.    - For each valid $(a, b)$, update transitions $dp[u + a][v + b] |= (dp[u][v] \ll (a \cdot b))$.
5. 4. Collect all achievable values of $K$ across all $u \le N, v \le N$.
6. 5. Answer each query $K$ in $O(1)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^4 / 64 + Q)`
- **Space Complexity**: `O(N^4 / 64)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    if (!(cin >> N >> Q)) return 0;

    // dp[r][c] is bitset of achievable unfixed entries
    bitset<905> dp[35][35];
    dp[0][0][0] = 1;

    for (int u = 2; u <= N; ++u) {
        for (int v = 2; v <= N; ++v) {
            int e_add = u * v;
            for (int r = 0; r <= N - u; ++r) {
                for (int c = 0; c <= N - v; ++c) {
                    dp[r + u][c + v] |= (dp[r][c] << e_add);
                }
            }
        }
    }

    bitset<905> reachable;
    for (int r = 0; r <= N; ++r) {
        for (int c = 0; c <= N; ++c) {
            reachable |= dp[r][c];
        }
    }

    int total_cells = N * N;
    while (Q--) {
        int K;
        cin >> K;
        int unfixed = total_cells - K;
        if (unfixed >= 0 && unfixed <= total_cells && reachable[unfixed]) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
