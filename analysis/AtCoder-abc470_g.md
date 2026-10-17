# Problem Analysis: AtCoder-abc470_g — Range Mex Sum

**Problem ID**: `AtCoder-abc470_g`  
**Contest**: `abc470`  
**Rating / Difficulty**: 2094  
**URL**: https://atcoder.jp/contests/abc470/tasks/abc470_g  
**VJudge Tag**: `[problem:AtCoder-abc470_g]`  
**Category File**: [`../categories/data_structures/monotonic_range_mex_segment_tree_beats.md`](../categories/data_structures/monotonic_range_mex_segment_tree_beats.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree Beats`  

---

## 1. Problem Statement & Key Idea
Given an array A of length N, find the sum of mex(A[L..R]) over all 1 <= L <= R <= N.

**Key Insight**: For a fixed left endpoint L, as the right endpoint R increases from L to N, the prefix MEX f(L, R) = mex(A[L..R]) is a non-decreasing function of R. When L increases to L + 1 (removing element x = A[L]), for all R from L to next_occ(x) - 1, the subarray no longer contains x. Therefore, any f(L, R) that was greater than x must now become at most x: f(L+1, R) = min(f(L, R), x) for R in [L, next_occ(x) - 1]. Since f is monotonically non-decreasing in R, applying chmin(x) replaces a suffix of values > x with x. We can maintain this sequence using a Segment Tree Beats or a standard lazy segment tree with range assignment.

## 2. Core Observation & Invariant
MEX is monotonic in R for fixed L. Removing A[L] performs a range chmin update on a contiguous interval, which on a monotonic sequence is equivalent to a binary search and range assignment.

## 3. Step-by-Step Algorithm
1. Compute the initial MEX values f(1, R) for all R in [1, N] using two pointers / frequency counts.
2. Build a Lazy Segment Tree over R in [1, N] storing sum and max.
3. Precompute next occurrence next_occ[i] for each index i.
4. For L from 1 to N:
5.   Add tree.query_sum(L, N) to the total answer.
6.   Let x = A[L] and R_limit = next_occ[L] - 1.
7.   If L <= R_limit:
8.     On the interval [L, R_limit], find the first position where value > x.
9.     Update that range to x using lazy range assignment.
10. Output the total accumulated sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Segment tree range chmin on monotonic sequences for cumulative range MEX queries.
- **Reusable Pattern**: Cumulative range MEX sum via sweeping L and performing range assignment updates on monotonic right-endpoint profiles.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    long long sum;
    int max_val;
    int lazy; // -1: none
};

int n;
vector<int> a;
vector<Node> tree;

void apply_lazy(int u, int l, int r, int val) {
    tree[u].lazy = val;
    tree[u].max_val = val;
    tree[u].sum = 1LL * (r - l + 1) * val;
}

void push(int u, int l, int r) {
    if (tree[u].lazy != -1) {
        int mid = (l + r) / 2;
        apply_lazy(2 * u, l, mid, tree[u].lazy);
        apply_lazy(2 * u + 1, mid + 1, r, tree[u].lazy);
        tree[u].lazy = -1;
    }
}

void pull(int u) {
    tree[u].sum = tree[2 * u].sum + tree[2 * u + 1].sum;
    tree[u].max_val = max(tree[2 * u].max_val, tree[2 * u + 1].max_val);
}

void build(int u, int l, int r, const vector<int>& init_val) {
    tree[u].lazy = -1;
    if (l == r) {
        tree[u].sum = init_val[l];
        tree[u].max_val = init_val[l];
        return;
    }
    int mid = (l + r) / 2;
    build(2 * u, l, mid, init_val);
    build(2 * u + 1, mid + 1, r, init_val);
    pull(u);
}

void update_range(int u, int l, int r, int ql, int qr, int val) {
    if (ql > qr) return;
    if (ql <= l && r <= qr) {
        apply_lazy(u, l, r, val);
        return;
    }
    push(u, l, r);
    int mid = (l + r) / 2;
    if (ql <= mid) update_range(2 * u, l, mid, ql, qr, val);
    if (qr > mid) update_range(2 * u + 1, mid + 1, r, ql, qr, val);
    pull(u);
}

long long query_sum(int u, int l, int r, int ql, int qr) {
    if (ql > qr) return 0;
    if (ql <= l && r <= qr) return tree[u].sum;
    push(u, l, r);
    int mid = (l + r) / 2;
    long long res = 0;
    if (ql <= mid) res += query_sum(2 * u, l, mid, ql, qr);
    if (qr > mid) res += query_sum(2 * u + 1, mid + 1, r, ql, qr);
    return res;
}

int find_first_greater(int u, int l, int r, int ql, int qr, int val) {
    if (ql <= l && r <= qr && tree[u].max_val <= val) return -1;
    if (l == r) return l;
    push(u, l, r);
    int mid = (l + r) / 2;
    if (ql <= mid) {
        int res = find_first_greater(2 * u, l, mid, ql, qr, val);
        if (res != -1) return res;
    }
    if (qr > mid) {
        return find_first_greater(2 * u + 1, mid + 1, r, ql, qr, val);
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    a.resize(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<int> init_mex(n + 1, 0);
    vector<int> freq(n + 2, 0);
    int cur_mex = 0;
    for (int r = 1; r <= n; ++r) {
        if (a[r] <= n + 1) freq[a[r]]++;
        while (freq[cur_mex] > 0) cur_mex++;
        init_mex[r] = cur_mex;
    }

    tree.resize(4 * n + 5);
    build(1, 1, n, init_mex);

    vector<int> next_occ(n + 1, n + 1);
    vector<int> last_pos(n + 2, n + 1);
    for (int i = n; i >= 1; --i) {
        if (a[i] <= n + 1) {
            next_occ[i] = last_pos[a[i]];
            last_pos[a[i]] = i;
        }
    }

    long long total_ans = 0;

    for (int l = 1; l <= n; ++l) {
        total_ans += query_sum(1, 1, n, l, n);

        int x = a[l];
        int r_limit = min(n, next_occ[l] - 1);
        if (l <= r_limit) {
            int pos = find_first_greater(1, 1, n, l, r_limit, x);
            if (pos != -1 && pos <= r_limit) {
                update_range(1, 1, n, pos, r_limit, x);
            }
        }
    }

    cout << total_ans << "\n";
    return 0;
}
```
