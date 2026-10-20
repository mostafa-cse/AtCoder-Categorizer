# Problem Analysis: AtCoder-code_festival_2017_qualb_e — E. Popping Balls

**Problem ID**: `AtCoder-code_festival_2017_qualb_e`  
**Contest**: `code_festival_2017_qualb`  
**Rating / Difficulty**: 2937  
**URL**: https://atcoder.jp/contests/code_festival_2017_qualb/tasks/code_festival_2017_qualb_e  
**VJudge Tag**: `[problem:AtCoder-code_festival_2017_qualb_e]`  
**Category File**: [`../categories/combinatorics/popping_balls_grid_walk_reachability_dp.md`](../categories/combinatorics/popping_balls_grid_walk_reachability_dp.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Product Trick`  

---

## 1. Problem Statement & Key Idea
We have A red balls and B blue balls. C balls are drawn from the left and D from the right. Count the number of distinct sequences of colors drawn.

## 2. Core Observation & Invariant
Model the drawing process as a grid walk in the (x, y) plane representing remaining red and blue balls. Different drawing orders can yield the same multiset or sequence of drawn balls. By analyzing the boundary of the reachable region, the distinct output sequences correspond bijectively to valid grid paths avoiding certain forbidden boundaries. The Product Trick / binomial convolution computes the number of non-overlapping configurations.

## 3. Step-by-Step Algorithm
1. 1. Rephrase the drawing choices into horizontal and vertical steps on an A x B grid.
2. 2. Identify the boundary conditions where left/right draws interact.
3. 3. Compute path counts using precomputed factorials and modular combinations.
4. 4. Output final count modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(A + B)`
- **Space Complexity**: `O(A + B)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

static const int MOD = 1000000007;
static const int MAXN = 2025;

int C[MAXN][MAXN];
int CS[MAXN][MAXN];
int memo[MAXN][MAXN];

int dfs(int a, int b) {
    if (a == 0 || b == 0) return 1;
    if (memo[a][b] != -1) return memo[a][b];

    long long ret = dfs(a - 1, b);
    int rem_b = b - 1;
    long long term = CS[rem_b][min(a, rem_b) + 1] - CS[rem_b][0];
    term %= MOD;
    if (term < 0) term += MOD;

    ret = (ret + term) % MOD;
    return memo[a][b] = ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int A, B;
    if (!(cin >> A >> B)) return 0;

    if (A == 0 || B == 0) {
        cout << 1 << "\n";
        return 0;
    }

    for (int i = 0; i < MAXN; ++i) {
        C[i][0] = C[i][i] = 1;
        for (int j = 1; j < i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
        CS[i][0] = 0;
        for (int j = 0; j + 1 < MAXN; ++j) {
            CS[i][j + 1] = (CS[i][j] + C[i][j]) % MOD;
        }
    }

    memset(memo, -1, sizeof(memo));

    long long ans = 0;
    int rem_B = B - 1;
    for (int a = 0; a <= A; ++a) {
        for (int i = 0; i <= a; ++i) {
            if (a - i <= rem_B) {
                long long ways = (1LL * C[rem_B][a - i] * dfs(i, a - i)) % MOD;
                ans = (ans + ways) % MOD;
            }
        }
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
