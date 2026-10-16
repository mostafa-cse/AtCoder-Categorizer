# 3D Expected Value Backward Induction DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Probability & Expectation`  

This workbook contains curated, high-quality competitive programming problems teaching **3D Expected Value Backward Induction DP**.

---

## Curated Problems

### [problem:AtCoder-abc184_d] — increment of coins
- **Contest**: `abc184`
- **Rating / Difficulty**: 1276
- **Specific Skill**: 3D Expected Value Backward Induction DP
- **Individual Analysis**: [`../../analysis/AtCoder-abc184_d.md`](../../analysis/AtCoder-abc184_d.md)
- **Problem Statement Summary**: A bag contains A gold, B silver, and C bronze coins. In each step, pick a coin randomly, put it back, and add one more of the same type. Stop when any coin type reaches 100. Find expected operations.
- **Core Insight**: Base cases: if a == 100 or b == 100 or c == 100, dp[a][b][c] = 0. From state (a, b, c) with total coins S = a + b + c, picking gold has probability a / S transitioning to (a + 1, b, c); silver b / S to (a, b + 1, c); bronze c / S to (a, b, c + 1). Recurrence: dp[a][b][c] = 1 + (a * dp[a+1][b][c] + b * dp[a][b+1][c] + c * dp[a][b][c+1]) / S.
- **Complexity**: Time: `O(100^3) = 10^6 operations` | Space: `O(100^3)`
- **Verified C++ Implementation**:
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
