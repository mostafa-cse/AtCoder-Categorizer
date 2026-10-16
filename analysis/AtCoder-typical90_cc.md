# Problem Analysis: AtCoder-typical90_cc — Friendly Group

**Problem ID**: `AtCoder-typical90_cc`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 081)  
**Rating / Difficulty**: 1750 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_cc  
**VJudge Tag**: `[problem:AtCoder-typical90_cc]`  
**Category File**: [`../categories/data_structures/difference_arrays_imos.md`](../categories/data_structures/difference_arrays_imos.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Prefix Sums & Difference Arrays`  
- **Topic (Skill)**: `2D Prefix Sums for Bounded Window Maximization`  

---

## 1. Problem Statement & Key Idea
N students with height A_i <= 5000 and weight B_i <= 5000. Find maximum students in a group with max_A - min_A <= K and max_B - min_B <= K.

**Core Idea**: Represent students on a 5000 x 5000 2D frequency grid. A valid group is bounded by a rectangle of size (K + 1) x (K + 1).

## 2. Core Observation & Invariant
Compute 2D prefix sums on the coordinate grid. Slide a (K + 1) x (K + 1) window over all positions to find the maximum sum in O(M^2) where M = 5000.

## 3. Step-by-Step Algorithm
1. Build count[A_i][B_i]++.
2. Compute 2D prefix sums pref[r][c].
3. Loop r from 1 to 5000, c from 1 to 5000: query sum in rectangle [r, min(5000, r + K)] x [c, min(5000, c + K)].
4. Output max rectangle sum.

## 4. Complexity Analysis
Time: O(N + M^2) where M = 5000, Space: O(M^2).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 5000;
int pref[MAX + 2][MAX + 2];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        pref[a][b]++;
    }

    // 2D Prefix Sums
    for (int i = 1; i <= MAX; ++i) {
        for (int j = 1; j <= MAX; ++j) {
            pref[i][j] += pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
        }
    }

    int max_students = 0;
    for (int i = 1; i <= MAX; ++i) {
        int r2 = min(MAX, i + k);
        for (int j = 1; j <= MAX; ++j) {
            int c2 = min(MAX, j + k);
            int cur = pref[r2][c2] - pref[i - 1][c2] - pref[r2][j - 1] + pref[i - 1][j - 1];
            max_students = max(max_students, cur);
        }
    }

    cout << max_students << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
2D prefix sums for sliding bounding-box query maximization.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 2D Prefix sums, coordinate discretization, and 2D sliding window maximization.
- **Reusable Pattern**: `2D Prefix Sum Window Maximization.`

---
Back to [2D Prefix Sums for Bounded Window Maximization](../categories/data_structures/difference_arrays_imos.md) | [Categories Directory](../categories/README.md)