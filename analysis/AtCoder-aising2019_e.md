# Problem Analysis: AtCoder-aising2019_e — E - Attack to a Tree

**Problem ID**: `AtCoder-aising2019_e`  
**Contest**: `aising2019`  
**Rating / Difficulty**: 2595  
**URL**: https://atcoder.jp/contests/aising2019/tasks/aising2019_e  
**VJudge Tag**: `[problem:AtCoder-aising2019_e]`  
**Category File**: [`../categories/dynamic_programming_dp/attack_to_a_tree_knapsack_dp.md`](../categories/dynamic_programming_dp/attack_to_a_tree_knapsack_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `More Tricks`  
- **Topic (Skill)**: `Combining Subtrees Technique`  

---

## 1. Problem Statement & Key Idea
Find the minimum number of edge removals in a vertex-weighted tree so that every connected component has a positive sum.

## 2. Core Observation & Invariant
In each connected component, vertices can be deactivated or partitioned by cutting edges. For each subtree rooted at $u$, we maintain tree knapsack DP states: the minimum cuts to make all separated subtrees valid, distinguishing whether the connected component containing $u$ has a strictly positive sum ($dp_1$) or a negative/arbitrary sum ($dp_2$). Tree knapsack merging takes $O(N^2)$ total time.

## 3. Step-by-Step Algorithm
1. 1. Root tree arbitrarily at vertex 1.
2. 2. For each node $u$ with subtree size $sz_u$, maintain $dp[u][k]$: the minimal component sum for $k$ cuts in $u$'s subtree.
3. 3. Merge child subtrees using standard size-bounded tree knapsack transitions in $O(sz_u \cdot sz_v)$.
4. 4. If a component sum $> 0$, it can be finalized by cutting the edge to its parent.
5. 5. The answer is the minimum $k$ such that the root component sum is positive.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int N;
vector<long long> A;
vector<vector<int>> adj;

pair<pair<vector<long long>, vector<long long>>, int> dfs(int u, int p) {
    vector<long long> dp1 = {INF, INF};
    vector<long long> dp2 = {INF, INF};
    if (A[u] > 0) dp1[1] = A[u];
    dp2[1] = A[u];
    int sz = 1;

    for (int v : adj[u]) {
        if (v == p) continue;
        auto child = dfs(v, u);
        auto& cdp1 = child.first.first;
        auto& cdp2 = child.first.second;
        int csz = child.second;

        int new_sz = sz + csz;
        vector<long long> new_dp1(new_sz + 1, INF);
        vector<long long> new_dp2(new_sz + 1, INF);

        for (int j = 1; j <= sz; ++j) {
            long long v1 = dp1[j], v2 = dp2[j];
            if (v1 == INF && v2 == INF) continue;
            for (int k = 1; k <= csz; ++k) {
                long long cv1 = cdp1[k], cv2 = cdp2[k];
                // Option 1: Cut edge (u, v)
                if (cv1 != INF || cv2 < 0) {
                    if (v1 != INF) new_dp1[j + k] = min(new_dp1[j + k], v1);
                    if (v2 != INF) new_dp2[j + k] = min(new_dp2[j + k], v2);
                }
                // Option 2: Do not cut edge (u, v)
                if (v1 != INF && cv1 != INF) {
                    new_dp1[j + k - 1] = min(new_dp1[j + k - 1], v1 + cv1);
                }
                if (v2 != INF && cv2 != INF) {
                    new_dp2[j + k - 1] = min(new_dp2[j + k - 1], v2 + cv2);
                }
                if (v1 != INF && cv2 != INF) {
                    new_dp2[j + k - 1] = min(new_dp2[j + k - 1], v1 + cv2);
                }
                if (v2 != INF && cv1 != INF) {
                    new_dp2[j + k - 1] = min(new_dp2[j + k - 1], v2 + cv1);
                }
            }
        }
        dp1 = move(new_dp1);
        dp2 = move(new_dp2);
        sz = new_sz;
    }

    return {{dp1, dp2}, sz};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;
    A.resize(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    adj.resize(N);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto root_res = dfs(0, -1);
    auto& dp1 = root_res.first.first;
    auto& dp2 = root_res.first.second;

    for (int k = 1; k <= N; ++k) {
        if (dp1[k] != INF || dp2[k] < 0) {
            cout << k - 1 << "\n";
            return 0;
        }
    }

    cout << -1 << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
