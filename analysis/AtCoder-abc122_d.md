# Problem Analysis: AtCoder-abc122_d — We Like AGC

**Problem ID**: `AtCoder-abc122_d`  
**Contest**: `abc122`  
**Rating / Difficulty**: 1533  
**URL**: https://atcoder.jp/contests/abc122/tasks/abc122_d  
**VJudge Tag**: `[problem:AtCoder-abc122_d]`  
**Category File**: [`../categories/dp/forbidden_pattern_last3_dp.md`](../categories/dp/forbidden_pattern_last3_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Dynamic Programming on Last 3 Characters / Forbidden Pattern Counting`  

---

## 1. Problem Statement & Key Idea
Find the number of strings of length N consisting of 'A', 'G', 'C', 'T' that do not contain 'AGC' as a substring, and where swapping any two adjacent characters also does not create 'AGC', modulo 10^9 + 7.

**Key Insight**: Forbidden 3-character patterns: 'AGC', 'GAC', 'ACG'. Forbidden 4-character patterns: 'A?GC' (e.g. AGTC->ATGC), 'AG?C'. The validity of appending a character depends only on the last 3 characters.

## 2. Core Observation & Invariant
Encoding 4 characters ('A'=0, 'G'=1, 'C'=2, 'T'=3) yields 4^3 = 64 states. DP state: `dp[len][c1][c2][c3]` tracking the last 3 characters. Transitions check all 4 choices for the next character c4.

## 3. Step-by-Step Algorithm
1. Map 'A'->0, 'G'->1, 'C'->2, 'T'->3. Define dummy initial characters.
2. Initialize dp[dummy][dummy][dummy] = 1.
3. For step from 1 to N:
4.   For each (c1, c2, c3):
5.     For next character c4 in 0..3:
6.       Check if (c2, c3, c4) == 'AGC', 'GAC', 'ACG', or (c1, c2, c4) == 'AGC', or (c1, c3, c4) == 'AGC'.
7.       If valid: next_dp[c2][c3][c4] = (next_dp[c2][c3][c4] + dp[c1][c2][c3]) % MOD.
8. Sum next_dp over all states and print result.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 4^4)`
- **Space Complexity**: `O(4^3)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

// A=0, G=1, C=2, T=3, dummy=4
bool is_valid(int c1, int c2, int c3, int c4) {
    // Contains "AGC"
    if (c2 == 0 && c3 == 1 && c4 == 2) return false;
    // Swap c3, c4 -> GAC
    if (c2 == 1 && c3 == 0 && c4 == 2) return false;
    // Swap c3, c4 -> ACG
    if (c2 == 0 && c3 == 2 && c4 == 1) return false;
    // Swap c2, c3 -> A?GC
    if (c1 == 0 && c2 == 1 && c4 == 2) return false;
    // Swap c1, c2 -> AG?C
    if (c1 == 0 && c3 == 1 && c4 == 2) return false;
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int dp[5][5][5] = {0};
    dp[4][4][4] = 1;

    for (int len = 0; len < n; ++len) {
        int next_dp[5][5][5] = {0};
        for (int c1 = 0; c1 < 5; ++c1) {
            for (int c2 = 0; c2 < 5; ++c2) {
                for (int c3 = 0; c3 < 5; ++c3) {
                    if (!dp[c1][c2][c3]) continue;
                    for (int c4 = 0; c4 < 4; ++c4) {
                        if (is_valid(c1, c2, c3, c4)) {
                            next_dp[c2][c3][c4] = (next_dp[c2][c3][c4] + dp[c1][c2][c3]) % MOD;
                        }
                    }
                }
            }
        }
        for (int c1 = 0; c1 < 5; ++c1) {
            for (int c2 = 0; c2 < 5; ++c2) {
                for (int c3 = 0; c3 < 5; ++c3) {
                    dp[c1][c2][c3] = next_dp[c1][c2][c3];
                }
            }
        }
    }

    int ans = 0;
    for (int c1 = 0; c1 < 4; ++c1) {
        for (int c2 = 0; c2 < 4; ++c2) {
            for (int c3 = 0; c3 < 4; ++c3) {
                ans = (ans + dp[c1][c2][c3]) % MOD;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Suffix state compression DP for forbidden substring avoidance under adjacent transpositions.
- **Reusable Pattern**: `Suffix Window DP: maintain last K-1 characters as state to validate incoming characters.`
