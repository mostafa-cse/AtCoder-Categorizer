# Problem Analysis: AtCoder-arc189_d — Takahashi is Slime

**Problem ID**: `AtCoder-arc189_d`  
**Contest**: `arc189`  
**Rating / Difficulty**: 2006  
**URL**: https://atcoder.jp/contests/arc189/tasks/arc189_d  
**VJudge Tag**: `[problem:AtCoder-arc189_d]`  
**Category File**: [`../categories/data_structures/subarray_monotonic_doubling_expansion_segment_tree.md`](../categories/data_structures/subarray_monotonic_doubling_expansion_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree / Fenwick Tree`  
- **Topic (Skill)**: `Subarray Monotonic Doubling Expansion via Segment Tree Range Max`  

---

## 1. Problem Statement & Key Idea
N slimes are in a row with sizes A_1, ..., A_N. A slime of size X can absorb an adjacent slime of size Y iff X > Y, increasing its size to X + Y. For each starting position i (1 <= i <= N), find the maximum size Takahashi can reach if he starts as slime i.

**Key Idea**: As a slime absorbs adjacent slimes, the absorbed region forms a contiguous subarray [L, R] with sum S = sum_{k=L}^R A_k. It can expand left if S > A_{L-1} and right if S > A_{R+1}. Since the absorbed elements sum to S, whenever it absorbs past a neighbor larger than its previous elements, its sum at least doubles. Using a Segment Tree on range maximums, we can binary search the maximal interval [L', R'] with elements < S to expand greedily in O(log N) per doubling step.

## 2. Core Observation & Invariant
Slime expansion is contiguous and monotone; because size at least doubles on each boundary break, at most O(log(sum A)) expansion phases occur per slime.

## 3. Step-by-Step Algorithm
1. Build prefix sums of A for O(1) range sum queries.
2. Build a Segment Tree on A for range maximum queries.
3. For each starting position i from 1 to N:
4.   Initialize [L, R] = [i, i] and sum S = A[i].
5.   Loop:
6.     Expand L to the left as long as A[L-1] < S (binary search with Segment Tree).
7.     Expand R to the right as long as A[R+1] < S (binary search with Segment Tree).
8.     Update S = prefix_sum[R] - prefix_sum[L - 1].
9.     If neither boundary can be absorbed (or bounds reached), terminate.
10.   ans[i] = S.
11. Output all ans[i].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log^2 N)`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Monotonic subarray expansion with logarithmic phase doubling using Segment Tree queries.

**Reusable Pattern**: Doubling Segment Expansion: Expanding an interval greedily while checking boundary conditions with binary search on Segment Tree maximums.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

struct SegTree {
    int n;
    vector<long long> tree;
    SegTree(int n) : n(n), tree(4 * n, 0) {}

    void build(const vector<long long>& a, int node, int l, int r) {
        if (l == r) {
            tree[node] = a[l];
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    long long query(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return tree[node];
        if (r < ql || l > qr) return 0;
        int mid = l + (r - l) / 2;
        return max(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    vector<long long> pref(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        pref[i] = pref[i - 1] + a[i];
    }

    SegTree st(n);
    st.build(a, 1, 1, n);

    auto query_sum = [&](int l, int r) {
        return pref[r] - pref[l - 1];
    };

    vector<long long> ans(n + 1);

    for (int i = 1; i <= n; ++i) {
        int l = i, r = i;
        long long s = a[i];

        while (true) {
            bool changed = false;

            // Try to expand left
            if (l > 1 && a[l - 1] < s) {
                // Binary search leftmost index L' in [1, l - 1] such that max(L' .. l - 1) < s
                int low = 1, high = l - 1, best_l = l - 1;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    if (st.query(1, 1, n, mid, l - 1) < s) {
                        best_l = mid;
                        high = mid - 1;
                    } else {
                        low = mid + 1;
                    }
                }
                l = best_l;
                s = query_sum(l, r);
                changed = true;
            }

            // Try to expand right
            if (r < n && a[r + 1] < s) {
                // Binary search rightmost index R' in [r + 1, n] such that max(r + 1 .. R') < s
                int low = r + 1, high = n, best_r = r + 1;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    if (st.query(1, 1, n, r + 1, mid) < s) {
                        best_r = mid;
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                r = best_r;
                s = query_sum(l, r);
                changed = true;
            }

            if (!changed) break;
        }

        ans[i] = s;
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
