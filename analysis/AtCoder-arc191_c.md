# Problem Analysis: AtCoder-arc191_c — C. A^n - 1

**Problem ID**: `AtCoder-arc191_c`  
**Contest**: `arc191`  
**Rating / Difficulty**: 2198  
**URL**: https://atcoder.jp/contests/arc191/tasks/arc191_c  
**VJudge Tag**: `[problem:AtCoder-arc191_c]`  
**Category File**: [`../categories/number_theory/binomial_multiplicative_order_construction.md`](../categories/number_theory/binomial_multiplicative_order_construction.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Multiplicative Order and Carmichael's Lambda Function`  

---

## 1. Problem Statement & Key Idea
Find (A, M) with A, M <= 10^18 such that ord_M(A) = N. Setting (A, M) = (N + 1, N^2) guarantees that (N+1)^n = 1 + nN mod N^2 by the Binomial Theorem, so (N+1)^n = 1 mod N^2 iff N divides n, making the order exactly N for all N >= 2. For N = 1, (2, 1) works.

## 2. Core Observation & Invariant
In the binomial expansion (1 + N)^n = 1 + nN + C(n, 2) N^2 + ..., every term for k >= 2 contains N^k and is divisible by N^2. Thus (N+1)^n = 1 + nN mod N^2 for all n, so the smallest positive integer with (N+1)^n = 1 mod N^2 is n = N. Since N <= 10^9, N^2 <= 10^{18} fits in a 64-bit integer.

## 3. Step-by-Step Algorithm
1. For each test case:
2.   If N == 1, output 2 1.
3.   Else output (N + 1) (N * N).

## 4. Complexity Analysis
- **Time Complexity**: `O(1) per testcase`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>

using namespace std;

void solve() {
    long long N;
    cin >> N;
    if (N == 1) {
        cout << 2 << " " << 1 << "\n";
    } else {
        long long A = N + 1;
        long long M = N * N;
        cout << A << " " << M << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
