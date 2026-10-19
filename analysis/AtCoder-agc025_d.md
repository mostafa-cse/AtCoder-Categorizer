# Problem Analysis: AtCoder-agc025_d — D - Choosing Points

**Problem ID**: `AtCoder-agc025_d`  
**Contest**: `agc025`  
**Rating / Difficulty**: 2868  
**URL**: https://atcoder.jp/contests/agc025/tasks/agc025_d  
**VJudge Tag**: `[problem:AtCoder-agc025_d]`  
**Category File**: [`../categories/basics/lattice_distance_graph_bipartite_four_coloring.md`](../categories/basics/lattice_distance_graph_bipartite_four_coloring.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Pigeonhole Principle`  

---

## 1. Problem Statement & Key Idea
Given N and constants D_1, D_2, choose N^2 points from the 2N x 2N grid of lattice points [0, 2N-1]^2 such that no two chosen points have Euclidean distance sqrt(D_1) or sqrt(D_2).

## 2. Core Observation & Invariant
Any distance sqrt(D) graph on the integer lattice Z^2 is bipartite! Factoring D = 4^k D' where D' not equiv 0 mod 4: if D' equiv 1, 3 mod 4, a 2-coloring is ((x >> k) + (y >> k)) mod 2; if D' equiv 2 mod 4, a 2-coloring is (x >> k) mod 2. Combining the 2-colorings for D_1 and D_2 produces a 4-coloring of the 4N^2 points. By the Pigeonhole Principle, at least one color class contains >= N^2 points, and every color class is an independent set in both graphs.

## 3. Step-by-Step Algorithm
1. 1. For each point (x, y) in [0, 2N-1]^2, compute its bipartite color c_1 in {0, 1} for D_1 and c_2 in {0, 1} for D_2.
2. 2. Assign point (x, y) to bucket c = 2 c_1 + c_2 in {0, 1, 2, 3}.
3. 3. Select any bucket with size >= N^2.
4. 4. Output the first N^2 points from that bucket.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int get_color(int x, int y, int D) {
    int k = 0;
    while (D % 4 == 0) {
        D /= 4;
        k++;
    }
    if (D % 4 == 2) {
        return (x >> k) & 1;
    } else {
        return ((x >> k) + (y >> k)) & 1;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, D1, D2;
    if (!(cin >> N >> D1 >> D2)) return 0;

    vector<pair<int, int>> buckets[4];
    for (int x = 0; x < 2 * N; ++x) {
        for (int y = 0; y < 2 * N; ++y) {
            int c1 = get_color(x, y, D1);
            int c2 = get_color(x, y, D2);
            int c = (c1 << 1) | c2;
            buckets[c].push_back({x, y});
        }
    }

    int target = N * N;
    for (int c = 0; c < 4; ++c) {
        if ((int)buckets[c].size() >= target) {
            for (int i = 0; i < target; ++i) {
                cout << buckets[c][i].first << " " << buckets[c][i].second << "\n";
            }
            break;
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
