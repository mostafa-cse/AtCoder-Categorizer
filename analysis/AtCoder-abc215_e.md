# Problem Analysis: AtCoder-abc215_e — Chain Contestant

**Problem ID**: `AtCoder-abc215_e`  
**Contest**: `abc215`  
**Rating / Difficulty**: 1413  
**URL**: https://atcoder.jp/contests/abc215/tasks/abc215_e  
**VJudge Tag**: `[problem:AtCoder-abc215_e]`  
**Category File**: [`../categories/dp/bitmask_dp_contiguous_blocks.md`](../categories/dp/bitmask_dp_contiguous_blocks.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP with Contiguous Element Tracking`  

---

## 1. Problem Statement & Key Idea
Given a string S of length N consisting of uppercase letters 'A' through 'J' (10 contest types). Find the number of non-empty subsequences such that for every contest type that appears, all its occurrences appear consecutively in the subsequence, modulo 998244353.

**Key Insight**: Use bitmask DP where the state tracks the set of contest types already completed, along with the most recent contest type.

## 2. Core Observation & Invariant
Since there are only 10 contest types ('A'..'J'), 2^10 = 1024. For a new contest type x to be appended to a subsequence, either x is identical to the last participated contest type, or x has NEVER been participated in before (x is not in the bitmask).

## 3. Step-by-Step Algorithm
1. Define dp[mask][last] where mask is a bitmask of used types (0..1023), and last in 0..9 is the last contest type used.
2. For each character c in S, let x = c - 'A':
3.   Start new single-element subsequence: new_dp[1 << x][x] += 1.
4.   For each mask in 1..1023 and each last in 0..9:
5.     If dp[mask][last] == 0, continue.
6.     If last == x: append to same contiguous block: new_dp[mask][x] = (new_dp[mask][x] + dp[mask][last]) % MOD.
7.     Else if !(mask & (1 << x)): start new block: new_dp[mask | (1 << x)][x] = (new_dp[mask | (1 << x)][x] + dp[mask][last]) % MOD.
8. After processing all characters, sum dp[mask][last] over all mask > 0 and all last.
9. Print sum % MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 2^10 * 10)`
- **Space Complexity**: `O(2^10 * 10)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    // dp[mask][last_type]: mask in 0..1023, last_type in 0..9
    vector<vector<int>> dp(1024, vector<int>(10, 0));

    for (char ch : s) {
        int x = ch - 'A';
        vector<vector<int>> next_dp = dp;

        // Start a new subsequence consisting solely of x
        next_dp[1 << x][x] = (next_dp[1 << x][x] + 1) % MOD;

        for (int mask = 1; mask < 1024; ++mask) {
            for (int last = 0; last < 10; ++last) {
                int val = dp[mask][last];
                if (!val) continue;

                if (last == x) {
                    // Continue the same contiguous block
                    next_dp[mask][x] = (next_dp[mask][x] + val) % MOD;
                } else if (!(mask & (1 << x))) {
                    // Start a new block of type x that was never visited
                    next_dp[mask | (1 << x)][x] = (next_dp[mask | (1 << x)][x] + val) % MOD;
                }
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int mask = 1; mask < 1024; ++mask) {
        for (int last = 0; last < 10; ++last) {
            ans = (ans + dp[mask][last]) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitmask state encoding of visited categories combined with the active block boundary state.
- **Reusable Pattern**: `Contiguous category block DP: dp[visited_mask][current_active_category].`
