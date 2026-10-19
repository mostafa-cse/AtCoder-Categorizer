# Problem Analysis: AtCoder-abc228_g — Digits on Grid

**Problem ID**: `AtCoder-abc228_g`  
**Contest**: `abc228`  
**Rating / Difficulty**: 2711  
**URL**: https://atcoder.jp/contests/abc228/tasks/abc228_g  
**VJudge Tag**: `[problem:AtCoder-abc228_g]`  
**Category File**: [`../categories/dynamic_programming_dp/digits_on_grid_subset_automata_dp.md`](../categories/dynamic_programming_dp/digits_on_grid_subset_automata_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Counting distinct 2N-digit sequences produced by Takahashi (row moves) and Aoki (column moves) on an H x W grid (H, W <= 10). Modeled as a DFA using the subset construction (powerset automaton) where states at even steps are row subsets R in [1, 2^H - 1] and at odd steps are column subsets C in [1, 2^W - 1].

## 2. Core Observation & Invariant
For each digit d in 1..9, the reachable columns from row mask R are the union of columns containing d across rows in R. Similarly, reachable rows from column mask C are the union of rows containing d across columns in C. There are at most 2^{10} = 1024 states, making DP over 2N steps extremely fast.

## 3. Step-by-Step Algorithm
1. 1. Precompute transition tables trans_R[r_mask][d] -> c_mask and trans_C[c_mask][d] -> r_mask for all d in 1..9.
2. 2. Initialize dp_R[(1 << H) - 1] = 1.
3. 3. Repeat N times:
4.    - Takahashi step: compute dp_C[c_mask] by summing dp_R[r_mask] for all d in 1..9.
5.    - Aoki step: compute next dp_R[r_mask] by summing dp_C[c_mask] for all d in 1..9.
6. 4. Output sum of dp_R modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 9 * (2^H + 2^W))`
- **Space Complexity**: `O(2^H + 2^W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

static const long long MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W, N;
    if (!(cin >> H >> W >> N)) return 0;

    vector<string> grid(H);
    for (int i = 0; i < H; ++i) {
        cin >> grid[i];
    }

    vector<vector<int>> row_digit_cols(H, vector<int>(10, 0));
    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            int d = grid[r][c] - '0';
            row_digit_cols[r][d] |= (1 << c);
        }
    }

    vector<vector<int>> col_digit_rows(W, vector<int>(10, 0));
    for (int c = 0; c < W; ++c) {
        for (int r = 0; r < H; ++r) {
            int d = grid[r][c] - '0';
            col_digit_rows[c][d] |= (1 << r);
        }
    }

    // Precompute transitions for all row masks
    int max_R = 1 << H;
    int max_C = 1 << W;

    vector<vector<int>> trans_R(max_R, vector<int>(10, 0));
    for (int r_mask = 1; r_mask < max_R; ++r_mask) {
        for (int d = 1; d <= 9; ++d) {
            int c_mask = 0;
            for (int r = 0; r < H; ++r) {
                if ((r_mask >> r) & 1) {
                    c_mask |= row_digit_cols[r][d];
                }
            }
            trans_R[r_mask][d] = c_mask;
        }
    }

    vector<vector<int>> trans_C(max_C, vector<int>(10, 0));
    for (int c_mask = 1; c_mask < max_C; ++c_mask) {
        for (int d = 1; d <= 9; ++d) {
            int r_mask = 0;
            for (int c = 0; c < W; ++c) {
                if ((c_mask >> c) & 1) {
                    r_mask |= col_digit_rows[c][d];
                }
            }
            trans_C[c_mask][d] = r_mask;
        }
    }

    vector<long long> dp_R(max_R, 0);
    dp_R[max_R - 1] = 1;

    vector<long long> dp_C(max_C, 0);
    vector<long long> next_R(max_R, 0);

    for (int round_idx = 0; round_idx < N; ++round_idx) {
        // Takahashi step: R -> C
        fill(dp_C.begin(), dp_C.end(), 0);
        for (int r_mask = 1; r_mask < max_R; ++r_mask) {
            long long count = dp_R[r_mask];
            if (!count) continue;
            for (int d = 1; d <= 9; ++d) {
                int c_mask = trans_R[r_mask][d];
                if (c_mask != 0) {
                    dp_C[c_mask] = (dp_C[c_mask] + count) % MOD;
                }
            }
        }

        // Aoki step: C -> R
        fill(next_R.begin(), next_R.end(), 0);
        for (int c_mask = 1; c_mask < max_C; ++c_mask) {
            long long count = dp_C[c_mask];
            if (!count) continue;
            for (int d = 1; d <= 9; ++d) {
                int r_mask = trans_C[c_mask][d];
                if (r_mask != 0) {
                    next_R[r_mask] = (next_R[r_mask] + count) % MOD;
                }
            }
        }
        dp_R = next_R;
    }

    long long ans = 0;
    for (int r_mask = 1; r_mask < max_R; ++r_mask) {
        ans = (ans + dp_R[r_mask]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
