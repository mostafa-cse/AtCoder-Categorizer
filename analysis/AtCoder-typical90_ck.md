# Problem Analysis: AtCoder-typical90_ck — Partitions and Inversions

**Problem ID**: `AtCoder-typical90_ck`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 089)  
**Rating / Difficulty**: 2600 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ck  
**VJudge Tag**: `[problem:AtCoder-typical90_ck]`  
**Category File**: [`../categories/dp/prefix_sum_dp.md`](../categories/dp/prefix_sum_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Two Pointers with Fenwick Tree Inversions + Prefix Sum Accelerated Partition DP`  

---

## 1. Problem Statement & Key Idea
Partition array A of length N into contiguous subarrays such that each subarray contains at most K inversions. Count valid partitions modulo 10^9+7.

**Core Idea**: For each right bound r, the left bound L[r] such that inversions in A[L[r]..r] <= K is monotonic non-decreasing (Two Pointers with Fenwick Tree).

## 2. Core Observation & Invariant
Transition is dp[r] = sum_{j = L[r] - 1}^{r - 1} dp[j]. This is a contiguous range sum of DP values, evaluated in O(1) via prefix sums of dp!

## 3. Step-by-Step Algorithm
1. Coordinate compress A.
2. Maintain two-pointer window [l, r] with Fenwick Tree counting inversions.
3. For each r: expand r, add inversions. While inversions > K: shrink l, subtract inversions.
4. dp[r] = (pref[r - 1] - pref[l - 2]) % MOD.
5. Output dp[N].

## 4. Complexity Analysis
Time: O(N log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1e9 + 7;

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
    int query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n + 1);
    vector<int> coords;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        coords.push_back(a[i]);
    }

    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());

    auto get_id = [&](int x) {
        return (int)(lower_bound(coords.begin(), coords.end(), x) - coords.begin()) + 1;
    };

    for (int i = 1; i <= n; ++i) a[i] = get_id(a[i]);

    int m = coords.size();
    Fenwick ft(m);

    vector<long long> dp(n + 1, 0);
    vector<long long> pref(n + 1, 0);

    dp[0] = 1;
    pref[0] = 1;

    int l = 1;
    long long cur_inversions = 0;

    for (int r = 1; r <= n; ++r) {
        cur_inversions += ft.query(a[r] + 1, m);
        ft.add(a[r], 1);

        while (cur_inversions > k) {
            ft.add(a[l], -1);
            cur_inversions -= ft.query(1, a[l] - 1);
            l++;
        }

        // Sum dp[j] for j in [l - 1, r - 1]
        long long sum = pref[r - 1];
        if (l - 2 >= 0) sum = (sum - pref[l - 2] + MOD) % MOD;

        dp[r] = sum;
        pref[r] = (pref[r - 1] + dp[r]) % MOD;
    }

    cout << dp[n] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Two pointers with Fenwick tree inversion maintenance and prefix-sum accelerated partition DP.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Sliding window dynamic inversion maintenance, prefix sum DP acceleration, and contiguous partition transitions.
- **Reusable Pattern**: `Two Pointers with Fenwick Tree Inversions + Prefix Sum DP.`

---
Back to [Two Pointers with Fenwick Tree Inversions + Prefix Sum Accelerated Partition DP](../categories/dp/prefix_sum_dp.md) | [Categories Directory](../categories/README.md)