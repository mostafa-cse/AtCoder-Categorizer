# Problem Analysis: AtCoder-arc097_b — Equals

**Problem ID**: `AtCoder-arc097_b`  
**Contest**: `abc097`  
**Rating / Difficulty**: 1270  
**URL**: https://atcoder.jp/contests/abc097/tasks/arc097_b  
**VJudge Tag**: `[problem:AtCoder-arc097_b]`  
**Category File**: [`../categories/data_structures/dsu_permutation_cycles.md`](../categories/data_structures/dsu_permutation_cycles.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Disjoint Set Union`  
- **Topic (Skill)**: `Permutation Position Cycles via DSU`  

---

## 1. Problem Statement & Key Idea
Given permutation p_1..p_N. You can swap p_{x_j} and p_{y_j} for M given pairs (x_j, y_j) any number of times. Maximize the count of indices i where p_i == i.

**Key Idea**: Swapping elements between indices x and y connects them in a permutation graph. Any two positions in the same connected component can have their values interchanged arbitrarily.

## 2. Core Observation & Invariant
Build a Disjoint Set Union (DSU) where each given pair (x, y) unites the positions x and y. An element p_i can eventually be placed at position i if and only if its current position i and its target position p_i belong to the SAME connected component: find(i) == find(p_i)!

## 3. Step-by-Step Algorithm
1. Initialize DSU on N elements.
2. For each swap pair (x, y): unite(x, y).
3. Initialize count = 0.
4. For each i from 1 to N: if find(i) == find(p[i]): count++.
5. Print count.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) * alpha(N))`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> p(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
    }

    DSU dsu(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        dsu.unite(u, v);
    }

    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        if (dsu.find(i) == dsu.find(p[i])) {
            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Determining reachable permutation states via DSU connected components.
- **Reusable Pattern**: `Reachable permutation fixed points: find(current_index) == find(target_index).`
