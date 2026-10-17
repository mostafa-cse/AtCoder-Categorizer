# Problem Analysis: AtCoder-abc165_f — LIS on Tree

**Problem ID**: `AtCoder-abc165_f`  
**Contest**: `abc165`  
**Rating / Difficulty**: 1843  
**URL**: https://atcoder.jp/contests/abc165/tasks/abc165_f  
**VJudge Tag**: `[problem:AtCoder-abc165_f]`  
**Category File**: [`../categories/dp/rollback_lis_on_tree_dfs.md`](../categories/dp/rollback_lis_on_tree_dfs.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Tree DFS / LIS`  
- **Topic (Skill)**: `Rollback LIS on Tree via DFS Call-Stack Undo`  

---

## 1. Problem Statement & Key Idea
Given a tree of N vertices with vertex values A_i. For EVERY vertex u in 1..N, find the length of the Longest Increasing Subsequence (LIS) on the unique simple path from the root (1) to u.

**Key Insight**: Maintain the standard Patience Sorting LIS array dp[k] during a DFS traversal. When visiting node u with value A_u, binary search the replacement position pos, record the overwritten value (pos, old_val), update dp[pos] = A_u, record ans[u] = size of dp, recurse on children, and rollback dp[pos] = old_val on exit.

## 2. Core Observation & Invariant
Because each node performs exactly one position update and one rollback in O(log N), all N queries are answered in O(N log N) total time.

## 3. Step-by-Step Algorithm
1. Root tree at 1.
2. Maintain vector<long long> dp (the tails array for LIS).
3. dfs(u, parent):
4.   pos = lower_bound(dp, A_u) - dp.begin().
5.   bool added = (pos == dp.size());
6.   old_val = added ? -1 : dp[pos];
7.   if added: dp.push_back(A_u); else dp[pos] = A_u;
8.   ans[u] = dp.size();
9.   For each child v of u: dfs(v, u);
10.   // Rollback
11.   if added: dp.pop_back(); else dp[pos] = old_val;
12. Print ans[1..N].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<long long> a;
vector<vector<int>> adj;
vector<int> ans;
vector<long long> dp;

void dfs(int u, int p) {
    auto it = lower_bound(dp.begin(), dp.end(), a[u]);
    int pos = it - dp.begin();
    bool added = (it == dp.end());
    long long old_val = added ? -1 : *it;

    if (added) {
        dp.push_back(a[u]);
    } else {
        dp[pos] = a[u];
    }

    ans[u] = dp.size();

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
        }
    }

    // Rollback
    if (added) {
        dp.pop_back();
    } else {
        dp[pos] = old_val;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    a.assign(n + 1, 0);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    ans.assign(n + 1, 0);
    dfs(1, 0);

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Rollback data structure history management on tree call-stacks for tree path queries.
- **Reusable Pattern**: `Tree LIS Rollback: lower_bound + save overwritten tail element + restore on DFS exit.`
