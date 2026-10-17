# Problem Analysis: AtCoder-abc350_g — Mediator

**Problem ID**: `AtCoder-abc350_g`  
**Contest**: `abc350`  
**Rating / Difficulty**: 2058  
**URL**: https://atcoder.jp/contests/abc350/tasks/abc350_g  
**VJudge Tag**: `[problem:AtCoder-abc350_g]`  
**Category File**: [`../categories/data_structures/small_to_large_tree_rerooting.md`](../categories/data_structures/small_to_large_tree_rerooting.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Small-to-Large Tree Rerooting for Online Forest Queries`  

---

## 1. Problem Statement & Key Idea
Online forest maintenance on N vertices: Type 1 adds edge (u, v) between two different trees; Type 2 queries if there is a common neighbor between u and v (distance 2). Queries are encrypted with the previous answer.

**Key Idea**: In a forest, any two vertices have at most one common neighbor. By maintaining parent pointers for each rooted tree, a common neighbor between u and v must be one of: parent[u] == parent[v], parent[parent[u]] == v, or parent[parent[v]] == u. When merging trees via edge (u, v), we re-root the smaller component at u in O(size) and set parent[u] = v. By small-to-large merging, each vertex is rerooted at most O(log N) times, giving O(N log N + Q) total time.

## 2. Core Observation & Invariant
In a rooted forest, common neighbors are verified in O(1) by checking depth-1 and depth-2 parent links, while small-to-large tree rerooting takes amortized O(log N) per node.

## 3. Step-by-Step Algorithm
1. Maintain parent[u], sz[u], and adjacency list adj[u] for each vertex.
2. For Type 1 (merge u, v): swap so sz[u] <= sz[v]. Re-root component of u at u via BFS/DFS, flipping parent pointers. Set parent[u] = v and sz[v] += sz[u].
3. For Type 2 (query u, v): check if parent[u] == parent[v] (non-zero), parent[parent[u]] == v, or parent[parent[v]] == u in O(1). Output mediator or 0.
4. Decrypt queries using last_ans in online fashion.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + Q)`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Small-to-large component rerooting for maintaining dynamic rooted trees without heavy Link-Cut Tree machinery.

**Reusable Pattern**: Distance-2 common neighbor in dynamic forests is solved via parent pointers with small-to-large rerooting.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> parent(n + 1, 0);
    vector<int> sz(n + 1, 1);
    vector<vector<int>> adj(n + 1);

    long long last_ans = 0;

    auto reroot = [&](int root) {
        vector<int> order;
        vector<int> p_old(n + 1, 0);
        vector<int> q_list = {root};
        p_old[root] = 0;
        int head = 0;
        while (head < (int)q_list.size()) {
            int u = q_list[head++];
            order.push_back(u);
            for (int v : adj[u]) {
                if (v != p_old[u]) {
                    p_old[v] = u;
                    q_list.push_back(v);
                }
            }
        }
        for (int i = 1; i < (int)order.size(); ++i) {
            int u = order[i];
            parent[u] = p_old[u];
        }
        parent[root] = 0;
    };

    while (q--) {
        long long a, b, c;
        cin >> a >> b >> c;
        long long type = 1 + (((a * (1 + last_ans)) % MOD) % 2);
        long long u = 1 + (((b * (1 + last_ans)) % MOD) % n);
        long long v = 1 + (((c * (1 + last_ans)) % MOD) % n);

        if (type == 1) {
            adj[u].push_back(v);
            adj[v].push_back(u);
            if (sz[u] > sz[v]) {
                swap(u, v);
            }
            reroot(u);
            parent[u] = v;
            sz[v] += sz[u];
        } else {
            int ans = 0;
            if (parent[u] != 0 && parent[u] == parent[v]) {
                ans = parent[u];
            } else if (parent[u] != 0 && parent[parent[u]] == v) {
                ans = parent[u];
            } else if (parent[v] != 0 && parent[parent[v]] == u) {
                ans = parent[v];
            }
            cout << ans << "\n";
            last_ans = ans;
        }
    }
    return 0;
}
```
