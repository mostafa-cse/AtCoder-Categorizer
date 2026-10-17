# Problem Analysis: AtCoder-abc171_f — Strivore

**Problem ID**: `AtCoder-abc171_f`  
**Contest**: `abc171`  
**Rating / Difficulty**: 1795  
**URL**: https://atcoder.jp/contests/abc171/tasks/abc171_f  
**VJudge Tag**: `[problem:AtCoder-abc171_f]`  
**Category File**: [`../categories/combinatorics/canonical_subsequence_embedding_superstrings.md`](../categories/combinatorics/canonical_subsequence_embedding_superstrings.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Subsequence Counting`  
- **Topic (Skill)**: `Canonical Greedy Subsequence Embedding / Distinct Superstring Counting`  

---

## 1. Problem Statement & Key Idea
Given string S of length N. Insert any lowercase English letter K times to form a string of length N + K. Count the number of distinct resulting strings, modulo 10^9 + 7.

**Key Insight**: A superstring T contains S iff the greedy leftmost match of S in T succeeds. Let the greedy match of S complete at index i in [N, N + K]. Then each non-matched character before index i has 25 choices (cannot match current character), the N matched characters are fixed, and characters after index i have 26 choices.

## 2. Core Observation & Invariant
Summing over the terminal match index i: sum_{i=N}^{N + K} C(i - 1, N - 1) * 25^{i - N} * 26^{N + K - i} mod 10^9 + 7.

## 3. Step-by-Step Algorithm
1. Read K and string S. N = |S|.
2. Precompute factorials and powers of 25 and 26.
3. ans = 0.
4. For i = N to N + K:
5.   ways = C(i - 1, N - 1) * pow25[i - N] % MOD * pow26[N + K - i] % MOD.
6.   ans = (ans + ways) % MOD.
7. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + K)`
- **Space Complexity**: `O(N + K)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    string s;
    cin >> s;
    int n = s.size();

    int max_len = n + k;
    vector<long long> fact(max_len + 1), inv(max_len + 1);
    vector<long long> pow25(max_len + 1), pow26(max_len + 1);

    fact[0] = inv[0] = 1;
    pow25[0] = pow26[0] = 1;

    for (int i = 1; i <= max_len; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
        pow25[i] = (pow25[i - 1] * 25) % MOD;
        pow26[i] = (pow26[i - 1] * 26) % MOD;
    }
    inv[max_len] = power(fact[max_len], MOD - 2);
    for (int i = max_len - 1; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int total, int choose) -> long long {
        if (choose < 0 || choose > total) return 0;
        return fact[total] * inv[choose] % MOD * inv[total - choose] % MOD;
    };

    long long ans = 0;
    for (int i = n; i <= max_len; ++i) {
        long long ways = nCr(i - 1, n - 1) * pow25[i - n] % MOD * pow26[max_len - i] % MOD;
        ans = (ans + ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Canonical leftmost greedy embedding to count distinct superstrings without overcounting.
- **Reusable Pattern**: `Leftmost Greedy Subsequence Embedding: sum C(i - 1, N - 1) * 25^{i - N} * 26^{L - i}.`
