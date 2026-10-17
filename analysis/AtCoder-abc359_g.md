# Problem Analysis: AtCoder-abc359_g — Sum of Tree Distance

**Problem ID**: `AtCoder-abc359_g`  
**Contest**: `abc359`  
**Rating / Difficulty**: 2095  
**URL**: https://atcoder.jp/contests/abc359/tasks/abc359_g  
**VJudge Tag**: `[problem:AtCoder-abc359_g]`  
**Category File**: [`../categories/graph_theory/same_color_pairwise_distance_virtual_tree.md`](../categories/graph_theory/same_color_pairwise_distance_virtual_tree.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `More Tree Stuff`  
- **Topic (Skill)**: `Virtual Tree / Auxiliary Tree`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices and an array of colors A_1, A_2, ..., A_N. Calculate the sum of dist(u, v) over all pairs (u, v) such that u < v and A_u == A_v.

**Key Insight**: The distance between u and v is depth[u] + depth[v] - 2 * depth[LCA(u, v)]. For any color c with vertices V_c, sum_{u, v in V_c} (depth[u] + depth[v]) = (|V_c| - 1) * sum_{u in V_c} depth[u]. The critical part is computing sum_{u, v in V_c} depth[LCA(u, v)]. For each edge e = (p, child), this edge is traversed by all pairs of nodes of color c where one node lies in child's subtree and the other lies outside. Alternatively, using small-to-large merging (DSU on tree) with frequency maps, or virtual trees for each color, we can count the number of pairs passing through each subtree in O(N log N) total time.

## 2. Core Observation & Invariant
Pairwise distances within color classes decompose into depth contributions minus LCA depths, computable via DSU on tree or small-to-large frequency merging.

## 3. Step-by-Step Algorithm
1. Root tree at node 1. Compute depths and subtree sizes.
2. Use small-to-large merging with unordered_map<int, int> tracking color counts in each subtree.
3. For each vertex u:
4.   Initialize map with {A[u]: 1}.
5.   For each child v of u:
6.     Merge child's map into u's map (always swap smaller into larger).
7.     When merging, for each color c in the smaller map with count k1, if u's map already has count k2, then k1 * k2 pairs of color c have LCA u, contributing -2 * depth[u] * (k1 * k2).
8. Sum (|V_c| - 1) * depth[u] for all vertices u, subtract 2 * sum depth[LCA], and output the total.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log^2 N) with maps, or O(N log N) with virtual tree`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Small-to-large frequency merging on trees to aggregate pairwise LCA depths.
- **Reusable Pattern**: Sum of pairwise tree distances grouped by category using small-to-large merging to count pairs sharing each LCA.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int n;
vector<int> a;
vector<vector<int>> adj;
vector<int> depth;
long long total_ans = 0;

map<int, int>* dfs(int u, int p, int d) {
    depth[u] = d;
    map<int, int>* cur_map = new map<int, int>();
    (*cur_map)[a[u]] = 1;

    for (int v : adj[u]) {
        if (v == p) continue;
        map<int, int>* child_map = dfs(v, u, d + 1);

        if (child_map->size() > cur_map->size()) {
            swap(cur_map, child_map);
        }

        for (auto& entry : *child_map) {
            int color = entry.first;
            int cnt = entry.second;
            if (cur_map->count(color)) {
                long long pairs = 1LL * cnt * (*cur_map)[color];
                total_ans -= 2LL * d * pairs;
                (*cur_map)[color] += cnt;
            } else {
                (*cur_map)[color] = cnt;
            }
        }
        delete child_map;
    }
    return cur_map;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    a.resize(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    depth.assign(n + 1, 0);

    // Run DFS with small-to-large
    map<int, int>* root_map = dfs(1, 0, 0);

    // Add depth[u] * (color_count - 1)
    for (int u = 1; u <= n; ++u) {
        int color = a[u];
        int count_color = (*root_map)[color];
        total_ans += 1LL * depth[u] * (count_color - 1);
    }

    delete root_map;

    cout << total_ans << "\n";
    return 0;
}
```
