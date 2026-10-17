# Problem Analysis: AtCoder-agc017_d — Game on Tree

**Problem ID**: `AtCoder-agc017_d`  
**Contest**: `agc017`  
**Rating / Difficulty**: 2156  
**URL**: https://atcoder.jp/contests/agc017/tasks/agc017_d  
**VJudge Tag**: `[problem:AtCoder-agc017_d]`  
**Category File**: [`../categories/game_theory/green_hackenbush_trees_colon_principle.md`](../categories/game_theory/green_hackenbush_trees_colon_principle.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Hackenbush`  
- **Topic (Skill)**: `Green Hackenbush on Trees and Graphs`  

---

## 1. Problem Statement & Key Idea
Determine the winner of Green Hackenbush on a rooted tree where players alternate cutting edges and components disconnected from the root are removed. Solved via the Colon Principle.

## 2. Core Observation & Invariant
According to the Colon Principle in combinatorial game theory, attaching a subtree with Grundy value G(v) to a parent u via a single edge yields an equivalent game with Grundy value G(v) + 1. Multiple branches incident to the same root vertex behave as independent games summed via XOR: G(u) = XOR_{v in children(u)} (G(v) + 1). Alice wins iff G(root) != 0.

## 3. Step-by-Step Algorithm
1. Root the tree arbitrarily at vertex 1.
2. Perform a post-order DFS: for a leaf node, Grundy value is 0.
3. For any internal node u, compute G(u) = XOR_{v in children(u)} (dfs(v) + 1).
4. If G(1) != 0, print "Alice"; otherwise print "Bob".

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>

using namespace std;

int dfs(int u, int p, const vector<vector<int>>& g) {
    int g_val = 0;
    for (int v : g[u]) {
        if (v == p) continue;
        g_val ^= (dfs(v, u, g) + 1);
    }
    return g_val;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    int g_root = dfs(1, 0, g);
    if (g_root != 0) {
        cout << "Alice\n";
    } else {
        cout << "Bob\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
