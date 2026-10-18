# Problem Analysis: AtCoder-tenka1_2014_qualB_d — D. 天下一芸術 (Tenka1 Art)

**Problem ID**: `AtCoder-tenka1_2014_qualB_d`  
**Contest**: `tenka1-2014-qualb`  
**Rating / Difficulty**: 2572  
**URL**: https://atcoder.jp/contests/tenka1-2014-qualb/tasks/tenka1_2014_qualB_d  
**VJudge Tag**: `[problem:AtCoder-tenka1_2014_qualB_d]`  
**Category File**: [`../categories/dynamic_programming_dp/tenka1_art_bitmask_transitive_closure.md`](../categories/dynamic_programming_dp/tenka1_art_bitmask_transitive_closure.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Given an N x N target grid painted with N overlapping rectangular brush strokes and a list of brush sizes A_i, determine whether the target grid could have been produced by painting rectangles of sizes A_i in some order.

## 2. Core Observation & Invariant
Each color i must cover a bounding box [L_i, R_i] x [T_i, B_i]. If another color j overlaps inside color i's bounding box, color j must have been painted strictly after color i. This defines a directed dependency graph. Furthermore, colors with identical sizes can be assigned to brush dimensions. We compute the transitive closure of dependencies to check for cycles, and then use bitmask dynamic programming over subset configurations to match colors to sizes.

## 3. Step-by-Step Algorithm
1. Find bounding box [L_i, R_i] x [T_i, B_i] for each color i.
2. For each cell (y, x) inside color i's bounding box with color j != i, add directed edge i -> j.
3. Compute transitive closure using Floyd-Warshall bitwise OR; if any i has edge i -> i, output 0 (cycle detected).
4. Sort identical brush size counts V into groups.
5. Run bitmask DP dp[i][mask]: 1 if subset mask of colors can be assigned to the first i size groups respecting dependencies.
6. Output dp[|V|][(1 << N) - 1].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 + |V| * 3^N)`
- **Space Complexity**: `O(2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int A[30];
int H, W;
int BB[300][300];
int L[30], R[30], T[30], B[30];
vector<int> V, MA[18];
int mat[20];
int dpdp[20][1 << 18];
int ms[1 << 18];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> N)) return 0;
    for (int i = 0; i < N; i++) cin >> A[i];
    sort(A, A + N);

    V.push_back(1);
    for (int i = 1; i < N; i++) {
        if (A[i] == A[i - 1]) V.back()++;
        else V.push_back(1);
    }

    for (int i = 0; i < N; i++) {
        L[i] = T[i] = 305;
        R[i] = B[i] = -1;
    }

    cin >> H >> W;
    for (int y = 0; y < H; y++) {
        for (int x = 0; x < W; x++) {
            cin >> BB[y][x];
            int i = BB[y][x];
            L[i] = min(L[i], x);
            R[i] = max(R[i], x);
            T[i] = min(T[i], y);
            B[i] = max(B[i], y);
        }
    }

    for (int i = 0; i < N; i++) {
        if (L[i] > R[i]) continue;
        for (int y = T[i]; y <= B[i]; y++) {
            for (int x = L[i]; x <= R[i]; x++) {
                if (BB[y][x] != i) {
                    mat[BB[y][x]] |= (1 << i);
                }
            }
        }
    }

    // Transitive closure
    for (int i = 0; i < N; i++) {
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                mat[x] |= (((mat[x] >> i) & (mat[i] >> y) & 1) << y);
            }
        }
    }

    for (int i = 0; i < N; i++) {
        if (mat[i] & (1 << i)) {
            cout << 0 << "\n";
            return 0;
        }
    }

    for (int mask = 0; mask < (1 << N); mask++) {
        for (int x = 0; x < N; x++) {
            if (mask & (1 << x)) {
                ms[mask] |= mat[x];
            }
        }
    }

    for (int mask = 0; mask < (1 << N); mask++) {
        int cnt = 0;
        for (int b = 0; b < N; b++) {
            if (mask & (1 << b)) cnt++;
        }
        MA[cnt].push_back(mask);
    }

    dpdp[0][0] = 1;
    for (size_t i = 0; i < V.size(); i++) {
        int cur_cnt = V[i];
        for (int mask = 0; mask < (1 << N); mask++) {
            if (!dpdp[i][mask]) continue;
            for (int mask2 : MA[cur_cnt]) {
                if ((mask & mask2) == 0 && (ms[mask2] & mask) == ms[mask2] && (ms[mask2] & mask2) == 0) {
                    dpdp[i + 1][mask | mask2] = 1;
                }
            }
        }
    }

    cout << dpdp[V.size()][(1 << N) - 1] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
