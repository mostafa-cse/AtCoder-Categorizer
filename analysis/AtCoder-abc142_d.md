# Problem Analysis: AtCoder-abc142_d — Disjoint Set of Common Divisors

**Problem ID**: `AtCoder-abc142_d`  
**Contest**: `abc142`  
**Rating / Difficulty**: 827  
**URL**: https://atcoder.jp/contests/abc142/tasks/abc142_d  
**VJudge Tag**: `[problem:AtCoder-abc142_d]`  
**Category File**: [`../categories/number_theory/coprime_divisor_selection.md`](../categories/number_theory/coprime_divisor_selection.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Prime Factorization & GCD`  
- **Topic (Skill)**: `Coprime Divisor Selection via Prime Factorization of GCD`  

---

## 1. Problem Statement & Key Idea
Given two positive integers A, B <= 10^12. Select a subset of common divisors such that any two chosen divisors are mutually coprime. Maximize the number of chosen divisors.

**Key Idea**: Any common divisor of A and B must divide G = gcd(A, B). Two divisors are coprime if and only if they share no prime factor.

## 2. Core Observation & Invariant
To maximize the number of pairwise coprime divisors, each chosen divisor > 1 should be a distinct prime factor of G! (Selecting a composite divisor p*q would prevent selecting either p or q, reducing the total count). Including 1 (which is coprime to all numbers), the maximum count is 1 + (number of distinct prime factors of G).

## 3. Step-by-Step Algorithm
1. Compute G = gcd(A, B).
2. Prime factorize G by testing factors d from 2 up to sqrt(G).
3. Count distinct prime factors: for each d dividing G, increment count and divide G by d until G % d != 0.
4. If G > 1 after trial division, increment count by 1.
5. Answer is 1 + count.

## 4. Complexity Analysis
- **Time Complexity**: `O(log(min(A, B)) + sqrt(gcd(A, B)))`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <numeric>

using namespace std;

long long gcd_ll(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    long long g = gcd_ll(a, b);

    long long prime_count = 0;
    for (long long d = 2; d * d <= g; ++d) {
        if (g % d == 0) {
            prime_count++;
            while (g % d == 0) {
                g /= d;
            }
        }
    }
    if (g > 1) {
        prime_count++;
    }

    cout << prime_count + 1 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Maximizing independent coprime elements via prime factors of GCD.
- **Reusable Pattern**: `Max pairwise coprime divisors of (A, B) = 1 + omega(gcd(A, B)).`
