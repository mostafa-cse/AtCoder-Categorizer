# Problem Analysis: AtCoder-arc139_c — C. One Three Nine

**Problem ID**: `AtCoder-arc139_c`  
**Contest**: `arc139`  
**Rating / Difficulty**: 2406  
**URL**: https://atcoder.jp/contests/arc139/tasks/arc139_c  
**VJudge Tag**: `[problem:AtCoder-arc139_c]`  
**Category File**: [`../categories/basics/constructive_grid_parity_linear_combination.md`](../categories/basics/constructive_grid_parity_linear_combination.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Select the maximum number of grid cells (X, Y) in an N x M grid such that all X + 3Y are distinct and all 3X + Y are distinct. Theoretical upper bound 3*min(N, M) + max(N, M) - 3 (minus 1 if N=M even) is achieved via an optimal snake-like serpentine walk.

## 2. Core Observation & Invariant
Each step (i, j) -> (i, j+1) increases 3X+Y by 1, while (i, j) -> (i+1, j-2) also increases 3X+Y by 1. A continuous walk from (1, 1) to (N, M) covering width-3/5 diagonal bands ensures all 3X+Y and X+3Y values are distinct.

## 3. Step-by-Step Algorithm
1. 1. Assume without loss of generality N <= M (swap coordinates if N > M).
2. 2. Construct the active interval [L_i, R_i] for each row i: rows 1 and 2 cover [1, 3], odd rows 2k-1 cover [2k-3, 2k+1], even rows 2k cover [2k-1, 2k+1], with row N extending to M.
3. 3. Output the total count and all chosen coordinates.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    bool swapped = false;
    if (N > M) {
        swap(N, M);
        swapped = true;
    }

    vector<pair<int, int>> pts;
    for (int i = 1; i <= N; i++) {
        int L = 1, R = 1;
        if (i == 1 || i == 2) {
            L = 1;
            R = min(M, 3);
        } else if (i % 2 == 1) {
            int k = (i + 1) / 2;
            L = (k == 2 ? 1 : 2 * k - 3);
            R = min(M, 2 * k + 1);
        } else {
            int k = i / 2;
            L = 2 * k - 1;
            R = min(M, 2 * k + 1);
        }
        if (i == N) {
            R = M;
        }
        for (int j = L; j <= R; j++) {
            pts.push_back({i, j});
        }
    }

    if (swapped) {
        for (auto& p : pts) swap(p.first, p.second);
    }

    cout << pts.size() << "\n";
    for (auto& p : pts) {
        cout << p.first << " " << p.second << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
