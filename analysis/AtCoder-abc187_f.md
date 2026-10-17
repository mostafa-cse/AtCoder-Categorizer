# Problem Analysis: AtCoder-abc187_f — Close Group

**Problem ID**: `AtCoder-abc187_f`  
**Contest**: `abc187`  
**Rating / Difficulty**: 1895  
**URL**: https://atcoder.jp/contests/abc187/tasks/abc187_f  
**VJudge Tag**: `[problem:AtCoder-abc187_f]`  
**Category File**: [`../categories/dp/minimum_clique_partition_submask_dp.md`](../categories/dp/minimum_clique_partition_submask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Bitmask DP`  
- **Topic (Skill)**: `Minimum Clique Partition via O(3^N) Submask Enumeration DP`  

---

## 1. Problem Statement & Key Idea
Given an undirected graph with N vertices (N <= 18) and M edges. Partition the vertices into the minimum number of subsets such that every subset induces a clique (complete graph).

**Key Insight**: Step 1: Identify all subsets mask that are cliques in O(N * 2^N). For these subsets, dp[mask] = 1. Step 2: For other subsets, partition into two non-empty disjoint submasks: dp[mask] = min_{sub} (dp[sub] + dp[mask ^ sub]).

## 2. Core Observation & Invariant
Iterating over all submasks for all masks takes O(3^N) = 3^{18} ~ 3.8 * 10^8 operations, running in ~0.3s.

## 3. Step-by-Step Algorithm
1. Build adjacency bitmasks adj[u].
2. Initialize dp[1 << N] = INF.
3. For mask = 1 to (1 << N) - 1:
4.   Check if mask is a clique:
5.   bool ok = true;
6.   for i in mask: if ((mask & adj[i]) != (mask ^ (1 << i))) { ok = false; break; }
7.   if ok: dp[mask] = 1;
8. For mask = 1 to (1 << N) - 1:
9.   if dp[mask] == 1: continue;
10.   sub = (mask - 1) & mask;
11.   while sub > (mask ^ sub):
12.     dp[mask] = min(dp[mask], dp[sub] + dp[mask ^ sub]);
13.     sub = (sub - 1) & mask;
14. Print dp[(1 << N) - 1].

## 4. Complexity Analysis
- **Time Complexity**: `O(3^N)`
- **Space Complexity**: `O(2^N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> adj(n, 0);
    for (int i = 0; i < n; ++i) adj[i] |= (1 << i);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u] |= (1 << v);
        adj[v] |= (1 << u);
    }

    int total_masks = 1 << n;
    vector<int> dp(total_masks, INF);

    // Identify cliques
    for (int mask = 1; mask < total_masks; ++mask) {
        bool is_clique = true;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if ((mask & adj[i]) != mask) {
                    is_clique = false;
                    break;
                }
            }
        }
        if (is_clique) dp[mask] = 1;
    }

    // Submask enumeration DP
    for (int mask = 1; mask < total_masks; ++mask) {
        if (dp[mask] == 1) continue;

        for (int sub = (mask - 1) & mask; sub > (mask ^ sub); sub = (sub - 1) & mask) {
            dp[mask] = min(dp[mask], dp[sub] + dp[mask ^ sub]);
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Solving minimum clique cover using bitmask clique filtering and submask enumeration DP.
- **Reusable Pattern**: `O(3^N) Submask Partition DP: sub = (mask - 1) & mask with symmetry break sub > (mask ^ sub).`
