# Problem Analysis: AtCoder-abc188_e — Peddler

**Problem ID**: `AtCoder-abc188_e`  
**Contest**: `abc188`  
**Rating / Difficulty**: 1170  
**URL**: https://atcoder.jp/contests/abc188/tasks/abc188_e  
**VJudge Tag**: `[problem:AtCoder-abc188_e]`  
**Category File**: [`../categories/dp/dag_minimum_ancestor_cost_dp.md`](../categories/dp/dag_minimum_ancestor_cost_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `DAG DP`  
- **Topic (Skill)**: `DAG Topological Minimum Ancestor Cost DP`  

---

## 1. Problem Statement & Key Idea
N towns in a DAG with edges X_i -> Y_i (X_i < Y_i). Gold price at town i is A_i. Buy gold at town x and sell at town y reachable from x. Maximize profit A_y - A_x.

**Key Idea**: For each town v, we want to know the minimum gold price among all towns that can reach v: min_anc[v].

## 2. Core Observation & Invariant
Since edges strictly satisfy X_i < Y_i, vertices 1..N are already topologically sorted! Process u from 1 to N: initialize min_anc[v] = INF. For each neighbor v of u, update min_anc[v] = min({min_anc[v], min_anc[u], A_u}). The maximum profit selling at v is A_v - min_anc[v].

## 3. Step-by-Step Algorithm
1. Initialize min_anc array of size N + 1 to INF.
2. Iterate u from 1 to N: for each edge u -> v: min_anc[v] = min({min_anc[v], min_anc[u], A[u]}).
3. Initialize max_profit = -INF.
4. For v from 1 to N: if min_anc[v] != INF: max_profit = max(max_profit, A[v] - min_anc[v]).
5. Output max_profit.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    vector<long long> min_anc(n + 1, INF);
    long long max_profit = -INF;

    for (int u = 1; u <= n; ++u) {
        if (min_anc[u] != INF) {
            max_profit = max(max_profit, a[u] - min_anc[u]);
        }
        long long current_min = min(min_anc[u], a[u]);
        for (int v : adj[u]) {
            min_anc[v] = min(min_anc[v], current_min);
        }
    }

    cout << max_profit << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Propagating extremal ancestor values along DAG topological order.
- **Reusable Pattern**: `DAG min ancestor: min_anc[v] = min(min_anc[v], min(min_anc[u], cost[u])).`
