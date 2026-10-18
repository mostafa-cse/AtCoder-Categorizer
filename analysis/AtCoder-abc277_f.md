# Problem Analysis: AtCoder-abc277_f — F. Sorting a Matrix

**Problem ID**: `AtCoder-abc277_f`  
**Contest**: `abc277`  
**Rating / Difficulty**: 2400  
**URL**: https://atcoder.jp/contests/abc277/tasks/abc277_f  
**VJudge Tag**: `[problem:AtCoder-abc277_f]`  
**Category File**: [`../categories/graph_theory/matrix_row_column_sort_dummy_node_topological_sort.md`](../categories/graph_theory/matrix_row_column_sort_dummy_node_topological_sort.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Topological Sorting`  

---

## 1. Problem Statement & Key Idea
Columns must satisfy precedence constraints from every row simultaneously. Inserting dummy nodes between consecutive value groups prevents O(W^2) edge explosion. A valid sort exists iff the column constraint graph is a DAG and row value intervals do not overlap, solved in O(H W log W) time.

## 2. Core Observation & Invariant
A matrix can be sorted in row-major order iff (1) there exists a global column permutation making every row's non-zero elements non-decreasing, and (2) the intervals [min_i, max_i] of non-zero elements across rows can be ordered non-overlappingly. Column precedence constraints are modeled as directed edges between column groups via dummy nodes; a valid column permutation exists iff this graph is a DAG (acyclic).

## 3. Step-by-Step Algorithm
1. For each row, group column indices by non-zero value and sort unique values v_1 < v_2 < ... < v_k.
2. For each adjacent pair (v_p, v_{p+1}), create a dummy vertex with incoming edges from cols(v_p) and outgoing edges to cols(v_{p+1}).
3. Run Kahn's topological sort on the resulting graph; if a cycle exists, output 'No'.
4. For each row, find interval [min_i, max_i] of non-zero elements. Sort intervals by min_i; if any consecutive intervals overlap (max_i > min_{i+1}), output 'No'; otherwise 'Yes'.

## 4. Complexity Analysis
- **Time Complexity**: `O(H W \log W)`
- **Space Complexity**: `O(H W)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int H, W;
    if (!(cin >> H >> W)) return 0;
    vector<vector<int>> A(H, vector<int>(W));
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) cin >> A[i][j];
    }

    int num_nodes = W;
    vector<vector<int>> adj(W);
    vector<int> in_degree(W, 0);

    for (int r = 0; r < H; r++) {
        map<int, vector<int>> val_cols;
        for (int c = 0; c < W; c++) {
            if (A[r][c] > 0) val_cols[A[r][c]].push_back(c);
        }
        if (val_cols.size() <= 1) continue;

        auto it = val_cols.begin();
        for (size_t p = 0; p < val_cols.size() - 1; p++) {
            auto next_it = next(it);
            int dummy = num_nodes++;
            adj.emplace_back();
            in_degree.push_back(0);

            for (int c : it->second) {
                adj[c].push_back(dummy);
                in_degree[dummy]++;
            }
            for (int c : next_it->second) {
                adj[dummy].push_back(c);
                in_degree[c]++;
            }
            it = next_it;
        }
    }

    queue<int> q;
    for (int u = 0; u < num_nodes; u++) {
        if (in_degree[u] == 0) q.push(u);
    }

    int visited = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        visited++;
        for (int v : adj[u]) {
            if (--in_degree[v] == 0) q.push(v);
        }
    }

    if (visited < num_nodes) {
        cout << "No\n";
        return 0;
    }

    vector<pair<int, int>> intervals;
    for (int r = 0; r < H; r++) {
        int mn = 1e9, mx = -1;
        for (int c = 0; c < W; c++) {
            if (A[r][c] > 0) {
                mn = min(mn, A[r][c]);
                mx = max(mx, A[r][c]);
            }
        }
        if (mx != -1) intervals.push_back({mn, mx});
    }

    sort(intervals.begin(), intervals.end());
    for (size_t i = 0; i + 1 < intervals.size(); i++) {
        if (intervals[i].second > intervals[i + 1].first) {
            cout << "No\n";
            return 0;
        }
    }

    cout << "Yes\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
