# Problem Analysis: AtCoder-abc286_g — Unique Walk

**Problem ID**: `AtCoder-abc286_g`  
**Contest**: `abc286`  
**Rating / Difficulty**: 2135  
**URL**: https://atcoder.jp/contests/abc286/tasks/abc286_g  
**VJudge Tag**: `[problem:AtCoder-abc286_g]`  
**Category File**: [`../categories/graph_theory/contracted_multigraph_eulerian_trail.md`](../categories/graph_theory/contracted_multigraph_eulerian_trail.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Eulerian Path`  
- **Topic (Skill)**: `Eulerian Path and Cycle`  

---

## 1. Problem Statement & Key Idea
Given a connected graph and a subset of K special edges S, determine if there exists a walk that traverses each edge in S exactly once, while other edges may be traversed any number of times.

**Key Insight**: Since non-special edges can be traversed arbitrarily many times without restriction, we can contract each connected component formed by non-special edges E \ S into a single super-vertex using DSU. The problem then reduces to determining if the contracted multigraph whose edge set is S possesses an Eulerian trail! An Eulerian trail exists iff the multigraph is connected (ignoring isolated vertices) and the number of vertices with odd degree is either 0 or 2.

## 2. Core Observation & Invariant
Contracting unrestricted edges collapses the problem into verifying Eulerian trail conditions (connectivity and <= 2 odd-degree vertices) on the contracted multigraph of special edges.

## 3. Step-by-Step Algorithm
1. Contract all non-special edges E \ S using DSU.
2. For each special edge in S, connect the two DSU component roots and increment their degrees.
3. Check that all components with positive degree belong to a single connected component in S.
4. Count vertices with odd degree.
5. Output Yes if connected and odd_count in {0, 2}; otherwise No.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M alpha(N))`
- **Space Complexity**: `O(N + M)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Edge contraction via DSU and Eulerian trail condition verification on induced multigraphs.
- **Reusable Pattern**: Traversing a specific edge subset exactly once with arbitrary auxiliary edge usage reduces to Eulerian trails on contracted components.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int u, int v) {
        parent[find(u)] = find(v);
    }
};

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m + 1);
    for (int i = 1; i <= m; ++i) {
        cin >> edges[i].u >> edges[i].v;
    }

    int k;
    cin >> k;
    vector<bool> is_special(m + 1, false);
    for (int i = 0; i < k; ++i) {
        int x;
        cin >> x;
        is_special[x] = true;
    }

    DSU dsu(n);
    for (int i = 1; i <= m; ++i) {
        if (!is_special[i]) {
            dsu.unite(edges[i].u, edges[i].v);
        }
    }

    vector<int> degree(n + 1, 0);
    DSU special_dsu(n);

    int first_special = -1;
    for (int i = 1; i <= m; ++i) {
        if (is_special[i]) {
            int root_u = dsu.find(edges[i].u);
            int root_v = dsu.find(edges[i].v);
            degree[root_u]++;
            degree[root_v]++;
            special_dsu.unite(root_u, root_v);
            first_special = root_u;
        }
    }

    bool connected = true;
    int odd_count = 0;
    for (int i = 1; i <= n; ++i) {
        if (dsu.find(i) == i && degree[i] > 0) {
            if (special_dsu.find(i) != special_dsu.find(first_special)) {
                connected = false;
            }
            if (degree[i] % 2 != 0) {
                odd_count++;
            }
        }
    }

    if (connected && (odd_count == 0 || odd_count == 2)) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```
