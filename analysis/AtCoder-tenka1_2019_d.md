# Problem Analysis: AtCoder-tenka1_2019_d — Three Colors

**Problem ID**: `AtCoder-tenka1_2019_d`  
**Contest**: `tenka1-2019`  
**Rating / Difficulty**: 2237  
**URL**: https://atcoder.jp/contests/tenka1-2019/tasks/tenka1_2019_d  
**VJudge Tag**: `[problem:AtCoder-tenka1_2019_d]`  
**Category File**: [`../categories/dp/knapsack_three_colors_triangle_inequality_complementary_counting.md`](../categories/dp/knapsack_three_colors_triangle_inequality_complementary_counting.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Count the number of ways to paint N integers with Red, Green, or Blue so that the sum of each color can form a non-degenerate triangle.

## 2. Core Observation & Invariant
Side lengths R, G, B form a non-degenerate triangle iff max(R, G, B) < S / 2 where S = sum A_i. By complementary counting, subtract invalid colorings where some color has sum >= ceil(S / 2). By symmetry, colorings with R >= ceil(S / 2) can be multiplied by 3. If S is even, colorings with two colors equal to S / 2 (and the third 0) are double-counted in 3 * invalid1 and must be added back via PIE. Both counts reduce to 0/1 knapsack dynamic programming.

## 3. Step-by-Step Algorithm
1. 1. Compute total sum S = sum(A) and threshold half = (S + 1) / 2.
2. 2. Compute dp[s] (ways to choose elements summing to s for Red, with remaining elements having 2 color choices): transition next_dp[s] = 2 * dp[s] + dp[s - a_i].
3. 3. Sum dp[s] for s in [half, S] to obtain invalid1.
4. 4. If S is even, compute dp2[s] (ways to partition into Red and Green with Blue = 0) and obtain invalid2 = dp2[S / 2].
5. 5. Final answer is (3^N - 3 * invalid1 + 3 * invalid2) modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * S)`
- **Space Complexity**: `O(S)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

static const int MOD = 998244353;

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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    int S = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        S += a[i];
    }

    int half = (S + 1) / 2;

    vector<long long> dp(S + 1, 0);
    dp[0] = 1;

    for (int x : a) {
        vector<long long> next_dp(S + 1, 0);
        for (int s = 0; s <= S; ++s) {
            if (dp[s] == 0) continue;
            next_dp[s] = (next_dp[s] + 2LL * dp[s]) % MOD;
            if (s + x <= S) {
                next_dp[s + x] = (next_dp[s + x] + dp[s]) % MOD;
            }
        }
        dp = move(next_dp);
    }

    long long invalid1 = 0;
    for (int s = half; s <= S; ++s) {
        invalid1 = (invalid1 + dp[s]) % MOD;
    }

    long long invalid2 = 0;
    if (S % 2 == 0) {
        vector<long long> dp2(S / 2 + 1, 0);
        dp2[0] = 1;
        for (int x : a) {
            for (int s = S / 2; s >= x; --s) {
                dp2[s] = (dp2[s] + dp2[s - x]) % MOD;
            }
        }
        invalid2 = dp2[S / 2];
    }

    long long total = power(3, n);
    long long ans = (total - 3LL * invalid1 % MOD + 3LL * invalid2 % MOD + 2LL * MOD) % MOD;
    cout << ans << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
