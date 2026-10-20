# Problem Analysis: AtCoder-keyence2019_f — F - Paper Cutting

**Problem ID**: `AtCoder-keyence2019_f`  
**Contest**: `keyence2019`  
**Rating / Difficulty**: 2967  
**URL**: https://atcoder.jp/contests/keyence2019/tasks/keyence2019_f  
**VJudge Tag**: `[problem:AtCoder-keyence2019_f]`  
**Category File**: [`../categories/math/grid_paper_cutting_piece_contribution_expectation.md`](../categories/math/grid_paper_cutting_piece_contribution_expectation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
A paper of size H x W has H-1 horizontal and W-1 vertical cut lines (N = H + W - 2). We choose a permutation of K cut lines uniformly at random and cut along them sequentially. Find the expected total piece perimeter/count times P(N, K) modulo 10^9+7.

## 2. Core Observation & Invariant
By linearity of expectation, the expected number of pieces after t cuts depends on the number of horizontal cuts h and vertical cuts w made among the t cuts. Since each cut is chosen uniformly from all remaining grid lines, (h, w) follows a hypergeometric distribution. The expected product E[h * w] = t(t-1)(H-1)(W-1) / (N(N-1)). This allows the total sum over all steps to be evaluated in O(K)!

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials and modular inverses up to max(H, W, N).
2. 2. Use linearity of expectation: express expected piece count and cell boundary contribution at step t in terms of E[h_t w_t] = t(t-1)(H-1)(W-1) / (N(N-1)).
3. 3. Sum the expectation formula across t = 1 ... K.
4. 4. Multiply by P(N, K) = N! / (N - K)! modulo 10^9+7.
5. 5. Output the result.

## 4. Complexity Analysis
- **Time Complexity**: `O(K)`
- **Space Complexity**: `O(H + W)`

## 5. C++ Source Code
```cpp
#include <iostream>

using namespace std;

const int MOD = 1e9 + 7;

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

    long long H, W, K;
    if (!(cin >> H >> W >> K)) return 0;

    long long N = H + W;

    // sum_{t=1}^K t(t-1) = (K+1)*K*(K-1)/3
    long long sum_t_t1 = (K + 1) % MOD * (K % MOD) % MOD * ((K - 1) % MOD) % MOD * modInverse(3) % MOD;
    long long sum_t = K % MOD * ((K + 1) % MOD) % MOD * modInverse(2) % MOD;
    long long sum_1 = K % MOD;

    long long term1 = 0;
    if (N > 1) {
        long long num = sum_t_t1 * (H % MOD) % MOD * (W % MOD) % MOD;
        long long den = (N % MOD) * ((N - 1) % MOD) % MOD;
        term1 = num * modInverse(den) % MOD;
    }

    long long E_sum = (term1 + sum_t + sum_1) % MOD;

    // Multiply by P(N, K) = N! / (N - K)!
    long long p_n_k = 1;
    for (long long i = N - K + 1; i <= N; ++i) {
        p_n_k = (p_n_k * (i % MOD)) % MOD;
    }

    long long ans = (E_sum * p_n_k) % MOD;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
