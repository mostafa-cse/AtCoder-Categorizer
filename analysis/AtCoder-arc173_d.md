# Problem Analysis: AtCoder-arc173_d — D. Bracket Walk

**Problem ID**: `AtCoder-arc173_d`  
**Contest**: `arc173`  
**Rating / Difficulty**: 2598  
**URL**: https://atcoder.jp/contests/arc173/tasks/arc173_d  
**VJudge Tag**: `[problem:AtCoder-arc173_d]`  
**Category File**: [`../categories/graph_theory/bracket_walk_bellman_ford_cycle_detection.md`](../categories/graph_theory/bracket_walk_bellman_ford_cycle_detection.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Cycles`  
- **Topic (Skill)**: `Cycle Detection`  

---

## 1. Problem Statement & Key Idea
Determine if a strongly connected graph with '(' and ')' edges admits a closed walk covering every edge that forms a regular bracket sequence.

## 2. Core Observation & Invariant
With '(' as $+1$ and ')' as $-1$, a closed walk covering all edges can balance to 0 while keeping all prefix sums $\ge 0$ iff either: (1) both positive and negative cycles exist (allowing arbitrary balance pump and deflation), or (2) all cycles have weight 0 (potential field ensures zero net sum). A walk is impossible iff strictly one sign of cycles exists.

## 3. Step-by-Step Algorithm
1. 1. Assign weight $+1$ for '(' and $-1$ for ')'.
2. 2. Run Bellman-Ford / SPFA to detect negative cycles.
3. 3. Negate edge weights and run Bellman-Ford / SPFA to detect positive cycles.
4. 4. Output Yes if `has_negative_cycle == has_positive_cycle`, otherwise No.

## 4. Complexity Analysis
- **Time Complexity**: `O(N M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int u, v, w;
};

bool has_negative_cycle(int N, const vector<Edge>& edges) {
    vector<int> dist(N + 1, 0);
    for (int iter = 0; iter < N; ++iter) {
        bool updated = false;
        for (const auto& e : edges) {
            if (dist[e.u] + e.w < dist[e.v]) {
                dist[e.v] = dist[e.u] + e.w;
                updated = true;
            }
        }
        if (!updated) return false;
    }
    for (const auto& e : edges) {
        if (dist[e.u] + e.w < dist[e.v]) {
            return true;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<Edge> edges_neg, edges_pos;
    for (int i = 0; i < M; ++i) {
        int u, v;
        char c;
        cin >> u >> v >> c;
        int w = (c == '(' ? 1 : -1);
        edges_neg.push_back({u, v, w});
        edges_pos.push_back({u, v, -w});
    }

    bool has_neg = has_negative_cycle(N, edges_neg);
    bool has_pos = has_negative_cycle(N, edges_pos);

    if (has_neg == has_pos) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
