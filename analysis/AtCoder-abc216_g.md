# Problem Analysis: AtCoder-abc216_g — 01Sequence

**Problem ID**: `AtCoder-abc216_g`  
**Contest**: `abc216`  
**Rating / Difficulty**: 1963  
**URL**: https://atcoder.jp/contests/abc216/tasks/abc216_g  
**VJudge Tag**: `[problem:AtCoder-abc216_g]`  
**Category File**: [`../categories/data_structures/greedy_interval_filling_dsu_fenwick.md`](../categories/data_structures/greedy_interval_filling_dsu_fenwick.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `DSU / Fenwick Tree`  
- **Topic (Skill)**: `Greedy Rightmost Interval 1-Filling via DSU Predecessor Jumping and Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
Given N and M intervals [L_i, R_i] with required minimum number of 1s X_i. Construct a 0-1 sequence of length N that satisfies all constraints while minimizing the total number of 1s.

Sort constraints by R_i ascending. To help future overlapping intervals, any needed 1s should be placed as far right as possible within [L_i, R_i]. Query the number of existing 1s in [L_i, R_i] via a Fenwick Tree. If count < X_i, greedily place 1s at the largest unoccupied indices <= R_i. Finding the largest available 0 position <= x is accelerated to nearly O(1) using a DSU predecessor pointer: parent[x] = find(x - 1) when position x is filled.

## 2. Core Observation & Invariant
DSU predecessor jumping eliminates scanning already-filled indices, achieving linear-logarithmic interval filling.

## 3. Step-by-Step Algorithm
1. Sort constraints by R_i ascending.
2. Initialize Fenwick Tree and DSU parent[i] = i for i = 0..N.
3. For each constraint (L_i, R_i, X_i):
4.   existing = query(R_i) - query(L_i - 1).
5.   needed = X_i - existing.
6.   while needed > 0:
7.     idx = find(R_i).
8.     ans[idx] = 1, update Fenwick at idx.
9.     parent[idx] = find(idx - 1).
10.     needed--.
11. Print ans[1..N].

## 4. Complexity Analysis
- **Time Complexity**: `O(N * alpha(N) + M log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Constraint {
    int l, r, x;
};

int parent_dsu[200005];

int find_set(int v) {
    if (v == parent_dsu[v]) return v;
    return parent_dsu[v] = find_set(parent_dsu[v]);
}

int bit_tree[200005];
int n_size;

void bit_add(int idx, int val) {
    for (; idx <= n_size; idx += idx & -idx) bit_tree[idx] += val;
}

int bit_query(int idx) {
    int sum = 0;
    for (; idx > 0; idx -= idx & -idx) sum += bit_tree[idx];
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    n_size = n;

    vector<Constraint> cons(m);
    for (int i = 0; i < m; ++i) {
        cin >> cons[i].l >> cons[i].r >> cons[i].x;
    }

    sort(cons.begin(), cons.end(), [](const Constraint& a, const Constraint& b) {
        return a.r < b.r;
    });

    for (int i = 0; i <= n; ++i) {
        parent_dsu[i] = i;
    }

    vector<int> ans(n + 1, 0);

    for (const auto& c : cons) {
        int existing = bit_query(c.r) - bit_query(c.l - 1);
        int needed = c.x - existing;

        while (needed > 0) {
            int pos = find_set(c.r);
            if (pos < c.l) break;

            ans[pos] = 1;
            bit_add(pos, 1);
            parent_dsu[pos] = find_set(pos - 1);
            needed--;
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining DSU fast-forwarding for unoccupied index discovery with Fenwick tree range counting.
- **Reusable Pattern**: `Greedy Rightmost Fill: DSU find(R) jumps directly to the latest available free index.`
