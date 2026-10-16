# Problem Analysis: AtCoder-abc089_d — Practical Skill Test

**Problem ID**: `AtCoder-abc089_d`  
**Contest**: `abc089`  
**Rating / Difficulty**: 1220  
**URL**: https://atcoder.jp/contests/abc089/tasks/abc089_d  
**VJudge Tag**: `[problem:AtCoder-abc089_d]`  
**Category File**: [`../categories/data_structures/modulo_d_strided_prefix_sums.md`](../categories/data_structures/modulo_d_strided_prefix_sums.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Prefix Sums`  
- **Topic (Skill)**: `Modulo-D Strided Prefix Sums`  

---

## 1. Problem Statement & Key Idea
An H x W grid contains numbers 1..H*W. You move from number x to x + D at cost equal to Manhattan distance between their coordinates. Answer Q queries: total cost to move from L to R (where R - L is a multiple of D).

**Key Idea**: Numbers x, x + D, x + 2D, ... form independent arithmetic progressions for each remainder class modulo D.

## 2. Core Observation & Invariant
Precompute 1D prefix sums for each modulo class: cost[i] = cost[i - D] + dist(pos[i - D], pos[i]) for all i > D. Then the total cost to move from L to R is simply cost[R] - cost[L] in O(1) per query!

## 3. Step-by-Step Algorithm
1. Store coordinates of each value 1..H*W in pos array.
2. Initialize cost array of size H*W + 1 to 0.
3. For i from D + 1 to H*W: cost[i] = cost[i - D] + abs(pos[i].r - pos[i - D].r) + abs(pos[i].c - pos[i - D].c).
4. For each query (L, R): print cost[R] - cost[L].

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W + Q)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct Coord {
    int r, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, d;
    if (!(cin >> h >> w >> d)) return 0;

    int total_cells = h * w;
    vector<Coord> pos(total_cells + 1);

    for (int r = 1; r <= h; ++r) {
        for (int c = 1; c <= w; ++c) {
            int val;
            cin >> val;
            pos[val] = {r, c};
        }
    }

    vector<long long> cost(total_cells + 1, 0);
    for (int i = d + 1; i <= total_cells; ++i) {
        cost[i] = cost[i - d] + abs(pos[i].r - pos[i - d].r) + abs(pos[i].c - pos[i - d].c);
    }

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << cost[r] - cost[l] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 1D prefix sums partitioned by stride D for range query acceleration.
- **Reusable Pattern**: `Strided prefix sum: cost[i] = cost[i - D] + dist(pos[i - D], pos[i]); query: cost[R] - cost[L].`
