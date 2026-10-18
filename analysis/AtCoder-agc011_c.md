# Problem Analysis: AtCoder-agc011_c — C. Squared Graph

**Problem ID**: `AtCoder-agc011_c`  
**Contest**: `agc011`  
**Rating / Difficulty**: 2355  
**URL**: https://atcoder.jp/contests/agc011/tasks/agc011_c  
**VJudge Tag**: `[problem:AtCoder-agc011_c]`  
**Category File**: [`../categories/graph_theory/tensor_product_bipartite_components.md`](../categories/graph_theory/tensor_product_bipartite_components.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Depth First Search (DFS)`  

---

## 1. Problem Statement & Key Idea
Count connected components in the tensor product graph $G \times G$. Isolated vertices yield $I(2N - I)$ components; bipartite component pairs produce 2 components each, while any pair containing a non-bipartite component forms 1 component, evaluated via DFS in $O(N + M)$.

## 2. Core Observation & Invariant
In the tensor product graph $G \times G$, pairs $(a, b)$ with an isolated vertex in $G$ form isolated vertices in $G \times G$, yielding $I(2N - I)$ components. For non-isolated connected components $C_i, C_j$: if both are bipartite, $C_i \times C_j$ splits into 2 connected components (preserving color parity agreement/disagreement); if at least one is non-bipartite, $C_i \times C_j$ forms exactly 1 connected component because odd cycles allow arbitrary walk length parities.

## 3. Step-by-Step Algorithm
1. Traverse $G$ via DFS to classify all connected components into isolated vertices ($I$), bipartite components ($B$), and non-bipartite components ($N_{non}$).
2. Count tensor product components via formula: $I(2N - I) + (B + N_{non})^2 + B^2$.
3. Evaluated in $O(N + M)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    vector<int> color(n + 1, -1);
    long long iso = 0, bip = 0, non_bip = 0;

    for (int i = 1; i <= n; i++) {
        if (color[i] != -1) continue;
        if (g[i].empty()) {
            iso++;
            continue;
        }
        bool is_bip = true;
        queue<int> q;
        color[i] = 0;
        q.push(i);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : g[u]) {
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    q.push(v);
                } else if (color[v] == color[u]) {
                    is_bip = false;
                }
            }
        }
        if (is_bip) bip++;
        else non_bip++;
    }

    long long ans = iso * (2LL * n - iso) + (bip + non_bip) * (bip + non_bip) + bip * bip;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
