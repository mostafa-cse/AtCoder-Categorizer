# Problem Analysis: AtCoder-abc162_e — Sum of gcd of Tuples

**Problem ID**: `AtCoder-abc162_e`  
**Contest**: `abc162`  
**Rating / Difficulty**: 1662  
**URL**: https://atcoder.jp/contests/abc162/tasks/abc162_e  
**VJudge Tag**: `[problem:AtCoder-abc162_e]`  
**Category File**: [`../categories/number_theory/gcd_tuple_sum_inclusion_exclusion.md`](../categories/number_theory/gcd_tuple_sum_inclusion_exclusion.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Inclusion-Exclusion`  
- **Topic (Skill)**: `Inclusion-Exclusion Multiple Counting from K down to 1`  

---

## 1. Problem Statement & Key Idea
Find the sum of gcd(A_1, ..., A_N) over all K^N integer sequences 1 <= A_i <= K, modulo 10^9 + 7.

**Key Insight**: Count sequences with gcd EXACTLY equal to g. The number of sequences where each element is a multiple of g is floor(K / g)^N. Subtract counts for multiples 2g, 3g, ... by processing g from K down to 1.

## 2. Core Observation & Invariant
Let cnt[g] be the number of tuples with gcd equal to g. Then cnt[g] = (K / g)^N - sum_{m=2}^{K/g} cnt[m * g]. Total sum over all g is sum_{g=1}^K g * cnt[g].

## 3. Step-by-Step Algorithm
1. Initialize cnt[K + 1].
2. For g from K down to 1:
3.   total_multiples = power(K / g, N, MOD).
4.   For m = 2 to K / g:
5.     total_multiples = (total_multiples - cnt[m * g] + MOD) % MOD.
6.   cnt[g] = total_multiples.
7. ans = sum_{g=1}^K (g * cnt[g]) % MOD.
8. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(K log K)`
- **Space Complexity**: `O(K)`

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> cnt(k + 1, 0);
    long long ans = 0;

    for (int g = k; g >= 1; --g) {
        long long ways = power(k / g, n);
        for (int m = 2 * g; m <= k; m += g) {
            ways = (ways - cnt[m] + MOD) % MOD;
        }
        cnt[g] = ways;
        ans = (ans + 1LL * g * cnt[g]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Reverse sieve inclusion-exclusion for exact greatest common divisor tuple counting.
- **Reusable Pattern**: `GCD Count via Multiple Sieve: cnt[g] = (K/g)^N - sum_{m>=2} cnt[m*g].`
