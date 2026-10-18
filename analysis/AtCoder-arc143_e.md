# Problem Analysis: AtCoder-arc143_e — E. Reversi

**Problem ID**: `AtCoder-arc143_e`  
**Contest**: `arc143`  
**Rating / Difficulty**: 2521  
**URL**: https://atcoder.jp/contests/arc143/tasks/arc143_e  
**VJudge Tag**: `[problem:AtCoder-arc143_e]`  
**Category File**: [`../categories/graph_theory/reversi_tree_parity_topological_sort.md`](../categories/graph_theory/reversi_tree_parity_topological_sort.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Topological Sorting`  

---

## 1. Problem Statement & Key Idea
Given a tree of $N$ vertices with black/white pieces, repeatedly select a white piece, remove it, and flip all adjacent pieces. Find the lexicographically smallest removal sequence of all $N$ vertices, or determine if impossible. A vertex $v$ receives flips from all neighbors removed before $v$. Hence, the parity of the number of neighbors removed before $v$ must match its initial color requirement: if initially white ('W'), it needs an even number of flips to remain white when removed; if black ('B'), it needs an odd number of flips.

## 2. Core Observation & Invariant
In a tree, every edge $(u, v)$ must be directed either $u \to v$ ($u$ removed before $v$) or $v \to u$ ($v$ removed before $u$). The required in-degree parity at every vertex uniquely determines the direction of all $N - 1$ tree edges! Root the tree arbitrarily and orient edges bottom-up from leaves to root. If the root's required parity matches its final in-degree, a valid DAG exists; otherwise, no valid sequence exists (output -1). Kahn's algorithm with a min-priority queue finds the lexicographically first topological sort.

## 3. Step-by-Step Algorithm
1. 1. Build adjacency list of the tree.
2. 2. Root the tree at vertex 1 and perform post-order DFS:
3.    - For each child $c$ of $u$, if $c$ needs an odd flip to satisfy its parity, edge must be $u \to c$; else $c \to u$.
4.    - Adjust parent $u$'s parity flip requirement accordingly.
5. 3. Check if root vertex 1's required parity is met. If not, output -1.
6. 4. Build directed graph from oriented edges, compute in-degrees.
7. 5. Insert all vertices with in-degree 0 into `std::priority_queue<int, vector<int>, greater<int>>`.
8. 6. Repeatedly extract the minimum vertex, append to order, decrement neighbor in-degrees, and push newly zero-in-degree neighbors.
9. 7. If order length is $N$, output sequence; else output -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    string s;
    cin >> s;

    vector<int> parent(n + 1, 0);
    vector<int> order;
    order.reserve(n);
    vector<int> q;
    q.reserve(n);
    vector<bool> visited(n + 1, false);

    q.push_back(1);
    visited[1] = true;

    for (size_t i = 0; i < q.size(); ++i) {
        int u = q[i];
        order.push_back(u);
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                parent[v] = u;
                q.push_back(v);
            }
        }
    }

    vector<int> in_from_children(n + 1, 0);

    for (int i = n - 1; i >= 1; --i) {
        int u = order[i];
        int needed_parity = (s[u - 1] == 'W' ? 0 : 1);
        int current_parity = in_from_children[u] % 2;
        int p = parent[u];
        if (current_parity == needed_parity) {
            // edge u -> p
            in_from_children[p]++;
        } else {
            // edge p -> u
            // u does not contribute to p's incoming count
        }
    }

    int root_needed = (s[0] == 'W' ? 0 : 1);
    if (in_from_children[1] % 2 != root_needed) {
        cout << -1 << "\n";
        return 0;
    }

    vector<vector<int>> dag(n + 1);
    vector<int> in_degree(n + 1, 0);

    for (int i = 1; i < n; ++i) {
        int u = order[i];
        int p = parent[u];
        int needed_parity = (s[u - 1] == 'W' ? 0 : 1);
        int current_parity = in_from_children[u] % 2;
        if (current_parity == needed_parity) {
            // u -> p
            dag[u].push_back(p);
            in_degree[p]++;
        } else {
            // p -> u
            dag[p].push_back(u);
            in_degree[u]++;
        }
    }

    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 1; i <= n; ++i) {
        if (in_degree[i] == 0) {
            pq.push(i);
        }
    }

    vector<int> res;
    res.reserve(n);

    while (!pq.empty()) {
        int u = pq.top();
        pq.pop();
        res.push_back(u);
        for (int v : dag[u]) {
            in_degree[v]--;
            if (in_degree[v] == 0) {
                pq.push(v);
            }
        }
    }

    if ((int)res.size() < n) {
        cout << -1 << "\n";
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        cout << res[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
