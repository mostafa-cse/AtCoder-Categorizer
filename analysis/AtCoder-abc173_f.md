# Problem Analysis: AtCoder-abc173_f — Intervals on Tree

**Problem ID**: `AtCoder-abc173_f`  
**Contest**: `abc173`  
**Rating / Difficulty**: 1892  
**URL**: https://atcoder.jp/contests/abc173/tasks/abc173_f  
**VJudge Tag**: `[problem:AtCoder-abc173_f]`  
**Category File**: [`../categories/combinatorics/forest_components_euler_contribution.md`](../categories/combinatorics/forest_components_euler_contribution.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Linearity of Expectation`  
- **Topic (Skill)**: `Forest Connected Components Identity (C = V - E) via Contribution to Sum`  

---

## 1. Problem Statement & Key Idea
Given a tree of N vertices labeled 1..N. For each pair 1 <= L <= R <= N, let C(L, R) be the number of connected components in the subgraph induced by vertices {L, L + 1, ..., R}. Find the sum of C(L, R) over all L <= R.

**Key Insight**: Any induced subgraph of a tree is an acyclic graph (a forest). For every forest, Connected Components = Vertices - Edges. Thus, sum C(L, R) = sum V(L, R) - sum E(L, R).

## 2. Core Observation & Invariant
By contribution to sum: Vertex v belongs to all [L, R] with 1 <= L <= v <= R <= N, which is v * (N - v + 1) intervals. Edge (u, v) with u < v belongs to all [L, R] with 1 <= L <= u < v <= R <= N, which is u * (N - v + 1) intervals.

## 3. Step-by-Step Algorithm
1. total_V = sum_{v=1}^N (v * (N - v + 1)).
2. total_E = sum_{(u, v) in E, u < v} (u * (N - v + 1)).
3. ans = total_V - total_E.
4. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long total_v = 0;
    for (long long v = 1; v <= n; ++v) {
        total_v += v * (n - v + 1);
    }

    long long total_e = 0;
    for (int i = 0; i < n - 1; ++i) {
        long long u, v;
        cin >> u >> v;
        if (u > v) swap(u, v);
        total_e += u * (n - v + 1);
    }

    cout << total_v - total_e << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Using the topological invariant C = V - E on tree subgraphs to compute component sums in linear time.
- **Reusable Pattern**: `Forest Connected Components Sum: ans = sum v*(N-v+1) - sum u*(N-v+1).`
