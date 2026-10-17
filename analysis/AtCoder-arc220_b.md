# Problem Analysis: AtCoder-arc220_b — B. Incomplete Shuffle

**Problem ID**: `AtCoder-arc220_b`  
**Contest**: `arc220`  
**Rating / Difficulty**: 2199  
**URL**: https://atcoder.jp/contests/arc220/tasks/arc220_b  
**VJudge Tag**: `[problem:AtCoder-arc220_b]`  
**Category File**: [`../categories/graph_theory/incomplete_shuffle_eulerian_trail_decomposition.md`](../categories/graph_theory/incomplete_shuffle_eulerian_trail_decomposition.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Eulerian Path`  
- **Topic (Skill)**: `Eulerian Path and Cycle`  

---

## 1. Problem Statement & Key Idea
N - 1 swaps of (i, j) with i < j generate precisely all single-cycle permutations of length N. In graph G with edges A_i -> B_i, making A_k = B_k corresponds to decomposing G into the minimum number of directed trails so that edges can form a single Eulerian circuit.

## 2. Core Observation & Invariant
If G already has an Eulerian circuit, answer is N. Otherwise, each connected component S requires max(1, sum_{v in S} max(0, in[v] - out[v])) trails. Total trails across all components gives minimum modifications, yielding max matching count N - sum trails.

## 3. Step-by-Step Algorithm
1. Build directed graph with edges A_i -> B_i and track in/out degrees.
2. Use DSU to find connected components of vertices with non-zero degree.
3. If all in_deg == out_deg and all edges lie in a single component, output N.
4. Otherwise, for each component S, compute trails = max(1, sum_{v in S} max(0, in_deg[v] - out_deg[v])).
5. Output N - sum_S trails.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> sz;
    DSU(int n) : parent(n), sz(n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            if (sz[root_i] < sz[root_j]) swap(root_i, root_j);
            parent[root_j] = root_i;
            sz[root_i] += sz[root_j];
            return true;
        }
        return false;
    }
};

void solve() {
    int N;
    if (!(cin >> N)) return;

    vector<int> A(N), B(N);
    vector<int> out_deg(N + 1, 0), in_deg(N + 1, 0);

    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        out_deg[A[i]]++;
    }
    for (int i = 0; i < N; ++i) {
        cin >> B[i];
        in_deg[B[i]]++;
    }

    DSU dsu(N + 1);
    for (int i = 0; i < N; ++i) {
        dsu.unite(A[i], B[i]);
    }

    // Check if graph already has an Eulerian circuit
    bool all_deg_equal = true;
    int num_vertices_with_edges = 0;
    for (int i = 1; i <= N; ++i) {
        if (out_deg[i] > 0 || in_deg[i] > 0) {
            num_vertices_with_edges++;
        }
        if (out_deg[i] != in_deg[i]) {
            all_deg_equal = false;
        }
    }

    if (all_deg_equal && dsu.sz[dsu.find(A[0])] == num_vertices_with_edges) {
        cout << N << "\n";
        return;
    }

    // Group vertices by DSU root
    vector<vector<int>> groups(N + 1);
    for (int i = 1; i <= N; ++i) {
        if (out_deg[i] > 0 || in_deg[i] > 0) {
            groups[dsu.find(i)].push_back(i);
        }
    }

    int ans = N;
    for (int i = 1; i <= N; ++i) {
        if (groups[i].empty()) continue;
        int res = 0;
        for (int v : groups[i]) {
            res += max(0, in_deg[v] - out_deg[v]);
        }
        ans -= max(1, res);
    }

    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
