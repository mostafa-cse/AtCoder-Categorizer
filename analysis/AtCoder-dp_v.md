# Problem Analysis: AtCoder-dp_v — Subtree

**Problem ID**: `AtCoder-dp_v`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 2100  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_v  
**VJudge Tag**: `[problem:AtCoder-dp_v]`  
**Category File**: [`../categories/dp/dp_on_trees.md`](../categories/dp/dp_on_trees.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `Tree DP with Subtree Rerooting without Division`  

---

## 1. Problem Statement & Key Idea
For every vertex v in a tree, compute the number of black-connected components containing v modulo M (M may not be prime).

**Core Idea**: Reroot the tree in O(N) using two DFS passes. Because M is composite, division by (down[child] + 1) is illegal; prefix and suffix products of children answers exclude a child in O(1) without division.

## 2. Core Observation & Invariant
For each node, children values can be preprocessed into prefix and suffix cumulative products. Excluded child contribution is calculated by multiplying prefix[:i-1] * suffix[i+1:].

## 3. Step-by-Step Algorithm
1. DFS1: down[u] = prod_{v in children} (down[v] + 1) mod M.
2. DFS2: compute parent contribution up[u] using prefix and suffix products of sibling values.
3. Ans[u] = down[u] * (up[u] + 1) mod M.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int n;
long long M;
vector<vector<int>> adj;
vector<long long> down_dp, ans;

void dfs1(int u, int p) {
    down_dp[u] = 1;
    for (int v : adj[u]) {
        if (v == p) continue;
        dfs1(v, u);
        down_dp[u] = (down_dp[u] * (down_dp[v] + 1)) % M;
    }
}

void dfs2(int u, int p, long long up_val) {
    ans[u] = (down_dp[u] * (up_val + 1)) % M;

    vector<int> children;
    for (int v : adj[u]) {
        if (v != p) children.push_back(v);
    }

    int deg = children.size();
    if (deg == 0) return;

    vector<long long> pref(deg + 1, 1), suff(deg + 1, 1);
    for (int i = 0; i < deg; ++i) {
        pref[i + 1] = (pref[i] * (down_dp[children[i]] + 1)) % M;
    }
    for (int i = deg - 1; i >= 0; --i) {
        suff[i] = (suff[i + 1] * (down_dp[children[i]] + 1)) % M;
    }

    for (int i = 0; i < deg; ++i) {
        int v = children[i];
        long long next_up = (up_val + 1) % M;
        next_up = (next_up * pref[i]) % M;
        next_up = (next_up * suff[i + 1]) % M;
        dfs2(v, u, next_up);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> M)) return 0;
    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    down_dp.assign(n + 1, 1);
    ans.assign(n + 1, 0);

    dfs1(1, 0);
    dfs2(1, 0, 0);

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
All-roots tree DP rerooting with non-invertible operators.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Tree rerooting technique without modular division via prefix/suffix product arrays.
- **Reusable Pattern**: `Division-free prefix/suffix rerooting on trees.`

---
Back to [Tree DP with Subtree Rerooting without Division](../categories/dp/dp_on_trees.md) | [Categories Directory](../categories/README.md)