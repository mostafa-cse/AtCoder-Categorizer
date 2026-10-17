# Problem Analysis: AtCoder-abc337_g — Tree And LCS

**Problem ID**: `AtCoder-abc337_g`  
**Contest**: `abc337`  
**Rating / Difficulty**: 2078  
**URL**: https://atcoder.jp/contests/abc337/tasks/abc337_g  
**VJudge Tag**: `[problem:AtCoder-abc337_g]`  
**Category File**: [`../categories/data_structures/tree_path_dominance_fenwick_dfs.md`](../categories/data_structures/tree_path_dominance_fenwick_dfs.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Binary Indexed Tree (BIT)`  
- **Topic (Skill)**: `BIT / Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices labeled 1 through N. For each vertex r, consider rooting the tree at r. Find the sum over all vertices v of the number of ancestors u of v such that u < v.

**Key Insight**: For any directed edge u -> v (where u is the parent of v in root r), the condition u < v adds 1 to the count for all nodes in the subtree of v. Rather than rerooting explicitly, consider a fixed root (say node 1). For every vertex x from 1 to N, all nodes y < x on the tree path from 1 to x are either in the component of the parent of x or in a child subtree of x. Using a Fenwick tree over DFS traversal enter/exit timestamps, we can query how many nodes y < x lie inside each subtree of x and outside, and translate these into difference array updates on the tree. A final prefix sum down the tree yields the exact answer for all r.

## 2. Core Observation & Invariant
Pairwise tree ancestor conditions can be decomposed into static subtree counts of smaller-labeled vertices using a Fenwick tree and tree difference arrays.

## 3. Step-by-Step Algorithm
1. Root tree at node 1. Compute DFS entry/exit times in and out, and subtree sizes.
2. Iterate x from 1 to N:
3.   Query the BIT for the number of elements < x in x's subtree.
4.   For each child c of x, query how many elements < x are in c's subtree.
5.   Add difference updates on the tree for each component.
6.   Insert x into the Fenwick tree at in[x].
7. Perform a top-down DFS to accumulate prefix sums of the tree difference array.
8. Output the results for all vertices 1..N.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Tree difference arrays combined with Fenwick tree range queries during DFS to aggregate ancestor relations.
- **Reusable Pattern**: Translating relative order constraints u < v across all possible roots into static subtree BIT queries and imos on trees.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<long long> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, long long delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    long long query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int n;
vector<vector<int>> adj;
vector<int> tin, tout;
vector<vector<int>> children;
int timer = 0;

void dfs_time(int u, int p) {
    tin[u] = ++timer;
    for (int v : adj[u]) {
        if (v != p) {
            children[u].push_back(v);
            dfs_time(v, u);
        }
    }
    tout[u] = timer;
}

vector<long long> diff;

void dfs_diff(int u) {
    for (int v : children[u]) {
        dfs_diff(v);
        diff[u] += diff[v];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    tin.assign(n + 1, 0);
    tout.assign(n + 1, 0);
    children.assign(n + 1, vector<int>());
    diff.assign(n + 2, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs_time(1, 0);

    Fenwick bit(n);
    vector<long long> ans(n + 1, 0);

    for (int x = 1; x <= n; ++x) {
        long long total_below = bit.query(tin[x], tout[x]);
        ans[1] += total_below;

        for (int c : children[x]) {
            long long below_c = bit.query(tin[c], tout[c]);
            diff[c] -= below_c;
        }
        diff[x] += total_below;

        bit.add(tin[x], 1);
    }

    dfs_diff(1);

    for (int i = 1; i <= n; ++i) {
        ans[i] = ans[1] + diff[i];
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
