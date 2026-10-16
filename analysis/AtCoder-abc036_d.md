# Problem Analysis: AtCoder-abc036_d — Coloring

**Problem ID**: `AtCoder-abc036_d`  
**Contest**: `abc036`  
**Rating / Difficulty**: 1602  
**URL**: https://atcoder.jp/contests/abc036/tasks/abc036_d  
**VJudge Tag**: `[problem:AtCoder-abc036_d]`  
**Category File**: [`../categories/dp/tree_dp_independent_set_coloring.md`](../categories/dp/tree_dp_independent_set_coloring.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Tree DP`  
- **Topic (Skill)**: `Tree DP: White or Black Coloring with No Adjacent Black Nodes`  

---

## 1. Problem Statement & Key Idea
Given a tree of N islands connected by N - 1 bridges. Color each island White or Black such that no two adjacent islands are both Black. Find the number of valid colorings, modulo 10^9 + 7.

**Key Insight**: Classic Tree DP modeling independent sets. For each node u, maintain dp[u][0] (u is White) and dp[u][1] (u is Black). If u is White, children can be White or Black; if u is Black, children MUST be White.

## 2. Core Observation & Invariant
Transitions for node u with children v: dp[u][0] = prod_{v} (dp[v][0] + dp[v][1]) % MOD; dp[u][1] = prod_{v} dp[v][0] % MOD. Answer is (dp[root][0] + dp[root][1]) % MOD.

## 3. Step-by-Step Algorithm
1. Root tree at 1 and run post-order DFS.
2. Base case for leaves: dp[leaf][0] = 1, dp[leaf][1] = 1.
3. For internal node u:
4.   w_ways = 1, b_ways = 1.
5.   For each child v of u:
6.     w_ways = (w_ways * (dp[v][0] + dp[v][1])) % MOD.
7.     b_ways = (b_ways * dp[v][0]) % MOD.
8.   dp[u][0] = w_ways, dp[u][1] = b_ways.
9. Print (dp[1][0] + dp[1][1]) % MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

vector<vector<int>> adj;
vector<long long> dp0, dp1;

void dfs(int u, int p) {
    dp0[u] = 1;
    dp1[u] = 1;

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
            dp0[u] = (dp0[u] * (dp0[v] + dp1[v])) % MOD;
            dp1[u] = (dp1[u] * dp0[v]) % MOD;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    adj.resize(n + 1);
    dp0.resize(n + 1);
    dp1.resize(n + 1);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);

    long long ans = (dp0[1] + dp1[1]) % MOD;
    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Tree independent set DP with 2-state child product transitions.
- **Reusable Pattern**: `Tree Vertex Coloring DP: dp[u][0] = prod(dp[v][0]+dp[v][1]), dp[u][1] = prod(dp[v][0]).`
