# Problem Analysis: AtCoder-agc030_d — Inversion Sum

**Problem ID**: `AtCoder-agc030_d`  
**Contest**: `agc030`  
**Rating / Difficulty**: 2712  
**URL**: https://atcoder.jp/contests/agc030/tasks/agc030_d  
**VJudge Tag**: `[problem:AtCoder-agc030_d]`  
**Category File**: [`../categories/math/inversion_sum_expected_swaps_dp.md`](../categories/math/inversion_sum_expected_swaps_dp.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Finding sum of inversions over 2^Q operation outcomes where each operation swaps A_X and A_Y with probability 1/2. By linearity of expectation, total inversions = 2^Q * sum_{i < j} P(A_i > A_j). Each swap operation (X, Y) only affects pairs involving X or Y, allowing an O(N) update per operation.

## 2. Core Observation & Invariant
In operation (X, Y): P(A_X > A_Y) and P(A_Y > A_X) become (P(A_X > A_Y) + P(A_Y > A_X)) / 2. For any third index k != X, Y: P(A_k > A_X) and P(A_k > A_Y) both become (P(A_k > A_X) + P(A_k > A_Y)) / 2, and symmetrically for P(A_X > A_k) and P(A_Y > A_k). All other pairs are untouched.

## 3. Step-by-Step Algorithm
1. 1. Initialize dp[i][j] = (A[i] > A[j] ? 1 : 0) for all i, j.
2. 2. For each operation (X, Y) with X != Y:
3.    - Set dp[X][Y] = dp[Y][X] = (dp[X][Y] + dp[Y][X]) * INV2 mod MOD.
4.    - For each k != X, Y: update dp[k][X] = dp[k][Y] = (dp[k][X] + dp[k][Y]) * INV2 mod MOD, and dp[X][k] = dp[Y][k] = (dp[X][k] + dp[Y][k]) * INV2 mod MOD.
5. 3. Sum dp[i][j] for all 0 <= i < j < N, multiply by 2^Q mod MOD, and print.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 + Q * N)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const long long MOD = 1000000007;
static const long long INV2 = 500000004;

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

int dp[3005][3005];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> A(n);
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (A[i] > A[j]) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = 0;
            }
        }
    }

    for (int step = 0; step < q; ++step) {
        int x, y;
        cin >> x >> y;
        --x; --y;
        if (x == y) continue;

        long long v_xy = 1LL * (dp[x][y] + dp[y][x]) * INV2 % MOD;
        dp[x][y] = dp[y][x] = v_xy;

        for (int k = 0; k < n; ++k) {
            if (k == x || k == y) continue;

            long long vk = 1LL * (dp[k][x] + dp[k][y]) * INV2 % MOD;
            dp[k][x] = dp[k][y] = vk;

            long long vx = 1LL * (dp[x][k] + dp[y][k]) * INV2 % MOD;
            dp[x][k] = dp[y][k] = vx;
        }
    }

    long long total_exp = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            total_exp = (total_exp + dp[i][j]) % MOD;
        }
    }

    long long ans = (total_exp * power(2, q)) % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
