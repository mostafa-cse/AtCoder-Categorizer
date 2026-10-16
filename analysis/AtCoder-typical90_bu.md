# Problem Analysis: AtCoder-typical90_bu — We Need Both a and b

**Problem ID**: `AtCoder-typical90_bu`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 073)  
**Rating / Difficulty**: 1800 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bu  
**VJudge Tag**: `[problem:AtCoder-typical90_bu]`  
**Category File**: [`../categories/dp/dp_on_trees.md`](../categories/dp/dp_on_trees.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `Tree Component Partition DP with 3 Characteristic States`  

---

## 1. Problem Statement & Key Idea
Tree with N vertices, each vertex labeled 'a' or 'b'. Delete a subset of edges to partition the tree into components such that EVERY component contains BOTH 'a' and 'b'. Count valid edge deletions modulo 10^9+7.

**Core Idea**: Subtree DP tracking the status of the connected component containing node u: (0) only 'a', (1) only 'b', (2) both 'a' and 'b'.

## 2. Core Observation & Invariant
For each child v of u, we can either CUT edge (u, v) (requiring child component to be valid: dp[v][2]), or KEEP edge (u, v) (merging child component into u's component). Use product rule to combine child states.

## 3. Step-by-Step Algorithm
1. Post-order DFS tree DP.
2. For leaf: set dp[leaf][label] = 1, others 0.
3. For node u with children v: combine product of (cut + keep) transitions.
4. Output dp[root][2].

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int n;
vector<char> label;
vector<vector<int>> adj;
long long dp[100005][3];

void dfs(int u, int p) {
    long long prod_all = 1;      // product of (dp[v][label] + 2*dp[v][2])
    long long prod_monochrome = 1; // product of (dp[v][label] + dp[v][2])

    int my_type = (label[u] == 'a' ? 0 : 1);

    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);

        long long term1 = (dp[v][my_type] + dp[v][2]) % MOD;
        prod_monochrome = (prod_monochrome * term1) % MOD;

        long long term2 = (dp[v][0] + dp[v][1] + 2 * dp[v][2]) % MOD;
        prod_all = (prod_all * term2) % MOD;
    }

    dp[u][my_type] = prod_monochrome;
    dp[u][1 - my_type] = 0;
    dp[u][2] = (prod_all - prod_monochrome + MOD) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    label.resize(n + 1);
    for (int i = 1; i <= n; ++i) cin >> label[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);

    cout << dp[1][2] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Tree component partition dynamic programming with 3 component states.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Connected component subtree DP, edge cut/keep branch combination, and modular state invariants.
- **Reusable Pattern**: `Tree Component Partition DP.`

---
Back to [Tree Component Partition DP with 3 Characteristic States](../categories/dp/dp_on_trees.md) | [Categories Directory](../categories/README.md)