# Problem Analysis: AtCoder-abc244_g — Construct Good Path

**Problem ID**: `AtCoder-abc244_g`  
**Contest**: `abc244`  
**Rating / Difficulty**: 2117  
**URL**: https://atcoder.jp/contests/abc244/tasks/abc244_g  
**VJudge Tag**: `[problem:AtCoder-abc244_g]`  
**Category File**: [`../categories/graph_theory/dfs_tree_parity_correction_detours.md`](../categories/graph_theory/dfs_tree_parity_correction_detours.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `DFS Tree`  

---

## 1. Problem Statement & Key Idea
Given a connected undirected graph and a binary parity string S, construct a walk of length at most 4N such that vertex v is visited an odd number of times iff S_v = 1.

**Key Insight**: Build a DFS spanning tree of the graph. Traverse the tree. When returning from a child v to parent u, check if the current visit parity of v matches S_v. If not, take an immediate 2-step detour u -> v -> u! This detour flips the parity of v while visiting u twice (leaving u's parity completely unchanged). Backtracking in this bottom-up manner fixes all vertices' parities. If the root's parity is incorrect at the very end, simply omit the final step of the walk.

## 2. Core Observation & Invariant
A 2-step edge detour u -> v -> u flips the parity of v without altering the parity of u, enabling bottom-up parity satisfaction on DFS trees.

## 3. Step-by-Step Algorithm
1. Construct DFS tree from vertex 1.
2. Record visits in a path array, maintaining current parity of each vertex.
3. On backtracking from child v to parent u:
4.   If cur_parity[v] != S[v]:
5.     Append v, flip parity of v.
6.     Append u, flip parity of u.
7. If cur_parity[root] != S[root], remove the final step from path.
8. Output walk length and sequence.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: DFS tree bottom-up parity correction using localized 2-step edge detours.
- **Reusable Pattern**: Satisfying arbitrary vertex visit parities on connected graphs via DFS spanning tree detours.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n, m;
vector<vector<int>> adj;
string s;
vector<bool> visited;
vector<int> path;
vector<int> cur_parity;

void dfs(int u) {
    visited[u] = true;
    path.push_back(u);
    cur_parity[u] ^= 1;

    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v);
            path.push_back(u);
            cur_parity[u] ^= 1;

            if (cur_parity[v] != (s[v - 1] - '0')) {
                path.push_back(v);
                cur_parity[v] ^= 1;
                path.push_back(u);
                cur_parity[u] ^= 1;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    cin >> s;

    visited.assign(n + 1, false);
    cur_parity.assign(n + 1, 0);

    dfs(1);

    if (cur_parity[1] != (s[0] - '0')) {
        path.pop_back();
        cur_parity[1] ^= 1;
    }

    cout << path.size() << "\n";
    for (int i = 0; i < (int)path.size(); ++i) {
        cout << path[i] << (i + 1 == (int)path.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
