# Problem Analysis: AtCoder-abc354_g — Select Strings

**Problem ID**: `AtCoder-abc354_g`  
**Contest**: `abc354`  
**Rating / Difficulty**: 2665  
**URL**: https://atcoder.jp/contests/abc354/tasks/abc354_g  
**VJudge Tag**: `[problem:AtCoder-abc354_g]`  
**Category File**: [`../categories/strings/select_strings_aho_corasick_min_cut.md`](../categories/strings/select_strings_aho_corasick_min_cut.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Aho Corasick`  
- **Topic (Skill)**: `Aho Corasick`  

---

## 1. Problem Statement & Key Idea
Finding the maximum weight subset of strings where no string is a substring of another reduces to the Maximum Weight Antichain in a Poset, solvable via Min-Cut on a bipartite flow network.

## 2. Core Observation & Invariant
The substring relation forms a partially ordered set (poset). A good subset is an antichain. By Dilworth's theorem and the Picard/Balinski reduction, the maximum weight antichain equals the total weight minus the minimum cut in a bipartite network: source -> L_i with capacity A_i, R_i -> sink with capacity A_i, and infinite capacity edges L_i -> R_j whenever S_i is a substring of S_j (i != j).

## 3. Step-by-Step Algorithm
1. 1. Build bipartite flow network with 2N+2 vertices (source, L_1..N, R_1..N, sink).
2. 2. Add edges source -> L_i (capacity A_i) and R_i -> sink (capacity A_i).
3. 3. For each pair (i, j) with i != j, if S_i is a substring of S_j, add edge L_i -> R_j with capacity infinity.
4. 4. Run Dinic's algorithm to compute the minimum s-t cut.
5. 5. Output sum(A_i) - min_cut.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 * max(|S|) + N^2.5)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <numeric>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    long long cap;
    long long flow;
    int rev;
};

class Dinic {
public:
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

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
            long long tr_flow = dfs(tr, t, min(pushed, edge.cap - edge.flow));
            if (tr_flow == 0) continue;
            edge.flow += tr_flow;
            adj[tr][edge.rev].flow -= tr_flow;
            return tr_flow;
        }
        return 0;
    }

    long long max_flow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, 1e18)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<string> S(N);
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }

    vector<long long> A(N);
    long long total_A = 0;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        total_A += A[i];
    }

    int src = 0;
    int dst = 2 * N + 1;
    Dinic dinic(2 * N + 2);

    for (int i = 0; i < N; ++i) {
        dinic.add_edge(src, 1 + i, A[i]);
        dinic.add_edge(1 + N + i, dst, A[i]);
    }

    const long long INF = 1e18;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (i != j && S[j].find(S[i]) != string::npos) {
                dinic.add_edge(1 + i, 1 + N + j, INF);
            }
        }
    }

    long long min_cut = dinic.max_flow(src, dst);
    cout << total_A - min_cut << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
