# Problem Analysis: AtCoder-arc066_c — Addition and Subtraction Hard

**Problem ID**: `AtCoder-arc066_c`  
**Contest**: `arc066`  
**Rating / Difficulty**: 2709  
**URL**: https://atcoder.jp/contests/arc066/tasks/arc066_c  
**VJudge Tag**: `[problem:AtCoder-arc066_c]`  
**Category File**: [`../categories/dynamic_programming_dp/addition_subtraction_hard_parentheses_dp.md`](../categories/dynamic_programming_dp/addition_subtraction_hard_parentheses_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Maximizing arithmetic expression by inserting parentheses. The effect of nested parentheses after a '-' sign corresponds to 3 negation depth states j in {0, 1, 2}: depth 0 (unflipped), depth 1 (flipped: + becomes -, - becomes +), and depth 2 (double flipped: both + and - become +). Transitions between these 3 states solve the problem in O(N) time.

## 2. Core Observation & Invariant
Once depth 2 is entered, every subsequent number can receive a positive sign (+) by appropriately opening/closing inner parentheses around each operator. Depth >= 3 is never needed. Thus, an O(N) DP with exactly 3 states suffices.

## 3. Step-by-Step Algorithm
1. 1. Initialize dp = [A_0, -INF, -INF].
2. 2. For each step i from 0 to N - 2 with operator op and next number a:
3.    - From state 0: op='+' stays 0 (+a); op='-' stays 0 (-a) or transitions to 1 (-a).
4.    - From state 1: op='+' stays 1 (-a) or closes to 0 (+a); op='-' stays 1 (+a), transitions to 2 (+a), or closes to 0 (-a).
5.    - From state 2: stays 2 (+a) for both '+' and '-'.
6. 3. Print max(dp[0], dp[1], dp[2]).

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

static const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> A(n);
    vector<char> ops(n - 1);

    cin >> A[0];
    for (int i = 0; i < n - 1; ++i) {
        cin >> ops[i] >> A[i + 1];
    }

    vector<long long> dp(3, -INF);
    dp[0] = A[0];

    for (int i = 0; i < n - 1; ++i) {
        char op = ops[i];
        long long a = A[i + 1];
        vector<long long> next_dp(3, -INF);

        // From state 0
        if (dp[0] != -INF) {
            if (op == '+') {
                next_dp[0] = max(next_dp[0], dp[0] + a);
            } else { // '-'
                next_dp[0] = max(next_dp[0], dp[0] - a);
                next_dp[1] = max(next_dp[1], dp[0] - a);
            }
        }

        // From state 1
        if (dp[1] != -INF) {
            if (op == '+') {
                next_dp[1] = max(next_dp[1], dp[1] - a);
                next_dp[0] = max(next_dp[0], dp[1] + a);
            } else { // '-'
                next_dp[1] = max(next_dp[1], dp[1] + a);
                next_dp[2] = max(next_dp[2], dp[1] + a);
                next_dp[0] = max(next_dp[0], dp[1] - a);
            }
        }

        // From state 2
        if (dp[2] != -INF) {
            next_dp[2] = max(next_dp[2], dp[2] + a);
        }

        dp = move(next_dp);
    }

    long long ans = max({dp[0], dp[1], dp[2]});
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
