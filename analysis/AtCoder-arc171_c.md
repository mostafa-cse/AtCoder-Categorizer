# Problem Analysis: AtCoder-arc171_c — Swap on Tree

**Problem ID**: `AtCoder-arc171_c`  
**Contest**: `arc171`  
**Rating / Difficulty**: 2244  
**URL**: https://atcoder.jp/contests/arc171/tasks/arc171_c  
**VJudge Tag**: `[problem:AtCoder-arc171_c]`  
**Category File**: [`../categories/dp/tree_dp_swap_on_tree_degree_factorial_subgraphs.md`](../categories/dp/tree_dp_swap_on_tree_degree_factorial_subgraphs.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Count the number of distinct permutations obtainable by repeatedly choosing an edge on a tree, swapping pieces on its endpoints, and deleting the edge.

## 2. Core Observation & Invariant
Two operation sequences produce identical permutations iff the set of used edges E' is identical AND for every vertex v, the relative order of use of incident edges in E' is identical. Since any local edge ordering at vertices is realizable, each spanning subgraph (V, E') contributes exactly prod_{v in V} (deg_{E'}(v))! distinct permutations. Summing this product over all 2^{N-1} edge subsets reduces to tree DP combining children polynomials.

## 3. Step-by-Step Algorithm
1. 1. Root the tree at vertex 1.
2. 2. For each vertex u, compute polynomial P(x) = prod_{v in children(u)} (dp0[v] + dp1[v] * x) = sum c_j x^j.
3. 3. Here dp0[u] corresponds to edge(u, parent) NOT chosen: contribution is sum c_j * j!.
4. 4. dp1[u] corresponds to edge(u, parent) CHOSEN: contribution is sum c_j * (j + 1)!.
5. 5. The answer for the entire tree is dp0[1] modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

vector<long long> fact;

void precompute(int n) {
    fact.resize(n + 1);
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    precompute(n + 5);

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // dp[u][0] = ways for subtree u when edge to parent is NOT chosen
    // dp[u][1] = ways for subtree u when edge to parent IS chosen
    vector<long long> dp0(n + 1, 0), dp1(n + 1, 0);

    auto dfs = [&](auto& self, int u, int p) -> void {
        // poly represents product of (dp0[v] + dp1[v] * x)
        vector<long long> poly = {1};

        for (int v : adj[u]) {
            if (v == p) continue;
            self(self, v, u);

            vector<long long> next_poly(poly.size() + 1, 0);
            for (size_t j = 0; j < poly.size(); ++j) {
                // not choosing edge (u, v): multiply by dp0[v]
                next_poly[j] = (next_poly[j] + poly[j] * dp0[v]) % MOD;
                // choosing edge (u, v): multiply by dp1[v] * x
                next_poly[j + 1] = (next_poly[j + 1] + poly[j] * dp1[v]) % MOD;
            }
            poly = move(next_poly);
        }

        // For dp0[u]: deg = j, factor is j!
        long long val0 = 0;
        for (size_t j = 0; j < poly.size(); ++j) {
            val0 = (val0 + poly[j] * fact[j]) % MOD;
        }
        dp0[u] = val0;

        // For dp1[u]: deg = j + 1, factor is (j + 1)!
        long long val1 = 0;
        for (size_t j = 0; j < poly.size(); ++j) {
            val1 = (val1 + poly[j] * fact[j + 1]) % MOD;
        }
        dp1[u] = val1;
    };

    dfs(dfs, 1, 0);

    cout << dp0[1] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
