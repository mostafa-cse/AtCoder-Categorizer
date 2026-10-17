# Problem Analysis: AtCoder-agc028_b — B. Removing Blocks

**Problem ID**: `AtCoder-agc028_b`  
**Contest**: `agc028`  
**Rating / Difficulty**: 2172  
**URL**: https://atcoder.jp/contests/agc028/tasks/agc028_b  
**VJudge Tag**: `[problem:AtCoder-agc028_b]`  
**Category File**: [`../categories/math/linearity_of_expectation_harmonic_prefix_sums.md`](../categories/math/linearity_of_expectation_harmonic_prefix_sums.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Compute the total cost of removing N blocks in all N! random orders. By Linearity of Expectation, block j is connected to block i at the moment i is removed iff block i is removed before all blocks strictly between i and j. The probability is 1 / (|j - i| + 1). Summing over all pairs yields a closed-form expression using Harmonic numbers H_m = sum_{k=1}^m 1/k.

## 2. Core Observation & Invariant
The set of blocks between i and j inclusive has size |j - i| + 1. The first block among them to be removed is uniformly distributed over the |j - i| + 1 candidates. Block j contributes to the cost of removing i iff i is chosen first among these blocks, with probability 1 / (|j - i| + 1). Summing over all i for a fixed j gives H_j + H_{N - j + 1} - 1. Multiplying by N! gives the exact answer.

## 3. Step-by-Step Algorithm
1. Precompute modular inverses and harmonic prefix sums H_m = sum_{k=1}^m k^{-1} mod (10^9 + 7) in O(N).
2. Compute N! mod (10^9 + 7).
3. For each block j from 1 to N, its total expected contribution factor is H_j + H_{N - j + 1} - 1.
4. Multiply each A_j by its factor, sum over all j, and multiply the total by N! mod (10^9 + 7).

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];

    vector<long long> inv(N + 1, 1);
    for (int i = 2; i <= N; ++i) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    }

    vector<long long> H(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        H[i] = (H[i - 1] + inv[i]) % MOD;
    }

    long long fact = 1;
    for (int i = 1; i <= N; ++i) {
        fact = (fact * i) % MOD;
    }

    long long total = 0;
    for (int j = 1; j <= N; ++j) {
        long long coeff = (H[j] + H[N - j + 1] - 1 + MOD) % MOD;
        long long term = (A[j] % MOD) * coeff % MOD;
        total = (total + term) % MOD;
    }

    long long ans = (total * fact) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
