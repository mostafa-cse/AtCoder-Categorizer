# Problem Analysis: AtCoder-arc152_d — D. Halftree

**Problem ID**: `AtCoder-arc152_d`  
**Contest**: `arc152`  
**Rating / Difficulty**: 2381  
**URL**: https://atcoder.jp/contests/arc152/tasks/arc152_d  
**VJudge Tag**: `[problem:AtCoder-arc152_d]`  
**Category File**: [`../categories/basics/cyclic_shift_halftree_grid_construction.md`](../categories/basics/cyclic_shift_halftree_grid_construction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Add (N-1)/2 edges to an empty graph such that shifting every edge by +K mod N forms a tree. Impossible iff N is even. For odd N, arranging vertices in an n x g grid (n = N/g, g = gcd(N, K)) and placing vertical edges in odd columns, horizontal edges from odd columns, and bottom horizontal edges from even columns constructs a valid spanning tree in O(N) time.

## 2. Core Observation & Invariant
Adding M edges doubles to 2M edges after the +K mod N shift. For the result to be a tree, 2M = N - 1, which requires N to be odd (impossible if N is even). For odd N, arranging vertices on an n x g torus grid where moving down a row represents +K mod N allows constructing a tree via interlaced vertical backbone paths and horizontal comb bridges.

## 3. Step-by-Step Algorithm
1. If N is even, output -1.
2. Let g = gcd(N, K), n = N / g. Construct an n x g grid with grid[r][c] = ((r * K) mod N + c) mod N.
3. In odd-numbered columns (0-indexed c even), add vertical edges between row 2r and 2r+1 for r in 0 .. (n-3)/2.
4. From odd-numbered columns c < g - 1, add horizontal edges to c+1 at rows 2r for r in 0 .. (n-3)/2.
5. From even-numbered columns c < g - 1, add a single horizontal edge to c+1 at row n - 2.
6. Output the (N-1)/2 constructed edges.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

long long gcd(long long a, long long b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long N, K;
    if (!(cin >> N >> K)) return 0;

    if (N % 2 == 0) {
        cout << -1 << "\n";
        return 0;
    }

    long long g = gcd(N, K);
    long long n = N / g;

    vector<vector<int>> grid(n, vector<int>(g));
    for (int r = 0; r < n; ++r) {
        long long base = (1LL * r * K) % N;
        for (int c = 0; c < g; ++c) {
            grid[r][c] = (base + c) % N;
        }
    }

    vector<pair<int, int>> edges;

    // 1. Vertical edges in odd-numbered columns (c = 0, 2, 4, ...):
    for (int c = 0; c < g; c += 2) {
        for (int r = 0; r < (n - 1) / 2; ++r) {
            edges.push_back({grid[2 * r][c], grid[2 * r + 1][c]});
        }
    }

    // 2. Horizontal edges from odd-numbered columns (c = 0, 2, 4, ... < g - 1):
    for (int c = 0; c < g - 1; c += 2) {
        for (int r = 0; r < (n - 1) / 2; ++r) {
            edges.push_back({grid[2 * r][c], grid[2 * r][c + 1]});
        }
    }

    // 3. Horizontal edges from even-numbered columns (c = 1, 3, 5, ... < g - 1):
    for (int c = 1; c < g - 1; c += 2) {
        edges.push_back({grid[n - 2][c], grid[n - 2][c + 1]});
    }

    cout << edges.size() << "\n";
    for (auto& e : edges) {
        cout << e.first << " " << e.second << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
