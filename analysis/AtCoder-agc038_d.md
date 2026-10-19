# Problem Analysis: AtCoder-agc038_d — Unique Path

**Problem ID**: `AtCoder-agc038_d`  
**Contest**: `agc038`  
**Rating / Difficulty**: 2682  
**URL**: https://atcoder.jp/contests/agc038/tasks/agc038_d  
**VJudge Tag**: `[problem:AtCoder-agc038_d]`  
**Category File**: [`../categories/graph_theory/unique_path_cycle_bridge_connectivity.md`](../categories/graph_theory/unique_path_cycle_bridge_connectivity.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Connectivity`  
- **Topic (Skill)**: `Articulation Bridges and Bridge Tree`  

---

## 1. Problem Statement & Key Idea
Construct a connected simple graph with N vertices and M edges such that given pairs (A_i, B_i) have a unique simple path (C_i = 0) or multiple simple paths (C_i = 1). A pair has a unique simple path iff all edges on the path are bridges. All C_i = 0 constraints can be contracted via DSU into trees of bridges. C_i = 1 constraints require endpoints to belong to a cycle, which imposes bounds on available cross-edges and component sizes.

## 2. Core Observation & Invariant
All C_i = 0 pairs must lie on a tree of bridges, meaning they cannot belong to the same 2-edge-connected component. We merge vertices connected by C_i = 0 into tree components. If any C_i = 1 pair is merged into the same tree component with only tree edges, they have a unique path, creating a contradiction. Edge bounds on component count K decide feasibility.

## 3. Step-by-Step Algorithm
1. 1. Run DSU on all pairs with C_i = 0.
2. 2. Check all pairs with C_i = 1: if both endpoints are in the same DSU component, output 'No'.
3. 3. Let K be the number of DSU components.
4. 4. If K == 1 and any C_i = 1: check if M >= N.
5. 5. If K == 2: impossible to have C_i = 1 without multiple paths between components.
6. 6. If M < N - 1 or M > N - 1 + max cycle edges, output 'No'. Otherwise 'Yes'.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) alpha(N))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    int components;

    DSU(int n) : parent(n), components(n) {
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
            parent[root_i] = root_j;
            components--;
            return true;
        }
        return false;
    }
};

struct Clue {
    int a, b, c;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long M;
    int Q;
    if (!(cin >> N >> M >> Q)) return 0;

    DSU dsu(N);
    vector<Clue> clues(Q);
    int c1_count = 0;

    for (int i = 0; i < Q; ++i) {
        cin >> clues[i].a >> clues[i].b >> clues[i].c;
        if (clues[i].c == 0) {
            dsu.unite(clues[i].a, clues[i].b);
        } else {
            c1_count++;
        }
    }

    for (int i = 0; i < Q; ++i) {
        if (clues[i].c == 1) {
            if (dsu.find(clues[i].a) == dsu.find(clues[i].b)) {
                cout << "No\n";
                return 0;
            }
        }
    }

    if (M == N - 1) {
        if (c1_count > 0) {
            cout << "No\n";
        } else {
            cout << "Yes\n";
        }
        return 0;
    }

    // M >= N
    long long k = dsu.components;
    if (k < 3) {
        cout << "No\n";
        return 0;
    }

    long long max_edges = N + k * (k - 3) / 2;
    if (M <= max_edges) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
