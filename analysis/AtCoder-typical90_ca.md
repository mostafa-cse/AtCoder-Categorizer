# Problem Analysis: AtCoder-typical90_ca — Two by Two

**Problem ID**: `AtCoder-typical90_ca`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 079)  
**Rating / Difficulty**: 850 (★3)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ca  
**VJudge Tag**: `[problem:AtCoder-typical90_ca]`  
**Category File**: [`../categories/basics/subgrid_elimination.md`](../categories/basics/subgrid_elimination.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy & Invariants`  
- **Topic (Skill)**: `Corner-First Unique Determinism / 2x2 Subgrid Elimination`  

---

## 1. Problem Statement & Key Idea
H x W matrices A and B. In one operation, add +-1 to any 2x2 subgrid. Can A be transformed to B, and what is the minimum operations?

**Core Idea**: The top-left cell (1, 1) can ONLY be altered by the single 2x2 subgrid rooted at (1, 1). Its operation count is uniquely determined!

## 2. Core Observation & Invariant
Process greedily in row-major order: at cell (r, c), diff = B_{r, c} - A_{r, c}. Apply diff to the 2x2 subgrid. After all (H-1)*(W-1) steps, verify if the remaining last row and last column match B.

## 3. Step-by-Step Algorithm
1. ops = 0.
2. For r from 0 to H - 2: for c from 0 to W - 2:
   - diff = B[r][c] - A[r][c]
   - ops += abs(diff)
   - Add diff to A[r][c], A[r+1][c], A[r][c+1], A[r+1][c+1].
3. If A == B: output 'Yes' and ops; else 'No'.

## 4. Complexity Analysis
Time: O(H * W), Space: O(H * W).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<vector<long long>> a(h, vector<long long>(w));
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) cin >> a[i][j];
    }

    vector<vector<long long>> b(h, vector<long long>(w));
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) cin >> b[i][j];
    }

    long long ops = 0;
    for (int r = 0; r < h - 1; ++r) {
        for (int c = 0; c < w - 1; ++c) {
            long long diff = b[r][c] - a[r][c];
            if (diff != 0) {
                ops += abs(diff);
                a[r][c] += diff;
                a[r + 1][c] += diff;
                a[r][c + 1] += diff;
                a[r + 1][c + 1] += diff;
            }
        }
    }

    if (a == b) {
        cout << "Yes\n" << ops << "\n";
    } else {
        cout << "No\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Corner-first unique deterministic greedy elimination.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Deterministic cascade elimination in grid operations and invariant propagation.
- **Reusable Pattern**: `Corner-First Deterministic Elimination.`

---
Back to [Corner-First Unique Determinism / 2x2 Subgrid Elimination](../categories/basics/subgrid_elimination.md) | [Categories Directory](../categories/README.md)