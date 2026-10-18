# Problem Analysis: AtCoder-arc079_d — F - Namori Grundy

**Problem ID**: `AtCoder-arc079_d`  
**Contest**: `arc079`  
**Rating / Difficulty**: 2636  
**URL**: https://atcoder.jp/contests/arc079/tasks/arc079_d  
**VJudge Tag**: `[problem:AtCoder-arc079_d]`  
**Category File**: [`../categories/game_theory/namori_grundy_cycle_mex.md`](../categories/game_theory/namori_grundy_cycle_mex.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
Given a directed functional graph where each vertex has out-degree 1, determine if there exists an assignment of non-negative integers g_u such that g_u = mex{g_v | u -> v}.

## 2. Core Observation & Invariant
The graph consists of a directed cycle with attached directed trees rooted along the cycle. Vertices with out-degree 0 (sinks) have Grundy value 0. In-tree vertices have uniquely determined Grundy values by bottom-up mex evaluation. For the cycle, each cycle vertex c_i has a set of values from its non-cycle predecessors. There are at most 2 candidate Grundy values for any cycle vertex. Testing both candidates and verifying cycle consistency resolves the problem in O(N).

## 3. Step-by-Step Algorithm
1. Find in-degrees and identify the directed cycle using Kahn's algorithm.
2. For all trees branching into the cycle, compute Grundy values using topological sorting.
3. For each cycle node, compute the set of Grundy values of its tree children.
4. Select one cycle vertex r, identify its two smallest candidate values not in its children's set.
5. Simulate propagation of candidate around the cycle.
6. If propagation returns the same candidate value at r, output POSSIBLE, else IMPOSSIBLE.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> P(N + 1);
    vector<vector<int>> out_adj(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> P[i];
        out_adj[P[i]].push_back(i);
    }

    vector<int> out_deg(N + 1);
    for (int i = 1; i <= N; ++i) {
        out_deg[i] = (int)out_adj[i].size();
    }

    queue<int> q;
    for (int i = 1; i <= N; ++i) {
        if (out_deg[i] == 0) q.push(i);
    }

    vector<bool> in_cycle(N + 1, true);
    vector<vector<int>> tree_vals(N + 1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        in_cycle[u] = false;

        sort(tree_vals[u].begin(), tree_vals[u].end());
        int mex = 0;
        for (int val : tree_vals[u]) {
            if (val == mex) mex++;
            else if (val > mex) break;
        }

        int p = P[u];
        tree_vals[p].push_back(mex);
        out_deg[p]--;
        if (out_deg[p] == 0) {
            q.push(p);
        }
    }

    int start_node = -1;
    for (int i = 1; i <= N; ++i) {
        if (in_cycle[i]) {
            start_node = i;
            break;
        }
    }

    if (start_node == -1) {
        cout << "POSSIBLE\n";
        return 0;
    }

    vector<int> cycle;
    int curr = start_node;
    while (true) {
        cycle.push_back(curr);
        int nxt = -1;
        for (int v : out_adj[curr]) {
            if (in_cycle[v]) {
                nxt = v;
                break;
            }
        }
        if (nxt == start_node) break;
        curr = nxt;
    }

    int K = (int)cycle.size();
    vector<int> m(K), m2(K);
    for (int i = 0; i < K; ++i) {
        int u = cycle[i];
        sort(tree_vals[u].begin(), tree_vals[u].end());
        tree_vals[u].erase(unique(tree_vals[u].begin(), tree_vals[u].end()), tree_vals[u].end());

        int mex = 0;
        for (int val : tree_vals[u]) {
            if (val == mex) mex++;
            else if (val > mex) break;
        }
        m[i] = mex;

        int mex2 = mex + 1;
        for (int val : tree_vals[u]) {
            if (val == mex2) mex2++;
            else if (val > mex2) break;
        }
        m2[i] = mex2;
    }

    auto check = [&](int val0) -> bool {
        int cur_val = val0;
        for (int i = K - 1; i >= 0; --i) {
            int next_val = (cur_val == m[i]) ? m2[i] : m[i];
            cur_val = next_val;
        }
        return cur_val == val0;
    };

    if (check(m[0]) || check(m2[0])) {
        cout << "POSSIBLE\n";
    } else {
        cout << "IMPOSSIBLE\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
