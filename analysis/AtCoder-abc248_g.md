# Problem Analysis: AtCoder-abc248_g — G. GCD cost on the tree

**Problem ID**: `AtCoder-abc248_g`  
**Contest**: `abc248`  
**Rating / Difficulty**: 2514  
**URL**: https://atcoder.jp/contests/abc248/tasks/abc248_g  
**VJudge Tag**: `[problem:AtCoder-abc248_g]`  
**Category File**: [`../categories/number_theory/gcd_cost_on_the_tree_mobius_inversion.md`](../categories/number_theory/gcd_cost_on_the_tree_mobius_inversion.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Multiplicative Functions`  
- **Topic (Skill)**: `Mobius Function and Mobius Inversion`  

---

## 1. Problem Statement & Key Idea
For all pairs of vertices $(u, v)$ on a tree, compute the sum over all simple paths of $\text{dist}(u, v) \cdot \gcd(\text{path\_nodes})$. Expressing $\gcd(X) = \sum_{d \mid X} \phi(d)$ transforms the sum into $\sum_{d} \phi(d) \sum_{u < v, \forall w \in \text{path}(u, v): d \mid A_w} \text{dist}(u, v)$. A path contains only multiples of $d$ if and only if $u$ and $v$ belong to the same connected component of the induced subgraph $V_d = \{v : d \mid A_v\}$.

## 2. Core Observation & Invariant
In any connected tree component $C$, the sum of distances between all pairs of nodes is $\sum_{e \in E_C} sz(e) \cdot (|C| - sz(e))$, where $sz(e)$ is the size of one of the subtrees formed by deleting edge $e$. By building induced subgraphs for each $d$ in $O(\sum_{v} d(A_v)) = O(N \log \max A)$, we compute subtree sizes via BFS/DFS and accumulate path distance sums in $O(N \log \max A)$ total time.

## 3. Step-by-Step Algorithm
1. 1. Precompute Euler's totient function $\phi(d)$ up to $\max A \le 10^5$ using a linear sieve.
2. 2. For each $d \in [1, \max A]$, collect all vertices $v$ where $d \mid A_v$.
3. 3. For each vertex in $V_d$, inspect tree neighbors: if a neighbor is also in $V_d$, add the edge to the induced graph.
4. 4. Find connected components of $V_d$ using BFS/DFS.
5. 5. For each component, compute subtree sizes and accumulate $\sum_{e} sz(e)(|C| - sz(e)) \pmod{998244353}$.
6. 6. Multiply each component's distance sum by $\phi(d)$ and add to the total answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log(\max A) + \max A)`
- **Space Complexity**: `O(N + \max A)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n + 1);
    int max_a = 0;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        if (a[i] > max_a) max_a = a[i];
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Precompute phi and divisors
    vector<int> phi(max_a + 1);
    for (int i = 0; i <= max_a; ++i) phi[i] = i;
    for (int i = 2; i <= max_a; ++i) {
        if (phi[i] == i) {
            for (int j = i; j <= max_a; j += i) {
                phi[j] -= phi[j] / i;
            }
        }
    }

    vector<vector<int>> nodes_with_div(max_a + 1);
    for (int i = 1; i <= n; ++i) {
        int val = a[i];
        for (int d = 1; d * d <= val; ++d) {
            if (val % d == 0) {
                nodes_with_div[d].push_back(i);
                if (d * d != val) {
                    nodes_with_div[val / d].push_back(i);
                }
            }
        }
    }

    vector<bool> in_comp(n + 1, false);
    vector<bool> visited(n + 1, false);
    vector<int> parent(n + 1, 0);
    vector<int> q;
    vector<int> sz(n + 1, 0);

    long long total_ans = 0;

    for (int d = 1; d <= max_a; ++d) {
        const auto& nodes = nodes_with_div[d];
        if (nodes.size() < 2) continue;

        for (int u : nodes) {
            in_comp[u] = true;
            visited[u] = false;
        }

        long long sum_F_d = 0;

        for (int root : nodes) {
            if (visited[root]) continue;

            q.clear();
            visited[root] = true;
            parent[root] = 0;
            q.push_back(root);

            for (size_t idx = 0; idx < q.size(); ++idx) {
                int u = q[idx];
                for (int v : adj[u]) {
                    if (in_comp[v] && !visited[v]) {
                        visited[v] = true;
                        parent[v] = u;
                        q.push_back(v);
                    }
                }
            }

            int m = (int)q.size();
            if (m < 2) continue;

            long long pair_count = ((long long)m * (m - 1) / 2) % MOD;
            long long dist_sum = 0;

            for (int u : q) sz[u] = 1;

            for (int idx = m - 1; idx >= 1; --idx) {
                int u = q[idx];
                int p = parent[u];
                sz[p] += sz[u];
                long long cur_term = ((long long)sz[u] * (m - sz[u])) % MOD;
                dist_sum = (dist_sum + cur_term) % MOD;
            }

            long long comp_cost = (pair_count + dist_sum) % MOD;
            sum_F_d = (sum_F_d + comp_cost) % MOD;
        }

        long long term = (sum_F_d * phi[d]) % MOD;
        total_ans = (total_ans + term) % MOD;

        for (int u : nodes) {
            in_comp[u] = false;
        }
    }

    cout << total_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
