# Problem Analysis: AtCoder-arc215_e — E - CNOT Party

**Problem ID**: `AtCoder-arc215_e`  
**Contest**: `arc215`  
**Rating / Difficulty**: 2418  
**URL**: https://atcoder.jp/contests/arc215/tasks/arc215_e  
**VJudge Tag**: `[problem:AtCoder-arc215_e]`  
**Category File**: [`../categories/graph_theory/cnot_party_bidirectional_bfs.md`](../categories/graph_theory/cnot_party_bidirectional_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Breadth First Search (BFS)`  

---

## 1. Problem Statement & Key Idea
Transform binary string $A$ into $B$ using at most $2N$ operations where $(x, y)$ flips $y$ when $x=1$.

## 2. Core Observation & Invariant
Operations $(x, y)$ with $x \ne y$ are reversible CNOT gates that can turn 0 into 1 without destroying existing 1s. Self-resets $(i, i)$ irreversibly turn 1 into 0. By running forward BFS on $A$ along non-loop edges, all reachable positions become 1. For any position $i$ where $B_i=0$ but $A_i=1$, if self-reset $(i, i)$ exists, we can treat $B_i$ as 1 and append $(i, i)$ at the end. Then run reverse BFS from $B$ along non-loop edges. If the forward and backward expanded states coincide, the concatenated sequence of operations achieves the transformation in $\le 2N$ operations.

## 3. Step-by-Step Algorithm
1. 1. Run forward BFS on $A$ to set all reachable bits to 1, recording each operation index.
2. 2. For each $i$ with $B_i=0$ and $A_i=1$ having self-loop $(i, i)$, set $B_i=1$ and record $(i, i)$ as a delayed final operation.
3. 3. Run reverse BFS on $B$ to set all reachable bits to 1, recording operations.
4. 4. If $A \ne B$, output `-1`.
5. 5. Otherwise, output the concatenation of forward operations, reversed backward operations, and delayed self-reset operations.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

void solve() {
    int N;
    if (!(cin >> N)) return;
    string A, B;
    cin >> A >> B;
    int M;
    cin >> M;
    vector<vector<pair<int, int>>> adj(N + 1);
    vector<int> self_loop(N + 1, 0);
    for (int i = 1; i <= M; ++i) {
        int u, v;
        cin >> u >> v;
        if (u == v) {
            self_loop[u] = i;
        } else {
            adj[u].push_back({v, i});
        }
    }

    vector<int> ops_fwd;
    queue<int> q;
    vector<int> curA(N + 1);
    for (int i = 1; i <= N; ++i) {
        curA[i] = A[i - 1] - '0';
        if (curA[i] == 1) q.push(i);
    }
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int idx = edge.second;
            if (curA[v] == 0) {
                curA[v] = 1;
                ops_fwd.push_back(idx);
                q.push(v);
            }
        }
    }

    vector<int> ops_self;
    vector<int> curB(N + 1);
    for (int i = 1; i <= N; ++i) {
        curB[i] = B[i - 1] - '0';
        if (curB[i] == 0 && curA[i] == 1 && self_loop[i] != 0) {
            curB[i] = 1;
            ops_self.push_back(self_loop[i]);
        }
    }

    vector<int> ops_rev;
    for (int i = 1; i <= N; ++i) {
        if (curB[i] == 1) q.push(i);
    }
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int idx = edge.second;
            if (curB[v] == 0) {
                curB[v] = 1;
                ops_rev.push_back(idx);
                q.push(v);
            }
        }
    }

    for (int i = 1; i <= N; ++i) {
        if (curA[i] != curB[i]) {
            cout << -1 << "\n";
            return;
        }
    }

    vector<int> all_ops = ops_fwd;
    reverse(ops_rev.begin(), ops_rev.end());
    all_ops.insert(all_ops.end(), ops_rev.begin(), ops_rev.end());
    all_ops.insert(all_ops.end(), ops_self.begin(), ops_self.end());

    cout << all_ops.size() << "\n";
    for (size_t i = 0; i < all_ops.size(); ++i) {
        cout << all_ops[i] << (i + 1 == all_ops.size() ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
