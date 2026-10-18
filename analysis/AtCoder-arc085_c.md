# Problem Analysis: AtCoder-arc085_c — E. MUL

**Problem ID**: `AtCoder-arc085_c`  
**Contest**: `arc085`  
**Rating / Difficulty**: 2571  
**URL**: https://atcoder.jp/contests/arc085/tasks/arc085_c  
**VJudge Tag**: `[problem:AtCoder-arc085_c]`  
**Category File**: [`../categories/graph_theory/mul_gemstones_divisibility_maximum_weight_closure.md`](../categories/graph_theory/mul_gemstones_divisibility_maximum_weight_closure.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Closure Problem`  

---

## 1. Problem Statement & Key Idea
Smashing gem $x$ smashes all multiples $2x, 3x, \dots \le N$. Earn $a_i$ for each retained gem. Maximize total earnings.

## 2. Core Observation & Invariant
If gem $y$ is kept, every divisor $x$ of $y$ must also be kept (otherwise smashing $x$ would have smashed $y$). Retaining a set of gems forms a closure on the divisibility DAG where $y \to x$ for all $x \mid y$. This is equivalent to Maximum Weight Closure via Dinic min-cut.

## 3. Step-by-Step Algorithm
1. 1. Construct flow network: source $S$, sink $T$, vertices $1 \dots N$.
2. 2. For each gem $i$ with $a_i > 0$, add edge $S \to i$ with capacity $a_i$.
3. 3. For each gem $i$ with $a_i < 0$, add edge $i \to T$ with capacity $-a_i$.
4. 4. For all pairs $j < i$ with $i \bmod j == 0$, add edge $i \to j$ with capacity $\infty$.
5. 5. Compute MinCut using Dinic. Answer is $\sum_{a_i > 0} a_i - \text{MinCut}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 \sqrt{N})`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    long long cap;
    long long flow;
    int rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level, ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, long long cap) {
        adj[from].push_back({to, cap, 0, (int)adj[to].size()});
        adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (auto& edge : adj[v]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }

    long long dfs(int v, int t, long long pushed) {
        if (pushed == 0) return 0;
        if (v == t) return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto& edge = adj[v][cid];
            int tr = edge.to;
            if (level[v] + 1 != level[tr] || edge.cap - edge.flow == 0) continue;
            long long tr_pushed = dfs(tr, t, min(pushed, edge.cap - edge.flow));
            if (tr_pushed == 0) continue;
            edge.flow += tr_pushed;
            adj[tr][edge.rev].flow -= tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    long long max_flow(int s, int t) {
        long long flow = 0;
        const long long INF = 1e18;
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

    int N;
    if (!(cin >> N)) return 0;
    vector<long long> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    int s = 0;
    int t = N + 1;
    Dinic dinic(N + 2);
    long long pos_sum = 0;
    const long long INF = 1e18;

    for (int i = 1; i <= N; ++i) {
        long long val = a[i - 1];
        if (val > 0) {
            pos_sum += val;
            dinic.add_edge(s, i, val);
        } else if (val < 0) {
            dinic.add_edge(i, t, -val);
        }
        for (int j = 1; j < i; ++j) {
            if (i % j == 0) {
                dinic.add_edge(i, j, INF);
            }
        }
    }

    long long cut = dinic.max_flow(s, t);
    cout << pos_sum - cut << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
