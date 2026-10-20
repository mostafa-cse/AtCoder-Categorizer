# Problem Analysis: AtCoder-agc022_e — E - Median Replace

**Problem ID**: `AtCoder-agc022_e`  
**Contest**: `agc022`  
**Rating / Difficulty**: 2963  
**URL**: https://atcoder.jp/contests/agc022/tasks/agc022_e  
**VJudge Tag**: `[problem:AtCoder-agc022_e]`  
**Category File**: [`../categories/basics/median_replace_stack_automaton_dp.md`](../categories/basics/median_replace_stack_automaton_dp.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Standard Template Library (STL)`  
- **Topic (Skill)**: `Stack`  

---

## 1. Problem Statement & Key Idea
Given a string S of odd length N <= 3 * 10^5 consisting of '0', '1', and '?', count the number of binary strings obtainable by replacing '?' such that repeatedly replacing 3 consecutive characters with their median reduces the string to '1', modulo 10^9+7.

## 2. Core Observation & Invariant
We simulate the median replacement greedily using a stack reduction. When scanning from left to right, two adjacent '1's can absorb any '0'. The stack can be canonicalized into a finite automaton of only 9 states! Transitions on '0' and '1' form a 9-state DFA, where accepting states correspond to stacks with majority '1's.

## 3. Step-by-Step Algorithm
1. 1. Build the 9-state DFA transition table trans[9][2].
2. 2. Set initial state 0 (empty stack).
3. 3. DP over the string: dp[i][state] is the number of ways to fill the first i characters ending in state.
4. 4. For character '0': transition to trans[state][0]. For '1': transition to trans[state][1]. For '?': sum transitions for both '0' and '1'.
5. 5. Sum dp[N][state] for all accepting states {1, 2, 5, 8} modulo 10^9+7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int trans[9][2] = {
    {3, 1}, {4, 2}, {5, 2},
    {6, 0}, {7, 1}, {8, 2},
    {3, 3}, {4, 4}, {5, 5}
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;

    vector<long long> dp(9, 0);
    dp[0] = 1;

    for (char c : s) {
        vector<long long> ndp(9, 0);
        if (c != '1') {
            for (int j = 0; j < 9; ++j) {
                if (dp[j]) {
                    ndp[trans[j][0]] = (ndp[trans[j][0]] + dp[j]) % MOD;
                }
            }
        }
        if (c != '0') {
            for (int j = 0; j < 9; ++j) {
                if (dp[j]) {
                    ndp[trans[j][1]] = (ndp[trans[j][1]] + dp[j]) % MOD;
                }
            }
        }
        dp = move(ndp);
    }

    // Accepting states where '1' can be achieved: {1, 2, 5, 8}
    long long ans = (dp[1] + dp[2] + dp[5] + dp[8]) % MOD;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
