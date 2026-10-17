# Problem Analysis: AtCoder-abc339_g — Smaller Sum

**Problem ID**: `AtCoder-abc339_g`  
**Contest**: `abc339`  
**Rating / Difficulty**: 1792  
**URL**: https://atcoder.jp/contests/abc339/tasks/abc339_g  
**VJudge Tag**: `[problem:AtCoder-abc339_g]`  
**Category File**: [`../categories/data_structures/persistent_segment_tree_online_range_bounded_sum.md`](../categories/data_structures/persistent_segment_tree_online_range_bounded_sum.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Persistent Segment Tree`  
- **Topic (Skill)**: `Persistent Segment Tree for Online Range Value-Bounded Sum`  

---

## 1. Problem Statement & Key Idea
Given an array A of N integers and Q online queries (L, R, X) encrypted with the previous answer. For each query, find the sum of all elements in A[L..R] that are <= X. (N, Q <= 2 * 10^5, A_i <= 10^9).

**Key Insight**: Coordinate-compress array values. Build a Persistent Segment Tree where version i contains all elements of prefix A[1..i]. A range query [L, R] evaluates query(root[R], <= X) - query(root[L - 1], <= X) in O(log N).

## 2. Core Observation & Invariant
Each point insertion adds O(log N) new nodes. Answering online queries takes O(log N) per query with O(N log N) space.

## 3. Step-by-Step Algorithm
1. Coordinate compress unique values of A.
2. Build persistent segment tree: root[0] is empty tree.
3. For i = 1 to N: root[i] = insert(root[i - 1], comp_val(A[i]), A[i]).
4. ans = 0.
5. For each encrypted query:
6.   decode L, R, X with ans.
7.   find rightmost compressed value <= X via upper_bound.
8.   ans = query(root[R], 0..comp_idx) - query(root[L - 1], 0..comp_idx).
9.   print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N log N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    int left_child, right_child;
    long long sum;
};

const int MAX_NODES = 200005 * 40;
Node tree[MAX_NODES];
int node_count = 0;

int insert(int prev, int l, int r, int pos, long long val) {
    int cur = ++node_count;
    tree[cur] = tree[prev];
    tree[cur].sum += val;

    if (l == r) return cur;

    int mid = l + (r - l) / 2;
    if (pos <= mid) {
        tree[cur].left_child = insert(tree[prev].left_child, l, mid, pos, val);
    } else {
        tree[cur].right_child = insert(tree[prev].right_child, mid + 1, r, pos, val);
    }
    return cur;
}

long long query(int node, int l, int r, int ql, int qr) {
    if (!node || l > qr || r < ql) return 0;
    if (ql <= l && r <= qr) return tree[node].sum;

    int mid = l + (r - l) / 2;
    return query(tree[node].left_child, l, mid, ql, qr) +
           query(tree[node].right_child, mid + 1, r, ql, qr);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    vector<long long> vals;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        vals.push_back(a[i]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    int m = vals.size();

    vector<int> roots(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        int pos = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        roots[i] = insert(roots[i - 1], 1, m, pos, a[i]);
    }

    int q;
    cin >> q;

    long long last_ans = 0;
    while (q--) {
        long long alpha, beta, gamma;
        cin >> alpha >> beta >> gamma;

        long long l = alpha ^ last_ans;
        long long r = beta ^ last_ans;
        long long x = gamma ^ last_ans;

        if (l > r) swap(l, r);

        auto it = upper_bound(vals.begin(), vals.end(), x);
        int max_pos = it - vals.begin();

        if (max_pos == 0) {
            last_ans = 0;
        } else {
            long long right_sum = query(roots[r], 1, m, 1, max_pos);
            long long left_sum = query(roots[l - 1], 1, m, 1, max_pos);
            last_ans = right_sum - left_sum;
        }

        cout << last_ans << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Persistent Segment Tree construction and online prefix version subtraction.
- **Reusable Pattern**: `Online Range Value Query: Version R minus Version L-1 on Persistent Segment Tree.`
