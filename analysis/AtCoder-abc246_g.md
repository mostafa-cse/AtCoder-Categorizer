# Problem Analysis: AtCoder-abc246_g — G. Game on Tree 3

**Problem ID**: `AtCoder-abc246_g`  
**Contest**: `abc246`  
**Rating / Difficulty**: 2313  
**URL**: https://atcoder.jp/contests/abc246/tasks/abc246_g  
**VJudge Tag**: `[problem:AtCoder-abc246_g]`  
**Category File**: [`../categories/dynamic_programming/tree_game_binary_search_defense_dp.md`](../categories/dynamic_programming/tree_game_binary_search_defense_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
In a tree game on $N$ vertices with root 1 and values $A_i$, Takahashi moves a piece downward while Aoki zeroes out an unvisited vertex. Takahashi wants to maximize the final value; Aoki wants to minimize it. Determine Takahashi's optimal score.

## 2. Core Observation & Invariant
To prevent Takahashi from reaching any vertex with score $\ge X$, Aoki must spend at least $\max(0, \sum_{v \in children(u)} dp[v] - 1) + [A_u \ge X]$ moves within the subtree of $u$ before Takahashi enters $u$.

## 3. Step-by-Step Algorithm
1. Binary search on the achievable score $X \in [1, 10^9]$.
2. For a fixed threshold $X$, run a bottom-up tree DP where $dp[u] = \max(0, \sum_{v \in children(u)} dp[v] - 1) + [A_u \ge X]$ for $u \neq 1$.
3. At root 1, Aoki can defend if and only if $\sum_{v \in children(1)} dp[v] \le 1$, achieving an $O(N \log(\max A))$ solution.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log (\max A_i))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1, 0);
    for (int i = 2; i <= n; ++i) {
        cin >> a[i];
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> parent(n + 1, 0);
    vector<int> order;
    order.reserve(n);
    vector<bool> vis(n + 1, false);

    queue<int> q;
    q.push(1);
    vis[1] = true;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);
        for (int v : adj[u]) {
            if (!vis[v]) {
                vis[v] = true;
                parent[v] = u;
                q.push(v);
            }
        }
    }

    vector<long long> dp(n + 1, 0);
    auto check = [&](long long x) -> bool {
        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            long long s = 0;
            for (int v : adj[u]) {
                if (v != parent[u]) {
                    s += dp[v];
                }
            }
            if (u == 1) {
                dp[u] = s;
            } else {
                dp[u] = max(0LL, s - 1) + (a[u] >= x ? 1 : 0);
            }
        }
        return dp[1] > 1;
    };

    long long low = 1, high = 1000000000, ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
