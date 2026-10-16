# Problem Analysis: AtCoder-abc054_c — One-stroke Path

**Problem ID**: `AtCoder-abc054_c`  
**Contest**: `abc054`  
**Rating / Difficulty**: 1244  
**URL**: https://atcoder.jp/contests/abc054/tasks/abc054_c  
**VJudge Tag**: `[problem:AtCoder-abc054_c]`  
**Category File**: [`../categories/graph_theory/hamiltonian_path_permutation_dfs.md`](../categories/graph_theory/hamiltonian_path_permutation_dfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Hamiltonian Paths`  
- **Topic (Skill)**: `Hamiltonian Path Permutation DFS`  

---

## 1. Problem Statement & Key Idea
Given an undirected graph with N vertices and M edges. Count the number of paths starting at vertex 1 that visit every vertex exactly once (N <= 8).

**Key Idea**: The problem asks for the count of Hamiltonian paths originating at vertex 1.

## 2. Core Observation & Invariant
Because N <= 8, the total number of permutations of vertices starting with vertex 1 is (N - 1)! <= 7! = 5040. We can either test all permutations with std::next_permutation or perform a simple backtracking DFS with visited bitmask.

## 3. Step-by-Step Algorithm
1. Write DFS(u, visited_mask):
2. If visited_mask == (1 << N) - 1, return 1.
3. Initialize paths = 0.
4. For each neighbor v in adj[u]: if !((visited_mask >> v) & 1): paths += DFS(v, visited_mask | (1 << v)).
5. Return paths; start with DFS(0, 1).

## 4. Complexity Analysis
- **Time Complexity**: `O(N!)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<vector<int>> adj;

int dfs(int u, int mask) {
    if (mask == (1 << n) - 1) return 1;

    int total_paths = 0;
    for (int v : adj[u]) {
        if (!((mask >> v) & 1)) {
            total_paths += dfs(v, mask | (1 << v));
        }
    }
    return total_paths;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    adj.resize(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        u--; v--; // 0-indexed
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    cout << dfs(0, 1) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting Hamiltonian paths via backtracking DFS on small graphs.
- **Reusable Pattern**: `Hamiltonian path count: DFS(u, mask) with mask == (1 << N) - 1 base case.`
