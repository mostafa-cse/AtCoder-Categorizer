# Problem Analysis: AtCoder-abc231_g — G. Balls in Boxes

**Problem ID**: `AtCoder-abc231_g`  
**Contest**: `abc231`  
**Rating / Difficulty**: 2606  
**URL**: https://atcoder.jp/contests/abc231/tasks/abc231_g  
**VJudge Tag**: `[problem:AtCoder-abc231_g]`  
**Category File**: [`../categories/math/balls_in_boxes_generating_functions.md`](../categories/math/balls_in_boxes_generating_functions.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Generating Functions`  

---

## 1. Problem Statement & Key Idea
There are N boxes with A_i balls. In each of K steps, add 1 ball to a uniformly random box. Find the expected value of prod B_i, the product of final ball counts, modulo 998244353.

## 2. Core Observation & Invariant
Expanding prod (A_i + c_i) expresses the expected product as sum_{m=0}^N [x^m] P(x) * (K^{\underline{m}} / N^m), where P(x) = prod_{i=1}^N (x + A_i) and K^{\underline{m}} is the falling factorial.

## 3. Step-by-Step Algorithm
1. Compute polynomial P(x) = prod_{i=1}^N (x + A_i) in O(N^2) time.
2. Iterate m from 0 to min(N, K), multiplying coefficient poly[m] by falling factorial K^{\underline{m}} and N^{-m} modulo 998244353. Sum results.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long K;
    if (!(cin >> N >> K)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    // poly[m] = coeff of x^m in prod (x + A_i)
    vector<long long> poly = {1};
    for (long long a : A) {
        vector<long long> next_poly(poly.size() + 1, 0);
        for (size_t deg = 0; deg < poly.size(); ++deg) {
            next_poly[deg + 1] = (next_poly[deg + 1] + poly[deg]) % MOD;
            next_poly[deg] = (next_poly[deg] + poly[deg] * a) % MOD;
        }
        poly = move(next_poly);
    }

    long long invN = modInverse(N);
    long long ans = 0;
    long long falling_K = 1;
    long long invN_pow = 1;

    long long max_m = min((long long)N, K);
    for (long long m = 0; m <= max_m; ++m) {
        long long coeff = poly[m];
        long long term = coeff * falling_K % MOD * invN_pow % MOD;
        ans = (ans + term) % MOD;

        falling_K = falling_K * ((K - m) % MOD) % MOD;
        invN_pow = invN_pow * invN % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
