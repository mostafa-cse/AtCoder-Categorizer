# Problem Analysis: AtCoder-abc021_d — 多重ループ

**Problem ID**: `AtCoder-abc021_d`  
**Contest**: `abc021`  
**Rating / Difficulty**: 1704  
**URL**: https://atcoder.jp/contests/abc021/tasks/abc021_d  
**VJudge Tag**: `[problem:AtCoder-abc021_d]`  
**Category File**: [`../categories/combinatorics/multiset_combination_stars_and_bars.md`](../categories/combinatorics/multiset_combination_stars_and_bars.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Stars and Bars`  
- **Topic (Skill)**: `Multiset Combination with Repetition: C(n + k - 1, k)`  

---

## 1. Problem Statement & Key Idea
Given integers n and k, count the number of sequences of integers (a_1, a_2, ..., a_k) such that 1 <= a_1 <= a_2 <= ... <= a_k <= n, modulo 10^9 + 7.

**Key Insight**: The number of non-decreasing sequences of length k with values from {1, ..., n} is equivalent to selecting k elements from n options with repetition (multiset combination), which is given by C(n + k - 1, k).

## 2. Core Observation & Invariant
By defining b_i = a_i + i - 1, the condition 1 <= a_1 <= a_2 <= ... <= a_k <= n becomes strictly increasing 1 <= b_1 < b_2 < ... < b_k <= n + k - 1. Choosing k distinct elements from {1, ..., n + k - 1} has exactly C(n + k - 1, k) ways.

## 3. Step-by-Step Algorithm
1. Precompute factorials and inverse factorials up to n + k.
2. Read n and k.
3. Compute combination C(n + k - 1, k) modulo 10^9 + 7.
4. Print result.

## 4. Complexity Analysis
- **Time Complexity**: `O(n + k)`
- **Space Complexity**: `O(n + k)`

## 5. Complete C++ Solution
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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    int max_val = n + k;
    vector<long long> fact(max_val + 1), inv(max_val + 1);
    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i <= max_val; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[max_val] = modInverse(fact[max_val]);
    for (int i = max_val - 1; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n_elem, int r_elem) -> long long {
        if (r_elem < 0 || r_elem > n_elem) return 0;
        return fact[n_elem] * inv[r_elem] % MOD * inv[n_elem - r_elem] % MOD;
    };

    cout << nCr(n + k - 1, k) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Recognizing combination with repetition and mapping non-decreasing sequences to strictly increasing sequences via index offset.
- **Reusable Pattern**: `Stars and Bars Non-Decreasing Sequence: C(n + k - 1, k).`
