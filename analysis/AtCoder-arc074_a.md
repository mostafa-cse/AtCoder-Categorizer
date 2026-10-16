# Problem Analysis: AtCoder-arc074_a — Chocolate Bar

**Problem ID**: `AtCoder-arc074_a`  
**Contest**: `abc062`  
**Rating / Difficulty**: 1223  
**URL**: https://atcoder.jp/contests/abc062/tasks/arc074_a  
**VJudge Tag**: `[problem:AtCoder-arc074_a]`  
**Category File**: [`../categories/basics/three_way_grid_partition_casework.md`](../categories/basics/three_way_grid_partition_casework.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Complete Search`  
- **Topic (Skill)**: `3-Way Grid Rectangular Partitioning Casework`  

---

## 1. Problem Statement & Key Idea
Divide an H x W grid into 3 non-empty rectangles using at most 2 straight cuts. Minimize the difference between the maximum and minimum area among the 3 rectangles.

**Key Idea**: The cuts can divide the grid into: (1) 3 vertical strips; (2) 3 horizontal strips; (3) 1 vertical strip and 2 horizontal strips; (4) 1 horizontal strip and 2 vertical strips.

## 2. Core Observation & Invariant
If H % 3 == 0 or W % 3 == 0, the difference is 0. Otherwise, iterate over all possible cut positions for the first piece (length 1 to H-1 or 1 to W-1). For the remaining rectangle, dividing it in half as equally as possible gives optimal sub-rectangles.

## 3. Step-by-Step Algorithm
1. If H % 3 == 0 or W % 3 == 0, output 0.
2. Function eval(H, W): iterate h from 1 to H - 1. Piece 1 has area h * W. Case A: remaining (H - h) x W is cut horizontally -> h1 = (H - h)/2, h2 = (H - h) - h1. Case B: remaining is cut vertically -> w1 = W/2, w2 = W - w1. Compute min max-min difference.
3. Run min(eval(H, W), eval(W, H)) and output.

## 4. Complexity Analysis
- **Time Complexity**: `O(H + W)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

long long solve(long long h, long long w) {
    if (h % 3 == 0 || w % 3 == 0) return 0;

    long long min_diff = h * w;

    // Horizontal first cut at height i
    for (long long i = 1; i < h; ++i) {
        long long s1 = i * w;

        // Subcase 1: remaining (h - i) x w split horizontally
        long long rem_h = h - i;
        long long s2a = (rem_h / 2) * w;
        long long s3a = (rem_h - rem_h / 2) * w;
        long long diff_a = max({s1, s2a, s3a}) - min({s1, s2a, s3a});
        min_diff = min(min_diff, diff_a);

        // Subcase 2: remaining (h - i) x w split vertically
        long long s2b = rem_h * (w / 2);
        long long s3b = rem_h * (w - w / 2);
        long long diff_b = max({s1, s2b, s3b}) - min({s1, s2b, s3b});
        min_diff = min(min_diff, diff_b);
    }

    return min_diff;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long h, w;
    if (!(cin >> h >> w)) return 0;

    cout << min(solve(h, w), solve(w, h)) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Exhaustive casework on geometric rectangle dissections.
- **Reusable Pattern**: `T-cut vs parallel cuts: iterate first cut coordinate, split remainder in half.`
