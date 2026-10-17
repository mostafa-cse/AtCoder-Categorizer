# Problem Analysis: AtCoder-abc379_g — G. Count Grid 3-coloring

**Problem ID**: `AtCoder-abc379_g`  
**Contest**: `abc379`  
**Rating / Difficulty**: 2304  
**URL**: https://atcoder.jp/contests/abc379/tasks/abc379_g  
**VJudge Tag**: `[problem:AtCoder-abc379_g]`  
**Category File**: [`../categories/miscellaneous/broken_profile_grid_3coloring.md`](../categories/miscellaneous/broken_profile_grid_3coloring.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Broken Profile DP / Plug DP`  

---

## 1. Problem Statement & Key Idea
Given an $H \times W$ grid ($HW \le 200$) with characters in $\{1, 2, 3, ?\}$, count valid 3-colorings where adjacent cells differ, modulo 998244353.

## 2. Core Observation & Invariant
Since $H \times W \le 200$, transposing ensures $W \le 14$. The frontier profile of the last $W$ assigned cells completely determines validity of subsequent cell assignments.

## 3. Step-by-Step Algorithm
1. Transpose grid if $W > H$ so that $W \le 14$. Encode the boundary profile of the last $W$ cells using 2 bits per cell in an unsigned 32-bit integer.
2. Perform cell-by-cell broken profile dynamic programming across all $H \times W$ cells.
3. At each cell, verify color compatibility with top and left neighbors and update profiles via bit shifts and open-addressing hash aggregation.

## 4. Complexity Analysis
- **Time Complexity**: `O(HW \cdot 3 \cdot 2^{W-1})`
- **Space Complexity**: `O(2^W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdint>

using namespace std;

const int MOD = 998244353;

struct HashTable {
    static const int SIZE = 1 << 16;
    static const int MASK = SIZE - 1;
    uint32_t keys[SIZE];
    int vals[SIZE];
    int head[SIZE];
    int nxt[SIZE];
    int sz;

    void clear() {
        fill(head, head + SIZE, -1);
        sz = 0;
    }

    void add(uint32_t k, int v) {
        int h = (k * 2654435761u) & MASK;
        for (int e = head[h]; e != -1; e = nxt[e]) {
            if (keys[e] == k) {
                vals[e] = (vals[e] + v) % MOD;
                return;
            }
        }
        keys[sz] = k;
        vals[sz] = v;
        nxt[sz] = head[h];
        head[h] = sz++;
    }
};

HashTable ht_cur, ht_nxt;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W;
    if (!(cin >> H >> W)) return 0;
    vector<string> grid(H);
    for (int i = 0; i < H; ++i) cin >> grid[i];

    if (W > H) {
        vector<string> transposed(W, string(H, ' '));
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                transposed[j][i] = grid[i][j];
            }
        }
        grid = transposed;
        swap(H, W);
    }

    ht_cur.clear();
    ht_cur.add(0, 1);

    int shift = 2 * (W - 1);

    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            ht_nxt.clear();
            char ch = grid[r][c];

            for (int i = 0; i < ht_cur.sz; ++i) {
                uint32_t m = ht_cur.keys[i];
                int ways = ht_cur.vals[i];

                int top = (m & 3);
                int left = ((m >> shift) & 3);

                for (int val = 0; val < 3; ++val) {
                    if (ch != '?' && ch - '1' != val) continue;
                    if (r > 0 && val == top) continue;
                    if (c > 0 && val == left) continue;

                    uint32_t nm = (m >> 2) | ((uint32_t)val << shift);
                    ht_nxt.add(nm, ways);
                }
            }
            ht_cur = ht_nxt;
        }
    }

    int ans = 0;
    for (int i = 0; i < ht_cur.sz; ++i) {
        ans = (ans + ht_cur.vals[i]) % MOD;
    }
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
