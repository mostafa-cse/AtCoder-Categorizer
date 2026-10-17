# Problem Analysis: AtCoder-abc295_f — F. substr = S

**Problem ID**: `AtCoder-abc295_f`  
**Contest**: `abc295`  
**Rating / Difficulty**: 2306  
**URL**: https://atcoder.jp/contests/abc295/tasks/abc295_f  
**VJudge Tag**: `[problem:AtCoder-abc295_f]`  
**Category File**: [`../categories/dynamic_programming/digit_dp_substring_occurrence_linearity.md`](../categories/dynamic_programming/digit_dp_substring_occurrence_linearity.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP`  

---

## 1. Problem Statement & Key Idea
Given digit string $S$ of length $\le 16$, compute the total occurrences of $S$ as substrings among all integers in $[L, R]$ for $T$ queries.

## 2. Core Observation & Invariant
By linearity of occurrences, the total occurrences of $S$ in numbers $\le N$ equals the sum over all possible total lengths $D$ and starting offsets $p$ of the number of integers matching $S$ at position $p$.

## 3. Step-by-Step Algorithm
1. Express $\sum_{k=L}^R f(k) = \text{count}(R) - \text{count}(L-1)$.
2. For a fixed bound $N$, iterate over all possible digit lengths $D \le \text{len}(N)$ and starting positions $p \in [0, D - |S|]$.
3. Directly evaluate the number of valid prefixes and suffixes that keep the reconstructed number $\le N$ without full automaton construction.

## 4. Complexity Analysis
- **Time Complexity**: `O(T (\log_{10} R)^2)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long count_occurrences(long long N, const string& S) {
    if (N <= 0) return 0;
    string N_str = to_string(N);
    int L_N = N_str.size();
    int M = S.size();

    long long total = 0;

    auto p10 = [](int p) -> long long {
        long long res = 1;
        for (int i = 0; i < p; ++i) res *= 10;
        return res;
    };

    for (int D = M; D < L_N; ++D) {
        for (int p = 0; p <= D - M; ++p) {
            if (p == 0) {
                if (S[0] == '0') continue;
                total += p10(D - M);
            } else {
                long long pref_choices = 9 * p10(p - 1);
                long long suf_choices = p10(D - M - p);
                total += pref_choices * suf_choices;
            }
        }
    }

    int D = L_N;
    for (int p = 0; p <= D - M; ++p) {
        int suf_len = D - M - p;
        long long suf_pow = p10(suf_len);

        if (p == 0) {
            if (S[0] == '0') continue;
            string N_mid = N_str.substr(p, M);
            if (S < N_mid) {
                total += suf_pow;
            } else if (S == N_mid) {
                if (suf_len == 0) {
                    total += 1;
                } else {
                    long long N_suf = stoll(N_str.substr(p + M, suf_len));
                    total += N_suf + 1;
                }
            }
        } else {
            long long N_pref = stoll(N_str.substr(0, p));
            long long min_pref = p10(p - 1);

            if (N_pref > min_pref) {
                long long num_smaller = N_pref - min_pref;
                total += num_smaller * suf_pow;
            }

            string N_mid = N_str.substr(p, M);
            if (S < N_mid) {
                total += suf_pow;
            } else if (S == N_mid) {
                if (suf_len == 0) {
                    total += 1;
                } else {
                    long long N_suf = stoll(N_str.substr(p + M, suf_len));
                    total += N_suf + 1;
                }
            }
        }
    }

    return total;
}

void solve() {
    string S;
    long long L, R;
    if (!(cin >> S >> L >> R)) return;
    long long ans = count_occurrences(R, S) - count_occurrences(L - 1, S);
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
