# Problem Analysis: AtCoder-abc411_g — Count Cycles

**Problem ID**: `AtCoder-abc411_g`  
**Contest**: `abc411`  
**Rating / Difficulty**: 2088  
**URL**: https://atcoder.jp/contests/abc411/tasks/abc411_g  
**VJudge Tag**: `[problem:AtCoder-abc411_g]`  
**Category File**: [`../categories/graph_theory/meet_in_the_middle_dense_cycle_counting.md`](../categories/graph_theory/meet_in_the_middle_dense_cycle_counting.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Cycles`  
- **Topic (Skill)**: `Cycle Detection`  

---

## 1. Problem Statement & Key Idea
Given an undirected graph with N vertices and M edges without multi-edges or self-loops, find the number of simple cycles in the graph modulo 998244353, where N <= 20.

**Key Insight**: With N <= 20, we can use Bitmask DP to count simple cycles. Every simple cycle has a unique minimum-indexed vertex v_0. For each choice of v_0 in [0, N-1], consider the induced subgraph on vertices {v_0, v_0 + 1, ..., N-1}. We define dp[mask][u] as the number of simple paths starting at v_0 and ending at u using the subset of vertices mask (with v_0 always included). A cycle is closed when an edge exists from u back to v_0 and the cycle has length >= 3. Since every cycle is counted in both directions (clockwise and counterclockwise), we sum all valid closures and divide by 2.

## 2. Core Observation & Invariant
Fixing the lexicographically smallest vertex v_0 in each cycle eliminates duplicate counting across different starting vertices; bitmask path DP counts all cycles of length >= 3 in O(2^N * N^2).

## 3. Step-by-Step Algorithm
1. Represent adjacency matrix using bitmasks.
2. Initialize total_cycles = 0.
3. For each starting vertex v_0 from 0 to N - 1:
4.   Define dp[mask][u] where mask is a subset of {v_0..N-1} containing v_0.
5.   dp[1 << v_0][v_0] = 1.
6.   For each mask containing v_0:
7.     For each endpoint u in mask with dp[mask][u] > 0:
8.       For each neighbor w > v_0 of u not in mask:
9.         dp[mask | (1 << w)][w] = (dp[mask | (1 << w)][w] + dp[mask][u]) % MOD.
10.       If __builtin_popcount(mask) >= 3 and edge(u, v_0) exists:
11.         total_cycles = (total_cycles + dp[mask][u]) % MOD.
12. Each cycle was traversed in 2 directions, so ans = total_cycles * inv(2) % MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^N * N^2)`
- **Space Complexity**: `O(2^N * N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Bitmask path DP with canonical minimum-vertex anchoring for exact simple cycle enumeration.
- **Reusable Pattern**: Fix minimum vertex v_0 and grow simple paths on subset masks to count simple cycles without duplicate permutations.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> adj(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u] |= (1 << v);
        adj[v] |= (1 << u);
    }

    long long total_cycles = 0;

    for (int v0 = 0; v0 < n; ++v0) {
        int sub_size = n - v0;
        int num_masks = 1 << sub_size;
        vector<vector<int>> dp(num_masks, vector<int>(sub_size, 0));

        dp[1][0] = 1;

        for (int mask = 1; mask < num_masks; ++mask) {
            for (int u_rel = 0; u_rel < sub_size; ++u_rel) {
                int ways = dp[mask][u_rel];
                if (!ways) continue;

                int u = v0 + u_rel;

                // Check if can close cycle to v0
                if (__builtin_popcount(mask) >= 3 && ((adj[u] >> v0) & 1)) {
                    total_cycles = (total_cycles + ways) % MOD;
                }

                int available_neighbors = adj[u] >> v0;
                int candidate_mask = available_neighbors & ~mask;

                while (candidate_mask > 0) {
                    int w_rel = __builtin_ctz(candidate_mask);
                    candidate_mask &= candidate_mask - 1;
                    int next_mask = mask | (1 << w_rel);
                    dp[next_mask][w_rel] = (dp[next_mask][w_rel] + ways) % MOD;
                }
            }
        }
    }

    long long inv2 = (MOD + 1) / 2;
    long long ans = (total_cycles % MOD * inv2) % MOD;
    cout << ans << "\n";

    return 0;
}
```
