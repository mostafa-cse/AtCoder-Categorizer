# Problem Analysis: AtCoder-arc167_d — D. Good Permutation

**Problem ID**: `AtCoder-arc167_d`  
**Contest**: `arc167`  
**Rating / Difficulty**: 2313  
**URL**: https://atcoder.jp/contests/arc167/tasks/arc167_d  
**VJudge Tag**: `[problem:AtCoder-arc167_d]`  
**Category File**: [`../categories/basics/functional_graph_cycle_merge_lexicographical_dsu.md`](../categories/basics/functional_graph_cycle_merge_lexicographical_dsu.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Given a permutation $P$ of length $N$, you can swap elements within existing cycles at most $C-1$ times to connect all elements into a single cycle. Find the lexicographically smallest permutation achievable.

## 2. Core Observation & Invariant
Merging $C$ disjoint cycles into a single $N$-cycle requires exactly $M = C - 1$ transpositions. Lexicographical minimization requires swapping $P_i$ with the smallest available element $r$ in a disjoint component as early as possible, or whenever $i$ is the maximum index of the current component containing 1.

## 3. Step-by-Step Algorithm
1. Decompose $P$ into cycles using DSU, maintaining the maximum index within each component.
2. Maintain a monotonic pointer $r$ to the smallest integer not yet merged with the component of 1.
3. Iterate $i$ from 1 to $N$: swap $P_i$ with $P_{pos[r]}$ if $r < P_i$ or if $i$ is the maximum index of component 1, advancing $r$ in $O(N \alpha(N))$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \alpha(N))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct DSU {
    int n;
    vector<int> parent, max_idx;
    DSU(int n) : n(n), parent(n + 1), max_idx(n + 1) {
        iota(parent.begin(), parent.end(), 0);
        iota(max_idx.begin(), max_idx.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int ri = find(i), rj = find(j);
        if (ri != rj) {
            parent[ri] = rj;
            max_idx[rj] = max(max_idx[rj], max_idx[ri]);
            return true;
        }
        return false;
    }
};

void solve() {
    int n;
    if (!(cin >> n)) return;

    vector<int> p(n + 1);
    vector<int> pos(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
        pos[p[i]] = i;
    }

    DSU dsu(n);
    for (int i = 1; i <= n; ++i) {
        dsu.unite(i, p[i]);
    }

    auto advance_r = [&](int cur_r) {
        while (cur_r <= n && dsu.find(cur_r) == dsu.find(1)) {
            cur_r++;
        }
        return cur_r;
    };

    int r = advance_r(2);

    for (int i = 1; i <= n; ++i) {
        r = advance_r(r);
        if (r > n) break;

        if (r < p[i]) {
            int j = pos[r];
            int val_i = p[i];
            swap(p[i], p[j]);
            pos[val_i] = j;
            pos[r] = i;
            dsu.unite(1, r);
            r = advance_r(r);
        } else if (dsu.max_idx[dsu.find(1)] == i) {
            int j = pos[r];
            int val_i = p[i];
            swap(p[i], p[j]);
            pos[val_i] = j;
            pos[r] = i;
            dsu.unite(1, r);
            r = advance_r(r);
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << p[i] << (i == n ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
