# Problem Analysis: AtCoder-arc008_4 — タコヤキオイシクナール

**Problem ID**: `AtCoder-arc008_4`  
**Contest**: `arc008`  
**Rating / Difficulty**: 2430  
**URL**: https://atcoder.jp/contests/arc008/tasks/arc008_4  
**VJudge Tag**: `[problem:AtCoder-arc008_4]`  
**Category File**: [`../categories/data_structures/affine_transformation_composition_dynamic_segment_tree.md`](../categories/data_structures/affine_transformation_composition_dynamic_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Dynamic Segment Tree`  

---

## 1. Problem Statement & Key Idea
Coordinate-compress updated box positions up to 10^12 and maintain compositions of affine transformations f(x) = a * x + b using a Segment Tree, tracking global minimum and maximum flavor across all M updates in O(M log M).

## 2. Core Observation & Invariant
Linear transformations compose associatively: f_R(f_L(x)) = a_R * (a_L * x + b_L) + b_R = (a_R * a_L) * x + (a_R * b_L + b_R). Because only at most M distinct machines are ever updated, coordinate compression reduces the pipeline to size <= M.

## 3. Step-by-Step Algorithm
1. 1. Collect and coordinate-compress all updated machine positions p_i into indices 0 to K - 1.
2. 2. Build a Segment Tree over size K, initialized with identity transformations (a=1, b=0).
3. 3. On each update, set the leaf at position p_i to (a_i, b_i) and pull composition values up the tree.
4. 4. The total transformation applied to flavor 1 is given by tree_a[root] * 1 + tree_b[root].
5. 5. Update running minimum and maximum and print both with 6 decimal places.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct SegTree {
    int n;
    vector<double> tree_a, tree_b;

    SegTree(int n) : n(n), tree_a(4 * n, 1.0), tree_b(4 * n, 0.0) {}

    void update(int node, int l, int r, int q_idx, double a_val, double b_val) {
        if (l == r) {
            tree_a[node] = a_val;
            tree_b[node] = b_val;
            return;
        }
        int mid = l + (r - l) / 2;
        if (q_idx <= mid) {
            update(2 * node, l, mid, q_idx, a_val, b_val);
        } else {
            update(2 * node + 1, mid + 1, r, q_idx, a_val, b_val);
        }
        double a_L = tree_a[2 * node], b_L = tree_b[2 * node];
        double a_R = tree_a[2 * node + 1], b_R = tree_b[2 * node + 1];
        tree_a[node] = a_R * a_L;
        tree_b[node] = a_R * b_L + b_R;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N;
    int M;
    if (!(cin >> N >> M)) return 0;

    struct Query {
        ll p;
        double a, b;
    };
    vector<Query> queries(M);
    vector<ll> pts;
    pts.reserve(M);

    for (int i = 0; i < M; i++) {
        cin >> queries[i].p >> queries[i].a >> queries[i].b;
        pts.push_back(queries[i].p);
    }

    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());
    int K = pts.size();

    SegTree seg(K);
    double min_val = 1.0, max_val = 1.0;

    for (int i = 0; i < M; i++) {
        int q_idx = lower_bound(pts.begin(), pts.end(), queries[i].p) - pts.begin();
        seg.update(1, 0, K - 1, q_idx, queries[i].a, queries[i].b);
        double val = seg.tree_a[1] * 1.0 + seg.tree_b[1];
        min_val = min(min_val, val);
        max_val = max(max_val, val);
    }

    cout << fixed << setprecision(6) << min_val << "\n" << max_val << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
