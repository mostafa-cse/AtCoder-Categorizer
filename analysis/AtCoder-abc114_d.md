# Problem Analysis: AtCoder-abc114_d — 756

**Problem ID**: `AtCoder-abc114_d`  
**Contest**: `abc114`  
**Rating / Difficulty**: 1337  
**URL**: https://atcoder.jp/contests/abc114/tasks/abc114_d  
**VJudge Tag**: `[problem:AtCoder-abc114_d]`  
**Category File**: [`../categories/number_theory/prime_exponent_partitioning_75.md`](../categories/number_theory/prime_exponent_partitioning_75.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Divisor Counting`  
- **Topic (Skill)**: `Prime Exponent Partitioning for Highly Composite Numbers`  

---

## 1. Problem Statement & Key Idea
Given N <= 100. Count the number of positive divisors of N! that have exactly 75 positive divisors.

**Key Idea**: If prime factorization of d is prod p_i^{e_i}, its divisor count is prod (e_i + 1) = 75.

## 2. Core Observation & Invariant
Factorizations of 75 into integers > 1: (1) 75 = (74 + 1) -> p^74; (2) 25 * 3 = (24 + 1)(2 + 1) -> p^24 * q^2; (3) 15 * 5 = (14 + 1)(4 + 1) -> p^14 * q^4; (4) 5 * 5 * 3 = (4 + 1)(4 + 1)(2 + 1) -> p^4 * q^4 * r^2. Compute prime factor exponents in N!, count primes with exponent >= 74, 24, 14, 4, 2, and apply inclusion/permutation counting.

## 3. Step-by-Step Algorithm
1. Compute prime factorization exponents of N! using trial division up to N.
2. Count c(k) = number of primes with exponent >= k in N!.
3. Ways for p^74: c(74).
4. Ways for p^24 * q^2: c(24) * (c(2) - 1).
5. Ways for p^14 * q^4: c(14) * (c(4) - 1).
6. Ways for p^4 * q^4 * r^2: (c(4) * (c(4) - 1) / 2) * (c(2) - 2).
7. Sum all 4 cases and output.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> exp(n + 1, 0);
    for (int i = 2; i <= n; ++i) {
        int temp = i;
        for (int p = 2; p <= n; ++p) {
            while (temp % p == 0) {
                exp[p]++;
                temp /= p;
            }
        }
    }

    auto count_at_least = [&](int k) {
        int cnt = 0;
        for (int p = 2; p <= n; ++p) {
            if (exp[p] >= k) cnt++;
        }
        return cnt;
    };

    long long ans = 0;

    // Case 1: p^74
    ans += count_at_least(74);

    // Case 2: p^24 * q^2
    ans += (long long)count_at_least(24) * (count_at_least(2) - 1);

    // Case 3: p^14 * q^4
    ans += (long long)count_at_least(14) * (count_at_least(4) - 1);

    // Case 4: p^4 * q^4 * r^2
    long long c4 = count_at_least(4);
    long long c2 = count_at_least(2);
    if (c4 >= 2 && c2 >= 3) {
        ans += (c4 * (c4 - 1) / 2) * (c2 - 2);
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Decomposing target divisor counts into prime exponent integer partitions.
- **Reusable Pattern**: `Target divisor count d = 75: partition into (e_1+1)...(e_k+1) and match prime exponents.`
