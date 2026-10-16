# Problem Analysis: AtCoder-abc282_e — Choose Two and Eat One

**Problem ID**: `AtCoder-abc282_e`  
**Contest**: `abc282`  
**Rating / Difficulty**: 1604  
**URL**: https://atcoder.jp/contests/abc282/tasks/abc282_e  
**VJudge Tag**: `[problem:AtCoder-abc282_e]`  
**Category File**: [`../categories/graph_theory/maximum_spanning_tree_modular_game.md`](../categories/graph_theory/maximum_spanning_tree_modular_game.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Minimum Spanning Tree`  
- **Topic (Skill)**: `Maximum Spanning Tree on Complete Graph with Modular Exponentiation`  

---

## 1. Problem Statement & Key Idea
N balls with values A_i. In each step, pick two balls x and y, score (x^y + y^x) % M points, and eat one of them. Repeat until 1 ball remains. Maximize total score.

**Key Insight**: The process of eating one of two balls corresponds exactly to building a spanning tree on the N balls! Total points collected is the sum of edge weights of the tree.

## 2. Core Observation & Invariant
Construct a complete graph of N vertices with edge weights w(u, v) = (A_u^{A_v} + A_v^{A_u}) % M. The maximum possible total score is the weight of the MAXIMUM Spanning Tree, solvable via Kruskal's or Prim's algorithm.

## 3. Step-by-Step Algorithm
1. Compute all N*(N-1)/2 pairwise edge weights using modular exponentiation.
2. Negate edge weights or sort descending.
3. Run Kruskal's algorithm with DSU to find the Maximum Spanning Tree.
4. Print total MST weight.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 log M + N^2 log N)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

long long power(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}

struct Edge {
    int u, v;
    long long weight;
    bool operator<(const Edge& other) const {
        return weight > other.weight; // Descending for Max Spanning Tree
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int u) {
        return parent[u] == u ? u : parent[u] = find(parent[u]);
    }
    bool unite(int u, int v) {
        int ru = find(u), rv = find(v);
        if (ru == rv) return false;
        parent[ru] = rv;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<Edge> edges;
    edges.reserve(n * (n - 1) / 2);

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            long long w = (power(a[i], a[j], m) + power(a[j], a[i], m)) % m;
            edges.push_back({i, j, w});
        }
    }

    sort(edges.begin(), edges.end());

    DSU dsu(n);
    long long max_score = 0;
    int edges_used = 0;

    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            max_score += e.weight;
            if (++edges_used == n - 1) break;
        }
    }

    cout << max_score << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Recognizing ball-eating reduction games as spanning tree weight maximization.
- **Reusable Pattern**: `Pair-Eat Tree Equivalence: game of pairing and eliminating one element is Maximum Spanning Tree.`
