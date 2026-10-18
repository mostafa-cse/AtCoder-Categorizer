# Problem Analysis: AtCoder-arc146_d — >=<

**Problem ID**: `AtCoder-arc146_d`  
**Contest**: `arc146`  
**Rating / Difficulty**: 2663  
**URL**: https://atcoder.jp/contests/arc146/tasks/arc146_d  
**VJudge Tag**: `[problem:AtCoder-arc146_d]`  
**Category File**: [`../categories/graph_theory/monotonic_inequalities_bfs.md`](../categories/graph_theory/monotonic_inequalities_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Breadth First Search (BFS)`  

---

## 1. Problem Statement & Key Idea
Minimizing the sum of sequence elements under trichotomy constraints (both <, both =, or both >) reduces to monotonic lower bound propagation via queue-based BFS.

## 2. Core Observation & Invariant
Each constraint (P, X, Q, Y) implies: if A_P >= X then A_Q >= Y; if A_P >= X+1 then A_Q >= Y+1 (and symmetrically). Maintaining lower bounds L[v] initialized to 1, any increase in L[P] triggers only thresholds <= L[P]. Since lower bounds only increase and each trigger is processed at most once, the propagation terminates at the unique minimal valid sequence, or detects impossibility if any L[v] > M.

## 3. Step-by-Step Algorithm
1. 1. Initialize lower bounds L[v] = 1 for all v in 1..N.
2. 2. Store sorted triggers for each variable v: threshold X -> target (Q, Y) and threshold X+1 -> target (Q, Y+1).
3. 3. Push all variables into a queue.
4. 4. While queue is not empty, pop u and fire all triggers with threshold <= L[u], updating target lower bounds.
5. 5. If any L[v] > M, return -1.
6. 6. Output sum of L[v].

## 4. Complexity Analysis
- **Time Complexity**: `O(N + K log K)`
- **Space Complexity**: `O(N + K)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Trigger {
    int threshold;
    int target_var;
    int target_val;

    bool operator<(const Trigger& other) const {
        return threshold < other.threshold;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, K;
    if (!(cin >> N >> M >> K)) return 0;

    vector<vector<Trigger>> adj(N + 1);
    for (int i = 0; i < K; ++i) {
        int P, X, Q, Y;
        cin >> P >> X >> Q >> Y;
        adj[P].push_back({X, Q, Y});
        adj[P].push_back({X + 1, Q, Y + 1});
        adj[Q].push_back({Y, P, X});
        adj[Q].push_back({Y + 1, P, X + 1});
    }

    for (int v = 1; v <= N; ++v) {
        sort(adj[v].begin(), adj[v].end());
    }

    vector<int> L(N + 1, 1);
    vector<int> ptr(N + 1, 0);
    queue<int> q;

    for (int v = 1; v <= N; ++v) {
        q.push(v);
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        while (ptr[u] < (int)adj[u].size() && adj[u][ptr[u]].threshold <= L[u]) {
            const auto& trig = adj[u][ptr[u]];
            ptr[u]++;

            if (trig.target_val > M) {
                cout << -1 << "\n";
                return 0;
            }

            if (trig.target_val > L[trig.target_var]) {
                L[trig.target_var] = trig.target_val;
                q.push(trig.target_var);
            }
        }
    }

    for (int v = 1; v <= N; ++v) {
        if (L[v] > M) {
            cout << -1 << "\n";
            return 0;
        }
    }

    long long sum = 0;
    for (int v = 1; v <= N; ++v) {
        sum += L[v];
    }

    cout << sum << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
