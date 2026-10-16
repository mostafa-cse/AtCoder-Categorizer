# Problem Analysis: AtCoder-abc172_d — Sum of Divisors

**Problem ID**: `AtCoder-abc172_d`  
**Contest**: `abc172`  
**Rating / Difficulty**: 963  
**URL**: https://atcoder.jp/contests/abc172/tasks/abc172_d  
**VJudge Tag**: `[problem:AtCoder-abc172_d]`  
**Category File**: [`../categories/math/divisor_contribution_summation.md`](../categories/math/divisor_contribution_summation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Number Theory`  
- **Topic (Skill)**: `Divisor Contribution Summation / Order-of-Summation Swap`  

---

## 1. Problem Statement & Key Idea
Let f(K) be the number of positive divisors of K. Compute sum_{K=1}^N K * f(K) for N <= 10^7.

**Key Idea**: Instead of computing f(K) for each K in O(N sqrt(N)), swap the order of summation and compute the contribution of each divisor d to all its multiples.

## 2. Core Observation & Invariant
A number d divides multiples d, 2d, 3d, ..., m*d where m = floor(N / d). Each multiple k*d contributes k*d to the sum. Summing over all multiples of d gives d * sum_{k=1}^m k = d * (m * (m + 1) / 2). Summing this over all d in 1..N yields exact O(N) complexity.

## 3. Step-by-Step Algorithm
1. Initialize total_sum = 0.
2. For d from 1 to N: let m = N / d; total_sum += d * (m * (m + 1) / 2).
3. Print total_sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long total_sum = 0;
    for (long long d = 1; d <= n; ++d) {
        long long m = n / d;
        total_sum += d * (m * (m + 1) / 2);
    }

    cout << total_sum << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Double counting and reversing summation loops from multiples to divisors.
- **Reusable Pattern**: `Divisor contribution: sum_{d=1}^N d * (floor(N/d) * (floor(N/d) + 1) / 2).`
