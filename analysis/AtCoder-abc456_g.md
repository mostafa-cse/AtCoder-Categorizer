# Problem Analysis: AtCoder-abc456_g — G - Count Holidays

**Problem ID**: `AtCoder-abc456_g`  
**Contest**: `abc456`  
**Rating / Difficulty**: 2488  
**URL**: https://atcoder.jp/contests/abc456/tasks/abc456_g  
**VJudge Tag**: `[problem:AtCoder-abc456_g]`  
**Category File**: [`../categories/math/count_holidays_generating_function_ntt.md`](../categories/math/count_holidays_generating_function_ntt.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Number Theoretic Transform (NTT)`  

---

## 1. Problem Statement & Key Idea
Count work schedules satisfying work-day constraints where the longest run of consecutive holidays is exactly $k$, for every $1 \le k \le N$ modulo 998244353.

## 2. Core Observation & Invariant
Holidays cannot cross forced workdays 'x', so $S$ splits into independent dot blocks of lengths $L_1, \dots, L_m$. Let $F(S, k)$ be schedules with longest holiday run $\le k$. Then $F(S, k) = \prod_j f(L_j, k)$. By generating functions or inclusion-exclusion, $f(n, k) = [x^n] \frac{1 - x^{k+1}}{1 - 2x + x^{k+2}} = \sum_{m=0}^{\lfloor (n+1)/(k+2) \rfloor} (-1)^m g(n, k, m)$, which evaluates in $O(n / (k+2))$ time. Summing over all $k$ yields total complexity $O(N \log N)$.

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials, inverse factorials, and powers of 2 up to $N$.
2. 2. Split $S$ by 'x' to find the lengths of all contiguous blocks of '.' characters.
3. 3. For each $k \in [1, N]$, compute $f(L, k)$ for each block length $L$ via inclusion-exclusion formula and multiply to obtain $F[k]$.
4. 4. For $k = 0$, $F[0] = 1$.
5. 5. For each $k \in [1, N]$, output $(F[k] - F[k-1]) \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;
const int MAX = 200000;

long long fact[MAX + 1];
long long inv[MAX + 1];
long long pow2[MAX + 1];

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

void init() {
    fact[0] = 1;
    pow2[0] = 1;
    for (int i = 1; i <= MAX; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
    inv[MAX] = power(fact[MAX], MOD - 2);
    for (int i = MAX - 1; i >= 0; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }
}

inline long long C(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD;
}

long long f(int n, int k) {
    if (k >= n) return pow2[n];
    long long ans = 0;
    int max_m = (n + 1) / (k + 2);
    for (int m = 0; m <= max_m; ++m) {
        int rem1 = n - (k + 2) * m;
        long long term1 = 0;
        if (rem1 >= 0) {
            term1 = (pow2[rem1] * C(n - (k + 1) * m, m)) % MOD;
        }
        long long term2 = 0;
        if (m >= 1) {
            int rem2 = n - (k + 2) * m + 1;
            if (rem2 >= 0) {
                term2 = (pow2[rem2] * C(n - (k + 1) * m, m - 1)) % MOD;
            }
        }
        long long val = (term1 + term2) % MOD;
        if (m % 2 == 1) {
            ans = (ans - val + MOD) % MOD;
        } else {
            ans = (ans + val) % MOD;
        }
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    init();

    int N;
    if (!(cin >> N)) return 0;
    string S;
    cin >> S;

    vector<int> blocks;
    int cur = 0;
    for (char ch : S) {
        if (ch == '.') {
            cur++;
        } else {
            if (cur > 0) blocks.push_back(cur);
            cur = 0;
        }
    }
    if (cur > 0) blocks.push_back(cur);

    vector<long long> F(N + 1, 1);
    for (int k = 1; k <= N; ++k) {
        long long prod = 1;
        for (int L : blocks) {
            prod = (prod * f(L, k)) % MOD;
        }
        F[k] = prod;
    }

    for (int k = 1; k <= N; ++k) {
        long long ans = (F[k] - F[k - 1] + MOD) % MOD;
        cout << ans << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
