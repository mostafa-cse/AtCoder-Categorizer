# Problem Analysis: AtCoder-dwacon5th_prelims_d — D - Square Rotation

**Problem ID**: `AtCoder-dwacon5th_prelims_d`  
**Contest**: `dwacon5th-prelims`  
**Rating / Difficulty**: 2875  
**URL**: https://atcoder.jp/contests/dwacon5th-prelims/tasks/dwacon5th_prelims_d  
**VJudge Tag**: `[problem:AtCoder-dwacon5th_prelims_d]`  
**Category File**: [`../categories/basics/periodic_residue_grid_capacity_enclosing_square.md`](../categories/basics/periodic_residue_grid_capacity_enclosing_square.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `2D Prefix Sum`  
- **Topic (Skill)**: `2D Prefix Sum`  

---

## 1. Problem Statement & Key Idea
Given N points in Z^2 and integer D, 90-degree rotations of D x D squares preserve coordinates modulo D. Find the minimum side length of an axis-aligned square that can enclose all points after arbitrary operations.

## 2. Core Observation & Invariant
Any point can be moved to any lattice position with the same (x mod D, y mod D). For an enclosing square of side length aD + b with offset (X, Y), each residue cell has capacity (a+1)^2, a(a+1), or a^2 forming 4 rectangular quadrants. Feasibility requires: all cells with count > a(a+1) lie in a (b+1) x (b+1) window, and no cell with count > a^2 lies in the forbidden (D - 1 - b) x (D - 1 - b) window. Using 2D prefix sums on a periodic 2D x 2D grid, each offset (X, Y) is tested in O(1) time.

## 3. Step-by-Step Algorithm
1. 1. Count points A_{i, j} for each residue (i, j) in [0, D-1]^2.
2. 2. Set a = ceil(sqrt(max A)) - 1.
3. 3. Binary search on b in [0, D-1].
4. 4. For a fixed b, build two 2D prefix sum tables over [0, 2D-1]^2 for thresholds a(a+1) and a^2.
5. 5. Test if any shift (X, Y) in [0, D-1]^2 satisfies both window conditions in O(1).
6. 6. Return aD + b_min.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + D^2 log D)`
- **Space Complexity**: `O(D^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int N, D;
int A[1005][1005];

int P1[2005][2005];
int P2[2005][2005];

int query_sum(int P[2005][2005], int r1, int c1, int r2, int c2) {
    if (r1 > r2 || c1 > c2) return 0;
    return P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1];
}

bool check(int b, int a, int T1) {
    // Square size in residues: (b + 1) x (b + 1)
    // Forbidden rectangle size: (D - 1 - b) x (D - 1 - b)
    int len_sq = b + 1;
    int len_forbid = D - 1 - b;

    for (int X = 0; X < D; ++X) {
        for (int Y = 0; Y < D; ++Y) {
            // Condition 1: sum of G1 in [X, X + b] x [Y, Y + b] == T1
            if (T1 > 0) {
                int s1 = query_sum(P1, X, Y, X + b, Y + b);
                if (s1 != T1) continue;
            }

            // Condition 2: sum of G2 in [X + b + 1, X + D - 1] x [Y + b + 1, Y + D - 1] == 0
            if (len_forbid > 0) {
                int s2 = query_sum(P2, X + b + 1, Y + b + 1, X + D - 1, Y + D - 1);
                if (s2 != 0) continue;
            }

            return true;
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> D)) return 0;

    int max_A = 0;
    for (int i = 0; i < N; ++i) {
        int x, y;
        cin >> x >> y;
        int rx = x % D;
        int ry = y % D;
        A[rx][ry]++;
        if (A[rx][ry] > max_A) max_A = A[rx][ry];
    }

    int a = 0;
    while ((a + 1) * (a + 1) < max_A) {
        a++;
    }

    long long thresh1 = 1LL * a * (a + 1);
    long long thresh2 = 1LL * a * a;

    int T1 = 0;
    for (int i = 0; i < 2 * D; ++i) {
        for (int j = 0; j < 2 * D; ++j) {
            int val = A[i % D][j % D];
            int g1 = (val > thresh1) ? 1 : 0;
            int g2 = (val > thresh2) ? 1 : 0;
            if (i < D && j < D && g1) T1++;
            P1[i + 1][j + 1] = g1 + P1[i][j + 1] + P1[i + 1][j] - P1[i][j];
            P2[i + 1][j + 1] = g2 + P2[i][j + 1] + P2[i + 1][j] - P2[i][j];
        }
    }

    int low = 0, high = D - 1, best_b = D;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid, a, T1)) {
            best_b = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    long long ans = 1LL * a * D + best_b;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
