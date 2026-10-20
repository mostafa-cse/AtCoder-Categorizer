# Problem Analysis: AtCoder-arc078_d — F - Mole and Abandoned Mine

**Problem ID**: `AtCoder-arc078_d`  
**Contest**: `arc078`  
**Rating / Difficulty**: 2956  
**URL**: https://atcoder.jp/contests/arc078/tasks/arc078_d  
**VJudge Tag**: `[problem:AtCoder-arc078_d]`  
**Category File**: [`../categories/dynamic_programming/unique_simple_path_submask_enumeration_bitmask_dp.md`](../categories/dynamic_programming/unique_simple_path_submask_enumeration_bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
In a connected undirected weighted graph with N <= 15 vertices, find the minimum total cost of edges to destroy such that there exists exactly one simple path between vertex 1 and vertex N.

## 2. Core Observation & Invariant
Minimizing destroyed edges is equivalent to maximizing the sum of costs of kept edges. The condition of a unique simple path between 1 and N implies that the kept subgraph consists of a simple path v_1, v_2, ..., v_k (v_1=1, v_k=N), where each vertex v_i is attached to a connected component C_i of vertices disjoint from all other components, and NO edges exist between C_i and C_j (i != j) except the path edges (v_i, v_{i+1}). Within each component C_i, ALL internal edges may be kept.

## 3. Step-by-Step Algorithm
1. 1. Precompute intra[mask]: the sum of weights of all edges with both endpoints inside mask.
2. 2. Define dp[mask][u]: maximum kept edge weight using vertex subset mask with active path endpoint at u.
3. 3. Base case: for every mask C containing 1 and not containing N, dp[C][0] = intra[C].
4. 4. Transitions: from dp[mask][u], choose next path vertex v not in mask adjacent to u. Enumerate all subsets of unused vertices sub to form component C = sub U {v}. Update dp[mask | C][v] = max(..., dp[mask][u] + weight(u, v) + intra[C]).
5. 5. The maximum kept edges is max_{mask} dp[mask][N-1]. Subtract from total graph edge weight.

## 4. Complexity Analysis
- **Time Complexity**: `O(3^N * N + 2^N * N^2)`
- **Space Complexity**: `O(2^N * N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<int>> adj(N, vector<int>(N, 0));
    vector<vector<bool>> has_edge(N, vector<bool>(N, false));
    long long total_cost = 0;

    for (int i = 0; i < M; ++i) {
        int u, v, c;
        cin >> u >> v >> c;
        --u; --v;
        adj[u][v] = c;
        adj[v][u] = c;
        has_edge[u][v] = true;
        has_edge[v][u] = true;
        total_cost += c;
    }

    int full_mask = (1 << N);
    vector<int> intra(full_mask, 0);

    for (int mask = 1; mask < full_mask; ++mask) {
        int lsb = __builtin_ctz(mask);
        int rest = mask ^ (1 << lsb);
        intra[mask] = intra[rest];
        for (int i = 0; i < N; ++i) {
            if ((rest >> i) & 1) {
                if (has_edge[lsb][i]) {
                    intra[mask] += adj[lsb][i];
                }
            }
        }
    }

    vector<vector<int>> dp(full_mask, vector<int>(N, -1));

    for (int C = 1; C < full_mask; ++C) {
        if ((C & 1) && !((C >> (N - 1)) & 1)) {
            dp[C][0] = intra[C];
        }
    }

    for (int mask = 1; mask < full_mask; ++mask) {
        for (int u = 0; u < N; ++u) {
            if (dp[mask][u] < 0) continue;
            int cur_val = dp[mask][u];

            int rem = (full_mask - 1) ^ mask;

            for (int v = 0; v < N; ++v) {
                if (!((mask >> v) & 1) && has_edge[u][v]) {
                    int valid_rem = rem;
                    if (v != N - 1) {
                        valid_rem &= ~(1 << (N - 1));
                    }

                    int sub_rem = valid_rem ^ (1 << v);
                    int sub = sub_rem;
                    while (true) {
                        int C = sub | (1 << v);
                        int cand = cur_val + adj[u][v] + intra[C];
                        int nxt_mask = mask | C;
                        if (cand > dp[nxt_mask][v]) {
                            dp[nxt_mask][v] = cand;
                        }
                        if (sub == 0) break;
                        sub = (sub - 1) & sub_rem;
                    }
                }
            }
        }
    }

    int max_kept = 0;
    for (int mask = 0; mask < full_mask; ++mask) {
        if (dp[mask][N - 1] > max_kept) {
            max_kept = dp[mask][N - 1];
        }
    }

    cout << total_cost - max_kept << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
