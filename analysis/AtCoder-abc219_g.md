# Problem Analysis: AtCoder-abc219_g — G. Propagation

**Problem ID**: `AtCoder-abc219_g`  
**Contest**: `abc219`  
**Rating / Difficulty**: 2287  
**URL**: https://atcoder.jp/contests/abc219/tasks/abc219_g  
**VJudge Tag**: `[problem:AtCoder-abc219_g]`  
**Category File**: [`../categories/data_structures/sqrt_decomp_heavy_light_lazy_propagation.md`](../categories/data_structures/sqrt_decomp_heavy_light_lazy_propagation.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Splitting Objects into Light and Heavy / Case Processing`  

---

## 1. Problem Statement & Key Idea
In a graph of $N$ vertices and $M$ edges where each vertex initially has value $x$, process $Q$ operations where choosing vertex $x$ sets the values of $x$ and all its neighbors to $x$'s current value.

## 2. Core Observation & Invariant
A vertex is heavy if $\deg(u) \ge B = \Theta(\sqrt{M})$ and light otherwise. Each heavy vertex has at most $O(\sqrt{M})$ heavy neighbors. Updates propagate lazily: a vertex's true current value is the latest update among its direct update and updates stored on its heavy neighbors.

## 3. Step-by-Step Algorithm
1. 1. Classify vertices with degree $\ge B \approx 450$ as heavy, and $< B$ as light. The number of heavy vertices is at most $2M / B = O(\sqrt{M})$.
2. 2. Maintain `val[u]`, `time[u]` (when $u$'s value was assigned), and for heavy vertices `lazy_val[u]`, `lazy_time[u]` (an update pending for all neighbors of $u$).
3. 3. Precompute `heavy_adj[u]` containing all heavy neighbors of $u$. Since there are at most $O(\sqrt{M})$ heavy vertices, $|heavy\_adj[u]| \le O(\sqrt{M})$ for all $u$.
4. 4. To inspect/update node $u$ at step $t$:
5.    - Resolve $u$'s value by checking `(val[u], time[u])` and `(lazy_val[h], lazy_time[h])` across all $h \in heavy\_adj[u]$, taking the one with maximal timestamp.
6.    - Now that $u$'s current value $c$ is determined, propagate $c$ to its neighbors:
7.      - If $u$ is light: directly update `val[v] = c`, `time[v] = t` for all $v \in adj[u]$. There are $< B$ neighbors, taking $O(B)$ time.
8.      - If $u$ is heavy: update `val[u] = c`, `time[u] = t`, and set `lazy_val[u] = c`, `lazy_time[u] = t`. Also directly update all $h \in heavy\_adj[u]$ in $O(\sqrt{M})$ time.
9. 5. Total runtime across $Q$ operations is $O(Q \sqrt{M} + M)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q \sqrt{M} + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int B = 450;

struct NodeInfo {
    int val;
    int time;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, Q;
    if (!(cin >> N >> M >> Q)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<bool> is_heavy(N + 1, false);
    for (int i = 1; i <= N; ++i) {
        if ((int)adj[i].size() >= B) {
            is_heavy[i] = true;
        }
    }

    vector<vector<int>> heavy_adj(N + 1);
    for (int i = 1; i <= N; ++i) {
        for (int v : adj[i]) {
            if (is_heavy[v]) {
                heavy_adj[i].push_back(v);
            }
        }
    }

    vector<NodeInfo> node_state(N + 1);
    vector<NodeInfo> lazy_heavy(N + 1);
    for (int i = 1; i <= N; ++i) {
        node_state[i] = {i, 0};
        lazy_heavy[i] = {0, -1};
    }

    auto get_current = [&](int u) {
        NodeInfo best = node_state[u];
        for (int h : heavy_adj[u]) {
            if (lazy_heavy[h].time > best.time) {
                best = lazy_heavy[h];
            }
        }
        return best.val;
    };

    for (int q = 1; q <= Q; ++q) {
        int x;
        cin >> x;
        int current_val = get_current(x);
        
        node_state[x] = {current_val, q};
        if (is_heavy[x]) {
            lazy_heavy[x] = {current_val, q};
        } else {
            for (int v : adj[x]) {
                node_state[v] = {current_val, q};
            }
        }
    }

    for (int i = 1; i <= N; ++i) {
        cout << get_current(i) << (i == N ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
