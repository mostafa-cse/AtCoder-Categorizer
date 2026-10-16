# Problem Analysis: AtCoder-abc079_d — Wall

**Problem ID**: `AtCoder-abc079_d`  
**Contest**: `abc079`  
**Rating / Difficulty**: 949  
**URL**: https://atcoder.jp/contests/abc079/tasks/abc079_d  
**VJudge Tag**: `[problem:AtCoder-abc079_d]`  
**Category File**: [`../categories/graph_theory/digit_transformation_floyd_warshall.md`](../categories/graph_theory/digit_transformation_floyd_warshall.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `All-Pairs Shortest Paths`  
- **Topic (Skill)**: `Digit Transformation Graph via Floyd-Warshall`  

---

## 1. Problem Statement & Key Idea
An H x W wall contains digits 0..9 and -1. Transforming digit i to j costs c_{i, j}. Find the minimum total cost to transform every digit on the wall into 1.

**Key Idea**: Direct transformation from i to 1 might not be optimal; an indirect path i -> k -> 1 may be cheaper. This is all-pairs shortest paths on a 10-node directed graph.

## 2. Core Observation & Invariant
Run Floyd-Warshall on the 10 x 10 cost matrix in 10^3 = 1000 operations. Then for each cell on the wall containing digit d != -1, add the optimal cost dist[d][1].

## 3. Step-by-Step Algorithm
1. Read the 10 x 10 matrix c.
2. Apply Floyd-Warshall: for k in 0..9, for i in 0..9, for j in 0..9: c[i][j] = min(c[i][j], c[i][k] + c[k][j]).
3. Initialize total_cost = 0.
4. For each of the H * W grid cells: read d; if d != -1 and d != 1: total_cost += c[d][1].
5. Print total_cost.

## 4. Complexity Analysis
- **Time Complexity**: `O(10^3 + H * W)`
- **Space Complexity**: `O(10^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<vector<int>> c(10, vector<int>(10));
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 10; ++j) {
            cin >> c[i][j];
        }
    }

    for (int k = 0; k < 10; ++k) {
        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j < 10; ++j) {
                c[i][j] = min(c[i][j], c[i][k] + c[k][j]);
            }
        }
    }

    long long total_cost = 0;
    for (int r = 0; r < h; ++r) {
        for (int col = 0; col < w; ++col) {
            int d;
            cin >> d;
            if (d != -1 && d != 1) {
                total_cost += c[d][1];
            }
        }
    }

    cout << total_cost << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Small-alphabet transformation graph precomputation using Floyd-Warshall.
- **Reusable Pattern**: `Floyd-Warshall precomputation on small state graphs before processing grid queries.`
