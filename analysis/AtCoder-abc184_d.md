# Problem Analysis: AtCoder-abc184_d — increment of coins

**Problem ID**: `AtCoder-abc184_d`  
**Contest**: `abc184`  
**Rating / Difficulty**: 1276  
**URL**: https://atcoder.jp/contests/abc184/tasks/abc184_d  
**VJudge Tag**: `[problem:AtCoder-abc184_d]`  
**Category File**: [`../categories/dp/expected_value_backward_induction_3d.md`](../categories/dp/expected_value_backward_induction_3d.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Probability & Expectation`  
- **Topic (Skill)**: `3D Expected Value Backward Induction DP`  

---

## 1. Problem Statement & Key Idea
A bag contains A gold, B silver, and C bronze coins. In each step, pick a coin randomly, put it back, and add one more of the same type. Stop when any coin type reaches 100. Find expected operations.

**Key Idea**: Let dp[a][b][c] be the expected number of additional operations to reach 100 coins from state (a, b, c).

## 2. Core Observation & Invariant
Base cases: if a == 100 or b == 100 or c == 100, dp[a][b][c] = 0. From state (a, b, c) with total coins S = a + b + c, picking gold has probability a / S transitioning to (a + 1, b, c); silver b / S to (a, b + 1, c); bronze c / S to (a, b, c + 1). Recurrence: dp[a][b][c] = 1 + (a * dp[a+1][b][c] + b * dp[a][b+1][c] + c * dp[a][b][c+1]) / S.

## 3. Step-by-Step Algorithm
1. Initialize 3D array dp[101][101][101] to 0.0.
2. Iterate a from 99 down to A, b from 99 down to B, c from 99 down to C.
3. Calculate S = a + b + c.
4. dp[a][b][c] = 1.0 + ((double)a * dp[a + 1][b][c] + (double)b * dp[a][b + 1][c] + (double)c * dp[a][b][c + 1]) / S.
5. Output dp[A][B][C] with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(100^3) = 10^6 operations`
- **Space Complexity**: `O(100^3)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

double dp[101][101][101];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int start_a, start_b, start_c;
    if (!(cin >> start_a >> start_b >> start_c)) return 0;

    for (int a = 99; a >= start_a; --a) {
        for (int b = 99; b >= start_b; --b) {
            for (int c = 99; c >= start_c; --c) {
                double s = a + b + c;
                dp[a][b][c] = 1.0 + (a * dp[a + 1][b][c] + b * dp[a][b + 1][c] + c * dp[a][b][c + 1]) / s;
            }
        }
    }

    cout << fixed << setprecision(9) << dp[start_a][start_b][start_c] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Multi-dimensional backward induction on absorbing Markov chains.
- **Reusable Pattern**: `Expected steps backward induction: dp[state] = 1 + sum p_i * dp[next_state_i].`
