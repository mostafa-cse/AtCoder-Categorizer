# Problem Analysis: AtCoder-abc428_g — G - Necklace

**Problem ID**: `AtCoder-abc428_g`  
**Contest**: `abc428`  
**Rating / Difficulty**: 2472  
**URL**: https://atcoder.jp/contests/abc428/tasks/abc428_g  
**VJudge Tag**: `[problem:AtCoder-abc428_g]`  
**Category File**: [`../categories/number_theory/necklace_dirichlet_convolution_polya.md`](../categories/number_theory/necklace_dirichlet_convolution_polya.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Multiplicative Functions`  
- **Topic (Skill)**: `Dirichlet convolution`  

---

## 1. Problem Statement & Key Idea
Count the number of non-empty circular necklaces of jewels modulo 998244353 whose beauty product equals $x$ for each $2 \le x \le U$.

## 2. Core Observation & Invariant
Since each jewel has beauty $\ge 2$, the maximum necklace length is $V = \lfloor \log_2 U \rfloor \le 20$. Let $A[n][s]$ be the number of linear jewel sequences of length $n$ with product $s$, which is computed by Dirichlet DP in $O(U \log^2 U)$. By Polya's Enumeration Theorem / Burnside's Lemma, rotational symmetry over length $L$ yields $\frac{1}{L} \sum_{d | L} \varphi(d) A[L/d][x^{1/d}]$. Summing over all $L \le V$ evaluates the count for all $x \le U$ simultaneously.

## 3. Step-by-Step Algorithm
1. 1. Compute frequency array of jewel beauties $freq[t]$ for $t \le U$.
2. 2. Initialize Dirichlet DP table $dp[0][1] = 1$. For $n = 0, \dots, V-1$, for each $s \le U$, transition to $s \cdot t \le U$ with $dp[n+1][s \cdot t] += dp[n][s] \cdot freq[t]$.
3. 3. Precompute Euler's totient function $\varphi(d)$ for $d \le V$.
4. 4. For each necklace length $L \in [1, V]$ and each divisor $d \mid L$, add the rotational contribution $\frac{\varphi(d)}{L} dp[L/d][y]$ to answer at index $y^d$ for all $y$ with $y^d \le U$.
5. 5. Print the resulting counts for $x = 2, \dots, U$.

## 4. Complexity Analysis
- **Time Complexity**: `O(U \log^2 U)`
- **Space Complexity**: `O(U \log U)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const int MOD = 998244353;

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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, U;
    if (!(cin >> N >> U)) return 0;

    int V = 0;
    while ((1 << (V + 1)) <= U) V++;

    vector<int> freq(U + 1, 0);
    for (int i = 0; i < N; ++i) {
        int b;
        cin >> b;
        if (b <= U) freq[b]++;
    }

    vector<vector<long long>> dp(V + 1, vector<long long>(U + 1, 0));
    dp[0][1] = 1;

    for (int n = 0; n < V; ++n) {
        for (int s = 1; s <= U; ++s) {
            long long val = dp[n][s];
            if (val == 0) continue;
            int max_t = U / s;
            for (int t = 2; t <= max_t; ++t) {
                if (freq[t] > 0) {
                    dp[n + 1][s * t] = (dp[n + 1][s * t] + val * freq[t]) % MOD;
                }
            }
        }
    }

    vector<int> phi(V + 1);
    for (int i = 0; i <= V; ++i) phi[i] = i;
    for (int i = 2; i <= V; ++i) {
        if (phi[i] == i) {
            for (int j = i; j <= V; j += i) {
                phi[j] -= phi[j] / i;
            }
        }
    }

    vector<long long> ans(U + 1, 0);

    for (int L = 1; L <= V; ++L) {
        long long invL = power(L, MOD - 2);
        for (int d = 1; d <= L; ++d) {
            if (L % d != 0) continue;
            long long w = phi[d] * invL % MOD;
            int L_div_d = L / d;

            long long y = 1;
            while (true) {
                long long yd = 1;
                bool overflow = false;
                for (int step = 0; step < d; ++step) {
                    if (yd > U / y) { overflow = true; break; }
                    yd *= y;
                }
                if (overflow || yd > U) break;
                ans[yd] = (ans[yd] + w * dp[L_div_d][y]) % MOD;
                y++;
            }
        }
    }

    for (int x = 2; x <= U; ++x) {
        cout << ans[x] << (x == U ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
