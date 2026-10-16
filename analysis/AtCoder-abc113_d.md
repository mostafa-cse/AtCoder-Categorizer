# Problem Analysis: AtCoder-abc113_d — Number of Amidakuji

**Problem ID**: `AtCoder-abc113_d`  
**Contest**: `abc113`  
**Rating / Difficulty**: 1597  
**URL**: https://atcoder.jp/contests/abc113/tasks/abc113_d  
**VJudge Tag**: `[problem:AtCoder-abc113_d]`  
**Category File**: [`../categories/dp/amidakuji_non_adjacent_bitmask_dp.md`](../categories/dp/amidakuji_non_adjacent_bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Bitmask DP`  
- **Topic (Skill)**: `DP over Amidakuji Horizontal Bars via Non-Adjacent Bitmasks`  

---

## 1. Problem Statement & Key Idea
An Amidakuji (ghost leg lottery) has width W (W <= 8) vertical lines and height H (H <= 100). At each horizontal level, horizontal rungs may connect adjacent vertical lines, with the condition that no two rungs share an endpoint. Find the number of valid amidakuji where vertical line 1 ends at vertical line K, modulo 10^9 + 7.

**Key Insight**: Each horizontal level corresponds to a bitmask of length W - 1 representing where rungs are placed. A mask is valid iff (mask & (mask << 1)) == 0. A rung at bit c swaps line c and c + 1.

## 2. Core Observation & Invariant
Because W <= 8, 2^(W-1) <= 128 masks. For each step of height from 1 to H, iterate over all valid masks and transition the column positions. dp[h][c] = number of ways after h steps to end at column c.

## 3. Step-by-Step Algorithm
1. Precompute all valid masks of length W - 1 where !(mask & (mask << 1)).
2. dp[W] initialized to 0; dp[0] = 1 (0-indexed line 0).
3. For step from 1 to H:
4.   next_dp[W] = 0.
5.   For each valid mask:
6.     For col from 0 to W - 1:
7.       If col > 0 and (mask has bit col - 1): dest = col - 1.
8.       Else if col < W - 1 and (mask has bit col): dest = col + 1.
9.       Else: dest = col.
10.       next_dp[dest] = (next_dp[dest] + dp[col]) % MOD.
11.   dp = move(next_dp).
12. Print dp[K - 1].

## 4. Complexity Analysis
- **Time Complexity**: `O(H * 2^(W-1) * W)`
- **Space Complexity**: `O(W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, k;
    if (!(cin >> h >> w >> k)) return 0;

    // Line k is 1-indexed; convert to 0-indexed
    k--;

    // Precompute valid masks of width w - 1
    int total_masks = 1 << (w - 1);
    vector<int> valid_masks;
    for (int mask = 0; mask < total_masks; ++mask) {
        if (!(mask & (mask << 1))) {
            valid_masks.push_back(mask);
        }
    }

    vector<long long> dp(w, 0);
    dp[0] = 1;

    for (int step = 0; step < h; ++step) {
        vector<long long> next_dp(w, 0);
        for (int mask : valid_masks) {
            for (int col = 0; col < w; ++col) {
                if (!dp[col]) continue;

                int dest = col;
                if (col > 0 && (mask & (1 << (col - 1)))) {
                    dest = col - 1;
                } else if (col < w - 1 && (mask & (1 << col))) {
                    dest = col + 1;
                }

                next_dp[dest] = (next_dp[dest] + dp[col]) % MOD;
            }
        }
        dp = move(next_dp);
    }

    cout << dp[k] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitmask generation of non-adjacent bridge configurations combined with permutation transition DP.
- **Reusable Pattern**: `Amidakuji Bitmask DP: valid masks satisfy !(m & (m << 1)), transition swaps line c and c+1.`
