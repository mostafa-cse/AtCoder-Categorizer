# Problem Analysis: AtCoder-arc185_e — E. Adjacent GCD

**Problem ID**: `AtCoder-arc185_e`  
**Contest**: `arc185`  
**Rating / Difficulty**: 2185  
**URL**: https://atcoder.jp/contests/arc185/tasks/arc185_e  
**VJudge Tag**: `[problem:AtCoder-arc185_e]`  
**Category File**: [`../categories/number_theory/eulers_totient_expansion_online_gcd_subsequence_dp.md`](../categories/number_theory/eulers_totient_expansion_online_gcd_subsequence_dp.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Multiplicative Functions`  
- **Topic (Skill)**: `Euler's Totient Function / Phi Function`  

---

## 1. Problem Statement & Key Idea
Given sequence A of length N <= 5 * 10^5, for each prefix m = 1..N find the sum of sum_{i=1}^{k-1} gcd(B_i, B_{i+1}) over all 2^m - 1 non-empty subsequences modulo 998244353. Adjacent pairs (A_i, A_m) appear in 2^{i-1} subsequences ending at m, allowing an online recurrence via Euler totient expansion.

## 2. Core Observation & Invariant
Ans(m) = 2 * Ans(m-1) + sum_{i < m} gcd(A_i, A_m) 2^{i-1}. Using the identity gcd(a, b) = sum_{d | gcd(a, b)} phi(d), the new contribution rewrites as sum_{d | A_m} phi(d) sum_{i < m, d | A_i} 2^{i-1}. Maintaining Sum[d] = sum_{i < m, d | A_i} 2^{i-1} across all divisors d <= 10^5 evaluates the contribution and updates in O(d(A_m)) time per step.

## 3. Step-by-Step Algorithm
1. Sieve Euler's totient function phi[1..100000] and precompute divisor lists divs[1..100000].
2. Maintain an array sum_d[1..100000] initialized to 0, and running answer cur_ans = 0.
3. For m = 1 to N: calculate new_contrib = sum_{d in divs[A_m]} (phi[d] * sum_d[d]) mod MOD.
4. Update cur_ans = (2 * cur_ans + new_contrib) mod MOD for m > 1 (cur_ans = 0 for m = 1). Print cur_ans.
5. For each d in divs[A_m], update sum_d[d] = (sum_d[d] + 2^{m-1}) mod MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(V log V + N * d(V))`
- **Space Complexity**: `O(V + N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;
const int MAXV = 100000;

int phi[MAXV + 1];
vector<int> divs[MAXV + 1];
long long sum_d[MAXV + 1];

void sieve() {
    for (int i = 0; i <= MAXV; ++i) phi[i] = i;
    for (int i = 2; i <= MAXV; ++i) {
        if (phi[i] == i) {
            for (int j = i; j <= MAXV; j += i) {
                phi[j] -= phi[j] / i;
            }
        }
    }
    for (int i = 1; i <= MAXV; ++i) {
        for (int j = i; j <= MAXV; j += i) {
            divs[j].push_back(i);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve();

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }

    long long cur_ans = 0;
    long long pow2 = 1; // 2^{m-1}

    for (int m = 1; m <= N; ++m) {
        int val = A[m];
        long long new_contrib = 0;
        for (int d : divs[val]) {
            new_contrib = (new_contrib + 1LL * phi[d] * sum_d[d]) % MOD;
        }

        if (m == 1) {
            cur_ans = 0;
        } else {
            cur_ans = (cur_ans * 2 + new_contrib) % MOD;
        }

        cout << cur_ans << "\n";

        for (int d : divs[val]) {
            sum_d[d] = (sum_d[d] + pow2) % MOD;
        }
        pow2 = (pow2 * 2) % MOD;
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
