# Problem Analysis: AtCoder-typical90_bn — Various Arrays

**Problem ID**: `AtCoder-typical90_bn`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 066)  
**Rating / Difficulty**: 1550 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bn  
**VJudge Tag**: `[problem:AtCoder-typical90_bn]`  
**Category File**: [`../categories/math/linearity_of_expectation.md`](../categories/math/linearity_of_expectation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probability & Expected Value`  
- **Topic (Skill)**: `Linearity of Expectation on Inversions`  

---

## 1. Problem Statement & Key Idea
N independent random variables A_i chosen uniformly from [L_i, R_i]. Find the expected number of inversions (pairs i < j with A_i > A_j).

**Core Idea**: Linearity of Expectation: The expected value of the sum of indicator variables equals the sum of their individual probabilities.

## 2. Core Observation & Invariant
E[Inversions] = sum_{1 <= i < j <= N} P(A_i > A_j). For fixed i < j, P(A_i > A_j) is the count of pairs (x, y) with x in [L_i, R_i], y in [L_j, R_j], x > y, divided by (R_i - L_i + 1) * (R_j - L_j + 1).

## 3. Step-by-Step Algorithm
1. ans = 0.0.
2. Loop 1 <= i < j <= N:
   - Count pairs (x, y) with x in [L_i, R_i], y in [L_j, R_j] such that x > y.
   - prob = pairs / ((R_i - L_i + 1) * (R_j - L_j + 1)).
   - ans += prob.
3. Output ans.

## 4. Complexity Analysis
Time: O(N^2 * (R - L)), Space: O(N).

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
    if (!(cin >> n)) return 0;

    vector<int> l(n), r(n);
    for (int i = 0; i < n; ++i) cin >> l[i] >> r[i];

    double expected_inversions = 0.0;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            long long total_pairs = (long long)(r[i] - l[i] + 1) * (r[j] - l[j] + 1);
            long long inv_count = 0;
            for (int x = l[i]; x <= r[i]; ++x) {
                // Count y in [l[j], r[j]] with y < x
                int valid_y = min(x - 1, r[j]) - l[j] + 1;
                if (valid_y > 0) {
                    inv_count += valid_y;
                }
            }
            expected_inversions += (double)inv_count / total_pairs;
        }
    }

    cout << fixed << setprecision(12) << expected_inversions << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Linearity of expectation summing pairwise inversion probabilities.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Linearity of Expectation on discrete independent random variables without joint distributions.
- **Reusable Pattern**: `Linearity of Expectation on Pairwise Indicators.`

---
Back to [Linearity of Expectation on Inversions](../categories/math/linearity_of_expectation.md) | [Categories Directory](../categories/README.md)