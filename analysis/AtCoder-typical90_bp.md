# Problem Analysis: AtCoder-typical90_bp — Paired Information

**Problem ID**: `AtCoder-typical90_bp`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 068)  
**Rating / Difficulty**: 1750 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bp  
**VJudge Tag**: `[problem:AtCoder-typical90_bp]`  
**Category File**: [`../categories/data_structures/alternating_prefix_dsu.md`](../categories/data_structures/alternating_prefix_dsu.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU) & Fenwick Tree`  
- **Topic (Skill)**: `Alternating Difference Prefix Sums & Interval DSU Reachability`  

---

## 1. Problem Statement & Key Idea
Array A of length N. Q queries: (0) told A_x + A_{x+1} = V; (1) given (x, y, v), if A_x = v, determine value of A_y or output 'Ambiguous'.

**Core Idea**: A_{x+1} + A_x = V defines an alternating linear relation. Two positions x and y are uniquely determinable iff they are in the same contiguous connected component.

## 2. Core Observation & Invariant
Let A_i = (-1)^{i-1} A_1 + C_i where C is an alternating sum of known adjacent sums. Then A_y = (-1)^{y - x} A_x + (C_y - (-1)^{y - x} C_x). Use DSU to verify contiguous connectivity.

## 3. Step-by-Step Algorithm
1. Offline all Type 0 sum constraints; precompute alternating base values.
2. In second pass: maintain DSU of contiguous known adjacencies.
3. For Type 1 queries: if dsu.same(x, y), evaluate A_y using alternating difference; else 'Ambiguous'.

## 4. Complexity Analysis
Time: O(Q log N), Space: O(N + Q).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i), root_j = find(j);
        if (root_i != root_j) parent[root_i] = root_j;
    }
    bool same(int i, int j) {
        return find(i) == find(j);
    }
};

struct Query {
    int t, x, y;
    long long v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<Query> queries(q);
    vector<long long> sum_adj(n, 0);

    for (int i = 0; i < q; ++i) {
        cin >> queries[i].t >> queries[i].x >> queries[i].y >> queries[i].v;
        if (queries[i].t == 0) {
            sum_adj[queries[i].x] = queries[i].v;
        }
    }

    // Precompute potential array assuming A[1] = 0
    // A[i+1] = sum_adj[i] - A[i]
    vector<long long> pot(n + 1, 0);
    for (int i = 1; i < n; ++i) {
        pot[i + 1] = sum_adj[i] - pot[i];
    }

    DSU dsu(n);
    for (const auto& qry : queries) {
        if (qry.t == 0) {
            dsu.unite(qry.x, qry.x + 1);
        } else {
            if (!dsu.same(qry.x, qry.y)) {
                cout << "Ambiguous\n";
            } else {
                long long d = qry.v - pot[qry.x];
                long long ans;
                if ((qry.x + qry.y) % 2 == 0) {
                    ans = pot[qry.y] + d;
                } else {
                    ans = pot[qry.y] - d;
                }
                cout << ans << "\n";
            }
        }
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Potential array precomputation with DSU contiguous connectivity validation.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Alternating linear systems, potential array offsets, and DSU interval reachability.
- **Reusable Pattern**: `Alternating Potential Offset & DSU Reachability.`

---
Back to [Alternating Difference Prefix Sums & Interval DSU Reachability](../categories/data_structures/alternating_prefix_dsu.md) | [Categories Directory](../categories/README.md)