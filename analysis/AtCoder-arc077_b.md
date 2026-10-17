# Problem Analysis: AtCoder-arc077_b — 11

**Problem ID**: `AtCoder-arc077_b`  
**Contest**: `abc066`  
**Rating / Difficulty**: 1715  
**URL**: https://atcoder.jp/contests/abc066/tasks/arc077_b  
**VJudge Tag**: `[problem:AtCoder-arc077_b]`  
**Category File**: [`../categories/combinatorics/single_duplicate_subsequence_counting.md`](../categories/combinatorics/single_duplicate_subsequence_counting.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Subsequence Counting`  
- **Topic (Skill)**: `Combinatorics on Single-Duplicate Sequence / Complementary Subsequence Counting`  

---

## 1. Problem Statement & Key Idea
Given an array of length N + 1 with elements in {1, ..., N}. Exactly one value appears twice, at indices l and r (1 <= l < r <= N + 1). For each k = 1 to N + 1, find the number of distinct subsequences of length k, modulo 10^9 + 7.

**Key Insight**: The total number of length-k subsequences of an (N+1)-element array is C(N+1, k). A subsequence is duplicated if and only if it uses the duplicated value, choosing it once from index l and once from index r, while the remaining k-1 elements come strictly from outside the range [l, r].

## 2. Core Observation & Invariant
The number of elements strictly outside [l, r] is m = (l - 1) + (N + 1 - r) = N - (r - l). The number of duplicate length-k subsequences is exactly C(m, k - 1). Thus, answer = C(N + 1, k) - C(m, k - 1) mod (10^9 + 7).

## 3. Step-by-Step Algorithm
1. Find indices l and r of the duplicate value.
2. m = N - (r - l).
3. Precompute factorials and inverses up to N + 1.
4. For k = 1 to N + 1:
5.   ans = (C(N + 1, k) - C(m, k - 1) + MOD) % MOD.
6.   Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

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

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n + 1);
    vector<int> first_pos(n + 1, -1);
    int l = -1, r = -1;

    for (int i = 0; i <= n; ++i) {
        cin >> a[i];
        if (first_pos[a[i]] != -1) {
            l = first_pos[a[i]];
            r = i;
        } else {
            first_pos[a[i]] = i;
        }
    }

    int m = n - (r - l);

    int max_val = n + 1;
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

    for (int k = 1; k <= n + 1; ++k) {
        long long total = nCr(n + 1, k);
        long long dup = nCr(m, k - 1);
        long long ans = (total - dup + MOD) % MOD;
        cout << ans << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting duplicate subsequences via identical complementary prefixes and suffixes around duplicate items.
- **Reusable Pattern**: `Single Duplicate Subsequence Deduction: Ans(k) = C(N+1, k) - C(outside, k-1).`
