# Problem Analysis: AtCoder-abc276_g — G. Count Sequences

**Problem ID**: `AtCoder-abc276_g`  
**Contest**: `abc276`  
**Rating / Difficulty**: 2278  
**URL**: https://atcoder.jp/contests/abc276/tasks/abc276_g  
**VJudge Tag**: `[problem:AtCoder-abc276_g]`  
**Category File**: [`../categories/basics/stars_and_bars_modular_difference_hockey_stick.md`](../categories/basics/stars_and_bars_modular_difference_hockey_stick.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Stars and Bars`  

---

## 1. Problem Statement & Key Idea
Count the number of non-decreasing sequences $0 \le A_1 \le A_2 \le \dots \le A_N \le M$ such that $A_{i+1} - A_i \not\equiv 0 \pmod 3$ for all $1 \le i < N$, modulo 998244353.

## 2. Core Observation & Invariant
Adjacent differences $d_i = a_{i+1} - a_i \not\equiv 0 \pmod 3$ decompose as $x_i + 3y_i$ with $x_i \in \{1, 2\}$. Fixing the count of $x_i = 1$ leaves the non-negative integer solutions to $\sum y_i \le L = \lfloor(M-B)/3\rfloor$, which evaluates in $O(1)$ via the hockey stick identity.

## 3. Step-by-Step Algorithm
1. 1. Let $d_i = a_{i+1} - a_i$. Since $a_i \le a_{i+1}$ and $a_i \not\equiv a_{i+1} \pmod 3$, each difference satisfies $d_i \ge 1$ and $d_i \bmod 3 \in \{1, 2\}$.\n2. Decompose $d_i = x_i + 3 y_i$ where $x_i \in \{1, 2\}$ and $y_i \ge 0$. Suppose $c$ of the $N-1$ differences have $x_i = 1$, and $(N-1-c)$ have $x_i = 2$. There are $\binom{N-1}{c}$ ways to choose their positions.\n3. The base sum is $B = c + 2(N-1-c)$. The condition $a_N \le M$ becomes $a_1 + 3\sum_{i=1}^{N-1} y_i \le M - B$. For a fixed sum $K = \sum y_i$, $a_1$ can take any integer value in $[0, M - B - 3K]$, which has $M - B + 1 - 3K$ choices.\n4. Summing over $K$ from $0$ to $L = \lfloor(M-B)/3\rfloor$: $\sum_{K=0}^L (M-B+1 - 3K) \binom{K + N - 2}{N - 2} = (M-B+1)\binom{L+N-1}{N-1} - 3(N-1)\binom{L+N-1}{N}$ by the hockey stick identity!\n5. Iterating $c$ from $0$ to $N-1$ computes each term in $O(1)$. Total time is $O(N + M)$ for precomputing factorials.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

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

const int MAX = 14000005;
long long fact[MAX];
long long invFact[MAX];

void init_fact(int limit) {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i <= limit; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[limit] = modInverse(fact[limit]);
    for (int i = limit - 1; i >= 1; i--) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    int max_val = n + m / 3 + 5;
    init_fact(max_val);

    long long ans = 0;
    for (int c = 0; c < n; c++) {
        long long B = 1LL * c * 1 + 1LL * (n - 1 - c) * 2;
        if (B > m) continue;

        int L = (m - B) / 3;
        long long term1 = (m - B + 1) % MOD * nCr(L + n - 1, n - 1) % MOD;
        long long term2 = 3LL * (n - 1) % MOD * nCr(L + n - 1, n) % MOD;
        long long ways_y = (term1 - term2 + MOD) % MOD;
        long long ways_c = nCr(n - 1, c);

        ans = (ans + ways_c * ways_y) % MOD;
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
