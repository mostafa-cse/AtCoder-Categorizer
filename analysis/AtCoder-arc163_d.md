# Problem Analysis: AtCoder-arc163_d — D. Sum of SCC

**Problem ID**: `AtCoder-arc163_d`  
**Contest**: `arc163`  
**Rating / Difficulty**: 2581  
**URL**: https://atcoder.jp/contests/arc163/tasks/arc163_d  
**VJudge Tag**: `[problem:AtCoder-arc163_d]`  
**Category File**: [`../categories/graph_theory/tournament_graph_scc_condensation_inversion_dp.md`](../categories/graph_theory/tournament_graph_scc_condensation_inversion_dp.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Special Graphs`  
- **Topic (Skill)**: `Tournament Graph`  

---

## 1. Problem Statement & Key Idea
Find the total number of SCCs across all tournaments on $N$ vertices with exactly $M$ forward edges.

## 2. Core Observation & Invariant
In any tournament, the condensation is a linear order $C_1 \to \dots \to C_k$. The number of SCCs is $1 + \sum_{A \subset V, A \ne \emptyset, A \ne V} [\text{all edges } A \to V \setminus A]$. The cross-edge forward count is the number of inversions $\text{inv}(A, V \setminus A)$, while internal edges can be chosen freely.

## 3. Step-by-Step Algorithm
1. 1. Precompute binomial coefficients up to $\binom{N}{2}$.
2. 2. Compute $DP[i][a][c]$: number of subsets of $\{1, \dots, i\}$ of size $a$ with $c$ cross pairs $(u \in A, v \in B, u < v)$.
3. 3. Base tournaments with $M$ forward edges is $\binom{\binom{N}{2}}{M}$.
4. 4. For each partition size $a \in [1, N-1]$ and cross forward count $c \le M$, multiply $DP[N][a][c]$ by $\binom{\binom{a}{2} + \binom{N-a}{2}}{M - c}$ and accumulate.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 M)`
- **Space Complexity**: `O(N M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    int total_edges = N * (N - 1) / 2;
    if (M < 0 || M > total_edges) {
        cout << 0 << "\n";
        return 0;
    }

    vector<vector<long long>> C(total_edges + 1, vector<long long>(total_edges + 1, 0));
    for (int i = 0; i <= total_edges; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    vector<vector<long long>> dp(N + 1, vector<long long>(total_edges + 1, 0));
    dp[0][0] = 1;

    for (int i = 0; i < N; ++i) {
        vector<vector<long long>> next_dp(N + 1, vector<long long>(total_edges + 1, 0));
        for (int a = 0; a <= i; ++a) {
            for (int c = 0; c <= total_edges; ++c) {
                long long ways = dp[a][c];
                if (!ways) continue;
                if (a + 1 <= N) {
                    next_dp[a + 1][c] = (next_dp[a + 1][c] + ways) % MOD;
                }
                if (c + a <= total_edges) {
                    next_dp[a][c + a] = (next_dp[a][c + a] + ways) % MOD;
                }
            }
        }
        dp = move(next_dp);
    }

    long long ans = C[total_edges][M];
    for (int a = 1; a < N; ++a) {
        int internal_edges = a * (a - 1) / 2 + (N - a) * (N - a - 1) / 2;
        for (int c = 0; c <= M; ++c) {
            long long ways_A = dp[a][c];
            if (!ways_A) continue;
            int rem_edges = M - c;
            if (rem_edges <= internal_edges) {
                long long ways_orient = C[internal_edges][rem_edges];
                ans = (ans + ways_A * ways_orient) % MOD;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
