# Problem Analysis: AtCoder-abc369_g — As far as possible

**Problem ID**: `AtCoder-abc369_g`  
**Contest**: `abc369`  
**Rating / Difficulty**: 2055  
**URL**: https://atcoder.jp/contests/abc369/tasks/abc369_g  
**VJudge Tag**: `[problem:AtCoder-abc369_g]`  
**Category File**: [`../categories/graph_theory/tree_longest_path_decomposition_greedy.md`](../categories/graph_theory/tree_longest_path_decomposition_greedy.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Tree Longest Path Decomposition and Greedy Subtree Weight`  

---

## 1. Problem Statement & Key Idea
Given a tree with N weighted edges. For each K = 1, 2, ..., N: Aoki chooses K vertices to maximize the minimum length of a walk starting and ending at vertex 1 that visits all chosen vertices. Takahashi seeks to minimize the walk. Find the optimal score for each K.

**Key Idea**: The shortest walk visiting a set S of vertices and starting/ending at 1 traverses every edge in the minimal subtree spanning S U {1} exactly twice. To maximize this subtree weight by picking K vertices, we root the tree at 1 and decompose the tree into disjoint paths by iteratively choosing the deepest child (heavy-light style longest-path decomposition). By submodularity of subtree edge weights, the optimal selection for any K is greedily formed by the sum of lengths of the top K paths in this longest-path decomposition.

## 2. Core Observation & Invariant
Max-weight subtree spanning root and K vertices reduces to greedily selecting the K longest branches in a heavy-child path decomposition.

## 3. Step-by-Step Algorithm
1. Root tree at 1. Compute max_d[u] = maximum distance from u to a leaf in its subtree via DFS.
2. Mark heavy[u] as the child achieving max_d[u].
3. Perform a second DFS decomposing the tree into disjoint paths: heavy edges extend the current path, while light edges start new paths.
4. Collect all path lengths and sort them in descending order.
5. For each K = 1 to N, output 2 * (prefix sum of top min(K, num_paths) path lengths).

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Greedy polymatroid tree optimization via heavy-path / deepest-leaf path decomposition.

**Reusable Pattern**: Top-K subtree coverage maximization on trees is solved via disjoint longest-path decomposition.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<long long> max_d(n + 1, 0);
    vector<int> heavy(n + 1, 0);

    auto dfs1 = [&](auto& self, int u, int p) -> void {
        for (auto& e : adj[u]) {
            if (e.to == p) continue;
            self(self, e.to, u);
            if (max_d[e.to] + e.w > max_d[u]) {
                max_d[u] = max_d[e.to] + e.w;
                heavy[u] = e.to;
            }
        }
    };
    dfs1(dfs1, 1, 0);

    vector<long long> paths;
    auto dfs2 = [&](auto& self, int u, int p, long long cur_len) -> void {
        if (heavy[u] != 0) {
            long long w = 0;
            for (auto& e : adj[u]) {
                if (e.to == heavy[u]) {
                    w = e.w;
                    break;
                }
            }
            self(self, heavy[u], u, cur_len + w);
        } else {
            paths.push_back(cur_len);
        }
        for (auto& e : adj[u]) {
            if (e.to == p || e.to == heavy[u]) continue;
            self(self, e.to, u, e.w);
        }
    };
    dfs2(dfs2, 1, 0, 0);

    sort(paths.rbegin(), paths.rend());

    long long current_sum = 0;
    int num_paths = paths.size();
    for (int k = 1; k <= n; ++k) {
        if (k - 1 < num_paths) {
            current_sum += paths[k - 1];
        }
        cout << current_sum * 2 << "\n";
    }
    return 0;
}
```
