# Problem Analysis: AtCoder-arc033_4 — D. 見たことのない多項式

**Problem ID**: `AtCoder-arc033_4`  
**Contest**: `arc033`  
**Rating / Difficulty**: 2470  
**URL**: https://atcoder.jp/contests/arc033/tasks/arc033_4  
**VJudge Tag**: `[problem:AtCoder-arc033_4]`  
**Category File**: [`../categories/math/polynomial_evaluation_lagrange_interpolation.md`](../categories/math/polynomial_evaluation_lagrange_interpolation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Lagrange Interpolation`  

---

## 1. Problem Statement & Key Idea
Given polynomial $P(x)$ of degree $N$ evaluated at points $x = 0, 1, \dots, N$, compute $P(T) \pmod{10^9+7}$. For consecutive integer sample points, Lagrange Interpolation simplifies to $O(N)$ using prefix and suffix products of $(T - j)$ and factorial inverses for the denominator $(i - j)!$.

## 2. Core Observation & Invariant
The denominator $\prod_{j \ne i} (i - j) = i! \times (N - i)! \times (-1)^{N - i}$ decomposes into precomputed factorials. The numerator $\prod_{j \ne i} (T - j)$ is computed in $O(1)$ per term using prefix and suffix product arrays.

## 3. Step-by-Step Algorithm
1. 1. If $T \le N$, return $A_T \pmod{10^9+7}$.
2. 2. Compute prefix products $pref[i] = \prod_{j=0}^{i-1} (T - j)$ and suffix products $suff[i] = \prod_{j=i+1}^N (T - j)$.
3. 3. Precompute factorials and modular inverses up to $N$.
4. 4. For each $i = 0 \dots N$, compute term $A_i \times (pref[i] \times suff[i]) \times \frac{(-1)^{N-i}}{i! (N - i)!} \pmod{10^9+7}$.
5. 5. Sum terms and output result.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

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
    if (!(cin >> N)) return 0;

    vector<long long> A(N + 1);
    for (int i = 0; i <= N; ++i) cin >> A[i];

    long long T;
    cin >> T;

    if (T <= N) {
        cout << (A[T] % MOD + MOD) % MOD << "\n";
        return 0;
    }

    vector<long long> pref(N + 1, 1), suff(N + 1, 1);
    for (int i = 1; i <= N; ++i) {
        pref[i] = (pref[i - 1] * ((T - (i - 1)) % MOD)) % MOD;
    }
    for (int i = N - 1; i >= 0; --i) {
        suff[i] = (suff[i + 1] * ((T - (i + 1)) % MOD)) % MOD;
    }

    vector<long long> fact(N + 1, 1), inv(N + 1, 1);
    for (int i = 1; i <= N; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    long long ans = 0;
    for (int i = 0; i <= N; ++i) {
        long long num = pref[i] * suff[i] % MOD;
        long long den = inv[i] * inv[N - i] % MOD;
        if ((N - i) % 2 == 1) den = (MOD - den) % MOD;

        long long term = (A[i] % MOD) * num % MOD * den % MOD;
        ans = (ans + term) % MOD;
    }

    cout << (ans % MOD + MOD) % MOD << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
