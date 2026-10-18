# Problem Analysis: AtCoder-arc093_c — E. Bichrome Spanning Tree

**Problem ID**: `AtCoder-arc093_c`  
**Contest**: `arc093`  
**Rating / Difficulty**: 2551  
**URL**: https://atcoder.jp/contests/arc093/tasks/arc093_c  
**VJudge Tag**: `[problem:AtCoder-arc093_c]`  
**Category File**: [`../categories/graph_theory/bichrome_spanning_tree_kruskal_lca.md`](../categories/graph_theory/bichrome_spanning_tree_kruskal_lca.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Minimum Spanning Tree (MST)`  
- **Topic (Skill)**: `Minimum Spanning Tree (MST) - Prim's and Kruskal's`  

---

## 1. Problem Statement & Key Idea
Color graph edges Black or White ($2^M$ colorings). Count colorings where the minimum weight bichromatic spanning tree has weight exactly $X$. Find an unconstrained MST $T_0$ with weight $W(T_0)$. For each edge $e = (u, v)$, the minimum weight spanning tree containing $e$ has cost $cost(e) = W(T_0) + W(e) - \max\_e$, where $\max\_e$ is the heaviest edge on the tree path between $u$ and $v$ in $T_0$. Count edges with $cost(e) < X$ ($C_<$) and $cost(e) == X$ ($C_=$).

## 2. Core Observation & Invariant
If $X < W(T_0)$, answer is 0. If $X > W(T_0)$, all $C_<$ edges must have the same color (2 choices) so that no tree with weight $< X$ is bichromatic; then at least one edge of $C_=$ must have the opposite color: $2 \cdot (2^{C_=} - 1) \cdot 2^{C_>}$. If $X = W(T_0)$, $C_< = 0$, and an MST is bichromatic iff $C_=$ is not monochromatic: $(2^{C_=} - 2) \cdot 2^{C_>}$.

## 3. Step-by-Step Algorithm
1. 1. Run Kruskal's algorithm to find MST $T_0$ with total weight $W(T_0)$.
2. 2. If $X < W(T_0)$, output 0.
3. 3. Precompute binary lifting table with max edge weights on paths in $T_0$.
4. 4. For every edge $e \notin T_0$, query maximum edge weight on tree path to compute $cost(e) = W(T_0) + W(e) - \max\_e$.
5. 5. Count $C_<, C_=, C_>$ against target weight $X$.
6. 6. If $X == W(T_0)$, output $(2^{C_=} - 2) \cdot 2^{C_>} \pmod{10^9 + 7}$.
7. 7. Else, output $2 \cdot (2^{C_=} - 1) \cdot 2^{C_>} \pmod{10^9 + 7}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(M \log N)`
- **Space Complexity**: `O(N \log N + M)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 1000000007;

struct Edge {
    int u, v;
    long long w;
    int id;
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

const int MAXN = 1005;
vector<pair<int, long long>> adj[MAXN];
int depth[MAXN];
int up[MAXN][15];
long long max_w[MAXN][15];

void dfs(int u, int p, int d, long long w) {
    depth[u] = d;
    up[u][0] = p;
    max_w[u][0] = w;
    for (auto const& edge : adj[u]) {
        int v = edge.first;
        long long weight = edge.second;
        if (v != p) {
            dfs(v, u, d + 1, weight);
        }
    }
}

long long get_max_edge(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    long long res = 0;
    int diff = depth[u] - depth[v];
    for (int i = 0; i < 15; ++i) {
        if ((diff >> i) & 1) {
            res = max(res, max_w[u][i]);
            u = up[u][i];
        }
    }
    if (u == v) return res;
    for (int i = 14; i >= 0; --i) {
        if (up[u][i] != up[v][i]) {
            res = max(res, max(max_w[u][i], max_w[v][i]));
            u = up[u][i];
            v = up[v][i];
        }
    }
    res = max(res, max(max_w[u][0], max_w[v][0]));
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    long long X;
    if (!(cin >> n >> m >> X)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        edges[i].id = i;
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w < b.w;
    });

    DSU dsu(n);
    long long mst_weight = 0;
    vector<bool> in_mst(m, false);

    for (int i = 0; i < m; ++i) {
        if (dsu.unite(edges[i].u, edges[i].v)) {
            mst_weight += edges[i].w;
            in_mst[edges[i].id] = true;
            adj[edges[i].u].push_back({edges[i].v, edges[i].w});
            adj[edges[i].v].push_back({edges[i].u, edges[i].w});
        }
    }

    if (X < mst_weight) {
        cout << 0 << "\n";
        return 0;
    }

    dfs(1, 1, 0, 0);
    for (int j = 1; j < 15; ++j) {
        for (int i = 1; i <= n; ++i) {
            up[i][j] = up[up[i][j - 1]][j - 1];
            max_w[i][j] = max(max_w[i][j - 1], max_w[up[i][j - 1]][j - 1]);
        }
    }

    int c_less = 0, c_eq = 0, c_greater = 0;
    for (int i = 0; i < m; ++i) {
        long long cost;
        if (in_mst[edges[i].id]) {
            cost = mst_weight;
        } else {
            long long mw = get_max_edge(edges[i].u, edges[i].v);
            cost = mst_weight + edges[i].w - mw;
        }

        if (cost < X) c_less++;
        else if (cost == X) c_eq++;
        else c_greater++;
    }

    long long ans = 0;
    if (X == mst_weight) {
        ans = (power(2, c_eq) - 2 + MOD) % MOD;
        ans = (ans * power(2, c_greater)) % MOD;
    } else {
        ans = 2 * (power(2, c_eq) - 1 + MOD) % MOD;
        ans = (ans * power(2, c_greater)) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
