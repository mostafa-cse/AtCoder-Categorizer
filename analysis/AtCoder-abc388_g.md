# Problem Analysis: AtCoder-abc388_g — Simultaneous Kagamimochi 2

**Problem ID**: `AtCoder-abc388_g`  
**Contest**: `abc388`  
**Rating / Difficulty**: 2001  
**URL**: https://atcoder.jp/contests/abc388/tasks/abc388_g  
**VJudge Tag**: `[problem:AtCoder-abc388_g]`  
**Category File**: [`../categories/data_structures/sparse_table_range_max_monotone_pair_matching.md`](../categories/data_structures/sparse_table_range_max_monotone_pair_matching.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree / Fenwick Tree`  
- **Topic (Skill)**: `Sparse Table Range Max Query with Binary Search for Monotone Pair Matching`  

---

## 1. Problem Statement & Key Idea
Given a sorted array A of length N. Process Q queries: for range [L, R], find the maximum number of pairs (i, j) with L <= i < j <= R such that 2 * A[i] <= A[j] and each element is used in at most one pair.

**Key Idea**: For a fixed subsegment of length M = R - L + 1, if k pairs can be formed, by exchange argument it is always optimal to pair the first k elements with the last k elements: 2 * A[L + t] <= A[R - k + 1 + t] for all 0 <= t < k. Let nxt[i] be the smallest index j such that 2 * A[i] <= A[j]. The condition becomes nxt[L + t] <= R - k + 1 + t, or equivalently nxt[L + t] - (L + t) <= R - L - 2k + 1. We binary search on k in [0, M / 2] and verify the condition in O(1) using a Sparse Table precomputed on val[i] = nxt[i] - i.

## 2. Core Observation & Invariant
Pairing extremal subsets (first k with last k) reduces bipartite matching feasibility to a range maximum query over nxt[i] - i.

## 3. Step-by-Step Algorithm
1. Precompute nxt[i] for all i using two pointers (smallest j such that 2 * A[i] <= A[j]). Set val[i] = nxt[i] - i (or INF if j does not exist).
2. Build a Sparse Table over val array for range maximum queries in O(1).
3. For each query (L, R): binary search k in [0, (R - L + 1) / 2].
4.   If k == 0: valid.
5.   Else: query max over [L, L + k - 1] in Sparse Table; check if max_val <= R - L - 2k + 1.
6. Output the maximum feasible k.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + Q log N)`
- **Space Complexity**: `O(N log N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Bipartite matching feasibility reduction to range maximum query with binary search.

**Reusable Pattern**: Monotone Pair Matching Check: 2 * A[L+t] <= A[R-k+1+t] <==> max_{t < k} (nxt[L+t] - (L+t)) <= R - L - 2k + 1.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> nxt(n);
    int ptr = 0;
    for (int i = 0; i < n; ++i) {
        while (ptr < n && a[ptr] < 2 * a[i]) {
            ptr++;
        }
        nxt[i] = (ptr < n ? ptr : INF);
    }

    vector<int> val(n);
    for (int i = 0; i < n; ++i) {
        val[i] = (nxt[i] == INF ? INF : nxt[i] - i);
    }

    int log_n = 0;
    while ((1 << log_n) <= n) log_n++;
    vector<vector<int>> st(log_n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        st[0][i] = val[i];
    }
    for (int k = 1; k < log_n; ++k) {
        for (int i = 0; i + (1 << k) <= n; ++i) {
            st[k][i] = max(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
        }
    }

    auto query_max = [&](int l, int r) {
        int len = r - l + 1;
        int k = 31 - __builtin_clz(len);
        return max(st[k][l], st[k][r - (1 << k) + 1]);
    };

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int l, r;
        cin >> l >> r;
        --l; --r;
        int len = r - l + 1;
        int low = 0, high = len / 2, ans = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                ans = max(ans, mid);
                low = mid + 1;
                continue;
            }
            int mx = query_max(l, l + mid - 1);
            if (mx <= len - 2 * mid + 1) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}
```
