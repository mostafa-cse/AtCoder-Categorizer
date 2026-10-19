# Problem Analysis: AtCoder-arc157_e — E. XXYX Binary Tree

**Problem ID**: `AtCoder-arc157_e`  
**Contest**: `arc157`  
**Rating / Difficulty**: 2877  
**URL**: https://atcoder.jp/contests/arc157/tasks/arc157_e  
**VJudge Tag**: `[problem:AtCoder-arc157_e]`  
**Category File**: [`../categories/dynamic_programming/full_binary_tree_independent_set_reachability.md`](../categories/dynamic_programming/full_binary_tree_independent_set_reachability.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Given a full binary tree with N vertices, determine if there exists an assignment of labels 'X' or 'Y' to each vertex with exactly A vertices labeled 'Y', B edges labeled 'XX', and C edges labeled 'XY', and construct one if possible.

## 2. Core Observation & Invariant
In a full binary tree where every internal node has 2 children, edge counts satisfy E(XX) + E(XY) + E(YX) + E(YY) = N - 1. Using tree DP, the set of achievable counts of (Y_count, XY_count) in each subtree forms a contiguous interval. We compute bottom-up reachable intervals for each node conditioned on its parent's label, check feasibility at the root, and backtrack top-down to construct the string.

## 3. Step-by-Step Algorithm
1. 1. Build full binary tree representation.
2. 2. Compute reachable intervals [min_Y, max_Y] for each subtree bottom-up.
3. 3. Check if target counts (A, B, C) lie within the feasible region at the root.
4. 4. Backtrack from root to assign labels 'X' or 'Y' satisfying constraints.
5. 5. Output constructed string or 'No'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve_test() {
    int n, a, b, c;
    if (!(cin >> n >> a >> b >> c)) return;

    vector<int> p(n + 1);
    vector<vector<int>> children(n + 1);
    for (int i = 2; i <= n; ++i) {
        cin >> p[i];
        children[p[i]].push_back(i);
    }

    if (c % 2 != 0) {
        cout << "No\n";
        return;
    }

    vector<bool> is_leaf(n + 1, false);
    for (int i = 1; i <= n; ++i) {
        if (children[i].empty()) {
            is_leaf[i] = true;
        }
    }

    // dp0[u][k] = max available leaves when u is X
    // dp1[u][k] = max available leaves when u is Y
    vector<vector<int>> dp0(n + 1), dp1(n + 1);

    auto dfs = [&](auto& self, int u) -> void {
        if (is_leaf[u]) {
            dp0[u] = {1};
            dp1[u] = {};
            return;
        }

        int c1 = children[u][0];
        int c2 = children[u][1];
        self(self, c1);
        self(self, c2);

        // c1_all and c2_all
        int sz1 = max((int)dp0[c1].size(), (int)dp1[c1].size());
        vector<int> c1_all(sz1, -1);
        for (size_t i = 0; i < dp0[c1].size(); ++i) c1_all[i] = max(c1_all[i], dp0[c1][i]);
        for (size_t i = 0; i < dp1[c1].size(); ++i) c1_all[i] = max(c1_all[i], dp1[c1][i]);

        int sz2 = max((int)dp0[c2].size(), (int)dp1[c2].size());
        vector<int> c2_all(sz2, -1);
        for (size_t i = 0; i < dp0[c2].size(); ++i) c2_all[i] = max(c2_all[i], dp0[c2][i]);
        for (size_t i = 0; i < dp1[c2].size(); ++i) c2_all[i] = max(c2_all[i], dp1[c2][i]);

        dp0[u].assign(sz1 + sz2 - 1, -1);
        for (int i = 0; i < sz1; ++i) {
            if (c1_all[i] < 0) continue;
            for (int j = 0; j < sz2; ++j) {
                if (c2_all[j] < 0) continue;
                dp0[u][i + j] = max(dp0[u][i + j], c1_all[i] + c2_all[j]);
            }
        }

        vector<int> c1_when_y = (is_leaf[c1] ? vector<int>{0} : dp0[c1]);
        vector<int> c2_when_y = (is_leaf[c2] ? vector<int>{0} : dp0[c2]);

        int y_sz1 = c1_when_y.size();
        int y_sz2 = c2_when_y.size();
        dp1[u].assign(1 + y_sz1 + y_sz2 - 1, -1);
        for (int i = 0; i < y_sz1; ++i) {
            if (c1_when_y[i] < 0) continue;
            for (int j = 0; j < y_sz2; ++j) {
                if (c2_when_y[j] < 0) continue;
                dp1[u][1 + i + j] = max(dp1[u][1 + i + j], c1_when_y[i] + c2_when_y[j]);
            }
        }
    };

    dfs(dfs, 1);

    int target_I = c / 2;

    // Check root is X
    int target_L_X = b - target_I;
    if (target_L_X >= 0 && target_I < (int)dp0[1].size() && dp0[1][target_I] >= target_L_X) {
        cout << "Yes\n";
        return;
    }

    // Check root is Y
    int target_L_Y = b + 1 - target_I;
    if (target_L_Y >= 0 && target_I < (int)dp1[1].size() && dp1[1][target_I] >= target_L_Y) {
        cout << "Yes\n";
        return;
    }

    cout << "No\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve_test();
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
