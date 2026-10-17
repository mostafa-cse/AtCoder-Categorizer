# Problem Analysis: AtCoder-abc131_f — Must Be Rectangular!

**Problem ID**: `AtCoder-abc131_f`  
**Contest**: `abc131`  
**Rating / Difficulty**: 1937  
**URL**: https://atcoder.jp/contests/abc131/tasks/abc131_f  
**VJudge Tag**: `[problem:AtCoder-abc131_f]`  
**Category File**: [`../categories/graph_theory/bipartite_component_grid_rectangulation.md`](../categories/graph_theory/bipartite_component_grid_rectangulation.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Connected Components / Bipartite Graphs`  
- **Topic (Skill)**: `Bipartite Component Product Transformation for 2D Grid Point Rectangulation`  

---

## 1. Problem Statement & Key Idea
Given N points (x_i, y_i) in 2D plane. If points exist at (x_1, y_1), (x_1, y_2), (x_2, y_1), you can add (x_2, y_2). Find maximum number of added points.

Model 2D points as edges in a bipartite graph between X coordinates and Y coordinates. The operation states: if edges (x_1, y_1), (x_1, y_2), (x_2, y_1) exist, add (x_2, y_2). This means any X and Y in the same connected component can eventually be connected! Each connected component becomes a complete bipartite graph K_{|X_c|, |Y_c|}. The maximum total points is sum_{c} (|X_c| * |Y_c|), and the number of added points is this sum minus N.

## 2. Core Observation & Invariant
Transitive closure on grid coordinates creates complete bipartite graphs on each connected component.

## 3. Step-by-Step Algorithm
1. Use Disjoint Set Union (DSU) with 2 * MAX vertices (X in 1..MAX, Y in MAX+1..2*MAX).
2. For each point (x, y), union x and y + MAX.
3. Track the count of X vertices and Y vertices in each DSU root.
4. Total possible points = sum_{roots} (size_x[r] * size_y[r]).
5. Output total_possible - N.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * alpha(MAX))`
- **Space Complexity**: `O(MAX)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 100001;

int parent_arr[2 * MAX];
long long size_x[2 * MAX];
long long size_y[2 * MAX];

int find_set(int v) {
    if (v == parent_arr[v]) return v;
    return parent_arr[v] = find_set(parent_arr[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        parent_arr[b] = a;
        size_x[a] += size_x[b];
        size_y[a] += size_y[b];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < 2 * MAX; ++i) {
        parent_arr[i] = i;
        if (i < MAX) size_x[i] = 1;
        else size_y[i] = 1;
    }

    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        union_sets(x, y + MAX);
    }

    long long max_points = 0;
    for (int i = 0; i < 2 * MAX; ++i) {
        if (parent_arr[i] == i) {
            max_points += size_x[i] * size_y[i];
        }
    }

    long long added = max_points - n;
    cout << added << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bipartite graph modeling of 2D coordinates with complete component product evaluation.
- **Reusable Pattern**: `Grid Point Rectangulation: Model (x, y) as bipartite edge; max edges = sum(X_c * Y_c).`
