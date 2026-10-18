# Problem Analysis: AtCoder-abc213_g — Connectivity 2

**Problem ID**: `AtCoder-abc213_g`  
**Contest**: `abc213`  
**Rating / Difficulty**: 2663  
**URL**: https://atcoder.jp/contests/abc213/tasks/abc213_g  
**VJudge Tag**: `[problem:AtCoder-abc213_g]`  
**Category File**: [`../categories/dynamic_programming_dp/connectivity_2_subgraph_dp.md`](../categories/dynamic_programming_dp/connectivity_2_subgraph_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Subset Convolution`  

---

## 1. Problem Statement & Key Idea
Count subgraphs where Vertex 1 is connected to Vertex k using connected component subset DP to enumerate connected induced subgraphs, then summing over all components containing both 1 and k.

## 2. Core Observation & Invariant
For each vertex subset S, compute C[S] = number of connected subgraphs on S by subtracting non-connected subgraphs (partitioning on the connected component containing the lowest set bit of S). In the full graph, if S is the connected component containing vertex 1, all edges inside S are chosen in C[S] ways, edges in V \ S are chosen in 2^(e(V \ S)) ways, and no cross-edges exist. Summing over all S containing {1, k} gives the exact answer.

## 3. Step-by-Step Algorithm
1. 1. Precompute edge count e[mask] for all 2^N subsets.
2. 2. Compute C[mask] using submask DP: C[mask] = 2^e[mask] - sum_{T subset mask, v in T, T != mask} C[T] * 2^e[mask ^ T].
3. 3. For each subset S containing vertex 0 (Vertex 1), calculate term = C[S] * 2^e[ALL ^ S].
4. 4. Add term to ans[k] for each k in S.
5. 5. Output ans[k] for each k = 2..N.

## 4. Complexity Analysis
- **Time Complexity**: `O(3^N)`
- **Space Complexity**: `O(2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const long long MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<bool>> adj(N, vector<bool>(N, false));
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u][v] = adj[v][u] = true;
    }

    int total_masks = 1 << N;
    vector<int> e(total_masks, 0);

    for (int mask = 1; mask < total_masks; ++mask) {
        int v = __builtin_ctz(mask);
        int rest = mask ^ (1 << v);
        int cnt = 0;
        for (int u = 0; u < N; ++u) {
            if ((rest & (1 << u)) && adj[v][u]) {
                cnt++;
            }
        }
        e[mask] = e[rest] + cnt;
    }

    vector<long long> pow2(M + 1, 1);
    for (int i = 1; i <= M; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    vector<long long> C(total_masks, 0);
    for (int mask = 1; mask < total_masks; ++mask) {
        int v = __builtin_ctz(mask);
        int rest = mask ^ (1 << v);
        int sub = rest;
        long long total_non_conn = 0;

        while (true) {
            int T = sub | (1 << v);
            if (T != mask) {
                total_non_conn = (total_non_conn + C[T] * pow2[e[mask ^ T]]) % MOD;
            }
            if (sub == 0) break;
            sub = (sub - 1) & rest;
        }

        C[mask] = (pow2[e[mask]] - total_non_conn + MOD) % MOD;
    }

    int ALL = total_masks - 1;
    vector<long long> ans(N, 0);

    for (int S = 1; S < total_masks; ++S) {
        if (!(S & 1)) continue; // Must contain vertex 0 (Vertex 1)
        long long term = C[S] * pow2[e[ALL ^ S]] % MOD;
        for (int k = 1; k < N; ++k) {
            if (S & (1 << k)) {
                ans[k] = (ans[k] + term) % MOD;
            }
        }
    }

    for (int k = 1; k < N; ++k) {
        cout << ans[k] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
