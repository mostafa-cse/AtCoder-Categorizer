# Problem Analysis: AtCoder-abc139_e — League

**Problem ID**: `AtCoder-abc139_e`  
**Contest**: `abc139`  
**Rating / Difficulty**: 1528  
**URL**: https://atcoder.jp/contests/abc139/tasks/abc139_e  
**VJudge Tag**: `[problem:AtCoder-abc139_e]`  
**Category File**: [`../categories/graph_theory/dag_longest_path_match_dependencies.md`](../categories/graph_theory/dag_longest_path_match_dependencies.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Directed Graphs`  
- **Topic (Skill)**: `DAG Longest Path / Topological Sort on Match Dependencies`  

---

## 1. Problem Statement & Key Idea
N players in a round-robin tournament. Each player has an ordered list of N - 1 opponents they must play in strict order. On each day, each player can play at most 1 match. Find the minimum days required to complete all N*(N-1)/2 matches, or -1 if impossible.

**Key Insight**: Each match between player u and v (u < v) is a node in a directed graph. A player's required order creates directed dependency edges between consecutive matches. The answer is the longest path in this DAG, or -1 if a cycle exists.

## 2. Core Observation & Invariant
There are N*(N-1)/2 <= 5 * 10^5 nodes and <= N*(N-2) edges. Detecting cycles and computing the longest path via Kahn's topological sort or memoized DFS takes linear time O(N^2).

## 3. Step-by-Step Algorithm
1. Map each unordered pair (u, v) with u < v to a unique match ID from 0 to N*(N-1)/2 - 1.
2. Build directed graph: for each player, add directed edge from match_k to match_{k+1}.
3. Compute in-degrees for all match nodes.
4. Queue all nodes with in-degree 0, initialized with dist = 1.
5. Run BFS (Kahn's algorithm):
6.   Pop node u with dist[u].
7.   For each neighbor v: in_degree[v]--, dist[v] = max(dist[v], dist[u] + 1).
8.   If in_degree[v] == 0, push v.
9. If processed node count < total_nodes, return -1 (cycle detected).
10. Return max(dist[u]) over all nodes.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    auto get_id = [&](int u, int v) -> int {
        if (u > v) swap(u, v);
        // u in 1..n-1, v in u+1..n
        return (u - 1) * n + (v - 1);
    };

    int total_nodes = n * n;
    vector<vector<int>> adj(total_nodes);
    vector<int> in_deg(total_nodes, 0);
    vector<bool> exists(total_nodes, false);

    for (int i = 1; i <= n; ++i) {
        int prev_match = -1;
        for (int j = 0; j < n - 1; ++j) {
            int opp;
            cin >> opp;
            int cur_match = get_id(i, opp);
            exists[cur_match] = true;
            if (prev_match != -1) {
                adj[prev_match].push_back(cur_match);
                in_deg[cur_match]++;
            }
            prev_match = cur_match;
        }
    }

    queue<int> q;
    vector<int> dist(total_nodes, 0);
    int active_nodes = 0;

    for (int i = 0; i < total_nodes; ++i) {
        if (exists[i]) {
            active_nodes++;
            if (in_deg[i] == 0) {
                dist[i] = 1;
                q.push(i);
            }
        }
    }

    int processed = 0;
    int max_days = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        processed++;
        max_days = max(max_days, dist[u]);

        for (int v : adj[u]) {
            dist[v] = max(dist[v], dist[u] + 1);
            if (--in_deg[v] == 0) {
                q.push(v);
            }
        }
    }

    if (processed < active_nodes) {
        cout << -1 << "\n";
    } else {
        cout << max_days << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Dependency modeling on scheduling games as longest path in a directed acyclic graph.
- **Reusable Pattern**: `Tournament Match Dependency DAG: pair(u, v) as node, in-degree Kahn BFS for longest path / cycle detection.`
