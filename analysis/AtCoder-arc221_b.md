# Problem Analysis: AtCoder-arc221_b — B. Two-Powered Sum

**Problem ID**: `AtCoder-arc221_b`  
**Contest**: `arc221`  
**Rating / Difficulty**: 2350  
**URL**: https://atcoder.jp/contests/arc221/tasks/arc221_b  
**VJudge Tag**: `[problem:AtCoder-arc221_b]`  
**Category File**: [`../categories/combinatorics/two_powered_sum_dag_stirling_dp.md`](../categories/combinatorics/two_powered_sum_dag_stirling_dp.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
Count reachable arrays formed by subset bitwise operations $A_i = \sum_{j \in S} 2^{j-1}$. Reversing the overwrite dependency DAG uniquely layers newly exposed elements, computed via Stirling numbers and $O(N^3)$ layer DP.

## 2. Core Observation & Invariant
An array $A$ is reachable iff its non-zero positions are partitioned into sets $U_v$ corresponding to operations $S_v$ such that the overwrite dependency graph on operations forms a DAG. Running operations in reverse uniquely partitions newly exposed elements at each step, yielding an exact $O(N^3)$ DP parameterized by total exposed elements and the size of the previous layer.

## 3. Step-by-Step Algorithm
1. Precompute Stirling numbers of the second kind $\{ {n \atop k} \}$ and binomial coefficients modulo $P$.
2. Define $dp[n][y]$ as the number of valid reverse operation sequences on $n$ elements where the most recently added layer has size $y$.
3. Transitions: choose $add$ new elements and partition them into $block$ parts with coefficient $(2^n - 2^{n-y})^{block}$, accelerated by precalculating $\text{coef}[block]$ over all previous $y$.
4. Sum $\sum_y dp[i][y] \binom{N}{i}$ over all non-zero subset sizes $i$ in $O(N^3)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long MOD;
    if (!(cin >> N >> MOD)) return 0;

    vector<vector<long long>> S(N + 1, vector<long long>(N + 1, 0));
    vector<vector<long long>> binom(N + 1, vector<long long>(N + 1, 0));

    for (int n = 0; n <= N; ++n) {
        S[n][n] = 1;
        binom[n][0] = 1;
        if (n != 0) S[n][1] = 1;
        for (int k = 2; k < n; ++k) {
            S[n][k] = (S[n - 1][k - 1] + (long long)k * S[n - 1][k]) % MOD;
        }
        for (int k = 1; k <= n; ++k) {
            binom[n][k] = (binom[n - 1][k - 1] + binom[n - 1][k]) % MOD;
        }
    }

    vector<long long> pow2(N + 1, 1);
    for (int i = 1; i <= N; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    vector<vector<long long>> dp(N + 1, vector<long long>(N + 1, 0));

    for (int n = 1; n <= N; ++n) {
        long long sum_s = 0;
        for (int k = 1; k <= n; ++k) {
            sum_s = (sum_s + S[n][k]) % MOD;
        }
        dp[n][n] = sum_s;
    }

    long long ans = 1;

    for (int n = 1; n <= N; ++n) {
        vector<long long> coef(N - n + 1, 0);
        for (int pre = 1; pre <= n; ++pre) {
            int rem = n - pre;
            long long res2 = ((pow2[pre] - 1 + MOD) % MOD) * pow2[rem] % MOD;

            long long p = 1;
            for (int block = 1; block <= N - n; ++block) {
                p = (p * res2) % MOD;
                coef[block] = (coef[block] + dp[n][pre] * p) % MOD;
            }
        }

        for (int add = 1; add <= N - n; ++add) {
            long long val = 0;
            for (int block = 1; block <= add; ++block) {
                val = (val + S[add][block] * coef[block]) % MOD;
            }
            dp[n + add][add] = (dp[n + add][add] + val * binom[n + add][add]) % MOD;
        }

        long long row_sum = 0;
        for (int y = 1; y <= n; ++y) {
            row_sum = (row_sum + dp[n][y]) % MOD;
        }
        ans = (ans + row_sum * binom[N][n]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
