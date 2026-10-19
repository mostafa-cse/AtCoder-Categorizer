# Problem Analysis: AtCoder-agc037_d — Sorting a Grid

**Problem ID**: `AtCoder-agc037_d`  
**Contest**: `agc037`  
**Rating / Difficulty**: 2689  
**URL**: https://atcoder.jp/contests/agc037/tasks/agc037_d  
**VJudge Tag**: `[problem:AtCoder-agc037_d]`  
**Category File**: [`../categories/graph_theory/sorting_a_grid_hall_matching.md`](../categories/graph_theory/sorting_a_grid_hall_matching.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Halls Theorem`  

---

## 1. Problem Statement & Key Idea
Permute an N x M grid in 3 steps into sorted order D_{i, j} = (i - 1)M + j. Step 2 requires each column of B to contain exactly one element destined for each target row 0..N-1. Constructing matrix B column-by-column corresponds to finding M edge-disjoint 1-factors in an M-regular bipartite multigraph, guaranteed to exist by Hall's Marriage Theorem.

## 2. Core Observation & Invariant
Target row of value v is tr(v) = (v - 1) / M. A bipartite graph with current rows on the left and target rows on the right has degree M for every vertex. By Hall's condition, every regular bipartite graph contains a perfect matching. Finding a matching via Kuhn's algorithm assigns one element per row to column col. Repeating M times completely constructs B. Sorting columns of B yields C, and sorting rows of C yields D.

## 3. Step-by-Step Algorithm
1. 1. For each column col = 0..M-1:
2.    - Build bipartite graph: left = current rows, right = target rows.
3.    - Add edge (i, tr) if row i contains an unused number with target row tr.
4.    - Find perfect matching using Kuhn's DFS.
5.    - Assign matched elements to B[i][col].
6. 2. Construct C by sorting each column of B by target row.
7. 3. Output B, then output C.

## 4. Complexity Analysis
- **Time Complexity**: `O(M * N^2)`
- **Space Complexity**: `O(N * M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool dfs(int u, const vector<vector<int>>& adj, vector<int>& match_right, vector<bool>& visited) {
    for (int v : adj[u]) {
        if (!visited[v]) {
            visited[v] = true;
            if (match_right[v] == -1 || dfs(match_right[v], adj, match_right, visited)) {
                match_right[v] = u;
                return true;
            }
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<int>> row_elems(N, vector<int>(M));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> row_elems[i][j];
        }
    }

    vector<vector<int>> B(N, vector<int>(M, 0));

    for (int col = 0; col < M; col++) {
        vector<vector<int>> adj(N);
        for (int i = 0; i < N; i++) {
            vector<bool> has_tr(N, false);
            for (int val : row_elems[i]) {
                int tr = (val - 1) / M;
                if (!has_tr[tr]) {
                    has_tr[tr] = true;
                    adj[i].push_back(tr);
                }
            }
        }

        vector<int> match_right(N, -1);
        for (int i = 0; i < N; i++) {
            vector<bool> visited(N, false);
            dfs(i, adj, match_right, visited);
        }

        for (int tr = 0; tr < N; tr++) {
            int i = match_right[tr];
            // find element in row_elems[i] with target row tr
            for (size_t idx = 0; idx < row_elems[i].size(); idx++) {
                if ((row_elems[i][idx] - 1) / M == tr) {
                    B[i][col] = row_elems[i][idx];
                    row_elems[i].erase(row_elems[i].begin() + idx);
                    break;
                }
            }
        }
    }

    // Build C
    vector<vector<int>> C(N, vector<int>(M, 0));
    for (int j = 0; j < M; j++) {
        vector<int> col_vals(N);
        for (int i = 0; i < N; i++) {
            col_vals[i] = B[i][j];
        }
        sort(col_vals.begin(), col_vals.end(), [&](int a, int b) {
            return (a - 1) / M < (b - 1) / M;
        });
        for (int i = 0; i < N; i++) {
            C[i][j] = col_vals[i];
        }
    }

    // Output B
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << B[i][j] << (j + 1 == M ? "" : " ");
        }
        cout << "\n";
    }

    // Output C
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << C[i][j] << (j + 1 == M ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
