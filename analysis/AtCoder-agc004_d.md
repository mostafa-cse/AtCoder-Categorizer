# Problem Analysis: AtCoder-agc004_d — D. Teleporter

**Problem ID**: `AtCoder-agc004_d`  
**Contest**: `agc004`  
**Rating / Difficulty**: 2346  
**URL**: https://atcoder.jp/contests/agc004/tasks/agc004_d  
**VJudge Tag**: `[problem:AtCoder-agc004_d]`  
**Category File**: [`../categories/basics/teleporter_tree_bottom_up_pruning.md`](../categories/basics/teleporter_tree_bottom_up_pruning.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Given a teleporter graph, find the minimum changes so every town reaches town 1 in exactly $K$ steps. Forces $a_1=1$ and prunes subtrees exceeding height $K-1$ greedily bottom-up in $O(N)$.

## 2. Core Observation & Invariant
For every city to reach capital 1 in exactly $K$ steps, city 1 must have a self-loop ($a_1 = 1$), forming a directed rooted tree towards 1 where every node has depth $\le K$. Any redirected edge is optimally pointed directly to root 1. Pruning subtrees greedily from the bottom up whenever a node's subtree height reaches $K-1$ minimizes edge modifications.

## 3. Step-by-Step Algorithm
1. If $a_1 \ne 1$, increment answer by 1 and set $a_1 = 1$.
2. Perform a bottom-up post-order DFS on the tree rooted at 1.
3. For each node $u \ne 1$, if its maximum distance to any leaf in its current subtree reaches $K - 1$ and $a_u \ne 1$, cut the edge $(u, a_u)$, reconnect $u$ directly to 1, increment answer by 1, and reset height to $-1$.
4. Runs in $O(N)$ time with a single DFS pass.

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
    long long K;
    if (!(cin >> N >> K)) return 0;

    vector<int> a(N + 1);
    int ans = 0;
    for (int i = 1; i <= N; ++i) {
        cin >> a[i];
    }

    if (a[1] != 1) {
        ans++;
        a[1] = 1;
    }

    vector<vector<int>> children(N + 1);
    for (int i = 2; i <= N; ++i) {
        children[a[i]].push_back(i);
    }

    // dfs returns height of subtree rooted at u (distance to deepest descendant)
    auto dfs = [&](auto& self, int u) -> int {
        int max_h = 0;
        for (int v : children[u]) {
            int h = self(self, v);
            max_h = max(max_h, h + 1);
        }
        if (u != 1 && a[u] != 1 && max_h == K - 1) {
            ans++;
            return -1; // cut u and connect directly to 1
        }
        return max_h;
    };

    dfs(dfs, 1);

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
