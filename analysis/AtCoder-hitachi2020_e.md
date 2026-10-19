# Problem Analysis: AtCoder-hitachi2020_e — E - Odd Sum Rectangles

**Problem ID**: `AtCoder-hitachi2020_e`  
**Contest**: `hitachi2020`  
**Rating / Difficulty**: 2732  
**URL**: https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_e  
**VJudge Tag**: `[problem:AtCoder-hitachi2020_e]`  
**Category File**: [`../categories/math/odd_sum_rectangles_hadamard_basis.md`](../categories/math/odd_sum_rectangles_hadamard_basis.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Vector Space and XOR Basis`  

---

## 1. Problem Statement & Key Idea
In a grid of (2^N - 1) rows and (2^M - 1) columns (N, M <= 10), fill each cell with 0 or 1 to maximize the number of subrectangles with odd sum.

## 2. Core Observation & Invariant
The 2D prefix sums of the grid modulo 2 can be viewed as evaluating a 2D parity function f(r, c) on a (2^N) x (2^M) grid. The oddness is maximized when each pair of column indices produces an optimal balance of odd/even row differences, reaching the theoretical upper bound (2^{2*max(N,M)} / 4) * (2^min(N,M) * (2^min(N,M) - 1) / 2). This upper bound is constructively achieved using a recursive Hadamard-style fractal construction: start with a 1x1 grid [1] for K=1; for K+1, place the solution of size 2^K - 1 in all four corners, set the center cell (2^K, 2^K) to 1, and fill the rest of the center row and column with 0.

## 3. Step-by-Step Algorithm
1. 1. Determine K = max(N, M).
2. 2. Recursively construct the (2^K - 1) x (2^K - 1) grid:
3.    a. Base case K = 1: grid is [[1]].
4.    b. For K > 1: copy previous grid of size sz = 2^{K-1} - 1 into all four corners: (r, c), (r, c + sz + 1), (r + sz + 1, c), and (r + sz + 1, c + sz + 1).
5.    c. Set center cell grid[sz][sz] = 1, leaving all other cells in row sz and col sz as 0.
6. 3. Output the subgrid consisting of the first 2^N - 1 rows and 2^M - 1 columns.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^{N+M})`
- **Space Complexity**: `O(2^{2 * max(N, M)})`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> build_grid(int K) {
    if (K == 1) {
        return {{1}};
    }
    vector<vector<int>> prev = build_grid(K - 1);
    int sz = prev.size();
    int new_sz = 2 * sz + 1;
    vector<vector<int>> grid(new_sz, vector<int>(new_sz, 0));

    for (int r = 0; r < sz; ++r) {
        for (int c = 0; c < sz; ++c) {
            grid[r][c] = prev[r][c];
            grid[r][c + sz + 1] = prev[r][c];
            grid[r + sz + 1][c] = prev[r][c];
            grid[r + sz + 1][c + sz + 1] = prev[r][c];
        }
    }
    grid[sz][sz] = 1;
    return grid;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    int K = max(N, M);
    vector<vector<int>> grid = build_grid(K);

    int R = (1 << N) - 1;
    int C = (1 << M) - 1;

    for (int r = 0; r < R; ++r) {
        for (int c = 0; c < C; ++c) {
            cout << grid[r][c];
        }
        cout << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
