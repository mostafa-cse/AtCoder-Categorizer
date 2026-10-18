# Problem Analysis: AtCoder-abc163_f — F. path pass i

**Problem ID**: `AtCoder-abc163_f`  
**Contest**: `abc163`  
**Rating / Difficulty**: 2470  
**URL**: https://atcoder.jp/contests/abc163/tasks/abc163_f  
**VJudge Tag**: `[problem:AtCoder-abc163_f]`  
**Category File**: [`../categories/graph_theory/path_pass_color_complement_tree_dfs.md`](../categories/graph_theory/path_pass_color_complement_tree_dfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `More Tree Stuff`  
- **Topic (Skill)**: `Virtual Tree / Auxiliary Tree`  

---

## 1. Problem Statement & Key Idea
For each color $k$, count tree paths visiting at least one vertex of color $k$. Use complement counting: total paths $\frac{N(N+1)}{2}$ minus paths completely avoiding color $k$. Deleting all vertices of color $k$ decomposes the tree into monochromatic components of non-$k$ vertices. Subtree sizes maintained during a single post-order DFS determine the size of each monochromatic component in $O(N)$ total time.

## 2. Core Observation & Invariant
When traversing child $v$ of vertex $u$ with color $c$, the size of the monochromatic component in $v$'s subtree bounded by color $c$ is $sz[v] - \Delta color\_sum[c]$, where $\Delta color\_sum[c]$ is the sum of subtrees of top occurrences of color $c$ inside $v$. Each component of size $S$ contributes $\frac{S(S+1)}{2}$ paths avoiding color $c$.

## 3. Step-by-Step Algorithm
1. 1. Run DFS from vertex 1 to compute subtree sizes and track `color_sum[c]` for each color.
2. 2. Before exploring child $v$ from vertex $u$ with color $c$, record `before = color_sum[c]`.
3. 3. After DFS returns from $v$, let `after = color_sum[c]`. The size of the component attached to $v$ without color $c$ is $S = sz[v] - (after - before)$.
4. 4. Add $\frac{S(S+1)}{2}$ to `bad_paths[c]`.
5. 5. After DFS finishes, the top component outside all occurrences of color $c$ has size $N - color\_sum[c]$, contributing $\frac{S_{top}(S_{top}+1)}{2}$ to `bad_paths[c]`.
6. 6. For each color $c$, output $\frac{N(N+1)}{2} - bad\_paths[c]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> colors;
vector<vector<int>> adj;
vector<long long> sz;
vector<long long> color_sum;
vector<long long> bad_paths;

void dfs(int u, int p) {
    sz[u] = 1;
    int c = colors[u];
    long long sum_children = 0;

    for (int v : adj[u]) {
        if (v == p) continue;
        long long before = color_sum[c];
        dfs(v, u);
        sz[u] += sz[v];
        long long after = color_sum[c];

        long long comp_sz = sz[v] - (after - before);
        bad_paths[c] += comp_sz * (comp_sz + 1) / 2;
        sum_children += (after - before);
    }
    color_sum[c] += sz[u] - sum_children;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n)) return 0;

    colors.resize(n + 1);
    for (int i = 1; i <= n; ++i) cin >> colors[i];

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    sz.assign(n + 1, 0);
    color_sum.assign(n + 1, 0);
    bad_paths.assign(n + 1, 0);

    dfs(1, 0);

    long long total_all = (long long)n * (n + 1) / 2;
    for (int c = 1; c <= n; ++c) {
        long long top_sz = n - color_sum[c];
        bad_paths[c] += top_sz * (top_sz + 1) / 2;
        long long ans = total_all - bad_paths[c];
        cout << ans << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
