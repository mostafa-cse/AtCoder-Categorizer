# Problem Analysis: AtCoder-arc161_c — Dyed by Majority (Odd Tree)

**Problem ID**: `AtCoder-arc161_c`  
**Contest**: `arc161`  
**Rating / Difficulty**: 1746  
**URL**: https://atcoder.jp/contests/arc161/tasks/arc161_c  
**VJudge Tag**: `[problem:AtCoder-arc161_c]`  
**Category File**: [`../categories/basics/tree_majority_forcing_bottom_up.md`](../categories/basics/tree_majority_forcing_bottom_up.md)  

- **Tag (Domain)**: `Greedy`  
- **Subtopic**: `Tree Algorithms`  
- **Topic (Skill)**: `Greedy Leaf-Upwards Forcing on Tree Majority Constraints`  

---

## 1. Problem Statement & Key Idea
Given a tree where every vertex has odd degree. Given target colors ('B' or 'W') for each vertex that must be the majority color among its neighbors. Construct a valid coloring of vertices or determine impossible.

**Key Insight**: Process vertices bottom-up by tree depth. Since degree d is odd, each vertex u needs >= (d + 1) / 2 neighbors matching S[u]. Propagating leaf constraints upwards forces parent colors greedily.

## 2. Core Observation & Invariant
A leaf has degree 1, so its unique neighbor's color is completely fixed by the leaf's required target. Working bottom-up, determine forced parent colors, assign any remaining unconstrained vertices arbitrarily, and verify validity.

## 3. Step-by-Step Algorithm
1. Root tree at 1. Compute BFS traversal order to process bottom-up.
2. Initialize color array with '?' (uncolored).
3. Process nodes bottom-up: for each node u, count already colored neighbors.
4. If parent must be colored S[u] to satisfy u's majority, force parent color.
5. If conflict occurs, output -1.
6. After bottom-up pass, fill remaining '?' with 'B'.
7. Verify all majority conditions; if any fails, output -1, else output colors.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    string s;
    cin >> s;

    vector<int> parent(n + 1, 0);
    vector<int> order;
    queue<int> q;

    parent[1] = 1;
    q.push(1);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
        for (int v : adj[u]) {
            if (v != parent[u]) {
                parent[v] = u;
                q.push(v);
            }
        }
    }

    reverse(order.begin(), order.end());
    string ans(n + 1, '?');
    vector<int> count_b(n + 1, 0), count_w(n + 1, 0);

    for (int u : order) {
        int deg = adj[u].size();
        int need = (deg + 1) / 2;

        char target = s[u - 1];
        if (target == 'B') {
            if (count_b[u] < need) {
                int p = parent[u];
                if (ans[p] == 'W') {
                    cout << -1 << "\n";
                    return;
                }
                ans[p] = 'B';
            }
        } else {
            if (count_w[u] < need) {
                int p = parent[u];
                if (ans[p] == 'B') {
                    cout << -1 << "\n";
                    return;
                }
                ans[p] = 'W';
            }
        }

        if (ans[u] == '?') ans[u] = 'B';
        if (u != 1) {
            int p = parent[u];
            if (ans[u] == 'B') count_b[p]++;
            else count_w[p]++;
        }
    }

    // Verify
    vector<int> final_b(n + 1, 0), final_w(n + 1, 0);
    for (int u = 1; u <= n; ++u) {
        for (int v : adj[u]) {
            if (ans[v] == 'B') final_b[u]++;
            else final_w[u]++;
        }
    }

    for (int u = 1; u <= n; ++u) {
        char maj = (final_b[u] > final_w[u]) ? 'B' : 'W';
        if (maj != s[u - 1]) {
            cout << -1 << "\n";
            return;
        }
    }

    cout << ans.substr(1) << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bottom-up leaf forcing and greedy coloring on trees with odd-degree constraints.
- **Reusable Pattern**: `Tree Majority Bottom-Up Forcing: Satisfy child constraints by forcing parent colors.`
