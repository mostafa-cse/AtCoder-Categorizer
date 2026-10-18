# Problem Analysis: AtCoder-abc261_h — Ex. Game on Graph

**Problem ID**: `AtCoder-abc261_h`  
**Contest**: `abc261`  
**Rating / Difficulty**: 2531  
**URL**: https://atcoder.jp/contests/abc261/tasks/abc261_h  
**VJudge Tag**: `[problem:AtCoder-abc261_h]`  
**Category File**: [`../categories/game_theory/game_on_graph_retrograde_dijkstra.md`](../categories/game_theory/game_on_graph_retrograde_dijkstra.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Graph Games`  
- **Topic (Skill)**: `Games on Arbitrary Graphs`  

---

## 1. Problem Statement & Key Idea
A game is played on a directed graph with edge weights $c_e \ge 0$. A token starts at vertex $v$. First Player wants to minimize total cost; Second Player wants to maximize total cost. At any step, the active player chooses an outgoing edge $(u, w)$, paying $c_e$ to the total score. If the active player cannot move (out-degree 0), the game ends. If Second Player can force infinite loops, cost is $\infty$.

## 2. Core Observation & Invariant
This is a zero-sum game on a graph with positive edge weights, solvable by Retrograde Dijkstra (value iteration on game graphs). Let $D[0][u]$ be the game value from $u$ when First Player moves, and $D[1][u]$ when Second Player moves. Terminal vertices (out-degree 0) have $D[0][t] = D[1][t] = 0$. In retrograde analysis:
- First Player (Min) can choose ANY outgoing edge, so $D[0][u] = \min_{(u, v)} (D[1][v] + c)$. The first time an edge reaches $u$ in Dijkstra, $D[0][u]$ is finalized.
- Second Player (Max) will choose the WORST option for First Player. Second Player's value $D[1][u] = \max_{(u, v)} (D[0][v] + c)$ can only be finalized when ALL outgoing moves from $u$ have been determined (i.e. remaining outgoing degree drops to 0)! The final edge that closes the degree determines the maximum.

## 3. Step-by-Step Algorithm
1. 1. Build reverse graph with incoming edges for each vertex. Compute initial out-degrees $out\_deg[u]$.
2. 2. Initialize distance array $D[2][N]$ with $\infty$.
3. 3. For all vertices with $out\_deg[u] == 0$, set $D[0][u] = D[1][u] = 0$ and push to priority queue.
4. 4. Run Dijkstra with states $(d, \text{player}, u)$:
5.    a. If state $(1, v)$ is finalized: for each incoming edge $(u, v)$ with weight $c$, candidate is $d + c$. If $d + c < D[0][u]$, finalize $D[0][u] = d + c$ and push $(D[0][u], 0, u)$.
6.    b. If state $(0, v)$ is finalized: for each incoming edge $(u, v)$ with weight $c$, decrement $out\_deg[u]$. Track maximum weight $\max(D[1][u], d + c)$. When $out\_deg[u] == 0$, push $(D[1][u], 1, u)$.
7. 5. If $D[0][v]$ is finalized, output $D[0][v]$; else output -1.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) \log(N + M))`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, start_v;
    if (!(cin >> n >> m >> start_v)) return 0;

    vector<vector<Edge>> rev_adj(n + 1);
    vector<int> out_deg(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        rev_adj[v].push_back({u, c});
        out_deg[u]++;
    }

    vector<vector<long long>> dist(2, vector<long long>(n + 1, -1));
    vector<int> rem_deg = out_deg;
    vector<long long> max_cand(n + 1, 0);

    typedef tuple<long long, int, int> State;
    priority_queue<State, vector<State>, greater<State>> pq;

    for (int i = 1; i <= n; ++i) {
        if (out_deg[i] == 0) {
            dist[0][i] = 0;
            dist[1][i] = 0;
            pq.push({0, 0, i});
            pq.push({0, 1, i});
        }
    }

    while (!pq.empty()) {
        auto [d, turn, u] = pq.top();
        pq.pop();

        if (d > dist[turn][u]) continue;

        int prev_turn = 1 - turn;
        for (const auto& edge : rev_adj[u]) {
            int p = edge.to;
            long long c = edge.w;
            if (prev_turn == 0) {
                // Takahashi's turn: Min
                if (dist[0][p] == -1 || d + c < dist[0][p]) {
                    dist[0][p] = d + c;
                    pq.push({d + c, 0, p});
                }
            } else {
                // Aoki's turn: Max
                if (rem_deg[p] > 0) {
                    if (d + c > max_cand[p]) max_cand[p] = d + c;
                    rem_deg[p]--;
                    if (rem_deg[p] == 0) {
                        dist[1][p] = max_cand[p];
                        pq.push({max_cand[p], 1, p});
                    }
                }
            }
        }
    }

    if (dist[0][start_v] == -1) {
        cout << "INFINITY\n";
    } else {
        cout << dist[0][start_v] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
