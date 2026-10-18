# Problem Analysis: AtCoder-agc010_c — C. Cleaning

**Problem ID**: `AtCoder-agc010_c`  
**Contest**: `agc010`  
**Rating / Difficulty**: 2346  
**URL**: https://atcoder.jp/contests/agc010/tasks/agc010_c  
**VJudge Tag**: `[problem:AtCoder-agc010_c]`  
**Category File**: [`../categories/dynamic_programming/tree_path_capacity_pairing_dp.md`](../categories/dynamic_programming/tree_path_capacity_pairing_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Determine if all stones on tree vertices can be removed by subtracting 1 along leaf-to-leaf paths. Rooted tree DP computes the required upward path capacity $c_v = 2 A_v - \sum c_w$ and verifies internal pairability in $O(N)$.

## 2. Core Observation & Invariant
Every path operation connects two leaves. In the tree rooted at a non-leaf vertex, each child $w$ passes $c_w$ paths upward to vertex $v$. To cover $A_v$ stones at $v$, the number of paths paired internally at $v$ must be $P = \sum c_w - A_v$, and the upward paths to parent must be $c_v = 2 A_v - \sum c_w$. Valid pairing requires $0 \le P \le A_v$ and $\max(c_w) \le A_v$.

## 3. Step-by-Step Algorithm
1. Root the tree at an arbitrary vertex of degree $\ge 2$ (handling $N=2$ as a base case $A_1 == A_2$).
2. Perform post-order DFS: leaves return $A_{\text{leaf}}$.
3. At internal vertex $v$, sum upward capacities from children $S = \sum c_w$. Check $S \ge A_v$, $2 A_v \ge S$, and $\max(c_w) \le A_v$. If violated, return impossible.
4. Propagate $c_v = 2 A_v - S$ upwards. At root $R$, verify $c_R == 0$ in $O(N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    if (N == 2) {
        if (A[1] == A[2]) cout << "YES\n";
        else cout << "NO\n";
        return 0;
    }

    int root = 1;
    for (int i = 1; i <= N; ++i) {
        if (adj[i].size() > 1) {
            root = i;
            break;
        }
    }

    bool possible = true;

    auto dfs = [&](auto& self, int u, int p) -> long long {
        if (!possible) return 0;
        if (adj[u].size() == 1 && u != root) {
            // leaf
            return A[u];
        }

        long long sum_c = 0;
        long long max_c = 0;
        for (int v : adj[u]) {
            if (v == p) continue;
            long long c = self(self, v, u);
            sum_c += c;
            max_c = max(max_c, c);
        }

        long long P = sum_c - A[u];
        long long up = 2 * A[u] - sum_c;

        if (P < 0 || up < 0 || max_c > A[u]) {
            possible = false;
            return 0;
        }

        return up;
    };

    long long root_up = dfs(dfs, root, 0);
    if (possible && root_up == 0) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
