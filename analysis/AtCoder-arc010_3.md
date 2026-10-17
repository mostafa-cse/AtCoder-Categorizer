# Problem Analysis: AtCoder-arc010_3 — 積み上げパズル

**Problem ID**: `AtCoder-arc010_3`  
**Contest**: `arc010`  
**Rating / Difficulty**: 2011  
**URL**: https://atcoder.jp/contests/arc010/tasks/arc010_3  
**VJudge Tag**: `[problem:AtCoder-arc010_3]`  
**Category File**: [`../categories/dynamic_programming/bitmask_dp_stream_consecutive_tracking.md`](../categories/dynamic_programming/bitmask_dp_stream_consecutive_tracking.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP with Stream Element Selection and Consecutive State Tracking`  

---

## 1. Problem Statement & Key Idea
N colored blocks of M types (M <= 10) arrive in a stream. Each block can be discarded or stacked. Stacking block of color c yields basic points P_c. If stacked immediately on top of the same color, bonus Y is awarded. If all M colors have been stacked at least once, bonus Z is awarded. Find the maximum possible total score.

**Key Idea**: M <= 10 allows representing the set of placed colors as a bitmask of size 2^M. The immediate consecutive bonus depends only on the color of the last stacked block (M + 1 states, including empty). State: dp[mask][last_color] = maximum score. For each arriving block of color c, either transition by not taking it (dp state preserved) or taking it (transitioning from dp[mask][last] with new mask = mask | (1 << c) and last = c, adding P_c + (last == c ? Y : 0)). If the new mask becomes (1 << M) - 1 for the first time, add bonus Z.

## 2. Core Observation & Invariant
Small color alphabet M <= 10 combined with 1-step lookback memory enables exact Bitmask DP on streaming decisions.

## 3. Step-by-Step Algorithm
1. Initialize dp[1 << M][M + 1] with -INF, dp[0][M] = 0 (where M denotes empty stack).
2. For each arriving block of color c (0 <= c < M) with score P_c:
3.   Create next_dp initialized to dp.
4.   For each mask from 0 to (1 << M) - 1:
5.     For each last from 0 to M:
6.       if dp[mask][last] == -INF: continue
7.       int nmask = mask | (1 << c);
8.       int score_gain = P_c + (last == c ? Y : 0);
9.       if (mask != (1 << M) - 1 && nmask == (1 << M) - 1) score_gain += Z;
10.       next_dp[nmask][c] = max(next_dp[nmask][c], dp[mask][last] + score_gain);
11.   dp = next_dp.
12. Output max over all dp[mask][last].

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M * 2^M)`
- **Space Complexity**: `O(M * 2^M)`

## 5. Core Algorithmic Skill & Learning Takeaway
Bitmask DP with consecutive state memory for stream selection.

**Reusable Pattern**: Mask + Last Element DP: Maintaining subset coverage and last chosen element in O(M * 2^M) space.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

const long long NEG_INF = -1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long y, z;
    if (!(cin >> n >> m >> y >> z)) return 0;

    map<char, int> color_idx;
    vector<long long> p(m);
    for (int i = 0; i < m; ++i) {
        char c;
        long long pt;
        cin >> c >> pt;
        color_idx[c] = i;
        p[i] = pt;
    }

    string s;
    cin >> s;

    int total_masks = (1 << m);
    // last_color: 0 .. m - 1, and m means empty
    vector<vector<long long>> dp(total_masks, vector<long long>(m + 1, NEG_INF));
    dp[0][m] = 0;

    for (char ch : s) {
        int c = color_idx[ch];
        vector<vector<long long>> next_dp = dp;

        for (int mask = 0; mask < total_masks; ++mask) {
            for (int last = 0; last <= m; ++last) {
                if (dp[mask][last] == NEG_INF) continue;

                int nmask = mask | (1 << c);
                long long gain = p[c];
                if (last == c) gain += y;
                if (mask != total_masks - 1 && nmask == total_masks - 1) gain += z;

                next_dp[nmask][c] = max(next_dp[nmask][c], dp[mask][last] + gain);
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int mask = 0; mask < total_masks; ++mask) {
        for (int last = 0; last <= m; ++last) {
            ans = max(ans, dp[mask][last]);
        }
    }

    cout << ans << "\n";
    return 0;
}
```
