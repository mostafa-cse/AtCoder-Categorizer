# Problem Analysis: AtCoder-abc338_g — G. evall

**Problem ID**: `AtCoder-abc338_g`  
**Contest**: `abc338`  
**Rating / Difficulty**: 2573  
**URL**: https://atcoder.jp/contests/abc338/tasks/abc338_g  
**VJudge Tag**: `[problem:AtCoder-abc338_g]`  
**Category File**: [`../categories/combinatorics/evall_arithmetic_substrings_contribution_technique.md`](../categories/combinatorics/evall_arithmetic_substrings_contribution_technique.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
Evaluate all valid arithmetic substrings $S[i..j]$ consisting of digits, '+', and '*' and compute their total sum modulo 998244353.

## 2. Core Observation & Invariant
Any valid arithmetic substring decomposes into terms separated by '+', where each term is a product of numbers separated by '*'. Scanning $j$ linearly, maintain base sums from preceding '+' blocks, historical product sums $H$ within the current block, and suffix expansions of the current number in $O(1)$ per digit.

## 3. Step-by-Step Algorithm
1. 1. Initialize total sum $tot = 0$, $B_{\text{sum}} = 0$, $num_{\text{prior}} = 0$, $prod_{\text{prev}} = 1$, $H = 0$.
2. 2. On '+': set $B_{\text{sum}} = last\_total$, add block digit count to $num_{\text{prior}}$, and reset block registers.
3. 3. On '*': update $H = (H \cdot cur\_num + cur\_suff\_sum)$, multiply $prod_{\text{prev}} \cdot= cur\_num$, reset number registers.
4. 4. On digit: update $cur\_num, cur\_len, cur\_suff\_sum$. Evaluate current total across all starting points and accumulate into $tot$.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    if (!(cin >> S)) return 0;

    long long tot = 0;
    long long B_sum = 0;
    long long num_prior_i = 0;

    long long prod_prev = 1;
    long long H = 0;
    long long cur_num = 0;
    long long cur_len = 0;
    long long cur_suff_sum = 0;

    long long last_total_at_j = 0;
    long long num_digits_in_block = 0;

    for (char c : S) {
        if (c == '+') {
            B_sum = last_total_at_j;
            num_prior_i = (num_prior_i + num_digits_in_block) % MOD;

            prod_prev = 1;
            H = 0;
            cur_num = 0;
            cur_len = 0;
            cur_suff_sum = 0;
            num_digits_in_block = 0;
        } else if (c == '*') {
            H = (H * cur_num + cur_suff_sum) % MOD;
            prod_prev = (prod_prev * cur_num) % MOD;
            cur_num = 0;
            cur_len = 0;
            cur_suff_sum = 0;
        } else {
            int d = c - '0';
            cur_num = (cur_num * 10 + d) % MOD;
            cur_len++;
            cur_suff_sum = (cur_suff_sum * 10 + cur_len * d) % MOD;
            num_digits_in_block++;

            long long val_inside = (H * cur_num + cur_suff_sum) % MOD;
            long long T_cur = (prod_prev * cur_num) % MOD;
            long long val_prior = (B_sum + num_prior_i * T_cur) % MOD;

            long long total_at_j = (val_inside + val_prior) % MOD;
            tot = (tot + total_at_j) % MOD;
            last_total_at_j = total_at_j;
        }
    }

    cout << tot << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
