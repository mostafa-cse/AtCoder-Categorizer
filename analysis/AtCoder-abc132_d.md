# Problem Analysis: AtCoder-abc132_d — Blue and Red Balls

**Problem ID**: `AtCoder-abc132_d`  
**Contest**: `abc132`  
**Rating / Difficulty**: 1167  
**URL**: https://atcoder.jp/contests/abc132/tasks/abc132_d  
**VJudge Tag**: `[problem:AtCoder-abc132_d]`  
**Category File**: [`../categories/combinatorics/alternating_block_stars_and_bars.md`](../categories/combinatorics/alternating_block_stars_and_bars.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Stars and Bars`  
- **Topic (Skill)**: `Alternating Block Partitioning via Stars and Bars`  

---

## 1. Problem Statement & Key Idea
There are K blue balls and N - K red balls. In each operation, collect a contiguous block of blue balls. For each i in 1..K, find the number of arrangements requiring exactly i operations, modulo 10^9 + 7.

**Key Idea**: Exactly i operations means the K blue balls are divided into exactly i non-empty contiguous blocks.

## 2. Core Observation & Invariant
Dividing K blue balls into i non-empty blocks is C(K - 1, i - 1) via Stars and Bars. These i blue blocks must be separated by at least one red ball, which means choosing i distinct insertion slots among the (N - K + 1) available positions between the red balls: C(N - K + 1, i). By rule of product, answer is C(K - 1, i - 1) * C(N - K + 1, i).

## 3. Step-by-Step Algorithm
1. Precompute combinations C(n, r) modulo 10^9 + 7 using Pascal's triangle or factorials.
2. For i from 1 to K: if i > N - K + 1, print 0; else ans = C(K - 1, i - 1) * C(N - K + 1, i) % MOD; print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2) or O(N)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<long long>> c(n + 2, vector<long long>(n + 2, 0));
    for (int i = 0; i <= n + 1; ++i) {
        c[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD;
        }
    }

    int red = n - k;
    for (int i = 1; i <= k; ++i) {
        if (i > red + 1) {
            cout << 0 << "\n";
        } else {
            long long blue_ways = c[k - 1][i - 1];
            long long red_ways = c[red + 1][i];
            long long ans = (blue_ways * red_ways) % MOD;
            cout << ans << "\n";
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combinatorial separation of two-color alternating contiguous runs.
- **Reusable Pattern**: `i non-empty blue blocks in red: C(K - 1, i - 1) * C(N - K + 1, i).`
