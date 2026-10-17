# Problem Analysis: AtCoder-arc015_3 — C. 変わった単位

**Problem ID**: `AtCoder-arc015_3`  
**Contest**: `arc015`  
**Rating / Difficulty**: 2185  
**URL**: https://atcoder.jp/contests/arc015/tasks/arc015_3  
**VJudge Tag**: `[problem:AtCoder-arc015_3]`  
**Category File**: [`../categories/graph_theory/multiplicative_potential_tree_traversal.md`](../categories/graph_theory/multiplicative_potential_tree_traversal.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Depth First Search (DFS)`  

---

## 1. Problem Statement & Key Idea
Given N <= 200 unit conversion rules 1 large = m small, find the largest unit and smallest unit that maximize the conversion factor M, and output 1large=Msmall. Unit conversions form a connected multiplicative tree.

## 2. Core Observation & Invariant
The problem guarantees a consistent multiplicative system where the maximum conversion factor fits in a 64-bit integer <= 10^9. Rooting the tree at an arbitrary vertex with reference potential 1.0 and propagating ratios pot[v] = pot[u] / m for edge 1 u = m v allows finding the maximum potential unit (largest) and minimum potential unit (smallest) via DFS.

## 3. Step-by-Step Algorithm
1. Map unit string names to vertex IDs.
2. For each conversion 1 u = m v, add directed edge u -> v with weight m and reverse edge v -> u with weight 1/m.
3. Run DFS from an arbitrary unit with initial potential 1.0. For each neighbor v with edge multiplier w, set pot[v] = pot[u] / w and recurse.
4. Find the vertex max_idx with maximum potential and min_idx with minimum potential.
5. Compute factor = round(pot[max_idx] / pot[min_idx]). Output 1<max_unit>=<factor><min_unit>.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cmath>
#include <iomanip>

using namespace std;

struct Edge {
    int to;
    double mult; // 1 * u = mult * to
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    map<string, int> name_to_id;
    vector<string> id_to_name;

    auto get_id = [&](const string& s) {
        if (name_to_id.find(s) == name_to_id.end()) {
            name_to_id[s] = (int)id_to_name.size();
            id_to_name.push_back(s);
        }
        return name_to_id[s];
    };

    vector<vector<Edge>> adj(500);

    for (int i = 0; i < N; ++i) {
        string large, small;
        double m;
        cin >> large >> m >> small;
        int u = get_id(large);
        int v = get_id(small);
        adj[u].push_back({v, m});
        adj[v].push_back({u, 1.0 / m});
    }

    int V = (int)id_to_name.size();
    vector<bool> vis(V, false);
    vector<double> pot(V, 0.0);

    auto dfs = [&](auto& self, int u) -> void {
        vis[u] = true;
        for (auto const& e : adj[u]) {
            if (!vis[e.to]) {
                pot[e.to] = pot[u] / e.mult;
                self(self, e.to);
            }
        }
    };

    pot[0] = 1.0;
    dfs(dfs, 0);

    int max_idx = 0, min_idx = 0;
    for (int i = 1; i < V; ++i) {
        if (pot[i] > pot[max_idx]) max_idx = i;
        if (pot[i] < pot[min_idx]) min_idx = i;
    }

    long long factor = (long long)round(pot[max_idx] / pot[min_idx]);

    cout << "1" << id_to_name[max_idx] << "=" << factor << id_to_name[min_idx] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
