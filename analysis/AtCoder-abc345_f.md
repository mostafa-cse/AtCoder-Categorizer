# Problem Analysis: AtCoder-abc345_f — Many Lamps

**Problem ID**: `AtCoder-abc345_f`  
**Contest**: `abc345`  
**Rating / Difficulty**: 2157  
**URL**: https://atcoder.jp/contests/abc345/tasks/abc345_f  
**VJudge Tag**: `[problem:AtCoder-abc345_f]`  
**Category File**: [`../categories/graph_theory/spanning_tree_leaf_root_parity_toggling.md`](../categories/graph_theory/spanning_tree_leaf_root_parity_toggling.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `DFS Tree`  

---

## 1. Problem Statement & Key Idea
Toggle edge endpoints to turn on exactly K lamps in a graph. Since each operation toggles 2 vertices, the total ON count is always even. On any spanning tree, bottom-up post-order toggling monotonically turns on lamps without ever decreasing the ON count.

## 2. Core Observation & Invariant
If K is odd, impossible (output "No"). In a tree, if child v is OFF and we toggle edge (u, v), v becomes ON. Whether u was ON or OFF, the total ON count changes by +2 or 0; it never decreases. Thus, the ON count increases in steps of 2, hitting every even target K up to the maximum achievable capacity.

## 3. Step-by-Step Algorithm
1. If K % 2 != 0, output "No".
2. Find spanning forest components via DFS.
3. In post-order traversal of the spanning tree: for each child v of u, if v is OFF and curr_on < K, toggle edge (u, v), updating lamp states and recording the operation.
4. If curr_on == K, output "Yes", the operation count, and the sequence of edge indices; otherwise output "No".

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int to;
    int id;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<Edge>> g(n + 1);
    for (int i = 1; i <= m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back({v, i});
        g[v].push_back({u, i});
    }

    if (k % 2 != 0) {
        cout << "No\n";
        return 0;
    }

    vector<bool> visited(n + 1, false);
    vector<int> state(n + 1, 0);
    vector<int> ops;
    int curr_on = 0;

    auto dfs = [&](auto& self, int u) -> void {
        visited[u] = true;
        for (auto& edge : g[u]) {
            int v = edge.to;
            if (visited[v]) continue;
            self(self, v);

            if (curr_on < k && state[v] == 0) {
                ops.push_back(edge.id);
                if (state[v] == 0) curr_on++; else curr_on--;
                state[v] ^= 1;
                if (state[u] == 0) curr_on++; else curr_on--;
                state[u] ^= 1;
            }
        }
    };

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            dfs(dfs, i);
        }
    }

    if (curr_on == k) {
        cout << "Yes\n";
        cout << ops.size() << "\n";
        for (size_t i = 0; i < ops.size(); ++i) {
            cout << ops[i] << (i + 1 == ops.size() ? "" : " ");
        }
        cout << "\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
