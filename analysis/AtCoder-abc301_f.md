# Problem Analysis: AtCoder-abc301_f — F. Anti-DDoS

**Problem ID**: `AtCoder-abc301_f`  
**Contest**: `abc301`  
**Rating / Difficulty**: 2548  
**URL**: https://atcoder.jp/contests/abc301/tasks/abc301_f  
**VJudge Tag**: `[problem:AtCoder-abc301_f]`  
**Category File**: [`../categories/dynamic_programming_dp/anti_ddos_subsequence_counting_dp.md`](../categories/dynamic_programming_dp/anti_ddos_subsequence_counting_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Count replacements of '?' with letters such that no 'DDoS'-like subsequence ($C \dots C \dots c' \dots C'$ with uppercase $C, C'$ and lowercase $c'$) is formed.

## 2. Core Observation & Invariant
Reverse the string $S$: the forbidden pattern becomes $C' \dots c' \dots C \dots C$. A reversed string is valid iff no duplicate uppercase letter appears after the first lowercase letter following an uppercase letter. Use DP on the prefix of reversed $S$ to track uppercase presence, and combinatorics on remaining question marks to count valid assignments of distinct uppercase letters.

## 3. Step-by-Step Algorithm
1. 1. Reverse string $S$.
2. 2. Precompute factorials, inverse factorials, and powers of 26.
3. 3. Compute $DP_0[i]$ (all lowercase) and $DP_1[i]$ (uppercase followed by uppercase).
4. 4. Iterate $i$ from $N-1$ down to 0: if $S[i]$ can be lowercase, combine $DP_1[i]$ with ways to assign question marks in $S[i+1 \dots N-1]$ to unused uppercase letters using $\sum_v \binom{q}{v} \frac{(26 - u)!}{(26 - u - v)!} 26^{q - v}$.
5. 5. Output total sum modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(26 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    reverse(s.begin(), s.end());
    int n = s.size();

    int max_val = max(26, n) + 1;
    vector<long long> fact(max_val, 1), ifact(max_val, 1), p26(max_val, 1);
    for (int i = 0; i < max_val - 1; ++i) {
        fact[i + 1] = (fact[i] * (i + 1)) % MOD;
        p26[i + 1] = (p26[i] * 26) % MOD;
    }
    ifact[max_val - 1] = power(fact[max_val - 1], MOD - 2);
    for (int i = max_val - 2; i >= 0; --i) {
        ifact[i] = (ifact[i + 1] * (i + 1)) % MOD;
    }

    auto binom = [&](int nn, int r) -> long long {
        if (r < 0 || r > nn) return 0;
        return fact[nn] * ifact[r] % MOD * ifact[nn - r] % MOD;
    };

    auto upper = [](char c) -> long long {
        if (c == '?') return 26;
        return (c >= 'A' && c <= 'Z' ? 1 : 0);
    };

    auto lower = [](char c) -> long long {
        if (c == '?') return 26;
        return (c >= 'a' && c <= 'z' ? 1 : 0);
    };

    vector<long long> dp0(n + 1, 0), dp1(n + 1, 0);
    dp0[0] = 1;

    for (int i = 0; i < n; ++i) {
        dp0[i + 1] = (dp0[i] * lower(s[i])) % MOD;
        dp1[i + 1] = (dp0[i] * upper(s[i]) + dp1[i] * upper(s[i])) % MOD;
    }

    long long ans = (dp0[n] + dp1[n]) % MOD;
    int q = 0;
    vector<bool> seen(26, false);
    int seen_count = 0;

    for (int i = n - 1; i >= 0; --i) {
        int u = seen_count;
        long long sub = 0;
        int max_v = min(26 - u, q);
        for (int v = 0; v <= max_v; ++v) {
            long long term = binom(q, v) * fact[26 - u] % MOD * ifact[26 - u - v] % MOD * p26[q - v] % MOD;
            sub = (sub + term) % MOD;
        }

        long long add = sub * lower(s[i]) % MOD * dp1[i] % MOD;
        ans = (ans + add) % MOD;

        if (s[i] == '?') {
            q++;
        } else if (s[i] >= 'A' && s[i] <= 'Z') {
            int ch = s[i] - 'A';
            if (seen[ch]) break;
            seen[ch] = true;
            seen_count++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
