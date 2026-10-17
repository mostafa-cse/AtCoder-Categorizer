# Problem Analysis: AtCoder-abc291_h — Centroid Decomposition Tree

**Problem ID**: `AtCoder-abc291_h`  
**Contest**: `abc291`  
**Rating / Difficulty**: 2090  
**URL**: https://atcoder.jp/contests/abc291/tasks/abc291_h  
**VJudge Tag**: `[problem:AtCoder-abc291_h]`  
**Category File**: [`../categories/data_structures/centroid_decomposition_tree_reconstruction.md`](../categories/data_structures/centroid_decomposition_tree_reconstruction.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Centroid Decomposition`  
- **Topic (Skill)**: `Centroid Decomposition`  

---

## 1. Problem Statement & Key Idea
You are given a tree T with N vertices. Construct a rooted tree R on the same N vertices such that: 1) For any u, v, the lowest common ancestor in R lies on the simple path between u and v in T. 2) For any vertex v, the subtree size of v in R is at most half the subtree size of its parent in R. Output the parent array of R.

**Key Insight**: The two required properties are precisely the defining invariants of the Centroid Decomposition Tree of T! The centroid of any tree splits the remaining components into sizes at most N / 2, and every path between vertices in different components passes through the centroid (which serves as their LCA in the centroid tree). Thus, the problem is solved by computing the Centroid Decomposition of the given tree T and outputting the centroid tree's parent pointers.

## 2. Core Observation & Invariant
A tree where every LCA(u, v) lies on T's path and subtree sizes halve at each step is uniquely satisfied by Centroid Decomposition.

## 3. Step-by-Step Algorithm
1. Compute subtree sizes using DFS to find the centroid of each component.
2. A vertex c is a centroid if every child subtree has size <= total / 2 and (total - size[c]) <= total / 2.
3. Set the centroid of the current component as a child of the previous centroid in R.
4. Mark c as removed and recurse on each adjacent component.
5. Output the parent pointers in tree R (with root having parent -1).

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Centroid decomposition algorithm and recognition of centroid hierarchy invariants.
- **Reusable Pattern**: Path-containment of LCAs and logarithmic height halving uniquely characterize Centroid Decomposition.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz;
vector<bool> removed;
vector<int> parent_r;

void get_sizes(int u, int p) {
    sz[u] = 1;
    for (int v : adj[u]) {
        if (v != p && !removed[v]) {
            get_sizes(v, u);
            sz[u] += sz[v];
        }
    }
}

int get_centroid(int u, int p, int total) {
    for (int v : adj[u]) {
        if (v != p && !removed[v] && sz[v] > total / 2) {
            return get_centroid(v, u, total);
        }
    }
    return u;
}

void decompose(int u, int p) {
    get_sizes(u, -1);
    int c = get_centroid(u, -1, sz[u]);

    parent_r[c] = p;
    removed[c] = true;

    for (int v : adj[c]) {
        if (!removed[v]) {
            decompose(v, c);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    sz.assign(n + 1, 0);
    removed.assign(n + 1, false);
    parent_r.assign(n + 1, -1);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    decompose(1, -1);

    for (int i = 1; i <= n; ++i) {
        cout << parent_r[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
