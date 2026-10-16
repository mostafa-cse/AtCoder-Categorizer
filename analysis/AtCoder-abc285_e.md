# Problem Analysis: AtCoder-abc285_e — Work or Rest

**Problem ID**: `AtCoder-abc285_e`  
**Contest**: `abc285`  
**Rating / Difficulty**: 1466  
**URL**: https://atcoder.jp/contests/abc285/tasks/abc285_e  
**VJudge Tag**: `[problem:AtCoder-abc285_e]`  
**Category File**: [`../categories/dp/circular_segment_decomposition_dp.md`](../categories/dp/circular_segment_decomposition_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Circular Segment Decomposition DP`  

---

## 1. Problem Statement & Key Idea
Schedule a repeating week of N days (N <= 5000) containing at least one rest day. On a workday, productivity is A[min(d_left, d_right)] where d_left and d_right are days to nearest rest days. Maximize total weekly productivity.

**Key Insight**: By rotational symmetry, fix day 1 as a rest day. The remaining days are partitioned into contiguous blocks of workdays between rest days. The productivity of a block of length L depends solely on L.

## 2. Core Observation & Invariant
Precompute val[L] = productivity of a contiguous block of L workdays between two rest days. Then dp[i] = max productivity using first i days ending with a rest day at day i. Transition: dp[i] = max_{j < i} (dp[j] + val[i - j - 1]).

## 3. Step-by-Step Algorithm
1. Precompute val[L] for L = 1..N: val[L] = sum_{k=1}^L A[min(k, L - k + 1)].
2. Initialize dp[N + 1] with 0.
3. For i from 1 to N:
4.   For j from 0 to i - 1:
5.     dp[i] = max(dp[i], dp[j] + val[i - j - 1]).
6. Print dp[N].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
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

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    // val[L]: productivity of L consecutive workdays between two rest days
    vector<long long> val(n + 1, 0);
    for (int L = 1; L <= n; ++L) {
        long long sum = 0;
        for (int k = 1; k <= L; ++k) {
            sum += a[min(k, L - k + 1)];
        }
        val[L] = sum;
    }

    vector<long long> dp(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            dp[i] = max(dp[i], dp[j] + val[i - j - 1]);
        }
    }

    cout << dp[n] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Circular symmetry breaking by fixing an anchor point followed by segment partitioning DP.
- **Reusable Pattern**: `Circular Interval Partitioning: fix index 1 as boundary, dp[i] = max(dp[j] + cost(segment)).`
