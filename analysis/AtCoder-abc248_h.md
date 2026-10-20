# Problem Analysis: AtCoder-abc248_h — Ex - Beautiful Subsequences

**Problem ID**: `AtCoder-abc248_h`  
**Contest**: `abc248`  
**Rating / Difficulty**: 2968  
**URL**: https://atcoder.jp/contests/abc248/tasks/abc248_h  
**VJudge Tag**: `[problem:AtCoder-abc248_h]`  
**Category File**: [`../categories/data_structures/permutation_range_difference_monotonic_stack_segment_tree.md`](../categories/data_structures/permutation_range_difference_monotonic_stack_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Monotonic Data Structures`  
- **Topic (Skill)**: `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`  

---

## 1. Problem Statement & Key Idea
Given a permutation P of (1, ..., N) and integer K in [0, 3], count pairs (L, R) (1 <= L <= R <= N) such that (max_{L <= i <= R} P_i) - (min_{L <= i <= R} P_i) - (R - L) <= K.

## 2. Core Observation & Invariant
For any range [L, R], the quantity f(L, R) = max P_i - min P_i - (R - L) is always >= 0, and f(L, R) = 0 iff the range is a contiguous interval of values. As R advances from 1 to N, monotonic stacks maintain the prefix maximums and minimums, performing range additions on L in [1, R]. Since K <= 3, a lazy segment tree can maintain the minimum value in each node and the counts of elements achieving min_val + d for d in {0, 1, 2, 3}.

## 3. Step-by-Step Algorithm
1. 1. Build a lazy segment tree where each node tracks min_val, cnt[0..3], and lazy addition tag.
2. 2. Maintain two monotonic stacks: decreasing stack for maximums, increasing stack for minimums.
3. 3. When processing R:
4.    - Decrement all existing values in the segment tree by 1 (due to R - L).
5.    - Pop from max-stack and update segment tree with +(P_R - P_{popped}) on popped ranges.
6.    - Pop from min-stack and update segment tree with +(P_{popped} - P_R) on popped ranges.
7.    - Push R onto both stacks and initialize index R with 0.
8.    - Query segment tree on [1, R] for the number of indices with value <= K.
9. 4. Sum results across all R in [1, N].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct Node {
    int min_val;
    int cnt[4];
    int lazy;

    Node() {
        min_val = 0;
        for (int i = 0; i < 4; ++i) cnt[i] = 0;
        lazy = 0;
    }
};

int N, K;
vector<Node> tree;

Node mergeNodes(const Node& left, const Node& right) {
    Node res;
    res.min_val = min(left.min_val, right.min_val);
    for (int d = 0; d < 4; ++d) {
        int target = res.min_val + d;
        int d_left = target - left.min_val;
        if (d_left >= 0 && d_left < 4) res.cnt[d] += left.cnt[d_left];
        int d_right = target - right.min_val;
        if (d_right >= 0 && d_right < 4) res.cnt[d] += right.cnt[d_right];
    }
    return res;
}

void applyLazy(int node, int val) {
    tree[node].min_val += val;
    tree[node].lazy += val;
}

void pushDown(int node) {
    if (tree[node].lazy != 0) {
        applyLazy(2 * node, tree[node].lazy);
        applyLazy(2 * node + 1, tree[node].lazy);
        tree[node].lazy = 0;
    }
}

void build(int node, int l, int r) {
    if (l == r) {
        tree[node].min_val = 0;
        tree[node].cnt[0] = 1;
        for (int i = 1; i < 4; ++i) tree[node].cnt[i] = 0;
        tree[node].lazy = 0;
        return;
    }
    int mid = (l + r) / 2;
    build(2 * node, l, mid);
    build(2 * node + 1, mid + 1, r);
    tree[node] = mergeNodes(tree[2 * node], tree[2 * node + 1]);
}

void updateRange(int node, int l, int r, int ql, int qr, int val) {
    if (ql <= l && r <= qr) {
        applyLazy(node, val);
        return;
    }
    pushDown(node);
    int mid = (l + r) / 2;
    if (ql <= mid) updateRange(2 * node, l, mid, ql, qr, val);
    if (qr > mid) updateRange(2 * node + 1, mid + 1, r, ql, qr, val);
    tree[node] = mergeNodes(tree[2 * node], tree[2 * node + 1]);
}

int queryRange(int node, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) {
        int count = 0;
        for (int d = 0; d < 4; ++d) {
            if (tree[node].min_val + d <= K) {
                count += tree[node].cnt[d];
            }
        }
        return count;
    }
    pushDown(node);
    int mid = (l + r) / 2;
    int res = 0;
    if (ql <= mid) res += queryRange(2 * node, l, mid, ql, qr);
    if (qr > mid) res += queryRange(2 * node + 1, mid + 1, r, ql, qr);
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> K)) return 0;

    vector<int> p(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> p[i];
    }

    tree.assign(4 * (N + 1), Node());
    build(1, 1, N);

    vector<pair<int, int>> max_st; // {val, index}
    vector<pair<int, int>> min_st; // {val, index}

    long long total_ans = 0;

    for (int r = 1; r <= N; ++r) {
        // 1. Shift -(R - L): for all previous L in [1, r-1], subtract 1
        if (r > 1) {
            updateRange(1, 1, N, 1, r - 1, -1);
        }

        // 2. Monotonic stack for maximum
        int last_l = r;
        while (!max_st.empty() && max_st.back().first < p[r]) {
            int val = max_st.back().first;
            int idx = max_st.back().second;
            max_st.pop_back();
            int prev_idx = max_st.empty() ? 1 : max_st.back().second + 1;
            updateRange(1, 1, N, prev_idx, idx, p[r] - val);
        }
        max_st.push_back({p[r], r});

        // 3. Monotonic stack for minimum
        while (!min_st.empty() && min_st.back().first > p[r]) {
            int val = min_st.back().first;
            int idx = min_st.back().second;
            min_st.pop_back();
            int prev_idx = min_st.empty() ? 1 : min_st.back().second + 1;
            updateRange(1, 1, N, prev_idx, idx, val - p[r]);
        }
        min_st.push_back({p[r], r});

        // 4. Query number of L in [1, r] with value <= K
        total_ans += queryRange(1, 1, N, 1, r);
    }

    cout << total_ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
