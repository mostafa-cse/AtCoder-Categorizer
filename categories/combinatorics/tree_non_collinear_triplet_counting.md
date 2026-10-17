# Tree Non-Collinear Triplet Counting via Junction Center Decomposition

**Domain**: `Combinatorics`  
**Subtopic**: `Tree Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Non-Collinear Triplet Counting via Junction Center Decomposition**.

---

## Curated Problems

### `[problem:AtCoder-abc312_g]` — Avoid Straight Line
- **Rating / Difficulty**: 1819
- **Contest**: `abc312`
- **Analysis**: [`analysis/AtCoder-abc312_g.md`](../../analysis/AtCoder-abc312_g.md)
- **Key Idea**: Three vertices i, j, k do NOT lie on a single path iff they branch out into three distinct components attached to a common center junction vertex u. For a vertex u, removing u splits the tree into components of sizes s_1, s_2, ..., s_d. The count of triplets centered at u is sum_{a < b < c} s_a * s_b * s_c.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz;
long long total_ans = 0;

void dfs(int u, int p) {
    sz[u] = 1;
    vector<long long> comps;

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
            sz[u] += sz[v];
            comps.push_back(sz[v]);
        }
    }
    if (n - sz[u] > 0) {
        comps.push_back(n - sz[u]);
    }

    // Compute e_3 of comps
    long long s1 = 0, s2 = 0, s3 = 0;
    for (long long x : comps) {
        s1 += x;
        s2 += x * x;
        s3 += x * x * x;
    }

    long long e1 = s1;
    long long e2 = (e1 * e1 - s2) / 2;
    long long e3 = (e1 * e1 * e1 - 3 * e1 * s2 + 2 * s3) / 6;

    total_ans += e3;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    sz.assign(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);

    cout << total_ans << "\n";
    return 0;
}
```
