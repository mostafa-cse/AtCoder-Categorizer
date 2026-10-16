# Problem Analysis: AtCoder-dp_c — Vacation

**Problem ID**: `AtCoder-dp_c`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 900  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_c  
**VJudge Tag**: `[problem:AtCoder-dp_c]`  
**Category File**: [`../categories/dp/1d_dp.md`](../categories/dp/1d_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Multi-State DP / Consecutive Constraints`  

---

## 1. Problem Statement & Key Idea
Choose activities A, B, or C over N days maximizing happiness, with the constraint that Taro cannot do the same activity two days in a row.

**Core Idea**: Maintain happiness while enforcing non-repeating consecutive activity constraints.

## 2. Core Observation & Invariant
Enforcing the constraint 'no two consecutive identical choices' requires augmenting the state with the identity of the last chosen activity.

## 3. Step-by-Step Algorithm
1. State: dp[day][act] where act in {0, 1, 2}.
2. dp[i][0] = a_i + max(dp[i-1][1], dp[i-1][2]), and symmetrically for 1 and 2.
3. Return max_{act} dp[N][act].

## 4. Complexity Analysis
Time: O(N), Space: O(1) rolling state.

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> dp(3, 0);

    for (int i = 0; i < n; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        vector<int> next_dp(3);
        next_dp[0] = a + max(dp[1], dp[2]);
        next_dp[1] = b + max(dp[0], dp[2]);
        next_dp[2] = c + max(dp[0], dp[1]);
        dp = next_dp;
    }

    cout << max({dp[0], dp[1], dp[2]}) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Classic 3-state Markov transition graph.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: State augmentation for path-dependent constraints and state-machine DP.
- **Reusable Pattern**: `Categorical state-machine DP with mutually exclusive transitions.`

---
Back to [Multi-State DP / Consecutive Constraints](../categories/dp/1d_dp.md) | [Categories Directory](../categories/README.md)