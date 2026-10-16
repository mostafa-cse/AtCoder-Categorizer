# Problem Analysis: AtCoder-abc165_e — Rotation Matching

**Problem ID**: `AtCoder-abc165_e`  
**Contest**: `abc165`  
**Rating / Difficulty**: 1620  
**URL**: https://atcoder.jp/contests/abc165/tasks/abc165_e  
**VJudge Tag**: `[problem:AtCoder-abc165_e]`  
**Category File**: [`../categories/basics/circular_rotation_matching_parity.md`](../categories/basics/circular_rotation_matching_parity.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Constructive Algorithms`  
- **Topic (Skill)**: `Constructive Distance Parity Partitioning on Circular Cycle`  

---

## 1. Problem Statement & Key Idea
N players are seated around a circular table. In each round, M pairs of players play simultaneously. Construct M pairs such that no two pairs ever play each other more than once under all possible circular rotations.

**Key Insight**: The distance between two players u and v along the circle must take M distinct values from 1 to M. To prevent chords with the same distance from ever colliding under rotation, partition the distances into odd and even sets with distinct endpoint sum parities.

## 2. Core Observation & Invariant
Divide the M matches into two groups centered at different points: Group 1 takes pairs (l, r) where (l + r) is odd, generating distances M, M-2, M-4... Group 2 takes pairs where (l + r) is even, generating distances M-1, M-3, M-5... Because endpoint sum parities never collide, all rotations are disjoint.

## 3. Step-by-Step Algorithm
1. Construct Group 1: l = 1, r = M + 1; while l < r: add pair (l, r), l++, r--.
2. Construct Group 2: l = M + 2, r = 2 * M + 1; while l < r: add pair (l, r), l++, r--.
3. Print the M pairs.

## 4. Complexity Analysis
- **Time Complexity**: `O(M)`
- **Space Complexity**: `O(M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<pair<int, int>> ans;

    // Group 1
    int l1 = 1, r1 = m + 1;
    while (l1 < r1) {
        ans.push_back({l1, r1});
        l1++;
        r1--;
    }

    // Group 2
    int l2 = m + 2, r2 = 2 * m + 1;
    while (l2 < r2) {
        ans.push_back({l2, r2});
        l2++;
        r2--;
    }

    for (const auto& p : ans) {
        cout << p.first << " " << p.second << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Rotational collision avoidance via parity-shifted chord grouping.
- **Reusable Pattern**: `Circular Distinct Distances: split into two mirror envelopes to avoid rotational chord clashes.`
