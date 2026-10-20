# Problem Analysis: AtCoder-abc235_h — Ex - Painting Weighted Graph

**Problem ID**: `AtCoder-abc235_h`  
**Contest**: `abc235`  
**Rating / Difficulty**: 2966  
**URL**: https://atcoder.jp/contests/abc235/tasks/abc235_h  
**VJudge Tag**: `[problem:AtCoder-abc235_h]`  
**Category File**: [`../categories/data_structures/kruskal_reconstruction_tree_polynomial_dp.md`](../categories/data_structures/kruskal_reconstruction_tree_polynomial_dp.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)`  

---

## 1. Problem Statement & Key Idea
In a connected undirected weighted graph with N vertices, M edges, and parameter K <= 300, count the number of reachable vertex subsets of size <= K formed by threshold reachability components, modulo 998244353.

## 2. Core Observation & Invariant
Reachability subsets using edges of weight <= w are precisely the subtrees in the Kruskal Reconstruction Tree (KRT). Multiple edges of the same weight merge multiple components simultaneously. Each KRT node represents a connected component at weight w. Choosing to paint a component adds all its leaves. A tree DP computes the generating polynomial P_u(X) = sum c_k X^k where c_k is the number of painted subsets of size k. When components merge, the new valid sets are prod_c P_c(X) - X^m + X, truncated to degree K.

## 3. Step-by-Step Algorithm
1. 1. Sort edges by weight and build the Kruskal Reconstruction Tree (KRT) with multi-way merges for equal-weight edges.
2. 2. For each leaf, P(X) = 1 + X.
3. 3. For an internal node with children c_1, ..., c_d: multiply their polynomials prod_{i=1}^d P_{c_i}(X), capped at degree K.
4. 4. Subtract X^{size} and add X to account for painting the full component.
5. 5. Output the sum of coefficients of P_{root}(X) for degrees <= K modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N K^2)`
- **Space Complexity**: `O(N K)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <numeric>

using namespace std;

const int MOD = 998244353;

// Polynomial multiplication truncated to degree K
vector<int> poly_mul(const vector<int>& a, const vector<int>& b, int K) {
    int deg_a = (int)a.size() - 1;
    int deg_b = (int)b.size() - 1;
    int deg_c = min(K, deg_a + deg_b);
    vector<int> c(deg_c + 1, 0);
    for (int i = 0; i <= deg_a; ++i) {
        if (!a[i]) continue;
        for (int j = 0; j <= deg_b && i + j <= deg_c; ++j) {
            c[i + j] = (c[i + j] + 1LL * a[i] * b[j]) % MOD;
        }
    }
    return c;
}

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int u, int v) {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u != root_v) {
            parent[root_v] = root_u;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    map<int, vector<pair<int, int>>> edges_by_weight;
    for (int i = 0; i < m; ++i) {
        int u, v, c;
        cin >> u >> v >> c;
        --u; --v;
        if (u != v) {
            edges_by_weight[c].push_back({u, v});
        }
    }

    DSU dsu(n);
    vector<vector<int>> dp(n, vector<int>{1, 1}); // 1 + X initially

    for (auto& entry : edges_by_weight) {
        const auto& edge_list = entry.second;
        map<int, vector<int>> adj;
        vector<int> active_roots;

        for (auto& edge : edge_list) {
            int ru = dsu.find(edge.first);
            int rv = dsu.find(edge.second);
            if (ru != rv) {
                adj[ru].push_back(rv);
                adj[rv].push_back(ru);
                active_roots.push_back(ru);
                active_roots.push_back(rv);
            }
        }

        sort(active_roots.begin(), active_roots.end());
        active_roots.erase(unique(active_roots.begin(), active_roots.end()), active_roots.end());

        map<int, bool> visited;
        for (int root : active_roots) {
            if (!visited[root]) {
                vector<int> comp;
                vector<int> q = {root};
                visited[root] = true;
                int head = 0;
                while (head < (int)q.size()) {
                    int curr = q[head++];
                    comp.push_back(curr);
                    for (int nxt : adj[curr]) {
                        if (!visited[nxt]) {
                            visited[nxt] = true;
                            q.push_back(nxt);
                        }
                    }
                }

                int num_comp = (int)comp.size();
                vector<int> cur_p = {1};
                for (int node : comp) {
                    cur_p = poly_mul(cur_p, dp[node], k);
                }

                // If all subcomponents are painted red, it now takes 1 operation instead of num_comp operations
                if (num_comp <= k) {
                    if ((int)cur_p.size() <= num_comp) cur_p.resize(num_comp + 1, 0);
                    cur_p[num_comp] = (cur_p[num_comp] - 1 + MOD) % MOD;
                }
                if (1 <= k) {
                    if ((int)cur_p.size() <= 1) cur_p.resize(2, 0);
                    cur_p[1] = (cur_p[1] + 1) % MOD;
                }

                int master_root = comp[0];
                dp[master_root] = move(cur_p);
                for (size_t idx = 1; idx < comp.size(); ++idx) {
                    dsu.parent[comp[idx]] = master_root;
                }
            }
        }
    }

    vector<int> total_p = {1};
    for (int i = 0; i < n; ++i) {
        if (dsu.find(i) == i) {
            total_p = poly_mul(total_p, dp[i], k);
        }
    }

    long long ans = 0;
    for (int coeff : total_p) {
        ans = (ans + coeff) % MOD;
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
