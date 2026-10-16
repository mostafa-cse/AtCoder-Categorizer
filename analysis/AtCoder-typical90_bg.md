# Problem Analysis: AtCoder-typical90_bg — Many Graph Queries

**Problem ID**: `AtCoder-typical90_bg`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 059)  
**Rating / Difficulty**: 2600 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bg  
**VJudge Tag**: `[problem:AtCoder-typical90_bg]`  
**Category File**: [`../categories/data_structures/bitset_optimizations.md`](../categories/data_structures/bitset_optimizations.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Bitset Optimization`  
- **Topic (Skill)**: `Batch Bitset Acceleration on DAG Reachability Queries`  

---

## 1. Problem Statement & Key Idea
Directed Acyclic Graph (DAG) with N <= 60000 vertices, M <= 100000 edges. Q <= 100000 queries: can A_i reach B_i? Output 'Yes' or 'No' for each query.

**Core Idea**: Single reachability takes O(N + M). With 10^5 queries, naive is TLE. Bit-parallelism processes 64 queries simultaneously using 64-bit integers.

## 2. Core Observation & Invariant
Group queries into batches of size W = 64. For each batch, dp[u] is a 64-bit integer representing reachability to the target of query q in the batch. Propagate backwards along topological order.

## 3. Step-by-Step Algorithm
1. Topologically sort vertices.
2. Divide Q queries into chunks of 64.
3. For each chunk: initialize dp[target_q] |= (1ULL << q).
4. In reverse topological order: dp[u] = OR_{v in adj[u]} dp[v].
5. Check if dp[start_q] has bit q set.

## 4. Complexity Analysis
Time: O((Q / 64) * (N + M)), Space: O(N + M).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Query {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].u >> queries[i].v;
    }

    vector<bool> ans(q, false);

    // Process in batches of 64
    for (int b = 0; b < q; b += 64) {
        int cur_batch = min(64, q - b);
        vector<uint64_t> dp(n + 1, 0);

        for (int i = 0; i < cur_batch; ++i) {
            dp[queries[b + i].v] |= (1ULL << i);
        }

        // Vertices are already topologically numbered 1..N (edges only go u < v)
        for (int u = n; u >= 1; --u) {
            for (int v : adj[u]) {
                dp[u] |= dp[v];
            }
        }

        for (int i = 0; i < cur_batch; ++i) {
            if ((dp[queries[b + i].u] >> i) & 1ULL) {
                ans[b + i] = true;
            }
        }
    }

    for (int i = 0; i < q; ++i) {
        cout << (ans[i] ? "Yes\n" : "No\n");
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Batch-parallel 64-bit word bitset acceleration on topological DAG transitions.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bit parallelism on word-level operations, batching queries, and topological reachability.
- **Reusable Pattern**: `Batch Bitset DAG Reachability.`

---
Back to [Batch Bitset Acceleration on DAG Reachability Queries](../categories/data_structures/bitset_optimizations.md) | [Categories Directory](../categories/README.md)