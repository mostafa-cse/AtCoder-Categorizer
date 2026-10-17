# Problem Analysis: AtCoder-abc158_e — Divisible Substring

**Problem ID**: `AtCoder-abc158_e`  
**Contest**: `abc158`  
**Rating / Difficulty**: 1866  
**URL**: https://atcoder.jp/contests/abc158/tasks/abc158_e  
**VJudge Tag**: `[problem:AtCoder-abc158_e]`  
**Category File**: [`../categories/number_theory/prime_modular_suffix_invariant.md`](../categories/number_theory/prime_modular_suffix_invariant.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Invariants`  
- **Topic (Skill)**: `Prime Modular Suffix Invariant for Divisible Substring Counting`  

---

## 1. Problem Statement & Key Idea
Given a numeric string S of length N and a prime P. Count substrings S[l..r] whose decimal value is divisible by P.

**Key Insight**: If P = 2 or P = 5: divisibility depends only on the last digit (S[r] % P == 0). If gcd(10, P) = 1: value of S[l..r] is (suf[l] - suf[r + 1]) * 10^{-(N - r)} mod P. Since 10 is invertible mod P, value = 0 (mod P) iff suf[l] = suf[r + 1] (mod P).

## 2. Core Observation & Invariant
Compute suffix values suf[i] = (suf[i + 1] + S[i] * 10^{N - 1 - i}) mod P. Count frequencies of remainders and sum C(cnt[rem], 2).

## 3. Step-by-Step Algorithm
1. If P == 2 or P == 5:
2.   For each r in 0..N-1: if (S[r] - '0') % P == 0, ans += (r + 1).
3. Else:
4.   suf = 0, power10 = 1, freq[P] = {0}, freq[0] = 1.
5.   For i = N - 1 down to 0:
6.     suf = (suf + (S[i] - '0') * power10) % P.
7.     power10 = (power10 * 10) % P.
8.     ans += freq[suf].
9.     freq[suf]++.
10. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(P)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, p;
    if (!(cin >> n >> p)) return 0;

    string s;
    cin >> s;

    long long ans = 0;

    if (p == 2 || p == 5) {
        for (int i = 0; i < n; ++i) {
            if ((s[i] - '0') % p == 0) {
                ans += (i + 1);
            }
        }
    } else {
        vector<long long> freq(p, 0);
        freq[0] = 1;
        long long cur_suf = 0;
        long long pow10 = 1;

        for (int i = n - 1; i >= 0; --i) {
            cur_suf = (cur_suf + (s[i] - '0') * pow10) % p;
            pow10 = (pow10 * 10) % p;
            ans += freq[cur_suf];
            freq[cur_suf]++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Partitioning modular substring divisibility into coprime suffix remainder equality and base factor cases.
- **Reusable Pattern**: `Coprime Base Suffix Invariant: S[l..r] = 0 mod P iff suf[l] == suf[r + 1] mod P.`
