# Problem Analysis: AtCoder-agc036_c — C. GP 2

**Problem ID**: `AtCoder-agc036_c`  
**Contest**: `agc036`  
**Rating / Difficulty**: 2357  
**URL**: https://atcoder.jp/contests/agc036/tasks/agc036_c  
**VJudge Tag**: `[problem:AtCoder-agc036_c]`  
**Category File**: [`../categories/basics/gp2_stars_and_bars_parity.md`](../categories/basics/gp2_stars_and_bars_parity.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Stars and Bars`  

---

## 1. Problem Statement & Key Idea
Characterize sequences reachable by $M$ operations of adding 2 to one element and 1 to another. Solved by stars and bars over each valid odd-element count $k \le M$ ($k \equiv M \pmod 2$) and subtracting the single exceeding element $> 2M$ in $O(N + M)$.

## 2. Core Observation & Invariant
A sequence of non-negative integers is reachable after $M$ operations of adding 2 to one element and 1 to another iff: (1) $\sum x_i = 3M$, (2) number of odd elements $k \le M$ and $k \equiv M \pmod 2$, and (3) $\max x_i \le 2M$. Since at most one element can exceed $2M$, complementary counting over each valid odd count $k$ yields exact closed forms via stars and bars.

## 3. Step-by-Step Algorithm
1. For each $k \in [0, M]$ with $k \equiv M \pmod 2$, choose $k$ odd positions in $\binom{N}{k}$ ways. Setting $x_i = 2 y_i + [i \text{ is odd}]$ reduces $\sum x_i = 3M$ to $\sum y_i = (3M - k)/2 = s$.
2. Total unconstrained non-negative solutions: $\binom{N}{k} \binom{s + N - 1}{N - 1}$.
3. Subtract cases where one element exceeds $2M$: if odd, $y_i \ge M$ with $k \binom{N}{k} \binom{s - M + N - 1}{N - 1}$ ways; if even, $y_i \ge M+1$ with $(N - k) \binom{N}{k} \binom{s - (M+1) + N - 1}{N - 1}$ ways.
4. Sum over all $k \le M$ in $O(N + M)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int MAX = 3000005;

long long fact[MAX], inv[MAX], ifact[MAX];

void init() {
    fact[0] = ifact[0] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++) inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    for (int i = 1; i < MAX; i++) {
        fact[i] = fact[i - 1] * i % MOD;
        ifact[i] = ifact[i - 1] * inv[i] % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    init();

    int n, m;
    if (!(cin >> n >> m)) return 0;

    long long ans = 0;
    for (int k = 0; k <= m; k++) {
        if ((3 * m - k) % 2 != 0) continue;

        // Total ways with sum 3M and k odd positions
        long long s = (3LL * m - k) / 2;
        long long total = nCr(n, k) * nCr(s + n - 1, n - 1) % MOD;

        // Exceeding 2M: at most one element > 2M
        // Case 1: exceeding element is odd (must have y_i >= M)
        if (s >= m) {
            long long rem_s = s - m;
            long long bad_odd = (long long)n * nCr(n - 1, k - 1) % MOD * nCr(rem_s + n - 1, n - 1) % MOD;
            total = (total - bad_odd + MOD) % MOD;
        }

        // Case 2: exceeding element is even (must have y_i >= M + 1)
        if (s >= m + 1) {
            long long rem_s = s - (m + 1);
            long long bad_even = (long long)n * nCr(n - 1, k) % MOD * nCr(rem_s + n - 1, n - 1) % MOD;
            total = (total - bad_even + MOD) % MOD;
        }

        ans = (ans + total) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
