# Problem Analysis: AtCoder-abc346_g — G. Alone

**Problem ID**: `AtCoder-abc346_g`  
**Contest**: `abc346`  
**Rating / Difficulty**: 2166  
**URL**: https://atcoder.jp/contests/abc346/tasks/abc346_g  
**VJudge Tag**: `[problem:AtCoder-abc346_g]`  
**Category File**: [`../categories/data_structures/rectangle_union_sweep_line_segment_tree.md`](../categories/data_structures/rectangle_union_sweep_line_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Find the number of pairs (L, R) such that at least one value appears uniquely in A[L..R]. For each occurrence p_k of value x, it is unique in A[L..R] iff p_{k-1} < L <= p_k and p_k <= R < p_{k+1}. The problem reduces to finding the area of the union of axis-aligned rectangles [p_{k-1}+1, p_k] x [p_k, p_{k+1}-1] via sweep-line and segment tree.

## 2. Core Observation & Invariant
Each occurrence generates an independent rectangle of valid (L, R) coordinates. The union of these rectangles covers all valid pairs. Sweeping L from 1 to N, we activate and deactivate intervals [R1, R2] on a segment tree tracking min coverage and zero-count. The number of covered R values at each step L is N - (zero_count if min == 0 else 0).

## 3. Step-by-Step Algorithm
1. For each distinct value x, collect occurrence indices p_0=0, p_1, ..., p_m, p_{m+1}=N+1.
2. For each occurrence p_k, create interval addition +1 at L = p_{k-1} + 1 on [p_k, p_{k+1} - 1] and removal -1 at L = p_k + 1.
3. Maintain coverage on [1, N] using a lazy segment tree storing minimum value and count of minimums.
4. Iterate L from 1 to N: apply all segment updates for L, then add the count of covered positions (N - zero_count) to the answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct SegTree {
    int n;
    vector<int> mn, cnt, lazy;
    SegTree(int n) : n(n), mn(4 * (n + 1)), cnt(4 * (n + 1)), lazy(4 * (n + 1)) {
        build(1, 1, n);
    }
    void build(int node, int l, int r) {
        mn[node] = 0;
        cnt[node] = r - l + 1;
        lazy[node] = 0;
        if (l == r) return;
        int mid = (l + r) / 2;
        build(2 * node, l, mid);
        build(2 * node + 1, mid + 1, r);
    }
    void apply(int node, int val) {
        mn[node] += val;
        lazy[node] += val;
    }
    void push(int node) {
        if (lazy[node] != 0) {
            apply(2 * node, lazy[node]);
            apply(2 * node + 1, lazy[node]);
            lazy[node] = 0;
        }
    }
    void pull(int node) {
        mn[node] = min(mn[2 * node], mn[2 * node + 1]);
        cnt[node] = 0;
        if (mn[2 * node] == mn[node]) cnt[node] += cnt[2 * node];
        if (mn[2 * node + 1] == mn[node]) cnt[node] += cnt[2 * node + 1];
    }
    void update(int node, int l, int r, int ql, int qr, int val) {
        if (ql <= l && r <= qr) {
            apply(node, val);
            return;
        }
        push(node);
        int mid = (l + r) / 2;
        if (ql <= mid) update(2 * node, l, mid, ql, qr, val);
        if (qr > mid) update(2 * node + 1, mid + 1, r, ql, qr, val);
        pull(node);
    }
    int get_covered() {
        return n - (mn[1] == 0 ? cnt[1] : 0);
    }
};

struct Event {
    int r1, r2, val;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<int> A(N + 1);
    vector<vector<int>> pos(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
        pos[A[i]].push_back(i);
    }

    vector<vector<Event>> events(N + 2);
    for (int x = 1; x <= N; ++x) {
        int m = (int)pos[x].size();
        for (int k = 0; k < m; ++k) {
            int p_prev = (k > 0 ? pos[x][k - 1] : 0);
            int p_curr = pos[x][k];
            int p_next = (k + 1 < m ? pos[x][k + 1] : N + 1);
            int l1 = p_prev + 1, l2 = p_curr;
            int r1 = p_curr, r2 = p_next - 1;
            if (l1 <= l2 && r1 <= r2) {
                events[l1].push_back({r1, r2, 1});
                events[l2 + 1].push_back({r1, r2, -1});
            }
        }
    }

    SegTree st(N);
    long long ans = 0;
    for (int l = 1; l <= N; ++l) {
        for (auto& e : events[l]) {
            st.update(1, 1, N, e.r1, e.r2, e.val);
        }
        ans += st.get_covered();
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
