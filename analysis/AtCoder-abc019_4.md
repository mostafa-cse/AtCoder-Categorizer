# Problem Analysis: AtCoder-abc019_4 — Takahashi and Tree

**Problem ID**: `AtCoder-abc019_4`  
**Contest**: `abc019`  
**Rating / Difficulty**: 1378  
**URL**: https://atcoder.jp/contests/abc019/tasks/abc019_4  
**VJudge Tag**: `[problem:AtCoder-abc019_4]`  
**Category File**: [`../categories/graph_theory/interactive_tree_diameter_2pass.md`](../categories/graph_theory/interactive_tree_diameter_2pass.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Tree Diameter`  
- **Topic (Skill)**: `Interactive Tree Diameter via 2-Query BFS/DFS`  

---

## 1. Problem Statement & Key Idea
An unweighted tree with N vertices (N <= 50). You can ask at most 2N distance queries '? u v' to get the distance between u and v. Find the diameter of the tree.

**Key Idea**: The diameter of any tree can be found in 2 passes: (1) pick arbitrary vertex 1, find farthest vertex u; (2) from u, find farthest vertex v. Distance dist(u, v) is the exact diameter!

## 2. Core Observation & Invariant
Pass 1: ask '? 1 i' for all i in 2..N (N - 1 queries). Let u be the vertex maximizing dist(1, u). Pass 2: ask '? u i' for all i != u (N - 1 queries). The maximum distance found is the exact diameter of the tree! Total queries: 2N - 2 <= 2N.

## 3. Step-by-Step Algorithm
1. For i from 2 to N: query '? 1 i' and find vertex u with maximum distance.
2. For i from 1 to N (i != u): query '? u i' and find maximum distance D.
3. Print '! D' and flush output.

## 4. Complexity Analysis
- **Time Complexity**: `O(N) queries`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int farthest_node = 1;
    long long max_d1 = -1;

    for (int i = 2; i <= n; ++i) {
        cout << "? 1 " << i << endl;
        long long dist;
        cin >> dist;
        if (dist > max_d1) {
            max_d1 = dist;
            farthest_node = i;
        }
    }

    long long diameter = 0;
    for (int i = 1; i <= n; ++i) {
        if (i == farthest_node) continue;
        cout << "? " << farthest_node << " " << i << endl;
        long long dist;
        cin >> dist;
        diameter = max(diameter, dist);
    }

    cout << "! " << diameter << endl;
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Double sweep tree diameter determination in an interactive query model.
- **Reusable Pattern**: `Tree diameter in 2 passes: find farthest from 1 -> u; find farthest from u -> diameter.`
