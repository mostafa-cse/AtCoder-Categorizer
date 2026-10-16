# Problem Analysis: AtCoder-typical90_bh — Chimera

**Problem ID**: `AtCoder-typical90_bh`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 060)  
**Rating / Difficulty**: 1600 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bh  
**VJudge Tag**: `[problem:AtCoder-typical90_bh]`  
**Category File**: [`../categories/dp/longest_increasing_subsequence.md`](../categories/dp/longest_increasing_subsequence.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Longest Bitonic Subsequence via Dual LIS`  

---

## 1. Problem Statement & Key Idea
Given array A of length N (N <= 3 * 10^5), find the maximum length of a bitonic subsequence (strictly increases up to peak, then strictly decreases).

**Core Idea**: For every peak element A[i], the optimal bitonic subsequence has length LIS_prefix(i) + LDS_suffix(i) - 1.

## 2. Core Observation & Invariant
Compute standard O(N log N) patience sorting LIS from left to right (inc[i]), and reverse LIS from right to left (dec[i]). Maximize inc[i] + dec[i] - 1 over all i.

## 3. Step-by-Step Algorithm
1. Compute inc[i] = length of LIS ending at i using binary search.
2. Reverse A, compute dec[i] = length of LDS starting at i.
3. Return max_{i} (inc[i] + dec[i] - 1).

## 4. Complexity Analysis
Time: O(N log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> get_lis(const vector<int>& a) {
    int n = a.size();
    vector<int> lis(n);
    vector<int> tails;

    for (int i = 0; i < n; ++i) {
        auto it = lower_bound(tails.begin(), tails.end(), a[i]);
        int idx = it - tails.begin();
        if (it == tails.end()) {
            tails.push_back(a[i]);
        } else {
            *it = a[i];
        }
        lis[i] = idx + 1;
    }
    return lis;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    auto inc = get_lis(a);

    vector<int> a_rev = a;
    reverse(a_rev.begin(), a_rev.end());
    auto dec = get_lis(a_rev);
    reverse(dec.begin(), dec.end());

    int max_len = 0;
    for (int i = 0; i < n; ++i) {
        max_len = max(max_len, inc[i] + dec[i] - 1);
    }

    cout << max_len << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Dual Longest Increasing Subsequence with binary search patience sorting.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bidirectional LIS decomposition, patience sorting with std::lower_bound, and bitonic subsequence optimization.
- **Reusable Pattern**: `Dual LIS Bitonic Peak Subsequence.`

---
Back to [Longest Bitonic Subsequence via Dual LIS](../categories/dp/longest_increasing_subsequence.md) | [Categories Directory](../categories/README.md)