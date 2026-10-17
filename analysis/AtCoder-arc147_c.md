# Problem Analysis: AtCoder-arc147_c — Min Diff Sum

**Problem ID**: `AtCoder-arc147_c`  
**Contest**: `arc147`  
**Rating / Difficulty**: 1704  
**URL**: https://atcoder.jp/contests/arc147/tasks/arc147_c  
**VJudge Tag**: `[problem:AtCoder-arc147_c]`  
**Category File**: [`../categories/basics/min_diff_sum_intervals_pairing.md`](../categories/basics/min_diff_sum_intervals_pairing.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Min Sum of Pairwise Differences on Intervals via Median Pairing`  

---

## 1. Problem Statement & Key Idea
Given N intervals [L_i, R_i], choose x_i in [L_i, R_i] for each i to minimize sum_{1 <= i < j <= N} |x_i - x_j|.

**Key Insight**: For sorted coordinates x_1 <= x_2 <= ... <= x_N, the sum of differences can be decomposed into sum_{k=1}^{floor(N/2)} (N - 2k + 1) * (x_{N - k + 1} - x_k). To minimize this, pair the largest L_i with the smallest R_j greedily.

## 2. Core Observation & Invariant
If the highest available L is greater than the lowest available R, their minimal distance is L - R, which contributes (N - 2k + 1) * (L - R). If L <= R, the intervals overlap and can be assigned identical values with 0 cost.

## 3. Step-by-Step Algorithm
1. Sort all L descending and all R ascending.
2. For k = 0 to N/2 - 1:
3.   weight = N - 1 - 2 * k.
4.   if L[k] > R[k]:
5.     ans += weight * (L[k] - R[k]).
6. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> L(n), R(n);
    for (int i = 0; i < n; ++i) {
        cin >> L[i] >> R[i];
    }

    sort(L.rbegin(), L.rend());
    sort(R.begin(), R.end());

    long long ans = 0;
    for (int k = 0; k < n / 2; ++k) {
        long long weight = n - 1 - 2LL * k;
        if (L[k] > R[k]) {
            ans += weight * (L[k] - R[k]);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pairwise distance coefficient decomposition and greedy extreme interval matching.
- **Reusable Pattern**: `Pairwise 1D Difference Minimization on Intervals: Pair descending L with ascending R.`
