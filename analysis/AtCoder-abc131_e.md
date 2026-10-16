# Problem Analysis: AtCoder-abc131_e — Friendships

**Problem ID**: `AtCoder-abc131_e`  
**Contest**: `abc131`  
**Rating / Difficulty**: 1433  
**URL**: https://atcoder.jp/contests/abc131/tasks/abc131_e  
**VJudge Tag**: `[problem:AtCoder-abc131_e]`  
**Category File**: [`../categories/graph_theory/star_graph_edge_reduction.md`](../categories/graph_theory/star_graph_edge_reduction.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Constructive Graph Theory`  
- **Topic (Skill)**: `Star Graph Baseline with Redundant Edge Reduction`  

---

## 1. Problem Statement & Key Idea
Construct a connected undirected graph with N vertices such that the number of pairs (u, v) with shortest distance = 2 is EXACTLY K. Output -1 if impossible.

**Key Insight**: A star graph with center 1 connected to leaves 2..N achieves the maximum possible number of distance-2 pairs: C(N-1, 2). Adding an edge between two leaves reduces the count of distance-2 pairs by exactly 1.

## 2. Core Observation & Invariant
Max pairs at distance 2 is max_K = (N - 1) * (N - 2) / 2. If K > max_K, it is impossible. Otherwise, start with the N - 1 star edges, and add exactly (max_K - K) leaf-to-leaf edges.

## 3. Step-by-Step Algorithm
1. Compute max_K = (N - 1) * (N - 2) / 2.
2. If K > max_K, output -1.
3. Construct base star graph: edges (1, i) for i in 2..N.
4. Collect all pairs of leaves (u, v) for 2 <= u < v <= N.
5. Add the first (max_K - K) pairs as additional edges.
6. Print total edge count, then print each edge.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    int max_k = (n - 1) * (n - 2) / 2;
    if (k > max_k) {
        cout << -1 << "\n";
        return 0;
    }

    vector<pair<int, int>> edges;
    // Base star graph
    for (int i = 2; i <= n; ++i) {
        edges.push_back({1, i});
    }

    // Add leaf edges to reduce distance-2 count by 1 each
    int needed = max_k - k;
    for (int u = 2; u <= n && needed > 0; ++u) {
        for (int v = u + 1; v <= n && needed > 0; ++v) {
            edges.push_back({u, v});
            needed--;
        }
    }

    cout << edges.size() << "\n";
    for (const auto& e : edges) {
        cout << e.first << " " << e.second << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Constructive graph design by starting from an extremum baseline and iteratively fine-tuning parameters.
- **Reusable Pattern**: `Distance-2 Pair Construction: Star graph gives C(N-1, 2); each added leaf edge decrements count by 1.`
