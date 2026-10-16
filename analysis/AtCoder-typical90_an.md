# Problem Analysis: AtCoder-typical90_an — Get More Money

**Problem ID**: `AtCoder-typical90_an`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 040)  
**Rating / Difficulty**: 2550 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_an  
**VJudge Tag**: `[problem:AtCoder-typical90_an]`  
**Category File**: [`../categories/graph_theory/network_flow_mincut.md`](../categories/graph_theory/network_flow_mincut.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Network Flow`  
- **Topic (Skill)**: `Maximum Weight Closure / Project Selection Problem via Min-Cut`  

---

## 1. Problem Statement & Key Idea
N houses with burglary alarms awarding reward A_i. Unlocking house i costs key price W. Opening house i requires owning keys for a prerequisite set of houses C_{i, j}. Find maximum net profit.

**Core Idea**: Maximum Weight Closure (Project Selection Problem) reducible to Minimum Cut (Dinic's Max-Flow algorithm).

## 2. Core Observation & Invariant
Net profit = A_i - W. Positive rewards connect from Source S to node i with capacity A_i. Costs connect from node i to Sink T with capacity W. Dependency i -> j has infinite capacity. Max Profit = sum(positive A_i) - MinCut.

## 3. Step-by-Step Algorithm
1. Build flow network: S -> i with cap A_i; i -> T with cap W; i -> j with cap INF for all prerequisites.
2. Run Dinic's Algorithm to find Max-Flow (equal to Min-Cut).
3. Output sum(positive A_i) - max_flow.

## 4. Complexity Analysis
Time: O(V^2 E) with Dinic, fast in practice, Space: O(V + E).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long cap;
    int rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level, ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, long long cap) {
        adj[from].push_back({to, cap, (int)adj[to].size()});
        adj[to].push_back({from, 0, (int)adj[from].size() - 1});
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto& e : adj[u]) {
                if (e.cap > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    long long dfs(int u, int t, long long pushed) {
        if (pushed == 0 || u == t) return pushed;
        for (int& cid = ptr[u]; cid < (int)adj[u].size(); ++cid) {
            auto& e = adj[u][cid];
            if (level[u] + 1 != level[e.to] || e.cap == 0) continue;
            long long tr = dfs(e.to, t, min(pushed, e.cap));
            if (tr == 0) continue;
            e.cap -= tr;
            adj[e.to][e.rev].cap += tr;
            return tr;
        }
        return 0;
    }

    long long max_flow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, INF)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long w;
    if (!(cin >> n >> w)) return 0;

    int s = 0, t = n + 1;
    Dinic dinic(n + 2);
    long long total_reward = 0;

    for (int i = 1; i <= n; ++i) {
        long long a;
        cin >> a;
        total_reward += a;
        dinic.add_edge(s, i, a);
        dinic.add_edge(i, t, w);

        int k;
        cin >> k;
        for (int j = 0; j < k; ++j) {
            int prereq;
            cin >> prereq;
            dinic.add_edge(i, prereq, INF);
        }
    }

    long long min_cut = dinic.max_flow(s, t);
    cout << total_reward - min_cut << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Project selection / maximum weight closure reduction to minimum cut.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Network flow modeling, Project Selection Problem, and Dinic's algorithm.
- **Reusable Pattern**: `Project Selection / Max-Weight Closure via Min-Cut.`

---
Back to [Maximum Weight Closure / Project Selection Problem via Min-Cut](../categories/graph_theory/network_flow_mincut.md) | [Categories Directory](../categories/README.md)