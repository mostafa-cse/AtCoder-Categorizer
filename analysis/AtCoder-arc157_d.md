# Problem Analysis: AtCoder-arc157_d — D. YY Garden

**Problem ID**: `AtCoder-arc157_d`  
**Contest**: `arc157`  
**Rating / Difficulty**: 2435  
**URL**: https://atcoder.jp/contests/arc157/tasks/arc157_d  
**VJudge Tag**: `[problem:AtCoder-arc157_d]`  
**Category File**: [`../categories/basics/yy_garden_grid_partition_2d_prefix_sum.md`](../categories/basics/yy_garden_grid_partition_2d_prefix_sum.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `2D Prefix Sum`  
- **Topic (Skill)**: `2D Prefix Sum`  

---

## 1. Problem Statement & Key Idea
Partition an $H \times W$ grid into rectangular blocks using horizontal and vertical fences such that every block contains exactly 2 'Y's. If total 'Y's is $K$, then $K$ must be even and the blocks form an $r \times c$ grid with $r \cdot c = K/2$. For each divisor $r$ of $K/2$, the row fence positions are uniquely fixed by row sums of $2c$, and column fences by column sums of $2r$, with intervening empty lines providing multiple fence placement combinations.

## 2. Core Observation & Invariant
Because fences span the entire grid, every row block must contain identical total 'Y' counts ($2c$), and every column block must contain $2r$ 'Y's. 2D prefix sums allow $O(1)$ verification of all $r \times c$ blocks across all divisors.

## 3. Step-by-Step Algorithm
1. 1. Compute 2D prefix sums of 'Y's in the grid, along with 1D row and column counts.
2. 2. Verify $K$ is positive and even; set $M = K / 2$.
3. 3. For each divisor $r$ of $M$, set $c = M / r$.
4. 4. Greedy-scan row sums to partition into $r$ groups of size $2c$. Multiply $(empty + 1)$ for choices in empty row boundaries.
5. 5. Similarly partition columns into $c$ groups of size $2r$.
6. 6. Using 2D prefix sums, check that all $r \times c$ rectangular blocks contain exactly 2 'Y's. If valid, add $(ways_r \times ways_c) \pmod{998244353}$ to the total.

## 4. Complexity Analysis
- **Time Complexity**: `O(H W + d(K/2) \cdot (K/2))`
- **Space Complexity**: `O(H W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

static const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    vector<string> grid(H);
    vector<vector<int>> pref(H + 1, vector<int>(W + 1, 0));
    vector<int> row_cnt(H, 0), col_cnt(W, 0);
    int total_y = 0;

    for (int i = 0; i < H; ++i) {
        cin >> grid[i];
        for (int j = 0; j < W; ++j) {
            int val = (grid[i][j] == 'Y' ? 1 : 0);
            row_cnt[i] += val;
            col_cnt[j] += val;
            total_y += val;
            pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + val;
        }
    }

    if (total_y == 0 || total_y % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    int M = total_y / 2;

    auto rect_sum = [&](int r1, int c1, int r2, int c2) {
        return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1];
    };

    long long total_ways = 0;

    for (int r = 1; r <= M; ++r) {
        if (r > H) break;
        if (M % r != 0) continue;
        int c = M / r;
        if (c > W) continue;

        int req_row = 2 * c;
        int r_part = 0;
        int i = 0, cur = 0;
        long long ways_r = 1;
        vector<int> row_bounds = {0};
        bool possible = true;

        while (i < H) {
            cur += row_cnt[i];
            if (cur == req_row) {
                r_part++;
                if (r_part < r) {
                    int j = i + 1;
                    int empty = 0;
                    while (j < H && row_cnt[j] == 0) {
                        empty++;
                        j++;
                    }
                    ways_r = (ways_r * (empty + 1)) % MOD;
                    row_bounds.push_back(i + 1);
                    i = j;
                    cur = 0;
                } else {
                    int j = i + 1;
                    while (j < H) {
                        if (row_cnt[j] > 0) { possible = false; break; }
                        j++;
                    }
                    row_bounds.push_back(H);
                    break;
                }
            } else if (cur > req_row) {
                possible = false;
                break;
            } else {
                i++;
            }
        }

        if (!possible || r_part != r) continue;

        int req_col = 2 * r;
        int c_part = 0;
        int j = 0;
        cur = 0;
        long long ways_c = 1;
        vector<int> col_bounds = {0};

        while (j < W) {
            cur += col_cnt[j];
            if (cur == req_col) {
                c_part++;
                if (c_part < c) {
                    int k = j + 1;
                    int empty = 0;
                    while (k < W && col_cnt[k] == 0) {
                        empty++;
                        k++;
                    }
                    ways_c = (ways_c * (empty + 1)) % MOD;
                    col_bounds.push_back(j + 1);
                    j = k;
                    cur = 0;
                } else {
                    int k = j + 1;
                    while (k < W) {
                        if (col_cnt[k] > 0) { possible = false; break; }
                        k++;
                    }
                    col_bounds.push_back(W);
                    break;
                }
            } else if (cur > req_col) {
                possible = false;
                break;
            } else {
                j++;
            }
        }

        if (!possible || c_part != c) continue;

        bool valid = true;
        for (int bi = 0; bi < r; ++bi) {
            for (int bj = 0; bj < c; ++bj) {
                if (rect_sum(row_bounds[bi], col_bounds[bj], row_bounds[bi + 1] - 1, col_bounds[bj + 1] - 1) != 2) {
                    valid = false;
                    break;
                }
            }
            if (!valid) break;
        }

        if (valid) {
            total_ways = (total_ways + ways_r * ways_c) % MOD;
        }
    }

    cout << total_ways << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
