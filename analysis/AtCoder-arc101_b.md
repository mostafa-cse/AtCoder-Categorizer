# Problem Analysis: AtCoder-arc101_b — Median of Medians

**Problem ID**: `AtCoder-arc101_b`  
**Contest**: `abc107`  
**Rating / Difficulty**: 2073  
**URL**: https://atcoder.jp/contests/abc107/tasks/arc101_b  
**VJudge Tag**: `[problem:AtCoder-arc101_b]`  
**Category File**: [`../categories/data_structures/binary_search_fenwick_median_of_medians.md`](../categories/data_structures/binary_search_fenwick_median_of_medians.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree / Fenwick Tree`  
- **Topic (Skill)**: `Binary Search on Answer with +1/-1 Reduction and Fenwick Tree Prefix Sum Inversion Counting`  

---

## 1. Problem Statement & Key Idea
Given an array A of N elements. For all 1 <= l <= r <= N, let m_{l, r} be the median of A[l..r]. Find the median of all N(N+1)/2 medians.

**Key Idea**: Binary search on the answer X. The median of a subsegment A[l..r] is >= X if and only if at least half of its elements are >= X. Replacing each element with b_i = +1 if A_i >= X else -1, the median condition becomes sum_{k=l}^r b_k > 0, which is equivalent to pref[r] > pref[l-1]. Counting such pairs (l-1, r) reduces to counting inversions in the prefix sum array, solvable in O(N log N) using a Fenwick tree. If the number of subsegments with median >= X is >= (N(N+1)/2) / 2 + 1, then the median of medians is >= X.

## 2. Core Observation & Invariant
Subsegment median comparison against X reduces to prefix sum inequalities pref[r] > pref[l-1] with +/-1 values, counted in O(N log N) via Fenwick tree.

## 3. Step-by-Step Algorithm
1. Binary search on X in [1, 10^9].
2. In check(X):
3.   Convert A to b with b_i = (+1 if A_i >= X else -1).
4.   Maintain prefix sums pref with pref[0] = 0.
5.   Insert pref[0] into a Fenwick tree shifted by N+1.
6.   For each r = 1..N: count l-1 such that pref[l-1] < pref[r] via Fenwick query, then insert pref[r].
7.   Return true iff count >= floor(total_intervals / 2) + 1.
8. Output the maximum X for which check(X) is true.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N log(max A))`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Binary searching for median values using +1/-1 transformation and prefix sum inversion counting with Fenwick tree.

**Reusable Pattern**: Median of subsegments: map elements to +/-1, then count valid ranges via Fenwick prefix sum order queries.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long total_intervals = 1LL * n * (n + 1) / 2;
    long long req = total_intervals / 2 + 1;

    auto check = [&](int x) -> bool {
        int offset = n + 1;
        Fenwick bit(2 * n + 2);
        bit.add(0 + offset, 1);

        long long count_valid = 0;
        int cur_pref = 0;

        for (int i = 0; i < n; ++i) {
            cur_pref += (a[i] >= x ? 1 : -1);
            count_valid += bit.query(cur_pref - 1 + offset);
            bit.add(cur_pref + offset, 1);
        }

        return count_valid >= req;
    };

    int low = 1, high = 1e9, ans = 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
