# Problem Analysis: AtCoder-abc157_d — Friend Suggestions

**Problem ID**: `AtCoder-abc157_d`  
**Contest**: `abc157`  
**Rating / Difficulty**: 1208  
**URL**: https://atcoder.jp/contests/abc157/tasks/abc157_d  
**VJudge Tag**: `[problem:AtCoder-abc157_d]`  
**Category File**: [`../categories/data_structures/dsu_component_sizing_exclusion.md`](../categories/data_structures/dsu_component_sizing_exclusion.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Disjoint Set Union`  
- **Topic (Skill)**: `DSU Component Sizing with Mutual Exclusion`  

---

## 1. Problem Statement & Key Idea
N users. M bidirectional friend links and K bidirectional block links. User y is a 'friend candidate' for x if x and y are connected via friends, are not direct friends, not blocked, and x != y. For each user, count their friend candidates.

**Key Idea**: Two users are connected via friends if and only if they belong to the same connected component in the friend graph.

## 2. Core Observation & Invariant
Let sz[x] be the size of the DSU component containing x. Candidates for x must be in the same component. Among the sz[x] users in x's component, we must exclude: (1) user x themselves (-1); (2) all direct friends of x (-deg_friends[x]); (3) all blocked users of x that belong to the SAME component (-blocked_in_same_component[x]).

## 3. Step-by-Step Algorithm
1. Build DSU on M friend edges.
2. Record degrees of direct friends: friend_cnt[i].
3. For each of K block edges (u, v): if find(u) == find(v), block_cnt[u]++, block_cnt[v]++.
4. For each user i: ans[i] = dsu.size(i) - 1 - friend_cnt[i] - block_cnt[i].
5. Print ans[1..N].

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M + K) * alpha(N))`
- **Space Complexity**: `O(N + M + K)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> sz;
    DSU(int n) : parent(n + 1), sz(n + 1, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            sz[root_j] += sz[root_i];
        }
    }
    int get_size(int i) {
        return sz[find(i)];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    DSU dsu(n);
    vector<int> friend_cnt(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        dsu.unite(u, v);
        friend_cnt[u]++;
        friend_cnt[v]++;
    }

    vector<int> block_cnt(n + 1, 0);
    for (int i = 0; i < k; ++i) {
        int u, v;
        cin >> u >> v;
        if (dsu.find(u) == dsu.find(v)) {
            block_cnt[u]++;
            block_cnt[v]++;
        }
    }

    for (int i = 1; i <= n; ++i) {
        int total = dsu.get_size(i) - 1 - friend_cnt[i] - block_cnt[i];
        cout << total << (i == n ? '\n' : ' ');
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Exclusion counting over DSU connected component sizes.
- **Reusable Pattern**: `Valid candidate count in DSU: component_size - 1 - direct_neighbors - blocked_in_component.`
