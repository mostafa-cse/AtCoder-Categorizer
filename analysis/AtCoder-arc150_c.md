# Problem Analysis: AtCoder-arc150_c — Path and Subsequence

**Problem ID**: `AtCoder-arc150_c`  
**Contest**: `arc150`  
**Rating / Difficulty**: 1802  
**URL**: https://atcoder.jp/contests/arc150/tasks/arc150_c  
**VJudge Tag**: `[problem:AtCoder-arc150_c]`  
**Category File**: [`../categories/graph_theory/subsequence_matching_graph_01bfs.md`](../categories/graph_theory/subsequence_matching_graph_01bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `0-1 BFS`  
- **Topic (Skill)**: `Worst-Case Subsequence Matching on Graph via 0-1 BFS`  

---

## 1. Problem Statement & Key Idea
Given an undirected connected graph with vertex labels A_u and a sequence S of length K. Does EVERY simple path from vertex 1 to vertex N contain S as a subsequence?

**Key Insight**: Every path contains S iff the path from 1 to N that matches the FEWEST elements of S matches all K elements. Find the minimum matched prefix length of S from 1 to N using 0-1 BFS.

## 2. Core Observation & Invariant
Let d[u] be the minimum prefix of S matched by any path from 1 to u. Traversing edge (u, v): if d[u] < K and A_v == S_{d[u] + 1}, matched count increases by 1 (edge weight 1); otherwise edge weight is 0. If min matched at N is K, every path contains S.

## 3. Step-by-Step Algorithm
1. Initialize d[1..N] = INF.
2. d[1] = (A[1] == S[1] ? 1 : 0).
3. Deque Q: push_front 1.
4. While Q not empty:
5.   u = Q.front(); Q.pop_front();
6.   For neighbor v of u:
7.     next_d = d[u] + (d[u] < K && A[v] == S[d[u] + 1] ? 1 : 0);
8.     if next_d < d[v]:
9.       d[v] = next_d;
10.       if (next_d == d[u]) Q.push_front(v); else Q.push_back(v);
11. Print 'Yes' if d[N] == K else 'No'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<int> s(k + 1);
    for (int i = 1; i <= k; ++i) cin >> s[i];

    vector<int> d(n + 1, INF);
    deque<int> dq;

    d[1] = (a[1] == s[1] ? 1 : 0);
    dq.push_front(1);

    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();

        for (int v : adj[u]) {
            int w = (d[u] < k && a[v] == s[d[u] + 1]) ? 1 : 0;
            int next_d = d[u] + w;
            if (next_d < d[v]) {
                d[v] = next_d;
                if (w == 0) dq.push_front(v);
                else dq.push_back(v);
            }
        }
    }

    if (d[n] == k) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Formulating universal subsequence path properties as worst-case 0-1 BFS shortest paths.
- **Reusable Pattern**: `Universal Path Property Check: Find worst-case path via 0-1 BFS and verify threshold.`
