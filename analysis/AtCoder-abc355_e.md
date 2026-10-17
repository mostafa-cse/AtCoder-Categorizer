# Problem Analysis: AtCoder-abc355_e — E. Guess the Sum

**Problem ID**: `AtCoder-abc355_e`  
**Contest**: `abc355`  
**Rating / Difficulty**: 2299  
**URL**: https://atcoder.jp/contests/abc355/tasks/abc355_e  
**VJudge Tag**: `[problem:AtCoder-abc355_e]`  
**Category File**: [`../categories/graph_theory/bfs_shortest_path_binary_interval_query.md`](../categories/graph_theory/bfs_shortest_path_binary_interval_query.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Breadth First Search (BFS)`  

---

## 1. Problem Statement & Key Idea
Given $N, L, R$, find $\sum_{k=L}^R A_k \bmod 100$ in at most 100 interactive queries of the form $(i, j)$ computing $\sum_{k=j \cdot 2^i}^{(j+1)2^i - 1} A_k \bmod 100$.

## 2. Core Observation & Invariant
Each query $(i, j)$ computes the sum over $[j \cdot 2^i, (j+1) \cdot 2^i - 1]$, which is the prefix sum difference $P[(j+1) \cdot 2^i] - P[j \cdot 2^i]$. In the graph with vertices $0, \dots, 2^N$ and undirected edges between $j \cdot 2^i$ and $(j+1) \cdot 2^i$, the minimum query sequence to obtain $P[R+1] - P[L]$ is the shortest path between $L$ and $R+1$ found by BFS.

## 3. Step-by-Step Algorithm
1. 1. The interval sum $\sum_{k=L}^R A_k = P[R + 1] - P[L]$ where $P[x] = \sum_{k=0}^{x-1} A_k$.
2. 2. A query $(i, j)$ gives $P[(j + 1)2^i] - P[j 2^i]$.
3. 3. View $0, 1, \dots, 2^N$ as vertices of an unweighted undirected graph. An available query $(i, j)$ connects vertex $u = j 2^i$ and vertex $v = (j + 1)2^i$ with an edge of weight 1.
4. 4. We need to express $P[R + 1] - P[L]$ using the minimum number of queries. This is precisely finding the shortest path from $L$ to $R + 1$ in this graph!
5. 5. Since the graph has $2^N + 1 \le 2^{18} + 1 \approx 262145$ vertices and each vertex has degree $O(N) = 18$, we run BFS from $L$ to $R + 1$ in $O(N 2^N)$ time.
6. 6. Trace back the shortest path. For each step $(u, v)$:
7.    - If $u < v$: query $(i, j)$ and add the answer modulo 100.
8.    - If $u > v$: query $(i, j)$ and subtract the answer modulo 100.
9. 7. Print `! ans` and terminate.

## 4. Complexity Analysis
- **Time Complexity**: `O(N 2^N)`
- **Space Complexity**: `O(2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    int i, j;
    int sgn; // +1 if moving forward (u < v), -1 if backward
};

int main() {
    int N, L, R;
    if (!(cin >> N >> L >> R)) return 0;

    int max_val = (1 << N);
    vector<int> dist(max_val + 1, -1);
    vector<int> parent_node(max_val + 1, -1);
    vector<pair<int, int>> parent_query(max_val + 1);
    vector<int> parent_sgn(max_val + 1, 0);

    queue<int> q;
    q.push(L);
    dist[L] = 0;

    int target = R + 1;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (u == target) break;

        for (int i = 0; i <= N; ++i) {
            int len = (1 << i);
            if (len > max_val) break;

            // Edge forward: u is j * len
            if (u % len == 0 && u + len <= max_val) {
                int v = u + len;
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent_node[v] = u;
                    parent_query[v] = {i, u / len};
                    parent_sgn[v] = 1;
                    q.push(v);
                }
            }
            // Edge backward: u is (j + 1) * len
            if (u % len == 0 && u - len >= 0) {
                int v = u - len;
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent_node[v] = u;
                    parent_query[v] = {i, v / len};
                    parent_sgn[v] = -1;
                    q.push(v);
                }
            }
        }
    }

    // Reconstruct path from target back to L
    vector<pair<pair<int, int>, int>> ops;
    int curr = target;
    while (curr != L) {
        ops.push_back({parent_query[curr], parent_sgn[curr]});
        curr = parent_node[curr];
    }
    reverse(ops.begin(), ops.end());

    int total_sum = 0;
    for (const auto& op : ops) {
        int i = op.first.first;
        int j = op.first.second;
        int sgn = op.second;

        cout << "? " << i << " " << j << endl;
        int res;
        cin >> res;
        if (res == -1) return 0;

        if (sgn == 1) {
            total_sum = (total_sum + res) % 100;
        } else {
            total_sum = (total_sum - res + 100) % 100;
        }
    }

    cout << "! " << total_sum << endl;
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
