# BIT / Fenwick Tree

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Binary Indexed Tree (BIT)`  

This workbook contains curated, high-quality competitive programming problems teaching **BIT / Fenwick Tree**.

---

## Curated Problems

### `[problem:AtCoder-abc337_g]` — Tree And LCS
- **Rating / Difficulty**: 2078
- **Contest**: `abc337`
- **Analysis**: [`analysis/AtCoder-abc337_g.md`](../../analysis/AtCoder-abc337_g.md)
- **Key Idea**: For any directed edge u -> v (where u is the parent of v in root r), the condition u < v adds 1 to the count for all nodes in the subtree of v. Rather than rerooting explicitly, consider a fixed root (say node 1). For every vertex x from 1 to N, all nodes y < x on the tree path from 1 to x are either in the component of the parent of x or in a child subtree of x. Using a Fenwick tree over DFS traversal enter/exit timestamps, we can query how many nodes y < x lie inside each subtree of x and outside, and translate these into difference array updates on the tree. A final prefix sum down the tree yields the exact answer for all r.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
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
