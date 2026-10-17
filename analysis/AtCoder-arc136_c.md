# Problem Analysis: AtCoder-arc136_c — Circular Addition

**Problem ID**: `AtCoder-arc136_c`  
**Contest**: `arc136`  
**Rating / Difficulty**: 2137  
**URL**: https://atcoder.jp/contests/arc136/tasks/arc136_c  
**VJudge Tag**: `[problem:AtCoder-arc136_c]`  
**Category File**: [`../categories/basics/circular_interval_increments_positive_variation.md`](../categories/basics/circular_interval_increments_positive_variation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Given a circular array A_1, ..., A_N, find the minimum number of interval increments needed to create A from an array of all zeros.

**Key Insight**: Each interval increment on a circle increases the maximum element by at most 1, so answer >= max_i A_i. Also, each interval increment contributes at most 1 to the sum of positive adjacent differences sum_{i=1}^N max(0, A_i - A_{i-1}) (wrapping around). Thus answer >= sum_{i=1}^N max(0, A_i - A_{i-1}). It can be shown that this theoretical lower bound is always tight: ans = max(max_i A_i, sum_{i=1}^N max(0, A_i - A_{i-1})).

## 2. Core Observation & Invariant
Circular range addition operations are bounded by max(max A, sum max(0, A_i - A_{i-1})), and this bound is always achievable.

## 3. Step-by-Step Algorithm
1. Compute max_val = max_i A_i.
2. Compute sum_pos_diff = sum_{i=0}^{N-1} max(0LL, A[i] - A[(i - 1 + N) % N]).
3. Output max(max_val, sum_pos_diff).

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Circular total variation analysis and invariant bound tightness proof.
- **Reusable Pattern**: Minimum circular interval additions equal max(max A, total positive cyclic differences).

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
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

    vector<long long> a(n);
    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    long long sum_pos_diff = 0;
    for (int i = 0; i < n; ++i) {
        int prev_idx = (i - 1 + n) % n;
        if (a[i] > a[prev_idx]) {
            sum_pos_diff += (a[i] - a[prev_idx]);
        }
    }

    long long ans = max(max_val, sum_pos_diff);
    cout << ans << "\n";
    return 0;
}
```
