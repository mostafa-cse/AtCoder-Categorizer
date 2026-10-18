# Problem Analysis: AtCoder-abc223_g — G. Vertex Deletion

**Problem ID**: `AtCoder-abc223_g`  
**Contest**: `abc223`  
**Rating / Difficulty**: 2351  
**URL**: https://atcoder.jp/contests/abc223/tasks/abc223_g  
**VJudge Tag**: `[problem:AtCoder-abc223_g]`  
**Category File**: [`../categories/graph_theory/rerooting_tree_maximum_matching.md`](../categories/graph_theory/rerooting_tree_maximum_matching.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `More Tree Stuff`  
- **Topic (Skill)**: `Rerooting Technique`  

---

## 1. Problem Statement & Key Idea
Count vertices whose deletion does not decrease the tree's maximum matching size. A vertex can be left unmatched iff all its neighbors are matched in their subtrees when rooted at $u$, solved via 2-pass rerooting DP in $O(N)$.

## 2. Core Observation & Invariant
Deleting vertex $u$ preserves the maximum matching size iff there exists a maximum matching that leaves $u$ unmatched. In a tree, a vertex $u$ can be left unmatched iff, when the tree is rooted at $u$, ALL of its neighbors are matched within their respective subtrees (so $u$ has no unmatched neighbor to greedily match with).

## 3. Step-by-Step Algorithm
1. Define $dp[u \to v] \in \{0, 1\}$ indicating whether $v$ is matched in the component without $u$: $v$ is matched iff $\exists w \in \text{adj}[v] \setminus \{u\}$ with $dp[v \to w] == 0$.
2. Pass 1 (post-order DFS): compute $dp[parent \to child]$ and count unmatched children for all nodes.
3. Pass 2 (pre-order DFS): compute $dp[child \to parent]$ by subtracting child's contribution from parent's unmatched count.
4. A vertex $u$ is valid iff its total count of unmatched neighbors is 0, solved in $O(N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // dp_down[u]: 1 if u is matched in its subtree, 0 if unmatched
    // count_unmatched_down[u]: number of children v of u with dp_down[v] == 0
    vector<int> dp_down(N + 1, 0);
    vector<int> count_unmatched_down(N + 1, 0);

    auto dfs1 = [&](auto& self, int u, int p) -> void {
        for (int v : adj[u]) {
            if (v == p) continue;
            self(self, v, u);
            if (dp_down[v] == 0) {
                count_unmatched_down[u]++;
            }
        }
        dp_down[u] = (count_unmatched_down[u] > 0) ? 1 : 0;
    };

    dfs1(dfs1, 1, 0);

    // dp_up[v]: 1 if parent u is matched in the component without v, 0 if unmatched
    int ans = 0;

    auto dfs2 = [&](auto& self, int u, int p, int dp_up_val) -> void {
        int total_unmatched_neighbors = count_unmatched_down[u];
        if (p != 0 && dp_up_val == 0) {
            total_unmatched_neighbors++;
        }

        if (total_unmatched_neighbors == 0) {
            ans++;
        }

        for (int v : adj[u]) {
            if (v == p) continue;
            // What is the status of u without child v?
            int unmatched_without_v = count_unmatched_down[u];
            if (dp_down[v] == 0) {
                unmatched_without_v--;
            }
            if (p != 0 && dp_up_val == 0) {
                unmatched_without_v++;
            }
            int u_status_for_v = (unmatched_without_v > 0) ? 1 : 0;
            self(self, v, u, u_status_for_v);
        }
    };

    dfs2(dfs2, 1, 0, 0);

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
