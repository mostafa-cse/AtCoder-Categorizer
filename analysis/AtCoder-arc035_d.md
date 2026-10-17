# Problem Analysis: AtCoder-arc035_d — D. 高橋くんとマラソンコース

**Problem ID**: `AtCoder-arc035_d`  
**Contest**: `arc035`  
**Rating / Difficulty**: 2173  
**URL**: https://atcoder.jp/contests/arc035/tasks/arc035_d  
**VJudge Tag**: `[problem:AtCoder-arc035_d]`  
**Category File**: [`../categories/data_structures/grid_paths_log_binomial_fenwick_tree.md`](../categories/data_structures/grid_paths_log_binomial_fenwick_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Given N checkpoints on a grid, moving only North or East, the number of paths between checkpoint i and i+1 is binom(dx + dy, dx). Compare total path products across query subsegments under point checkpoint modifications. Maintain logarithms of binomial coefficients in a Fenwick tree; compare range sums of log-probabilities.

## 2. Core Observation & Invariant
The problem guarantees that the larger path count is at least twice the smaller path count. Taking logarithms transforms product queries into range sum queries: sum_{i=l}^{r-1} log binom(dx_i + dy_i, dx_i). Precomputing log-factorials log(m!) allows O(1) evaluation of log binom, and a Fenwick tree supports O(log N) updates and range comparisons with double precision.

## 3. Step-by-Step Algorithm
1. Precompute logfact[m] = sum_{j=1}^m log(j) for m <= 2*10^6.
2. Initialize Fenwick tree with values log binom(dx_i + dy_i, dx_i) for segment i to i+1.
3. Type 1 query: update checkpoint k position; recalculate and apply point differences to segments k-1 and k in the Fenwick tree.
4. Type 2 query: query range sums s1 on [l1, r1-1] and s2 on [l2, r2-1]. Output FIRST if s1 > s2, else SECOND.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N + max_coord)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const int MAX = 2000005;
double logfact[MAX];

struct Fenwick {
    int n;
    vector<double> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0.0) {}
    void add(int i, double delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    double query(int i) {
        double sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    double query(int l, int r) {
        if (l > r) return 0.0;
        return query(r) - query(l - 1);
    }
};

double logcomb(int dx, int dy) {
    if (dx < 0 || dy < 0) return -1e18;
    return logfact[dx + dy] - logfact[dx] - logfact[dy];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    logfact[0] = 0.0;
    for (int i = 1; i < MAX; ++i) logfact[i] = logfact[i - 1] + log((double)i);

    int N;
    if (!(cin >> N)) return 0;

    vector<pair<int, int>> P(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> P[i].first >> P[i].second;
    }

    Fenwick ft(N);
    auto seg_val = [&](int i) -> double {
        int dx = P[i + 1].first - P[i].first;
        int dy = P[i + 1].second - P[i].second;
        return logcomb(dx, dy);
    };

    for (int i = 1; i < N; ++i) {
        ft.add(i, seg_val(i));
    }

    int Q;
    cin >> Q;
    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int k, a, b;
            cin >> k >> a >> b;
            double old_prev = (k > 1 ? seg_val(k - 1) : 0.0);
            double old_curr = (k < N ? seg_val(k) : 0.0);
            P[k] = {a, b};
            if (k > 1) {
                double new_prev = seg_val(k - 1);
                ft.add(k - 1, new_prev - old_prev);
            }
            if (k < N) {
                double new_curr = seg_val(k);
                ft.add(k, new_curr - old_curr);
            }
        } else {
            int l1, r1, l2, r2;
            cin >> l1 >> r1 >> l2 >> r2;
            double s1 = ft.query(l1, r1 - 1);
            double s2 = ft.query(l2, r2 - 1);
            if (s1 > s2) cout << "FIRST\n";
            else cout << "SECOND\n";
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
