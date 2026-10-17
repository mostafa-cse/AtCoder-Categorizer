# Problem Analysis: AtCoder-arc075_c — Meaningful Mean

**Problem ID**: `AtCoder-arc075_c`  
**Contest**: `arc075`  
**Rating / Difficulty**: 1979  
**URL**: https://atcoder.jp/contests/arc075/tasks/arc075_c  
**VJudge Tag**: `[problem:AtCoder-arc075_c]`  
**Category File**: [`../categories/data_structures/mean_threshold_prefix_inversion_fenwick.md`](../categories/data_structures/mean_threshold_prefix_inversion_fenwick.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Fenwick Tree / Coordinate Compression`  
- **Topic (Skill)**: `Mean Threshold Normalization to Prefix Monotonic Inversion Counting via Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
Given array A of length N and integer K. Count pairs (l, r) with 1 <= l <= r <= N such that the mean of subarray A[l..r] is at least K.

The condition sum_{i=l}^r A_i / (r - l + 1) >= K is equivalent to sum_{i=l}^r (A_i - K) >= 0. Transform array A into B_i = A_i - K. Compute prefix sums P_i = sum_{j=1}^i B_j with P_0 = 0. The condition becomes P_r - P_{l-1} >= 0, or P_r >= P_{l-1}. Coordinate-compress the N + 1 prefix sum values, and use a Fenwick tree to count pairs i < j with P_i <= P_j in O(N log N).

## 2. Core Observation & Invariant
Subtracting K normalizes mean thresholding into standard non-inversion counting on prefix sums.

## 3. Step-by-Step Algorithm
1. Compute normalized values B_i = A_i - K.
2. Compute prefix sums P_0 = 0, P_i = P_{i-1} + B_i.
3. Coordinate compress the N + 1 values of P.
4. ans = 0. Initialize Fenwick tree.
5. For each prefix sum P_i from 0 to N:
6.   ans += fenwick.query(compressed(P_i)).
7.   fenwick.add(compressed(P_i), 1).
8. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int idx, int val) {
        for (; idx <= n; idx += idx & -idx) tree[idx] += val;
    }
    int query(int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx) sum += tree[idx];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> p(n + 1, 0);
    vector<long long> vals;
    vals.push_back(0);

    for (int i = 0; i < n; ++i) {
        p[i + 1] = p[i] + (a[i] - k);
        vals.push_back(p[i + 1]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    auto get_rank = [&](long long val) -> int {
        return lower_bound(vals.begin(), vals.end(), val) - vals.begin() + 1;
    };

    Fenwick ft(vals.size());
    long long ans = 0;

    for (int i = 0; i <= n; ++i) {
        int r = get_rank(p[i]);
        ans += ft.query(r);
        ft.add(r, 1);
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Mean normalization transformation combined with Fenwick tree inversion/non-inversion counting.
- **Reusable Pattern**: `Mean >= K Counting: Normalize A_i - K, compute prefix sums, count P_r >= P_l via Fenwick.`
