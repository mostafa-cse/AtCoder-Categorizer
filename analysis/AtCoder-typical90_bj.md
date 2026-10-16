# Problem Analysis: AtCoder-typical90_bj — Paint All

**Problem ID**: `AtCoder-typical90_bj`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 062)  
**Rating / Difficulty**: 2100 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bj  
**VJudge Tag**: `[problem:AtCoder-typical90_bj]`  
**Category File**: [`../categories/graph_theory/reverse_graph_bfs.md`](../categories/graph_theory/reverse_graph_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Reverse Graph & BFS`  
- **Topic (Skill)**: `Reverse Topological / Reverse Graph BFS Ordering`  

---

## 1. Problem Statement & Key Idea
N balls initially white. Ball i can be painted black if ball A_i or B_i is already painted black, or unconditionally if A_i == i or B_i == i. Find an order to paint all balls black, or report -1 if impossible.

**Core Idea**: Think backwards from the goal state! Balls that can be painted unconditionally are terminal triggers.

## 2. Core Observation & Invariant
Construct reverse graph: directed edges A_i -> i and B_i -> i. Start a BFS from all balls with self-loops (A_i == i or B_i == i). Once ball u is reached, it enables any ball v having u as a prerequisite. Reversing the BFS traversal order gives the exact valid painting sequence!

## 3. Step-by-Step Algorithm
1. Build reverse adjacency list: rev[A_i].push_back(i) and rev[B_i].push_back(i).
2. Push all nodes with A_i == i or B_i == i into BFS queue.
3. Run BFS, recording visited vertices in an order list.
4. If order.size() < N, output -1.
5. Else, reverse(order) and print the sequence.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

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

    vector<vector<int>> rev(n + 1);
    queue<int> q;
    vector<bool> vis(n + 1, false);

    for (int i = 1; i <= n; ++i) {
        int a, b;
        cin >> a >> b;
        rev[a].push_back(i);
        rev[b].push_back(i);
        if (a == i || b == i) {
            vis[i] = true;
            q.push(i);
        }
    }

    vector<int> order;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);

        for (int v : rev[u]) {
            if (!vis[v]) {
                vis[v] = true;
                q.push(v);
            }
        }
    }

    if ((int)order.size() != n) {
        cout << -1 << "\n";
        return 0;
    }

    reverse(order.begin(), order.end());
    for (int x : order) {
        cout << x << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Backward BFS on prerequisite activation graph.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Reverse thinking, backward graph reachability, and topological activation ordering.
- **Reusable Pattern**: `Reverse Graph Activation BFS.`

---
Back to [Reverse Topological / Reverse Graph BFS Ordering](../categories/graph_theory/reverse_graph_bfs.md) | [Categories Directory](../categories/README.md)