# Problem Analysis: AtCoder-arc115_d — D. Odd Degree

**Problem ID**: `AtCoder-arc115_d`  
**Contest**: `arc115`  
**Rating / Difficulty**: 2325  
**URL**: https://atcoder.jp/contests/arc115/tasks/arc115_d  
**VJudge Tag**: `[problem:AtCoder-arc115_d]`  
**Category File**: [`../categories/graph_theory/spanning_forest_parity_handshaking_convolution.md`](../categories/graph_theory/spanning_forest_parity_handshaking_convolution.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `DFS Tree`  

---

## 1. Problem Statement & Key Idea
Given an undirected graph of $N$ vertices and $M$ edges, for each $k = 0, \dots, N$, count the number of spanning subgraphs having exactly $k$ vertices of odd degree, modulo 998244353.

## 2. Core Observation & Invariant
In any connected component with $V$ vertices and $E$ edges, for any fixed subset of non-tree edges and any subset of vertices $S$ with $|S|$ even, there exists a unique subset of spanning tree edges yielding odd degrees exactly at $S$.

## 3. Step-by-Step Algorithm
1. Find all connected components using BFS/DFS. For a component with $V_i$ vertices and $E_i$ edges, the number of subgraphs having $k$ odd-degree vertices ($k$ even) is $2^{E_i - V_i + 1} \binom{V_i}{k}$.
2. Represent each component by its generating function polynomial $P_i(x) = 2^{E_i - V_i + 1} \sum_{k \text{ even}} \binom{V_i}{k} x^k$.
3. Convolve the polynomials across all components in $O(N^2)$ time to obtain the answer for all $K$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

long long modPow(long long a, long long b) {
    long long res = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<vector<long long>> C(n + 1, vector<long long>(n + 1, 0));
    for (int i = 0; i <= n; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    vector<bool> vis(n + 1, false);
    vector<pair<int, int>> comps;

    for (int i = 1; i <= n; ++i) {
        if (!vis[i]) {
            vector<int> comp_nodes;
            queue<int> q;
            vis[i] = true;
            q.push(i);

            while (!q.empty()) {
                int u = q.front();
                q.pop();
                comp_nodes.push_back(u);
                for (int v : adj[u]) {
                    if (!vis[v]) {
                        vis[v] = true;
                        q.push(v);
                    }
                }
            }

            int v_cnt = comp_nodes.size();
            int e_cnt = 0;
            for (int u : comp_nodes) {
                e_cnt += adj[u].size();
            }
            e_cnt /= 2;

            comps.push_back({v_cnt, e_cnt});
        }
    }

    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    int cur_deg = 0;

    for (auto [v_cnt, e_cnt] : comps) {
        long long ways_factor = modPow(2, e_cnt - v_cnt + 1);
        vector<long long> comp_poly(v_cnt + 1, 0);
        for (int k = 0; k <= v_cnt; k += 2) {
            comp_poly[k] = (ways_factor * C[v_cnt][k]) % MOD;
        }

        vector<long long> new_dp(cur_deg + v_cnt + 1, 0);
        for (int i = 0; i <= cur_deg; ++i) {
            if (dp[i] == 0) continue;
            for (int j = 0; j <= v_cnt; j += 2) {
                if (comp_poly[j] == 0) continue;
                new_dp[i + j] = (new_dp[i + j] + dp[i] * comp_poly[j]) % MOD;
            }
        }

        dp = std::move(new_dp);
        cur_deg += v_cnt;
    }

    for (int k = 0; k <= n; ++k) {
        cout << (k < (int)dp.size() ? dp[k] : 0) << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
