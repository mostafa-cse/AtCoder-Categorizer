# Problem Analysis: AtCoder-arc123_d — Inc, Dec - Decomposition

**Problem ID**: `AtCoder-arc123_d`  
**Contest**: `arc123`  
**Rating / Difficulty**: 2143  
**URL**: https://atcoder.jp/contests/arc123/tasks/arc123_d  
**VJudge Tag**: `[problem:AtCoder-arc123_d]`  
**Category File**: [`../categories/dynamic_programming/median_deviation_monotonic_sequence_decomposition.md`](../categories/dynamic_programming/median_deviation_monotonic_sequence_decomposition.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `More Tricks`  
- **Topic (Skill)**: `Slope Trick`  

---

## 1. Problem Statement & Key Idea
Given array A, find non-decreasing B and non-increasing C such that B_i + C_i = A_i for all i, minimizing sum (|B_i| + |C_i|).

**Key Insight**: The monotonicity constraints B_i - B_{i-1} >= 0 and C_{i-1} - C_i >= 0 imply B_i - B_{i-1} >= max(0, A_i - A_{i-1}). To minimize total absolute values, the optimal step increments are exactly B_i - B_{i-1} = max(0, A_i - A_{i-1}). Expressing B_i = x + P_i and C_i = A_i - P_i - x for prefix increments P_i, the objective becomes sum (|x + P_i| + |x - (A_i - P_i)|). This is the sum of L1 distances from x to 2N fixed points, which is minimized when x is the median of the 2N points.

## 2. Core Observation & Invariant
Monotone split constraints fix step deltas greedily; the remaining single degree of freedom x is minimized at the median of 2N points.

## 3. Step-by-Step Algorithm
1. Compute prefix increments P_i = sum_{j=1}^i max(0LL, A[j] - A[j-1]).
2. Collect the 2N critical points: -P_i and A_i - P_i for each i.
3. Sort all 2N points.
4. Choose x as the median point (at index N).
5. Compute and output sum |x - z_k| over all 2N points.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Greedy delta tight-binding and median reduction for L1 convex function minimization.
- **Reusable Pattern**: Decomposing sequences into monotone components B + C = A reduces to finding the median of offset critical points.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> p(n, 0);
    for (int i = 1; i <= n - 1; ++i) {
        p[i] = p[i - 1] + max(0LL, a[i] - a[i - 1]);
    }

    vector<long long> z;
    for (int i = 0; i < n; ++i) {
        z.push_back(-p[i]);
        z.push_back(a[i] - p[i]);
    }

    sort(z.begin(), z.end());
    long long median = z[n];

    long long ans = 0;
    for (long long pt : z) {
        ans += abs(median - pt);
    }

    cout << ans << "\n";
    return 0;
}
```
