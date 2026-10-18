# Problem Analysis: AtCoder-abc287_h — Ex - Directed Graph Query

**Problem ID**: `AtCoder-abc287_h`  
**Contest**: `abc287`  
**Rating / Difficulty**: 2639  
**URL**: https://atcoder.jp/contests/abc287/tasks/abc287_h  
**VJudge Tag**: `[problem:AtCoder-abc287_h]`  
**Category File**: [`../categories/graph_theory/directed_graph_query_floyd_warshall.md`](../categories/graph_theory/directed_graph_query_floyd_warshall.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Floyd Warshall`  

---

## 1. Problem Statement & Key Idea
Given a directed graph of N vertices, the cost of a path is the maximum vertex index visited on the path. Answer Q reachability cost queries (s_i, t_i).

## 2. Core Observation & Invariant
The cost of a path is <= X iff there exists a path from s to t using only vertices from {1, 2, ..., X}. By processing vertices X = 1, 2, ..., N in increasing order, the reachable pairs within {1 ... X} can be updated dynamically using bitsets in O(N^2 / 64) per step, recording the minimum X where t becomes reachable from s.

## 3. Step-by-Step Algorithm
1. Maintain a reachability bitset reach[u] for each vertex u in [1, N].
2. Initialize answers ans[s][t] = -1.
3. For X = 1 ... N:
4. Insert vertex X. For all predecessors u of X and successors v of X within {1 ... X}, update reach[u] |= reach[X].
5. For all pairs (s, t) that become reachable at step X, record ans[s][t] = X.
6. For each of the Q queries (s_i, t_i), output ans[s_i][t_i].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 / 64 + Q)`
- **Space Complexity**: `O(N^2 / 64 + Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

const int MAXN = 2005;

bitset<MAXN> reach[MAXN];
bitset<MAXN> in_mask[MAXN];
short ans[MAXN][MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<int>> adj_out(N + 1);

    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        adj_out[u].push_back(v);
        if (v <= N && u <= N) {
            in_mask[v].set(u);
        }
    }

    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            ans[i][j] = -1;
        }
    }

    for (int X = 1; X <= N; ++X) {
        reach[X].set(X);
        for (int v : adj_out[X]) {
            if (v < X) {
                reach[X] |= reach[v];
            }
        }

        bitset<MAXN> current_in = in_mask[X];

        for (int u = 1; u < X; ++u) {
            if ((reach[u] & current_in).any()) {
                bitset<MAXN> new_reach = reach[X] & (~reach[u]);
                for (int v = new_reach._Find_first(); v <= X; v = new_reach._Find_next(v)) {
                    if (ans[u][v] == -1 && u != v) {
                        ans[u][v] = X;
                    }
                }
                reach[u] |= reach[X];
            }
        }

        for (int v = reach[X]._Find_first(); v <= X; v = reach[X]._Find_next(v)) {
            if (ans[X][v] == -1 && X != v) {
                ans[X][v] = X;
            }
        }
    }

    int Q;
    if (cin >> Q) {
        while (Q--) {
            int s, t;
            cin >> s >> t;
            cout << ans[s][t] << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
