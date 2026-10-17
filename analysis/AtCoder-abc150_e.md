# Problem Analysis: AtCoder-abc150_e — Change a Little Bit

**Problem ID**: `AtCoder-abc150_e`  
**Contest**: `abc150`  
**Rating / Difficulty**: 1851  
**URL**: https://atcoder.jp/contests/abc150/tasks/abc150_e  
**VJudge Tag**: `[problem:AtCoder-abc150_e]`  
**Category File**: [`../categories/combinatorics/expected_rank_bit_flip_cost.md`](../categories/combinatorics/expected_rank_bit_flip_cost.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Linearity of Expectation`  
- **Topic (Skill)**: `Expected Permutation Rank / Contribution to Sum on Bit-Flip Costs`  

---

## 1. Problem Statement & Key Idea
Given cost array C of length N. To transform bitstring S to T, let differing bits be flipped in optimal greedy order (cost C_{p_i} * rank). Find the sum of minimum costs over all 4^N pairs (S, T), modulo 10^9 + 7.

**Key Insight**: Sort C descending: C_1 >= C_2 >= ... >= C_N. In any pair (S, T), bit i differs with probability 1/2. When bit i differs, the expected number of elements among C_1..C_{i-1} that also differ is (i - 1) / 2. By linearity of expectation and symmetry, the total contribution of C_i over all 4^N pairs simplifies to C_i * 2^{2N - 2} * (i + 2) mod (10^9 + 7).

## 2. Core Observation & Invariant
Sorting C takes O(N log N). Evaluating the closed-form sum takes O(N).

## 3. Step-by-Step Algorithm
1. Sort C descending.
2. Precompute powers of 2 modulo 10^9 + 7.
3. ans = 0.
4. base_ways = 2^{2N - 2} % MOD.
5. For i = 1 to N:
6.   contribution = C[i - 1] * base_ways % MOD * (i + 2) % MOD.
7.   ans = (ans + contribution) % MOD.
8. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

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

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> c(n);
    for (int i = 0; i < n; ++i) cin >> c[i];

    sort(c.rbegin(), c.rend());

    long long base_ways = power(2, 2LL * n - 2);
    long long ans = 0;

    for (int i = 1; i <= n; ++i) {
        long long term = c[i - 1] % MOD * base_ways % MOD * (i + 2) % MOD;
        ans = (ans + term) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining greedy sorting priority with expected rank linearity across all bitstring pairs.
- **Reusable Pattern**: `Permutation Rank Contribution: Element at rank i contributes (i + 2) * 2^{2N - 2} * C_i.`
