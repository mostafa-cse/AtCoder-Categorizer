# Problem Analysis: AtCoder-abc242_h — Ex - Random Painting

**Problem ID**: `AtCoder-abc242_h`  
**Contest**: `abc242`  
**Rating / Difficulty**: 2835  
**URL**: https://atcoder.jp/contests/abc242/tasks/abc242_h  
**VJudge Tag**: `[problem:AtCoder-abc242_h]`  
**Category File**: [`../categories/combinatorics/segment_coverage_min_max_expectation_interval_dp.md`](../categories/combinatorics/segment_coverage_min_max_expectation_interval_dp.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
N cells initially white. M intervals [L_i, R_i] in a box. In each step, draw a random interval and paint its cells black. Find the expected number of steps until all N cells are black modulo 998244353.

## 2. Core Observation & Invariant
By Min-Max Expectation, E[max T_i] = sum_{empty != S} (-1)^{|S|+1} E[min_{i in S} T_i]. The time to hit at least one cell in S is a geometric random variable with expectation M / c(S), where c(S) is the number of intervals intersecting S. Crucially, c(S) = M - (intervals disjoint from S). For a chosen subset S = {s_1 < ... < s_k}, an interval is disjoint from S iff it lies entirely within one gap [s_j + 1, s_{j+1} - 1]. An interval DP computes the signed weights sum_{S: c(S) = c} (-1)^{|S|+1} in O(N^2 M) time.

## 3. Step-by-Step Algorithm
1. 1. Precompute cnt[l][r]: number of given intervals completely contained in [l, r].
2. 2. Define dp[i][k]: last chosen element of S is i, with k total disjoint intervals so far, storing sum of (-1)^|S|.
3. 3. Initialize dp[0][0] = 1.
4. 4. Transition from i to j in i+1..N+1: add cnt[i+1][j-1] to disjoint count k, multiplying by -1 if j <= N (adding an element to S).
5. 5. For each disjoint count k, c(S) = M - k. Extract ways = dp[N+1][k] (excluding empty set).
6. 6. Multiply by (-1) to obtain (-1)^{|S|+1}, and accumulate ways * M * inv(c) modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 * M)`
- **Space Complexity**: `O(N * M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> cnt(n + 2, vector<int>(n + 2, 0));
    for (int i = 0; i < m; ++i) {
        int l, r;
        cin >> l >> r;
        for (int left = 1; left <= l; ++left) {
            for (int right = r; right <= n; ++right) {
                cnt[left][right]++;
            }
        }
    }

    // dp[i][k]
    vector<vector<long long>> dp(n + 2, vector<long long>(m + 1, 0));
    dp[0][0] = 1;

    for (int i = 0; i <= n; ++i) {
        for (int k = 0; k <= m; ++k) {
            if (!dp[i][k]) continue;
            long long val = dp[i][k];
            for (int j = i + 1; j <= n + 1; ++j) {
                int add_cnt = (i + 1 <= j - 1) ? cnt[i + 1][j - 1] : 0;
                int nk = k + add_cnt;
                if (nk <= m) {
                    long long coeff = (j <= n) ? (MOD - 1) : 1;
                    dp[j][nk] = (dp[j][nk] + val * coeff) % MOD;
                }
            }
        }
    }

    long long ans = 0;
    int total_all = cnt[1][n];
    for (int k = 0; k <= m; ++k) {
        int c = m - k;
        if (c <= 0) continue;
        long long ways = dp[n + 1][k];
        if (k == total_all) {
            ways = (ways - 1 + MOD) % MOD;
        }
        long long term = (MOD - ways) % MOD;
        long long inv_c = modInverse(c);
        long long contrib = term * m % MOD * inv_c % MOD;
        ans = (ans + contrib) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
