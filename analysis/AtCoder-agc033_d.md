# Problem Analysis: AtCoder-agc033_d — D - Complexity

**Problem ID**: `AtCoder-agc033_d`  
**Contest**: `agc033`  
**Rating / Difficulty**: 2962  
**URL**: https://atcoder.jp/contests/agc033/tasks/agc033_d  
**VJudge Tag**: `[problem:AtCoder-agc033_d]`  
**Category File**: [`../categories/dynamic_programming/grid_complexity_state_value_inversion_interval_dp.md`](../categories/dynamic_programming/grid_complexity_state_value_inversion_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Given an H x W grid (H, W <= 185) with '#' and '.', find the minimum complexity to partition the grid into monochromatic rectangles, where complexity of monochromatic is 0, and a split into A, B has complexity 1 + max(c(A), c(B)).

## 2. Core Observation & Invariant
Any grid of size H x W can be partitioned with complexity at most ceil(log_2 H) + ceil(log_2 W) <= 16. Rather than computing complexity for every 4D subgrid [u, d, l, r] (which would require O(H^2 W^2) states), we invert the DP: fix complexity k in [0, 16], and let dp[u][d][l] denote the maximum right column r such that subgrid [u, d] x [l, r-1] has complexity <= k.

## 3. Step-by-Step Algorithm
1. 1. Compute 2D prefix sums for O(1) monochromatic rectangle queries.
2. 2. Base case (k=0): for each (u, d, l), binary search the maximum r such that [u, d] x [l, r-1] is monochromatic.
3. 3. For k = 1, 2, ...:
4.    - Vertical split: dp_{new}[u][d][l] = dp[u][d][dp[u][d][l]].
5.    - Horizontal split: max_m min(dp[u][m][l], dp[m+1][d][l]). Since dp[u][m][l] decreases with m and dp[m+1][d][l] increases with m, find optimal split m via binary search in O(log H).
6. 4. Terminate when dp[0][H-1][0] == W and output k.

## 4. Complexity Analysis
- **Time Complexity**: `O(H^2 W log(HW) log H)`
- **Space Complexity**: `O(H^2 W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

static short dp[185][185][186];
static short nxt[185][185][186];
static int pref[186][186];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    vector<string> grid(H);
    for (int i = 0; i < H; ++i) cin >> grid[i];

    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            pref[r + 1][c + 1] = pref[r][c + 1] + pref[r + 1][c] - pref[r][c] + (grid[r][c] == '#' ? 1 : 0);
        }
    }

    auto is_mono = [&](int r1, int r2, int c1, int c2) -> bool {
        int cnt = pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1];
        int area = (r2 - r1 + 1) * (c2 - c1 + 1);
        return cnt == 0 || cnt == area;
    };

    // Base case k = 0
    for (int u = 0; u < H; ++u) {
        for (int d = u; d < H; ++d) {
            for (int l = 0; l < W; ++l) {
                int lo = l, hi = W, best = l;
                while (lo <= hi) {
                    int mid = (lo + hi) / 2;
                    if (mid == l || is_mono(u, d, l, mid - 1)) {
                        best = mid;
                        lo = mid + 1;
                    } else {
                        hi = mid - 1;
                    }
                }
                dp[u][d][l] = best;
            }
        }
    }

    if (dp[0][H - 1][0] == W) {
        cout << 0 << "\n";
        return 0;
    }

    int k = 0;
    while (true) {
        k++;
        for (int u = 0; u < H; ++u) {
            for (int d = u; d < H; ++d) {
                for (int l = 0; l < W; ++l) {
                    // Vertical split
                    int r1 = dp[u][d][l];
                    int val_vert = (r1 < W ? dp[u][d][r1] : W);

                    // Horizontal split
                    int val_horiz = 0;
                    if (u < d) {
                        int lo = u, hi = d - 1;
                        while (lo <= hi) {
                            int mid = (lo + hi) / 2;
                            int f_top = dp[u][mid][l];
                            int f_bot = dp[mid + 1][d][l];
                            val_horiz = max(val_horiz, min(f_top, f_bot));
                            if (f_top >= f_bot) {
                                lo = mid + 1;
                            } else {
                                hi = mid - 1;
                            }
                        }
                    }

                    nxt[u][d][l] = max(val_vert, val_horiz);
                }
            }
        }

        for (int u = 0; u < H; ++u) {
            for (int d = u; d < H; ++d) {
                for (int l = 0; l < W; ++l) {
                    dp[u][d][l] = nxt[u][d][l];
                }
            }
        }

        if (dp[0][H - 1][0] == W) {
            cout << k << "\n";
            return 0;
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
