# Problem Analysis: AtCoder-abc112_d — Partition

**Problem ID**: `AtCoder-abc112_d`  
**Contest**: `abc112`  
**Rating / Difficulty**: 1025  
**URL**: https://atcoder.jp/contests/abc112/tasks/abc112_d  
**VJudge Tag**: `[problem:AtCoder-abc112_d]`  
**Category File**: [`../categories/number_theory/max_gcd_sum_partition.md`](../categories/number_theory/max_gcd_sum_partition.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Divisors & GCD`  
- **Topic (Skill)**: `Maximum GCD of Sum Partition / Divisor Feasibility`  

---

## 1. Problem Statement & Key Idea
Find positive integers a_1, ..., a_N such that sum a_i = M and gcd(a_1, ..., a_N) is maximized (N <= 10^5, M <= 10^9).

**Key Idea**: If g = gcd(a_1, ..., a_N), then each a_i is a multiple of g: a_i = g * k_i. Therefore M = sum a_i = g * sum k_i. This proves that g must be a divisor of M!

## 2. Core Observation & Invariant
Since each a_i >= 1, we have k_i >= 1, so sum k_i >= N. Thus, for g to be achievable, we must have M / g >= N, which is equivalent to g <= M / N. We simply find the maximum divisor g of M that satisfies g <= M / N.

## 3. Step-by-Step Algorithm
1. Find all divisors of M by checking d from 1 up to sqrt(M).
2. For each divisor d: if d <= M / N, ans = max(ans, d); if (M / d) <= M / N, ans = max(ans, M / d).
3. Output ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(sqrt(M))`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m;
    if (!(cin >> n >> m)) return 0;

    long long max_g = 1;
    for (long long d = 1; d * d <= m; ++d) {
        if (m % d == 0) {
            if (d <= m / n) {
                max_g = max(max_g, d);
            }
            long long other = m / d;
            if (other <= m / n) {
                max_g = max(max_g, other);
            }
        }
    }

    cout << max_g << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Determining feasibility of common divisor constraints on partitioned sums.
- **Reusable Pattern**: `Max GCD of N terms summing to M: largest divisor g of M with g <= floor(M / N).`
