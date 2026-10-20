# Problem Analysis: AtCoder-arc097_d — F. Monochrome Cat

**Problem ID**: `AtCoder-arc097_d`  
**Contest**: `arc097`  
**Rating / Difficulty**: 2948  
**URL**: https://atcoder.jp/contests/arc097/tasks/arc097_d  
**VJudge Tag**: `[problem:AtCoder-arc097_d]`  
**Category File**: [`../categories/graph_theory/monochrome_tree_parity_traversal_diameter_dp.md`](../categories/graph_theory/monochrome_tree_parity_traversal_diameter_dp.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Euler Tour Technique`  

---

## 1. Problem Statement & Key Idea
Given a black/white colored tree, a cat moves between adjacent vertices (flipping destination) or flips current vertex. Find minimum seconds to make all vertices black starting and ending anywhere.

## 2. Core Observation & Invariant
Prune all black leaves repeatedly until all leaves are white. In a closed Euler tour of the pruned tree with E edges, each edge is traversed twice and each vertex v is flipped deg(v) times. A vertex ending white requires 1 extra flip. An open walk from S to T traverses the simple path P once instead of twice, reducing edge traversals by 1 per edge and flips by 1 for all vertices along the path except T. Setting vertex weight to 2 if (col[v] + deg(v)) is odd and 0 if even, the savings from choosing path P equals the sum of vertex weights on P. Maximizing savings reduces to finding the weighted tree diameter!

## 3. Step-by-Step Algorithm
1. 1. Prune black leaves via BFS queue.
2. 2. Compute degrees in pruned tree and edge count E.
3. 3. Assign weight 2 to vertices with (col[v] + deg[v]) odd, 0 otherwise.
4. 4. Base cost = 2E + sum [odd].
5. 5. Find maximum weight simple path via tree DP.
6. 6. Answer is base cost minus maximum path weight.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> deg(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    string colors;
    cin >> colors;

    int white_count = 0;
    for (char c : colors) {
        if (c == 'W') white_count++;
    }

    if (white_count == 0) {
        cout << 0 << "\n";
        return 0;
    }
    if (white_count == 1) {
        cout << 1 << "\n";
        return 0;
    }

    queue<int> q;
    vector<bool> alive(n + 1, true);

    for (int i = 1; i <= n; ++i) {
        if (deg[i] <= 1 && colors[i - 1] == 'B') {
            alive[i] = false;
            q.push(i);
        }
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (alive[v]) {
                deg[v]--;
                if (deg[v] <= 1 && colors[v - 1] == 'B') {
                    alive[v] = false;
                    q.push(v);
                }
            }
        }
    }

    vector<int> rem_nodes;
    for (int i = 1; i <= n; ++i) {
        if (alive[i]) rem_nodes.push_back(i);
    }

    if (rem_nodes.size() <= 1) {
        cout << (white_count > 0 ? 1 : 0) << "\n";
        return 0;
    }

    vector<int> p_deg(n + 1, 0);
    int e_count = 0;
    for (int u : rem_nodes) {
        for (int v : adj[u]) {
            if (alive[v] && u < v) {
                e_count++;
                p_deg[u]++;
                p_deg[v]++;
            }
        }
    }

    vector<int> weight(n + 1, 0);
    int base_sum = 0;
    for (int u : rem_nodes) {
        int c = (colors[u - 1] == 'W' ? 1 : 0);
        if ((c + p_deg[u]) % 2 == 1) {
            weight[u] = 2;
            base_sum++;
        } else {
            weight[u] = 0;
        }
    }

    int base_total = 2 * e_count + base_sum;

    int root = rem_nodes[0];
    vector<int> order;
    order.reserve(rem_nodes.size());
    vector<int> parent(n + 1, 0);
    vector<int> st;
    st.push_back(root);
    vector<bool> vis(n + 1, false);
    vis[root] = true;

    while (!st.empty()) {
        int u = st.back();
        st.pop_back();
        order.push_back(u);
        for (int v : adj[u]) {
            if (alive[v] && !vis[v]) {
                vis[v] = true;
                parent[v] = u;
                st.push_back(v);
            }
        }
    }

    vector<int> d1(n + 1, 0);
    int max_path = 0;

    for (int i = (int)order.size() - 1; i >= 0; --i) {
        int u = order[i];
        int top1 = 0, top2 = 0;
        for (int v : adj[u]) {
            if (alive[v] && v != parent[u]) {
                int val = d1[v];
                if (val > top1) {
                    top2 = top1;
                    top1 = val;
                } else if (val > top2) {
                    top2 = val;
                }
            }
        }
        d1[u] = weight[u] + top1;
        int path_u = weight[u] + top1 + top2;
        if (path_u > max_path) {
            max_path = path_u;
        }
    }

    int ans = base_total - max_path;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
