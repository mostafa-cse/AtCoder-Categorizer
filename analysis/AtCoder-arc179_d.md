# Problem Analysis: AtCoder-arc179_d — D - Portable Gate

**Problem ID**: `AtCoder-arc179_d`  
**Contest**: `arc179`  
**Rating / Difficulty**: 2717  
**URL**: https://atcoder.jp/contests/arc179/tasks/arc179_d  
**VJudge Tag**: `[problem:AtCoder-arc179_d]`  
**Category File**: [`../categories/dynamic_programming_dp/portable_gate_tree_dp.md`](../categories/dynamic_programming_dp/portable_gate_tree_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Alice visits all vertices of a tree using a piece and a magical gate. Moving the piece to an adjacent vertex costs 1. Teleporting the piece to the gate or moving the gate to the piece costs 0. We want to find the minimum total movement cost to visit every vertex.

## 2. Core Observation & Invariant
The vertices visited by the gate form a connected subtree A containing the start vertex v. Any edge outside A belongs to a connected subtree B_i rooted at some l_i in A. In any subtree with m edges ending at depth d from its root, traversing all edges costs 2m - d. Since the sum of edges across all subtrees is N - 1, minimizing total cost is equivalent to maximizing the sum of saved endpoint distances sum(d). For a fixed root v, tree DP maintains: (1) height h(u), (2) dp0(u): max savings if u in A and the journey in A exits u to return to its parent, and (3) dp1(u): max savings if the journey in A terminates inside subtree u. Rerooting DP computes this for all possible roots v in O(N) time.

## 3. Step-by-Step Algorithm
1. 1. Root the tree arbitrarily and compute bottom-up tree DP messages: h(u) = 1 + max(h(c)), dp0(u) = sum(max(1 + h(c), dp0(c))), and dp1(u) = dp0(u) + max(0, max(1 + dp1(c) - max(1 + h(c), dp0(c)))).
2. 2. Define subtree message structure (h, val, diff) where val = max(1 + h, dp0) and diff = 1 + dp1 - val.
3. 3. Use prefix and suffix aggregates across children at each node to perform rerooting in O(deg(u)) per vertex.
4. 4. The maximum savings across all roots v is max_v dp1(v). The answer is 2*(N - 1) - max_v dp1(v).

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct SubtreeMsg {
    int h;     // height of subtree
    int val;   // max(1 + h, dp0)
    int diff;  // 1 + dp1 - val
};

int N;
vector<vector<int>> adj;
vector<SubtreeMsg> down;
int best_ans = 0;

void dfs_down(int u, int p) {
    int max_h = -1;
    int sum_val = 0;
    int max_diff = 0;

    for (int v : adj[u]) {
        if (v == p) continue;
        dfs_down(v, u);
        max_h = max(max_h, down[v].h);
        sum_val += down[v].val;
        max_diff = max(max_diff, down[v].diff);
    }

    int my_h = (max_h == -1 ? 0 : 1 + max_h);
    int my_dp0 = sum_val;
    int my_dp1 = my_dp0 + max_diff;
    int my_val = max(1 + my_h, my_dp0);
    int my_diff = 1 + my_dp1 - my_val;

    down[u] = {my_h, my_val, my_diff};
}

void dfs_reroot(int u, int p, SubtreeMsg up_msg) {
    vector<int> neighbors;
    vector<SubtreeMsg> msgs;

    for (int v : adj[u]) {
        if (v == p) {
            neighbors.push_back(v);
            msgs.push_back(up_msg);
        } else {
            neighbors.push_back(v);
            msgs.push_back(down[v]);
        }
    }

    int deg = neighbors.size();
    if (deg == 0) {
        best_ans = max(best_ans, 0);
        return;
    }

    // Compute answer when u is the root of the whole tree
    int total_val = 0;
    int max_diff = 0;
    for (int i = 0; i < deg; ++i) {
        total_val += msgs[i].val;
        max_diff = max(max_diff, msgs[i].diff);
    }
    int u_dp1 = total_val + max_diff;
    best_ans = max(best_ans, u_dp1);

    // Prefix and Suffix arrays
    vector<int> pref_h(deg + 1, -1), suff_h(deg + 1, -1);
    vector<int> pref_val(deg + 1, 0), suff_val(deg + 1, 0);
    vector<int> pref_diff(deg + 1, 0), suff_diff(deg + 1, 0);

    for (int i = 0; i < deg; ++i) {
        pref_h[i + 1] = max(pref_h[i], msgs[i].h);
        pref_val[i + 1] = pref_val[i] + msgs[i].val;
        pref_diff[i + 1] = max(pref_diff[i], msgs[i].diff);
    }
    for (int i = deg - 1; i >= 0; --i) {
        suff_h[i] = max(suff_h[i + 1], msgs[i].h);
        suff_val[i] = suff_val[i + 1] + msgs[i].val;
        suff_diff[i] = max(suff_diff[i + 1], msgs[i].diff);
    }

    for (int i = 0; i < deg; ++i) {
        int v = neighbors[i];
        if (v == p) continue;

        int rem_h_max = max(pref_h[i], suff_h[i + 1]);
        int rem_h = (rem_h_max == -1 ? 0 : 1 + rem_h_max);
        int rem_dp0 = pref_val[i] + suff_val[i + 1];
        int rem_max_diff = max(pref_diff[i], suff_diff[i + 1]);
        int rem_dp1 = rem_dp0 + rem_max_diff;

        int rem_val = max(1 + rem_h, rem_dp0);
        int rem_diff = 1 + rem_dp1 - rem_val;

        SubtreeMsg next_up = {rem_h, rem_val, rem_diff};
        dfs_reroot(v, u, next_up);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;

    adj.resize(N + 1);
    down.resize(N + 1);

    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs_down(1, 0);
    dfs_reroot(1, 0, {0, 0, 0});

    int ans = 2 * (N - 1) - best_ans;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
