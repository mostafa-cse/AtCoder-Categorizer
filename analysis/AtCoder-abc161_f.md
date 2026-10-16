# Problem Analysis: AtCoder-abc161_f — Division or Subtraction

**Problem ID**: `AtCoder-abc161_f`  
**Contest**: `abc161`  
**Rating / Difficulty**: 1528  
**URL**: https://atcoder.jp/contests/abc161/tasks/abc161_f  
**VJudge Tag**: `[problem:AtCoder-abc161_f]`  
**Category File**: [`../categories/number_theory/divisor_analysis_division_subtraction.md`](../categories/number_theory/divisor_analysis_division_subtraction.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Divisors`  
- **Topic (Skill)**: `Number Theory Divisor Analysis on N and N-1`  

---

## 1. Problem Statement & Key Idea
Given an integer N. An operation replaces N with N / K if N is divisible by K, or N - K otherwise. Count integers K >= 2 such that N eventually becomes 1.

**Key Insight**: Split into two cases: 1) K divides N initially; 2) K does not divide N initially.

## 2. Core Observation & Invariant
If K does not divide N, N -= K is repeated until N becomes N % K. For N to become 1, we must have N % K == 1 <=> K divides (N - 1). If K divides N, repeatedly divide N by K until not divisible, then test if the remaining value mod K == 1.

## 3. Step-by-Step Algorithm
1. Find all divisors of N - 1 greater than 1: all of them are valid K.
2. Find all divisors of N greater than 1. For each divisor d:
3.   Simulate: temp = N; while temp % d == 0: temp /= d.
4.   If temp % d == 1: add d to the set of valid K.
5. Print total count of unique valid K.

## 4. Complexity Analysis
- **Time Complexity**: `O(sqrt(N))`
- **Space Complexity**: `O(sqrt(N))`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    set<long long> valid_k;

    // Case 1: K does not divide N initially => K must divide N - 1
    long long n_minus_1 = n - 1;
    for (long long d = 1; d * d <= n_minus_1; ++d) {
        if (n_minus_1 % d == 0) {
            if (d >= 2) valid_k.insert(d);
            if (n_minus_1 / d >= 2) valid_k.insert(n_minus_1 / d);
        }
    }

    // Case 2: K divides N initially
    for (long long d = 1; d * d <= n; ++d) {
        if (n % d == 0) {
            auto test_k = [&](long long k) {
                if (k < 2) return;
                long long temp = n;
                while (temp % k == 0) temp /= k;
                if (temp % k == 1) valid_k.insert(k);
            };
            test_k(d);
            test_k(n / d);
        }
    }

    cout << valid_k.size() << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Modular arithmetic reduction of repeated subtraction combined with divisor analysis.
- **Reusable Pattern**: `Divisor Branching: test divisors of N-1 (mod K == 1) and test divisors of N via full division.`
