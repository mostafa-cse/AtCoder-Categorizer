# Problem Analysis: AtCoder-abc209_e — Shiritori

**Problem ID**: `AtCoder-abc209_e`  
**Contest**: `abc209`  
**Rating / Difficulty**: 2153  
**URL**: https://atcoder.jp/contests/abc209/tasks/abc209_e  
**VJudge Tag**: `[problem:AtCoder-abc209_e]`  
**Category File**: [`../categories/game_theory/retrograde_analysis_directed_cyclic_graphs.md`](../categories/game_theory/retrograde_analysis_directed_cyclic_graphs.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Graph Games`  
- **Topic (Skill)**: `Games on Arbitrary Graphs`  

---

## 1. Problem Statement & Key Idea
Model 3-character prefix/suffix word transitions as a directed graph. Determine whether Takahashi wins, Aoki wins, or the game draws if Takahashi plays word s_i first. Since cycles allow infinite play (Draw), classify vertex outcomes (Win/Lose/Draw) via retrograde analysis BFS on the reversed graph.

## 2. Core Observation & Invariant
When Takahashi says s_i, Aoki moves from vertex v = suffix3(s_i). In a finite impartial/normal play game on a directed graph with cycles: a state is LOSE if out-degree is 0 or all outgoing edges lead to WIN; a state is WIN if at least one outgoing edge leads to LOSE; all remaining undetermined states are DRAW. Retrograde BFS propagates known states backwards along reverse edges.

## 3. Step-by-Step Algorithm
1. Compress 3-letter prefixes and suffixes into integer vertex IDs. Add directed edges u -> v for each word.
2. Compute out-degrees for all vertices and build the reversed adjacency list.
3. Initialize a queue with all vertices having out_degree == 0, marking them as LOSE (-1).
4. Perform retrograde BFS: when popping a LOSE vertex v, any predecessor u can transition to LOSE, so mark u as WIN (+1) and push to queue. When popping a WIN vertex v, decrement out_degree[u]; if out_degree[u] reaches 0, all moves from u lead to WIN, so mark u as LOSE (-1) and push to queue.
5. For each word s_i with target suffix vertex v: if state[v] == -1, Aoki loses so Takahashi wins; if state[v] == 1, Aoki wins; if state[v] == 0, the outcome is Draw.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> s(n);
    map<string, int> str_to_id;
    auto get_id = [&](const string& str) {
        if (!str_to_id.count(str)) {
            int id = str_to_id.size();
            str_to_id[str] = id;
        }
        return str_to_id[str];
    };

    vector<pair<int, int>> edges(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
        string pre = s[i].substr(0, 3);
        string suf = s[i].substr(s[i].length() - 3, 3);
        edges[i] = {get_id(pre), get_id(suf)};
    }

    int V = str_to_id.size();
    vector<vector<int>> rev_adj(V);
    vector<int> out_deg(V, 0);

    for (int i = 0; i < n; ++i) {
        int u = edges[i].first;
        int v = edges[i].second;
        rev_adj[v].push_back(u);
        out_deg[u]++;
    }

    vector<int> state(V, 0); // 0 = Draw, 1 = Win, -1 = Lose
    queue<int> q;

    for (int i = 0; i < V; ++i) {
        if (out_deg[i] == 0) {
            state[i] = -1;
            q.push(i);
        }
    }

    while (!q.empty()) {
        int v = q.front();
        q.pop();

        for (int u : rev_adj[v]) {
            if (state[u] != 0) continue;

            if (state[v] == -1) {
                state[u] = 1;
                q.push(u);
            } else if (state[v] == 1) {
                out_deg[u]--;
                if (out_deg[u] == 0) {
                    state[u] = -1;
                    q.push(u);
                }
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        int target = edges[i].second;
        if (state[target] == -1) {
            cout << "Takahashi\n";
        } else if (state[target] == 1) {
            cout << "Aoki\n";
        } else {
            cout << "Draw\n";
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
