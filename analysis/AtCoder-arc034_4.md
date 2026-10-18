# Problem Analysis: AtCoder-arc034_4 — D. インフレゲーム (Inflation Game)

**Problem ID**: `AtCoder-arc034_4`  
**Contest**: `arc034`  
**Rating / Difficulty**: 2570  
**URL**: https://atcoder.jp/contests/arc034/tasks/arc034_4  
**VJudge Tag**: `[problem:AtCoder-arc034_4]`  
**Category File**: [`../categories/basics/inflation_game_stars_and_bars.md`](../categories/basics/inflation_game_stars_and_bars.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Stars and Bars`  

---

## 1. Problem Statement & Key Idea
We are given A addition cards and B multiplication cards. In each round, we choose a card to play. Addition cards add values to the total score, while multiplication cards multiply the score by factors. Find the expected maximum final score over all possible card draws.

## 2. Core Observation & Invariant
Since multiplication cards multiply all previous additions, all addition cards played before a multiplication card benefit from that factor. By Stars and Bars and linearity of expectation, the expected coefficient of each addition card depends symmetrically on the number of multiplication cards drawn after it. The distribution of multiplication cards among addition cards follows a negative hypergeometric / elementary symmetric polynomial distribution that can be computed via DP.

## 3. Step-by-Step Algorithm
1. Compute the elementary symmetric polynomials of card multipliers using dynamic programming.
2. Apply Stars and Bars combinatorial coefficients to determine the expected multiplier applied to each addition card.
3. Multiply expected addition sums by the derived scaling factor.
4. Output the expected score.

## 4. Complexity Analysis
- **Time Complexity**: `O(A * B)`
- **Space Complexity**: `O(A + B)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <numeric>

using namespace std;

// Compute combination nCr using double
double comb(int n, int r) {
    if (r < 0 || r > n) return 0.0;
    if (r == 0 || r == n) return 1.0;
    double res = 1.0;
    for (int i = 1; i <= r; i++) {
        res = res * (n - i + 1) / i;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int A, B, C;
    if (!(cin >> A >> B >> C)) return 0;

    double sum_a = 0.0;
    for (int i = 0; i < A; i++) {
        double a;
        cin >> a;
        sum_a += a;
    }

    vector<double> b_list(B);
    for (int i = 0; i < B; i++) {
        cin >> b_list[i];
    }

    vector<double> dp(B + 1, 0.0);
    dp[0] = 1.0;
    for (double b : b_list) {
        for (int k = B; k >= 1; k--) {
            dp[k] += dp[k - 1] * b;
        }
    }

    double denom_common = (B + C + 1.0) * comb(B + C, C);
    double total_mult = 0.0;

    for (int k = 0; k <= B; k++) {
        double num = comb(B - k + C, C);
        double denom = comb(B, k) * denom_common;
        double w_k = num / denom;
        total_mult += w_k * dp[k];
    }

    double ans = sum_a * total_mult;
    cout << fixed << setprecision(15) << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
