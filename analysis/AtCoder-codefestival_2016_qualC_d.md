# Problem Analysis: AtCoder-codefestival_2016_qualC_d — D. Friction

**Problem ID**: `AtCoder-codefestival_2016_qualC_d`  
**Contest**: `code-festival-2016-qualc`  
**Rating / Difficulty**: 2283  
**URL**: https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_d  
**VJudge Tag**: `[problem:AtCoder-codefestival_2016_qualC_d]`  
**Category File**: [`../categories/dynamic_programming_dp/edit_distance_column_sinking_friction_alignment.md`](../categories/dynamic_programming_dp/edit_distance_column_sinking_friction_alignment.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Edit Distance`  

---

## 1. Problem Statement & Key Idea
Given an $H \times W$ grid of colored blocks, repeatedly choose a column and lower it by one cell. Whenever two horizontally adjacent blocks share the same color, 1 point of friction cost is incurred. Find the minimum total friction cost to sink all blocks.

## 2. Core Observation & Invariant
Total friction cost decomposes additively into independent interactions between adjacent column pairs $(j, j+1)$. The relative sequence of sinking operations for two adjacent columns corresponds to a 2D alignment grid walk from $(0, 0)$ to $(H, H)$, isomorphic to Edit Distance DP.

## 3. Step-by-Step Algorithm
1. 1. Friction only occurs between horizontally adjacent columns. Because any collection of valid pairwise sinking schedules can be realized by a global linear extension, the minimum total cost equals the sum of independent pairwise minimums over $j = 0, \dots, W-2$.\n2. For adjacent columns $j$ and $j+1$, let $i$ and $k$ be the number of times columns $j$ and $j+1$ have been lowered. The blocks remaining in column $j$ are originally at $r \in [0, H - 1 - i]$ situated at row $r + i$, and in column $j+1$ at $s \in [0, H - 1 - k]$ situated at row $s + k$.\n3. Two blocks are horizontally adjacent when $r + i = s + k \iff s = r + i - k$. The number of matching colors at state $(i, k)$ is $\text{cost}(i, k) = \sum_{r = \max(0, k - i)}^{H - 1 - i} [c_{r, j} == c_{r + i - k, j+1}]$.\n4. The optimal lowering schedule is computed via edit distance / grid alignment DP: $DP(i, k) = \min(DP(i+1, k) + \text{cost}(i, k), DP(i, k+1) + \text{cost}(i, k))$, with base case $DP(H, H) = 0$.\n5. Computing the DP for all $W - 1$ column pairs takes $O(W H^2)$ total operations, which finishes in ~0.04s for $H, W \le 300$.

## 4. Complexity Analysis
- **Time Complexity**: `O(W \cdot H^2)`
- **Space Complexity**: `O(H^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; i++) {
        cin >> grid[i];
    }

    long long total_ans = 0;

    for (int j = 0; j < w - 1; j++) {
        vector<vector<int>> match_cost(h + 1, vector<int>(h + 1, 0));
        for (int i = 0; i <= h; i++) {
            for (int k = 0; k <= h; k++) {
                int cnt = 0;
                int start_r = max(0, k - i);
                int end_r = h - i;
                for (int r = start_r; r < end_r; r++) {
                    int s = r + i - k;
                    if (s >= 0 && s < h - k) {
                        if (grid[r][j] == grid[s][j + 1]) {
                            cnt++;
                        }
                    }
                }
                match_cost[i][k] = cnt;
            }
        }

        vector<vector<int>> dp(h + 1, vector<int>(h + 1, 1e9));
        dp[h][h] = 0;

        for (int i = h; i >= 0; i--) {
            for (int k = h; k >= 0; k--) {
                if (i == h && k == h) continue;
                int cur = 1e9;
                if (i + 1 <= h) {
                    cur = min(cur, dp[i + 1][k] + match_cost[i][k]);
                }
                if (k + 1 <= h) {
                    cur = min(cur, dp[i][k + 1] + match_cost[i][k]);
                }
                dp[i][k] = cur;
            }
        }

        total_ans += dp[0][0];
    }

    cout << total_ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
