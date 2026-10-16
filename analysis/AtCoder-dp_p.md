# Problem Analysis: AtCoder-dp_p — Independent Set

**Problem ID**: `AtCoder-dp_p`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1500  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_p  
**VJudge Tag**: `[problem:AtCoder-dp_p]`  
**Category File**: [`../categories/dp/dp_on_trees.md`](../categories/dp/dp_on_trees.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Count ways to paint vertices of a tree black or white such that no two adjacent vertices are both black.

**Core Idea**: Root tree arbitrarily. Maintain two states: dp[u][White] and dp[u][Black].

## 2. Core Observation & Invariant
If node u is Black, all children must be White. If u is White, each child can be independently either Black or White.

## 3. Step-by-Step Algorithm
1. Post-order DFS(u, parent).
2. dp[u][Black] = prod_{v in children} dp[v][White].
3. dp[u][White] = prod_{v in children} (dp[v][Black] + dp[v][White]).
4. Return (dp[root][Black] + dp[root][White]) mod MOD.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

void dfs(int u, int p, const vector<vector<int>>& adj, vector<long long>& white, vector<long long>& black) {
    white[u] = 1;
    black[u] = 1;

    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u, adj, white, black);
        white[u] = (white[u] * ((white[v] + black[v]) % MOD)) % MOD;
        black[u] = (black[u] * white[v]) % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> white(n + 1, 1), black(n + 1, 1);
    dfs(1, 0, adj, white, black);

    cout << (white[1] + black[1]) % MOD << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Tree independent set combinatorial DP.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Subtree DP, state-color branching, and product-rule combination over tree children.
- **Reusable Pattern**: `Two-state subtree product DP on trees.`

---
Back to [DP on Trees and DAGs](../categories/dp/dp_on_trees.md) | [Categories Directory](../categories/README.md)