# Problem Analysis: AtCoder-arc180_d — Division into 3

**Problem ID**: `AtCoder-arc180_d`  
**Contest**: `arc180`  
**Rating / Difficulty**: 2694  
**URL**: https://atcoder.jp/contests/arc180/tasks/arc180_d  
**VJudge Tag**: `[problem:AtCoder-arc180_d]`  
**Category File**: [`../categories/data_structures_ds/division_into_3_monotonic_stack.md`](../categories/data_structures_ds/division_into_3_monotonic_stack.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Monotonic Data Structures`  
- **Topic (Skill)**: `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`  

---

## 1. Problem Statement & Key Idea
Partitioning A[L..R] into 3 subarrays to minimize sum of maximums. The global maximum A_m in A[L..R] must fall into one of the 3 parts: if in the middle, cost is A_L + A_m + A_R; if in the left part, the middle part can be taken as a single element A_j, yielding min_{j=m+1..R-1} (A_m + A_j + max(A_{j+1..R})). Symmetrically for the right part. We solve the range query using offline sweep-line with a monotonic stack and range-add range-min segment tree.

## 2. Core Observation & Invariant
As R increases, the suffix maximum max(A_{j+1..R}) for each j is piecewise constant and maintained by a monotonic decreasing stack of values. When A_R arrives, popping smaller elements corresponds to range addition on the segment tree, updating A_j + max(A_{j+1..R}). Queries are answered with range minimum query on [m+1, R-1].

## 3. Step-by-Step Algorithm
1. 1. For each query [L, R], compute Option 1: A_L + max(A[L+1..R-1]) + A_R using Sparse Table RMQ in O(1).
2. 2. For Option 2 (max in left part): sweep R from 1 to N.
3.    - At step R, insert point R-1 into segment tree with value A_{R-1} + A_R.
4.    - While stack top value <= A_R, pop interval [l, r] and apply range_add(l, r, A_R - val) to segment tree.
5.    - Push updated range to stack.
6.    - For queries ending at R with argmax m: query segment tree min on [m+1, R-1] and add A_m.
7. 3. Reverse array and queries to solve Option 3 identically.
8. 4. Take the minimum over all 3 options for each query.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N + Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const long long INF = 1e18;

struct SegTree {
    int n;
    vector<long long> tree;
    vector<long long> lazy;

    SegTree(int n) : n(n), tree(4 * n, INF), lazy(4 * n, 0) {}

    void apply(int node, long long val) {
        if (tree[node] != INF) {
            tree[node] += val;
        }
        lazy[node] += val;
    }

    void push(int node) {
        if (lazy[node] != 0) {
            apply(2 * node, lazy[node]);
            apply(2 * node + 1, lazy[node]);
            lazy[node] = 0;
        }
    }

    void update_point(int node, int l, int r, int idx, long long val) {
        if (l == r) {
            tree[node] = val;
            lazy[node] = 0;
            return;
        }
        push(node);
        int mid = (l + r) / 2;
        if (idx <= mid) {
            update_point(2 * node, l, mid, idx, val);
        } else {
            update_point(2 * node + 1, mid + 1, r, idx, val);
        }
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    void range_add(int node, int l, int r, int ql, int qr, long long val) {
        if (ql <= l && r <= qr) {
            apply(node, val);
            return;
        }
        push(node);
        int mid = (l + r) / 2;
        if (ql <= mid) range_add(2 * node, l, mid, ql, qr, val);
        if (qr > mid) range_add(2 * node + 1, mid + 1, r, ql, qr, val);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    long long range_min(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return tree[node];
        push(node);
        int mid = (l + r) / 2;
        long long res = INF;
        if (ql <= mid) res = min(res, range_min(2 * node, l, mid, ql, qr));
        if (qr > mid) res = min(res, range_min(2 * node + 1, mid + 1, r, ql, qr));
        return res;
    }
};

struct Query {
    int L, R, id;
};

struct Element {
    long long val;
    int l, r;
};

void solve_case_x(int n, const vector<long long>& A, const vector<Query>& queries, vector<long long>& ans) {
    int q_size = queries.size();
    vector<vector<pair<int, int>>> by_R(n);
    for (int i = 0; i < q_size; ++i) {
        by_R[queries[i].R].push_back({queries[i].L, queries[i].id});
    }

    // Sparse Table for argmax
    vector<vector<int>> st(20, vector<int>(n));
    for (int i = 0; i < n; ++i) st[0][i] = i;
    for (int k = 1; (1 << k) <= n; ++k) {
        int half = 1 << (k - 1);
        for (int i = 0; i + (1 << k) <= n; ++i) {
            int i1 = st[k - 1][i];
            int i2 = st[k - 1][i + half];
            st[k][i] = (A[i1] >= A[i2] ? i1 : i2);
        }
    }

    auto get_argmax = [&](int l, int r) {
        int len = r - l + 1;
        int lg = 31 - __builtin_clz(len);
        int i1 = st[lg][l];
        int i2 = st[lg][r - (1 << lg) + 1];
        return (A[i1] >= A[i2] ? i1 : i2);
    };

    SegTree seg(n);
    vector<Element> stack;

    for (int R = 1; R < n; ++R) {
        long long init_val = A[R - 1] + A[R];
        seg.update_point(1, 0, n - 1, R - 1, init_val);

        int cur_l = R - 1;
        while (!stack.empty() && stack.back().val <= A[R]) {
            Element top = stack.back();
            stack.pop_back();
            seg.range_add(1, 0, n - 1, top.l, top.r, A[R] - top.val);
            cur_l = top.l;
        }
        stack.push_back({A[R], cur_l, R - 1});

        for (const auto& item : by_R[R]) {
            int L = item.first;
            int qid = item.second;
            int m = get_argmax(L, R);
            if (m + 1 <= R - 1) {
                long long val = seg.range_min(1, 0, n - 1, m + 1, R - 1);
                if (val < INF) {
                    ans[qid] = min(ans[qid], A[m] + val);
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> A(n);
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].L >> queries[i].R;
        queries[i].L--;
        queries[i].R--;
        queries[i].id = i;
    }

    // Sparse Table for RMQ (values)
    vector<vector<long long>> st_val(20, vector<long long>(n));
    for (int i = 0; i < n; ++i) st_val[0][i] = A[i];
    for (int k = 1; (1 << k) <= n; ++k) {
        int half = 1 << (k - 1);
        for (int i = 0; i + (1 << k) <= n; ++i) {
            st_val[k][i] = max(st_val[k - 1][i], st_val[k - 1][i + half]);
        }
    }

    auto get_max = [&](int l, int r) {
        int len = r - l + 1;
        int lg = 31 - __builtin_clz(len);
        return max(st_val[lg][l], st_val[lg][r - (1 << lg) + 1]);
    };

    vector<long long> ans(q, INF);
    // Option 1: A[L] + max(A[L+1..R-1]) + A[R]
    for (int i = 0; i < q; ++i) {
        ans[i] = A[queries[i].L] + get_max(queries[i].L + 1, queries[i].R - 1) + A[queries[i].R];
    }

    // Option 2: max in X
    solve_case_x(n, A, queries, ans);

    // Option 3: max in Z (symmetric by reversing A and queries)
    vector<long long> rev_A(A.rbegin(), A.rend());
    vector<Query> rev_queries(q);
    for (int i = 0; i < q; ++i) {
        rev_queries[i] = {n - 1 - queries[i].R, n - 1 - queries[i].L, i};
    }
    solve_case_x(n, rev_A, rev_queries, ans);

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
