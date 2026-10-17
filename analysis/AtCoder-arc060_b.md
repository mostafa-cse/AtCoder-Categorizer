# Problem Analysis: AtCoder-arc060_b — D. Digit Sum

**Problem ID**: `AtCoder-arc060_b`  
**Contest**: `arc060`  
**Rating / Difficulty**: 2261  
**URL**: https://atcoder.jp/contests/arc060/tasks/arc060_b  
**VJudge Tag**: `[problem:AtCoder-arc060_b]`  
**Category File**: [`../categories/math/digit_sum_base_sqrt_decomposition_divisors.md`](../categories/math/digit_sum_base_sqrt_decomposition_divisors.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Basic SQRT Decomposition`  

---

## 1. Problem Statement & Key Idea
Given integers $n$ and $s$, find the smallest integer base $b \ge 2$ such that the digit sum of $n$ in base $b$ equals $s$, or report -1 if impossible.

## 2. Core Observation & Invariant
If $n = s$, the smallest base is $n + 1$. If $n < s$, no such base exists. For $s < n$, we partition into $b \le \sqrt{n}$ and $b > \sqrt{n}$. For $b \le \sqrt{n}$, directly simulate the digit sum in $O(\sqrt{n} \log n)$. For $b > \sqrt{n}$, $n$ has at most 2 digits: $n = p b + q$ with $p + q = s$, so $p(b - 1) = n - s$. Because $p \le \sqrt{n}$, we check all divisors $p$ of $n - s$ in $O(\sqrt{n})$.

## 3. Step-by-Step Algorithm
1. Handle base cases: $n = s \implies n + 1$, $n < s \implies -1$.
2. Check all $b \in [2, \lfloor\sqrt{n}\rfloor]$ by computing $f(b, n)$ directly; return the first match.
3. For $p = 1 \dots \lfloor\sqrt{n}\rfloor$, if $(n - s) \bmod p == 0$, let $b = (n - s) / p + 1$ and $q = s - p$. If $b \ge 2, p < b, 0 \le q < b$, update the minimum valid $b$.
4. Output the minimum valid $b$ found, or -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(\sqrt{n})`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

long long f(long long b, long long n) {
    if (n < b) return n;
    return f(b, n / b) + (n % b);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, s;
    if (!(cin >> n >> s)) return 0;

    if (n == s) {
        cout << n + 1 << "\n";
        return 0;
    }
    if (n < s) {
        cout << -1 << "\n";
        return 0;
    }

    // Case 1: b <= sqrt(n)
    for (long long b = 2; b * b <= n; ++b) {
        if (f(b, n) == s) {
            cout << b << "\n";
            return 0;
        }
    }

    // Case 2: b > sqrt(n), so n has 2 digits: n = p*b + q with p + q = s
    // p * (b - 1) = n - s, with 1 <= p <= sqrt(n)
    // To minimize b, we maximize p, but let's collect all valid b and take min.
    long long ans = -1;
    long long diff = n - s;

    for (long long p = 1; p * p <= n; ++p) {
        if (diff % p == 0) {
            long long b = diff / p + 1;
            long long q = s - p;
            if (b >= 2 && p < b && q >= 0 && q < b) {
                if (ans == -1 || b < ans) {
                    ans = b;
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
