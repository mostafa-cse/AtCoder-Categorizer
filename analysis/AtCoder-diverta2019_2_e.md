# Problem Analysis: AtCoder-diverta2019_2_e — E - Balanced Piles

**Problem ID**: `AtCoder-diverta2019_2_e`  
**Contest**: `diverta2019_2`  
**Rating / Difficulty**: 2543  
**URL**: https://atcoder.jp/contests/diverta2019_2/tasks/diverta2019_2_e  
**VJudge Tag**: `[problem:AtCoder-diverta2019_2_e]`  
**Category File**: [`../categories/combinatorics/balanced_piles_height_dag_pie.md`](../categories/combinatorics/balanced_piles_height_dag_pie.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Count sequences of $H$ pile additions across $N$ piles such that at all times, the difference between the maximum and minimum pile heights is at most $D$.

## 2. Core Observation & Invariant
Let the maximum pile height increase from $0$ to $H$. Every time the minimum pile height must be raised to avoid exceeding difference $D$, we apply the Principle of Inclusion and Exclusion (PIE) over which piles reached height $h$. The transitions reduce to a linear recurrence on height $h$ with constant multiplier $W = \sum_{i=1}^N i!$, maintained via a sliding window of width $D$.

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials and their inverse factorials.
2. 2. Compute the transition coefficient $W = \sum_{i=1}^N i!$.
3. 3. Initialize $DP[0] = 1$.
4. 4. Maintain a sliding window sum of $DP[h - D \dots h - 1]$ to compute $DP[h]$ in $O(1)$ time.
5. 5. Compute the final answer by multiplying with valid ending configurations modulo $10^9+7$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + H)`
- **Space Complexity**: `O(H)`

## 5. C++ Source Code
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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, H, D;
    if (!(cin >> N >> H >> D)) return 0;

    long long W = 0;
    long long fact = 1;
    long long N_fact = 1;
    for (int i = 1; i <= N; ++i) {
        fact = (fact * i) % MOD;
        W = (W + fact) % MOD;
        if (i == N) N_fact = fact;
    }

    vector<long long> dp(H + 1, 0);
    dp[0] = 1;
    long long cur_sum = 1;

    for (int x = 1; x <= H; ++x) {
        dp[x] = (cur_sum * W) % MOD;
        cur_sum = (cur_sum + dp[x]) % MOD;
        if (x >= D) {
            cur_sum = (cur_sum - dp[x - D] + MOD) % MOD;
        }
    }

    long long ans = (dp[H] * N_fact) % MOD;
    ans = (ans * modInverse(W)) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
