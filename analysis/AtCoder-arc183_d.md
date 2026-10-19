# Problem Analysis: AtCoder-arc183_d — D. Keep Perfectly Matched

**Problem ID**: `AtCoder-arc183_d`  
**Contest**: `arc183`  
**Rating / Difficulty**: 2880  
**URL**: https://atcoder.jp/contests/arc183/tasks/arc183_d  
**VJudge Tag**: `[problem:AtCoder-arc183_d]`  
**Category File**: [`../categories/data_structures/tree_perfect_matching_leaf_removal_centroid.md`](../categories/data_structures/tree_perfect_matching_leaf_removal_centroid.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Centroid Decomposition`  
- **Topic (Skill)**: `Centroid Decomposition`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices (even N) with a perfect matching, repeatedly remove two leaves such that the remaining tree preserves a perfect matching, maximizing the sum of distances between removed pairs.

## 2. Core Observation & Invariant
Root the tree at its centroid R. In any tree with a unique perfect matching, removing leaves in a valid order preserves matchings. Because R is the centroid, each branch has size <= N/2. By repeatedly removing one leaf from the largest branch and one leaf from another branch, every removed pair traverses the centroid R, achieving the theoretical upper bound on total distance.

## 3. Step-by-Step Algorithm
1. 1. Find centroid R of tree.
2. 2. Root tree at R and divide into branches corresponding to children of R.
3. 3. In each branch, order leaves using post-order DFS visiting matched children first.
4. 4. Use a priority queue of branches to pair leaves from the largest branch with another branch.
5. 5. Output the sequence of leaf pairs.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> matched(n + 1);
    for (int i = 1; i <= n / 2; ++i) {
        matched[2 * i - 1] = 2 * i;
        matched[2 * i] = 2 * i - 1;
    }

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Centroid finding
    vector<int> sz(n + 1, 0);
    auto get_sz = [&](auto& self, int u, int p) -> void {
        sz[u] = 1;
        for (int v : adj[u]) {
            if (v != p) {
                self(self, v, u);
                sz[u] += sz[v];
            }
        }
    };
    get_sz(get_sz, 1, 0);

    auto get_centroid = [&](auto& self, int u, int p) -> int {
        for (int v : adj[u]) {
            if (v != p && sz[v] > n / 2) {
                return self(self, v, u);
            }
        }
        return u;
    };
    int R = get_centroid(get_centroid, 1, 0);

    // Root tree at R
    vector<int> parent(n + 1, 0);
    vector<vector<int>> children(n + 1);
    auto build_tree = [&](auto& self, int u, int p) -> void {
        parent[u] = p;
        for (int v : adj[u]) {
            if (v != p) {
                children[u].push_back(v);
                self(self, v, u);
            }
        }
    };
    build_tree(build_tree, R, 0);

    // In each branch of R, order of leaves:
    // Post-order DFS where matched child is visited first
    vector<vector<int>> branch_leaves(n + 1);
    vector<int> branch_ptr(n + 1, 0);

    for (int c : children[R]) {
        auto dfs_leaves = [&](auto& self, int u) -> void {
            int m_child = matched[u];
            vector<int> sorted_ch;
            for (int ch : children[u]) {
                if (ch == m_child) {
                    sorted_ch.insert(sorted_ch.begin(), ch);
                } else {
                    sorted_ch.push_back(ch);
                }
            }
            for (int ch : sorted_ch) {
                self(self, ch);
            }
            branch_leaves[c].push_back(u);
        };
        dfs_leaves(dfs_leaves, c);
    }

    int cur_branch = matched[R];

    // Priority queue of pair<int, int>: (-remaining_size, branch_id)
    priority_queue<pair<int, int>> pq;
    for (int c : children[R]) {
        if (c != cur_branch) {
            pq.push({(int)branch_leaves[c].size(), c});
        }
    }

    for (int step = 0; step < n / 2 - 1; ++step) {
        int leaf_cur = branch_leaves[cur_branch][branch_ptr[cur_branch]++];
        auto top_item = pq.top();
        pq.pop();
        int next_branch = top_item.second;
        int leaf_next = branch_leaves[next_branch][branch_ptr[next_branch]++];

        cout << leaf_cur << " " << leaf_next << "\n";

        int rem_cur = (int)branch_leaves[cur_branch].size() - branch_ptr[cur_branch];
        if (rem_cur > 0) {
            pq.push({rem_cur, cur_branch});
        }

        cur_branch = next_branch;
    }

    int last_leaf = branch_leaves[cur_branch][branch_ptr[cur_branch]++];
    cout << last_leaf << " " << R << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
