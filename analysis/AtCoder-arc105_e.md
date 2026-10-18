# Problem Analysis: AtCoder-arc105_e — E. Keep Graph Disconnected

**Problem ID**: `AtCoder-arc105_e`  
**Contest**: `arc105`  
**Rating / Difficulty**: 2615  
**URL**: https://atcoder.jp/contests/arc105/tasks/arc105_e  
**VJudge Tag**: `[problem:AtCoder-arc105_e]`  
**Category File**: [`../categories/game_theory/keep_graph_disconnected_component_parity.md`](../categories/game_theory/keep_graph_disconnected_component_parity.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Graph Games`  
- **Topic (Skill)**: `Games on Arbitrary Graphs`  

---

## 1. Problem Statement & Key Idea
Two players alternate adding an edge such that vertex 1 and vertex N remain disconnected. Normal play convention. Determine whether First or Second wins under optimal play.

## 2. Core Observation & Invariant
The game terminates when the graph is partitioned into two complete components of sizes n and N-n. Total edges is N(N-1)/2 - n(N-n). If N is odd, n(N-n) is always even, so total moves has fixed parity N(N-1)/2 - M. If N is even, parity depends on whether initial components containing 1 and N have same or different parity.

## 3. Step-by-Step Algorithm
1. Find connected component sizes x and y of vertex 1 and N via BFS.
2. If N is odd: First wins iff (N(N-1)/2 - M) is odd.
3. If N is even: if x % 2 != y % 2, First always wins; otherwise First wins iff (N(N-1)/2 - x*y - M) is odd.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

void solve_test() {
    int N, M;
    if (!(cin >> N >> M)) return;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto get_comp_size = [&](int start) {
        vector<bool> visited(N + 1, false);
        vector<int> q = {start};
        visited[start] = true;
        int size = 0;
        int head = 0;
        while (head < (int)q.size()) {
            int u = q[head++];
            size++;
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push_back(v);
                }
            }
        }
        return size;
    };

    long long total_max_edges = (long long)N * (N - 1) / 2;

    if (N % 2 == 1) {
        if ((total_max_edges - M) % 2 == 1) {
            cout << "First\n";
        } else {
            cout << "Second\n";
        }
    } else {
        int x = get_comp_size(1);
        int y = get_comp_size(N);
        if (x % 2 != y % 2) {
            cout << "First\n";
        } else {
            long long rem = total_max_edges - (long long)x * y - M;
            if (rem % 2 == 1 || rem % 2 == -1) {
                cout << "First\n";
            } else {
                cout << "Second\n";
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) {
            solve_test();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
