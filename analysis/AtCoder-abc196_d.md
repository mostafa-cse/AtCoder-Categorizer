# Problem Analysis: AtCoder-abc196_d — Hanjo

**Problem ID**: `AtCoder-abc196_d`  
**Contest**: `abc196`  
**Rating / Difficulty**: 1277  
**URL**: https://atcoder.jp/contests/abc196/tasks/abc196_d  
**VJudge Tag**: `[problem:AtCoder-abc196_d]`  
**Category File**: [`../categories/basics/grid_domino_tiling_backtracking.md`](../categories/basics/grid_domino_tiling_backtracking.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Backtracking`  
- **Topic (Skill)**: `Grid Domino Tiling Backtracking DFS`  

---

## 1. Problem Statement & Key Idea
An H x W room. Tile with A tatami mats of size 2x1 and B mats of size 1x1 such that 2A + B = H * W (H * W <= 16). Find the number of valid tilings.

**Key Idea**: The grid size H * W <= 16 is small enough for exact recursive cell-by-cell placement.

## 2. Core Observation & Invariant
Visit cells in row-major order: index k from 0 to H*W - 1 (r = k / W, c = k % W). If cell (r, c) is already covered, advance to k + 1. Otherwise, we can: (1) place a 1x1 mat if B > 0; (2) place a 2x1 horizontal mat if c + 1 < W and cell (r, c+1) is empty and A > 0; (3) place a 1x2 vertical mat if r + 1 < H and cell (r+1, c) is empty and A > 0.

## 3. Step-by-Step Algorithm
1. Write DFS(k, a_left, b_left, mask):
2. If k == H * W: return (a_left == 0 && b_left == 0 ? 1 : 0).
3. If (mask >> k) & 1: return DFS(k + 1, a_left, b_left, mask).
4. Try placing 1x1 mat: count += DFS(k + 1, a_left, b_left - 1, mask | (1 << k)).
5. Try horizontal 2x1 mat (if c + 1 < W and unmasked): count += DFS(k + 1, a_left - 1, b_left, mask | (1 << k) | (1 << (k + 1))).
6. Try vertical 1x2 mat (if r + 1 < H and unmasked): count += DFS(k + 1, a_left - 1, b_left, mask | (1 << k) | (1 << (k + W))).
7. Start DFS(0, A, B, 0).

## 4. Complexity Analysis
- **Time Complexity**: `O(3^(HW/2))`
- **Space Complexity**: `O(HW)`

## 5. Complete C++ Solution
```cpp
#include <iostream>

using namespace std;

int h, w, a_mats, b_mats;

long long dfs(int k, int a, int b, int mask) {
    if (k == h * w) {
        return (a == 0 && b == 0 ? 1 : 0);
    }
    if ((mask >> k) & 1) {
        return dfs(k + 1, a, b, mask);
    }

    int r = k / w;
    int c = k % w;
    long long ways = 0;

    // Place 1x1 mat
    if (b > 0) {
        ways += dfs(k + 1, a, b - 1, mask | (1 << k));
    }

    // Place 1x2 horizontal mat
    if (a > 0 && c + 1 < w && !((mask >> (k + 1)) & 1)) {
        ways += dfs(k + 1, a - 1, b, mask | (1 << k) | (1 << (k + 1)));
    }

    // Place 2x1 vertical mat
    if (a > 0 && r + 1 < h && !((mask >> (k + w)) & 1)) {
        ways += dfs(k + 1, a - 1, b, mask | (1 << k) | (1 << (k + w)));
    }

    return ways;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> h >> w >> a_mats >> b_mats)) return 0;

    cout << dfs(0, a_mats, b_mats, 0) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Exact grid domino tiling enumeration via cell-by-cell backtracking.
- **Reusable Pattern**: `Grid tiling DFS: scan cell k, try 1x1, 1x2 horizontal, 2x1 vertical.`
