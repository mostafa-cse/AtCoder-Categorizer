# Problem Analysis: AtCoder-arc090_b — People on a Line

**Problem ID**: `AtCoder-arc090_b`  
**Contest**: `abc087`  
**Rating / Difficulty**: 1452  
**URL**: https://atcoder.jp/contests/abc087/tasks/arc090_b  
**VJudge Tag**: `[problem:AtCoder-arc090_b]`  
**Category File**: [`../categories/data_structures/potentialized_weighted_dsu.md`](../categories/data_structures/potentialized_weighted_dsu.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Potentialized Disjoint Set Union (Weighted DSU)`  

---

## 1. Problem Statement & Key Idea
N people stand on a number line. M constraints of the form 'person R_i is at distance D_i to the right of person L_i' (pos[R_i] - pos[L_i] = D_i) are given. Determine whether a valid coordinate assignment exists without contradiction.

**Key Insight**: Use Potentialized (Weighted) DSU to maintain relative distance offsets pos[u] - pos[root[u]].

## 2. Core Observation & Invariant
Each constraint pos[v] - pos[u] = d defines a relative potential between u and v. If u and v belong to different components, unite them with offset d + weight[u] - weight[v]. If they already belong to the same component, check if weight[v] - weight[u] == d; any mismatch indicates an impossible contradiction.

## 3. Step-by-Step Algorithm
1. Initialize parent[i] = i, weight[i] = 0 for all i = 1..N.
2. find(u): path compression updates weight[u] += weight[old_parent].
3. unite(u, v, d) enforcing pos[v] - pos[u] = d:
4.   root_u = find(u), root_v = find(v).
5.   If root_u == root_v: return (weight[v] - weight[u] == d).
6.   parent[root_v] = root_u.
7.   weight[root_v] = d + weight[u] - weight[v].
8.   Return true.
9. If any unite returns false, print 'No'; else print 'Yes'.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) * alpha(N))`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct WeightedDSU {
    vector<int> parent;
    vector<long long> weight; // weight[i] = pos[i] - pos[parent[i]]

    WeightedDSU(int n) : parent(n + 1), weight(n + 1, 0) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }

    int find(int u) {
        if (parent[u] == u) return u;
        int root = find(parent[u]);
        weight[u] += weight[parent[u]];
        return parent[u] = root;
    }

    // Enforce pos[v] - pos[u] = d
    bool unite(int u, int v, long long d) {
        int ru = find(u);
        int rv = find(v);
        if (ru == rv) {
            return (weight[v] - weight[u] == d);
        }
        parent[rv] = ru;
        weight[rv] = d + weight[u] - weight[v];
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    WeightedDSU dsu(n);

    for (int i = 0; i < m; ++i) {
        int l, r;
        long long d;
        cin >> l >> r >> d;
        if (!dsu.unite(l, r, d)) {
            cout << "No\n";
            return 0;
        }
    }

    cout << "Yes\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Potentialized Disjoint Set Union for system of difference constraints.
- **Reusable Pattern**: `Weighted DSU Template: maintain potential relative to component root with path compression.`
