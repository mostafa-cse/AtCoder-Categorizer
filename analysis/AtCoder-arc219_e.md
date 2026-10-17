# Problem Analysis: AtCoder-arc219_e — E. Equal Distribution

**Problem ID**: `AtCoder-arc219_e`  
**Contest**: `arc219`  
**Rating / Difficulty**: 2164  
**URL**: https://atcoder.jp/contests/arc219/tasks/arc219_e  
**VJudge Tag**: `[problem:AtCoder-arc219_e]`  
**Category File**: [`../categories/graph_theory/hamiltonian_snake_cycle_circular_discrete_ivt.md`](../categories/graph_theory/hamiltonian_snake_cycle_circular_discrete_ivt.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Hamiltonian Path`  
- **Topic (Skill)**: `Hamiltonian Path and Cycle`  

---

## 1. Problem Statement & Key Idea
Partition a 2H x 2W grid containing 2HW strawberries into two connected regions A and B of size 2HW each containing exactly HW strawberries. Construct a Hamiltonian cycle on the 2H x 2W grid; any contiguous subsegment of length 2HW forms a connected path whose complement is also connected. By the discrete intermediate value theorem, a circular arc of length 2HW with exactly HW strawberries always exists.

## 2. Core Observation & Invariant
A standard snake Hamiltonian cycle visits columns in alternating up/down directions on rows 1..2H-1, then returns along row 0. On this cycle of length 4HW, let f(i) be the number of strawberries in the arc of length 2HW starting at cell i. Since f(i + 2HW) = 2HW - f(i) and f changes by at most 1 between adjacent starting points, by the discrete IVT there must be an index where f(i) = HW.

## 3. Step-by-Step Algorithm
1. Construct a Hamiltonian cycle of length 4HW on the 2H x 2W grid: snake down columns 2j and up columns 2j+1 on rows 1..2H-1, then return right-to-left along row 0.
2. Represent the strawberry presence along the cycle as a binary circular array of length 4HW.
3. Compute the sliding window sum of length 2HW. Find a starting index start where the strawberry sum is exactly HW.
4. Color the 2HW cells along the cycle starting at start with A, and color the remaining 2HW cells with B.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W) per testcase`
- **Space Complexity**: `O(H * W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve_case() {
    int H, W;
    if (!(cin >> H >> W)) return;
    int R = 2 * H, C = 2 * W;
    vector<string> S(R);
    for (int i = 0; i < R; ++i) cin >> S[i];

    vector<pair<int, int>> cycle;
    cycle.reserve(R * C);
    for (int j = 0; j < W; ++j) {
        int col1 = 2 * j;
        int col2 = 2 * j + 1;
        for (int r = 1; r < R; ++r) cycle.push_back({r, col1});
        for (int r = R - 1; r >= 1; --r) cycle.push_back({r, col2});
    }
    for (int c = C - 1; c >= 0; --c) {
        cycle.push_back({0, c});
    }

    int N = R * C;
    int L = 2 * H * W;
    vector<int> val(2 * N);
    for (int i = 0; i < N; ++i) {
        val[i] = (S[cycle[i].first][cycle[i].second] == 'o' ? 1 : 0);
        val[i + N] = val[i];
    }

    int cur = 0;
    for (int i = 0; i < L; ++i) cur += val[i];

    int target = H * W;
    int start = -1;
    if (cur == target) {
        start = 0;
    } else {
        for (int i = 1; i < N; ++i) {
            cur += val[i + L - 1] - val[i - 1];
            if (cur == target) {
                start = i;
                break;
            }
        }
    }

    vector<string> res(R, string(C, 'B'));
    for (int j = 0; j < L; ++j) {
        auto [r, c] = cycle[(start + j) % N];
        res[r][c] = 'A';
    }

    for (int i = 0; i < R; ++i) {
        cout << res[i] << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve_case();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
