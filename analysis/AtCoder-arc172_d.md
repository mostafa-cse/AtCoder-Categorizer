# Problem Analysis: AtCoder-arc172_d — D. Distance Ranking

**Problem ID**: `AtCoder-arc172_d`  
**Contest**: `arc172`  
**Rating / Difficulty**: 2936  
**URL**: https://atcoder.jp/contests/arc172/tasks/arc172_d  
**VJudge Tag**: `[problem:AtCoder-arc172_d]`  
**Category File**: [`../categories/basics/distance_ranking_simplex_basis_perturbation.md`](../categories/basics/distance_ranking_simplex_basis_perturbation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
In N-dimensional space, place N points with integer coordinates in [0, 10^8] such that their pairwise Euclidean distances strictly follow a given ranking order: d(p_{A_1}, p_{B_1}) < d(p_{A_2}, p_{B_2}) < ...

## 2. Core Observation & Invariant
Start from a regular simplex where all pairwise distances are equal to sqrt(2) * L: p_i[i] = L and 0 elsewhere. Perturb the coordinates: for each pair (i, j) with i < j, set p_i[j] = r_{i, j} where r_{i, j} in [1, M] is the rank of (i, j) from farthest to closest. The distance squared between p_i and p_j expands as 2L^2 - 2 L r_{i, j} + O(N M^2). For sufficiently large L (e.g. L = 5 * 10^7), the linear term -2 L r_{i, j} dominates all quadratic error terms, strictly ordering all pairwise distances as desired.

## 3. Step-by-Step Algorithm
1. 1. Let M = N(N-1)/2. Assign rank r_{u, v} = M - k to the k-th pair in the given distance sequence.
2. 2. Set L = 5 * 10^7.
3. 3. Construct coordinates: p_i[i] = L, p_i[j] = r_{i, j} for i < j, and 0 for i > j.
4. 4. Output the N x N matrix of integer coordinates.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    int m = n * (n - 1) / 2;
    vector<pair<int, int>> pairs(m);
    vector<vector<long long>> rank_table(n + 1, vector<long long>(n + 1, 0));

    for (int k = 0; k < m; ++k) {
        int u, v;
        cin >> u >> v;
        if (u > v) swap(u, v);
        pairs[k] = {u, v};
        // k = 0 is closest, k = m - 1 is farthest
        // We want -2 * L * r to be smallest for closest, largest for farthest
        // so r should be largest for k = 0, smallest for k = m - 1
        rank_table[u][v] = m - k;
    }

    long long L = 50000000LL; // 5 * 10^7 <= 10^8
    vector<vector<long long>> p(n, vector<long long>(n, 0));

    for (int i = 0; i < n; ++i) {
        p[i][i] = L;
        for (int j = i + 1; j < n; ++j) {
            p[i][j] = rank_table[i + 1][j + 1];
            p[j][i] = 0;
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << p[i][j] << (j + 1 == n ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
