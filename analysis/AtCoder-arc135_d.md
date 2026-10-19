# Problem Analysis: AtCoder-arc135_d — D - Add to Square

**Problem ID**: `AtCoder-arc135_d`  
**Contest**: `arc135`  
**Rating / Difficulty**: 2744  
**URL**: https://atcoder.jp/contests/arc135/tasks/arc135_d  
**VJudge Tag**: `[problem:AtCoder-arc135_d]`  
**Category File**: [`../categories/graph_theory/add_to_square_bipartite_potential.md`](../categories/graph_theory/add_to_square_bipartite_potential.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Min Cost Max Flow (MCMF)`  

---

## 1. Problem Statement & Key Idea
Given an H x W integer grid A, we can choose any 2x2 square and add an arbitrary integer z to all four cells. We want to minimize the sum of absolute values sum |A_{i,j}| and output the resulting grid.

## 2. Core Observation & Invariant
Adding z to a 2x2 square preserves the alternating row sums R_i = sum_j (-1)^{i+j} A_{i,j} and alternating column sums C_j = sum_i (-1)^{i+j} A_{i,j}. Working backwards from bottom-right (r = H-1 down to 1, c = W-1 down to 1), we can eliminate A_{r,c} to 0, which pushes all remaining non-zero values into row 0 and column 0 without changing the alternating sums. After clearing the subgrid, the problem reduces to matching the residual row potentials R_i and column potentials C_j greedily to minimize sum |A_{0,j}| + sum |A_{i,0}| + |A_{0,0}|, which achieves the theoretical lower bound max(sum |R_i|, sum |C_j|).

## 3. Step-by-Step Algorithm
1. 1. Iterate r from H-1 down to 1 and c from W-1 down to 1, adding -A[r][c] to the 2x2 square with bottom-right at (r, c) to make A[r][c] = 0.
2. 2. Extract row residues R[i] = A[i][0] and column residues C[j] = A[0][j].
3. 3. Pair positive and negative potentials between R and C using two pointers / greedy matching to minimize total absolute sum.
4. 4. Output the minimum total sum and the constructed grid.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    vector<vector<long long>> A(H, vector<long long>(W));
    for (int y = 0; y < H; y++) {
        for (int x = 0; x < W; x++) {
            cin >> A[y][x];
        }
    }

    // Step 1: Zero out everything except row 0 and col 0 from bottom-right up
    for (int y = H - 2; y >= 0; y--) {
        for (int x = W - 2; x >= 0; x--) {
            long long v = A[y + 1][x + 1];
            A[y][x] -= v;
            A[y][x + 1] -= v;
            A[y + 1][x] -= v;
            A[y + 1][x + 1] -= v;
        }
    }

    // Step 2: Cancel row 0 and col 0 elements
    for (int y = 1; y < H; y++) {
        for (int x = 1; x < W; x++) {
            long long mi = 0;
            if (x % 2 == y % 2) {
                if (A[y][0] > 0 && A[0][x] > 0) mi = min(A[y][0], A[0][x]);
                if (A[y][0] < 0 && A[0][x] < 0) mi = max(A[y][0], A[0][x]);
                A[y][0] -= mi;
                A[0][x] -= mi;
                if (x % 2 == 0) {
                    A[y][x] += mi;
                    A[0][0] += mi;
                } else {
                    A[y][x] -= mi;
                    A[0][0] -= mi;
                }
            } else if (x % 2 == 1) {
                if (A[y][0] < 0 && A[0][x] > 0) mi = min(-A[y][0], A[0][x]);
                if (A[y][0] > 0 && A[0][x] < 0) mi = max(-A[y][0], A[0][x]);
                A[0][0] -= mi;
                A[y][0] += mi;
                A[0][x] -= mi;
                A[y][x] += mi;
            } else {
                if (A[y][0] > 0 && A[0][x] < 0) mi = min(A[y][0], -A[0][x]);
                if (A[y][0] < 0 && A[0][x] > 0) mi = max(A[y][0], -A[0][x]);
                A[0][0] -= mi;
                A[y][0] -= mi;
                A[0][x] += mi;
                A[y][x] += mi;
            }
        }
    }

    long long sum = 0;
    for (int y = 0; y < H; y++) {
        for (int x = 0; x < W; x++) {
            sum += llabs(A[y][x]);
        }
    }

    cout << sum << "\n";
    for (int y = 0; y < H; y++) {
        for (int x = 0; x < W; x++) {
            cout << A[y][x] << (x == W - 1 ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
