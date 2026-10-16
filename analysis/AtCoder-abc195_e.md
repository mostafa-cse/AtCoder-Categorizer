# Problem Analysis: AtCoder-abc195_e — Lucky 7 Battle

**Problem ID**: `AtCoder-abc195_e`  
**Contest**: `abc195`  
**Rating / Difficulty**: 1609  
**URL**: https://atcoder.jp/contests/abc195/tasks/abc195_e  
**VJudge Tag**: `[problem:AtCoder-abc195_e]`  
**Category File**: [`../categories/game_theory/backward_game_theory_dp_modulo7.md`](../categories/game_theory/backward_game_theory_dp_modulo7.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Minimax`  
- **Topic (Skill)**: `Backward Game Theory DP modulo 7 with Controllable State Sets`  

---

## 1. Problem Statement & Key Idea
An N-digit number is built from left to right. In round i, digit S[i] is presented. The player indicated by X[i] ('T' for Takahashi, 'A' for Aoki) chooses whether to add S[i] or 0 to the number (shifted: val = (10*val + digit)%7 or (10*val)%7). Takahashi wins iff final value % 7 == 0. Determine who wins under optimal play.

**Key Insight**: Backward induction! Work backwards from round N to 0. Maintain the set of winning remainders W subseteq {0..6} from which Takahashi can guarantee victory.

## 2. Core Observation & Invariant
Base state at round N: W = {0}. For round i with digit d: for remainder r in 0..6, the next remainders are r0 = (10r) % 7 and r1 = (10r + d) % 7. If Takahashi moves, r in next_W if (r0 in W OR r1 in W). If Aoki moves, r in next_W if (r0 in W AND r1 in W). Takahashi wins iff 0 in W at step 0.

## 3. Step-by-Step Algorithm
1. Initialize win_set = {0}.
2. For i from N - 1 down to 0:
3.   int d = S[i] - '0'.
4.   bool takahashi = (X[i] == 'T').
5.   next_win_set = empty.
6.   For r from 0 to 6:
7.     int r0 = (10 * r) % 7;
8.     int r1 = (10 * r + d) % 7;
9.     if takahashi:
10.       if (r0 in win_set || r1 in win_set) next_win_set.insert(r);
11.     else (Aoki):
12.       if (r0 in win_set && r1 in win_set) next_win_set.insert(r);
13.   win_set = next_win_set.
14. Print 'Takahashi' if (0 in win_set) else 'Aoki'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s, x;
    if (!(cin >> n >> s >> x)) return 0;

    // dp[r]: true if Takahashi can win starting with remainder r
    vector<bool> dp(7, false);
    dp[0] = true;

    for (int i = n - 1; i >= 0; --i) {
        int d = s[i] - '0';
        bool is_t = (x[i] == 'T');
        vector<bool> next_dp(7, false);

        for (int r = 0; r < 7; ++r) {
            int r0 = (10 * r) % 7;
            int r1 = (10 * r + d) % 7;

            if (is_t) {
                // Takahashi wants at least one branch to win
                next_dp[r] = (dp[r0] || dp[r1]);
            } else {
                // Aoki forces both branches to be winning for Takahashi to win
                next_dp[r] = (dp[r0] && dp[r1]);
            }
        }
        dp = move(next_dp);
    }

    cout << (dp[0] ? "Takahashi" : "Aoki") << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Backward game DP tracking controllable winning subset states under existential/universal quantifiers.
- **Reusable Pattern**: `Controllable State Set Game DP: Takahashi uses OR, Aoki uses AND on reachable residue sets.`
