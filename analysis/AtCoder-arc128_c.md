# Problem Analysis: AtCoder-arc128_c — Max Dot

**Problem ID**: `AtCoder-arc128_c`  
**Contest**: `arc128`  
**Rating / Difficulty**: 1810  
**URL**: https://atcoder.jp/contests/arc128/tasks/arc128_c  
**VJudge Tag**: `[problem:AtCoder-arc128_c]`  
**Category File**: [`../categories/basics/suffix_average_monotonic_assignment.md`](../categories/basics/suffix_average_monotonic_assignment.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Convex Monotonic Variable Assignment via Suffix Average Efficiency`  

---

## 1. Problem Statement & Key Idea
Given array A of length N, and integers M and S. Choose real numbers 0 <= x_1 <= x_2 <= ... <= x_N <= M with sum(x_i) = S. Maximize sum_{i=1}^N x_i A_i.

**Key Insight**: By difference transformation y_i = x_i - x_{i - 1} >= 0, the sum condition becomes sum (N - i + 1) y_i = S, and the objective becomes sum (sum_{j=i}^N A_j) y_i. The marginal efficiency of variable y_i is the suffix average sum_{j=i}^N A_j / (N - i + 1).

## 2. Core Observation & Invariant
Optimal assignment fills the best suffix with M, and fills the next partial block with the remaining sum. Test all suffix lengths k in [1, N].

## 3. Step-by-Step Algorithm
1. Compute suffix sums of A.
2. ans = 0.0.
3. For suffix length len = 1 to N:
4.   If len * M >= S:
5.     avg = (double)S / len;
6.     score = (suffix_sum[N - len]) * avg;
7.     ans = max(ans, score);
8.   Else:
9.     rem_s = S - len * M;
10.     base_score = (suffix_sum[N - len]) * M;
11.     For rem_len = 1 to N - len:
12.       avg = (double)rem_s / rem_len;
13.       if (avg <= M) {
14.         score = base_score + (suffix_sum[N - len - rem_len] - suffix_sum[N - len]) * avg;
15.         ans = max(ans, score);
16.       }
17. Print ans with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2) or O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long M, S;
    if (!(cin >> n >> M >> S)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> suf(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        suf[i] = suf[i + 1] + a[i];
    }

    double max_ans = 0.0;

    for (int k = 1; k <= n; ++k) {
        if ((long long)k * M >= S) {
            double avg = (double)S / k;
            double score = suf[n - k] * avg;
            max_ans = max(max_ans, score);
        } else {
            long long rem_s = S - (long long)k * M;
            double base_score = suf[n - k] * (double)M;

            for (int j = 1; j <= n - k; ++j) {
                if ((long long)j * M >= rem_s) {
                    double avg = (double)rem_s / j;
                    double score = base_score + (suf[n - k - j] - suf[n - k]) * avg;
                    max_ans = max(max_ans, score);
                }
            }
        }
    }

    cout << fixed << setprecision(12) << max_ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Fractional knapsack under monotonicity constraints via suffix average sorting.
- **Reusable Pattern**: `Monotonic Sum Optimization: Evaluate suffix blocks saturated at M + remainder average.`
