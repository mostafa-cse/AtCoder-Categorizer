# Problem Analysis: AtCoder-arc100_c — Or Plus Max

**Problem ID**: `AtCoder-arc100_c`  
**Contest**: `arc100`  
**Rating / Difficulty**: 2111  
**URL**: https://atcoder.jp/contests/arc100/tasks/arc100_c  
**VJudge Tag**: `[problem:AtCoder-arc100_c]`  
**Category File**: [`../categories/dynamic_programming/sos_dp_top2_submask_aggregation.md`](../categories/dynamic_programming/sos_dp_top2_submask_aggregation.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Sum Over Subsets DP (SOS DP)`  

---

## 1. Problem Statement & Key Idea
Given an array A of length 2^N. For each K in [1, 2^N - 1], find max {A_u + A_v | u < v and (u OR v) <= K}.

**Key Insight**: The condition (u OR v) <= K is relaxed to considering all subsets where u and v are submasks of mask, which ensures (u OR v) is a submask of mask. For any bitmask, the maximum pair sum is obtained by the top two largest elements among all submasks! We use SOS DP (Fast Zeta Transform) to compute the pair (max1, max2) for every mask in O(N * 2^N). Then, answer for K is the prefix maximum of (max1 + max2) for all masks <= K.

## 2. Core Observation & Invariant
Submask containment relaxes bitwise OR constraints; maintaining top 2 elements via SOS DP solves pairwise maximums in O(N * 2^N).

## 3. Step-by-Step Algorithm
1. Initialize dp[mask] = {A[mask], -1} for all mask in [0, 2^N - 1].
2. For bit j from 0 to N - 1:
3.   For mask from 0 to 2^N - 1:
4.     If bit j is set in mask:
5.       Merge top-2 elements of dp[mask ^ (1 << j)] into dp[mask].
6. Compute prefix maximums over K = 1 to 2^N - 1 of (dp[K].max1 + dp[K].max2).
7. Output the running maximum for each K.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(2^N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: SOS DP / Fast Zeta Transform maintaining top-2 maximum elements across submasks.
- **Reusable Pattern**: Pairwise sum maximization under bitwise OR constraints via SOS DP tracking top two values.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Top2 {
    int max1, max2;
    void update(int val) {
        if (val > max1) {
            max2 = max1;
            max1 = val;
        } else if (val > max2) {
            max2 = val;
        }
    }
};

Top2 merge(const Top2& a, const Top2& b) {
    Top2 res = a;
    res.update(b.max1);
    res.update(b.max2);
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total = 1 << n;
    vector<Top2> dp(total, {-1, -1});
    for (int i = 0; i < total; ++i) {
        int a;
        cin >> a;
        dp[i].max1 = a;
    }

    for (int j = 0; j < n; ++j) {
        for (int mask = 0; mask < total; ++mask) {
            if ((mask >> j) & 1) {
                dp[mask] = merge(dp[mask], dp[mask ^ (1 << j)]);
            }
        }
    }

    int cur_max = 0;
    for (int k = 1; k < total; ++k) {
        cur_max = max(cur_max, dp[k].max1 + dp[k].max2);
        cout << cur_max << "\n";
    }

    return 0;
}
```
