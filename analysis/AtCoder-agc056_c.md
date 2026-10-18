# Problem Analysis: AtCoder-agc056_c — C. 01 Balanced

**Problem ID**: `AtCoder-agc056_c`  
**Contest**: `agc056`  
**Rating / Difficulty**: 2481  
**URL**: https://atcoder.jp/contests/agc056/tasks/agc056_c  
**VJudge Tag**: `[problem:AtCoder-agc056_c]`  
**Category File**: [`../categories/graph_theory/01_balanced_difference_constraints_01_bfs.md`](../categories/graph_theory/01_balanced_difference_constraints_01_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Satisfiability`  
- **Topic (Skill)**: `System Of Difference Constraints`  

---

## 1. Problem Statement & Key Idea
Find the lexicographically smallest 01 string $S$ of length $N$ such that each given substring $S[L_i \dots R_i]$ has an equal number of 0s and 1s. Let $dist[i]$ be the prefix difference (count of 1s minus count of 0s in $S[0 \dots i-1]$). Each step changes $dist$ by $\pm 1$: $|dist[i] - dist[i-1]| \le 1$. Equal 0s and 1s in $[L_i, R_i]$ means $dist[R_i] = dist[L_i - 1]$. Model as a system of difference constraints and shortest path on a parity-preserving graph with 0-weight edges for range constraints and 1-weight edges for adjacent prefix steps. 0-1 BFS finds potentials, determining $S[i-1] = '0'$ if $dist[i] > dist[i-1]$ else $'1'$.

## 2. Core Observation & Invariant
To make $S$ lexicographically smallest, we greedily want $S[i-1] = '0'$ wherever possible, which corresponds to setting $dist[i]$ larger than $dist[i-1]$. In 0-1 BFS starting from vertex 0, the shortest path distance represents the minimum potential satisfying the distance metric. Since adjacent vertices differ by at most 1, $dist[i] > dist[i-1]$ implies character '0', and $dist[i] < dist[i-1]$ implies character '1'.

## 3. Step-by-Step Algorithm
1. 1. Build an adjacency list of $N + 1$ vertices (0 to $N$).
2. 2. For each constraint $[L, R]$, add bidirectional edges $(L - 1, R)$ with weight 0.
3. 3. For each $i \in [0, N - 1]$, add bidirectional edges $(i, i + 1)$ with weight 1.
4. 4. Initialize `dist` array with -1 and run 0-1 BFS from vertex 0 using a deque.
5. 5. For each index $i$ from 1 to $N$, output '0' if $dist[i] > dist[i-1]$ else '1'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <deque>
#include <string>

using namespace std;

struct Edge {
    int to;
    int w;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int l, r;
        cin >> l >> r;
        adj[l - 1].push_back({r, 0});
        adj[r].push_back({l - 1, 0});
    }

    for (int i = 0; i < n; ++i) {
        adj[i].push_back({i + 1, 1});
        adj[i + 1].push_back({i, 1});
    }

    vector<int> dist(n + 1, -1);
    deque<int> dq;
    dist[0] = 0;
    dq.push_back(0);

    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();

        for (auto& edge : adj[u]) {
            int v = edge.to;
            int w = edge.w;
            if (dist[v] == -1 || dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                if (w == 0) {
                    dq.push_front(v);
                } else {
                    dq.push_back(v);
                }
            }
        }
    }

    string res = "";
    for (int i = 1; i <= n; ++i) {
        if (dist[i] > dist[i - 1]) {
            res += '0';
        } else {
            res += '1';
        }
    }

    cout << res << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
