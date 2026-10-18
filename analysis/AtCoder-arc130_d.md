# Problem Analysis: AtCoder-arc130_d — D. Zigzag Tree

**Problem ID**: `AtCoder-arc130_d`  
**Contest**: `arc130`  
**Rating / Difficulty**: 2437  
**URL**: https://atcoder.jp/contests/arc130/tasks/arc130_d  
**VJudge Tag**: `[problem:AtCoder-arc130_d]`  
**Category File**: [`../categories/dynamic_programming/zigzag_tree_bipartite_linear_extensions_tree_dp.md`](../categories/dynamic_programming/zigzag_tree_bipartite_linear_extensions_tree_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Count permutations of vertices on a tree where every vertex is a local extremum. Because trees are bipartite, the vertices alternate between local minima and local maxima, directing all edges. Reversing the permutation ($P'_i = N + 1 - P_i$) shows that both 2-colorings yield an identical number of linear extensions. Tree DP maintaining subtree relative rank $dp[u][r]$ with prefix/suffix sums merges subtrees in $O(N^2)$ total time.

## 2. Core Observation & Invariant
When merging child $v$ into $u$, if $u$ is a local maximum ($v < u$), $v$ must precede $u$ in the merged ordering, meaning the rank of $v$ in its own subtree is bounded by the number of elements allocated from $v$'s subtree before $u$. This evaluates to a prefix sum over $dp[v]$.

## 3. Step-by-Step Algorithm
1. 1. 2-color the tree with BFS/DFS to orient edges so that color 0 vertices are local minima and color 1 are local maxima.
2. 2. Precompute binomial coefficients up to $N$.
3. 3. Traverse vertices in post-order: initialize $dp[u] = [0, 1]$ (size 1, rank 1 has 1 way).
4. 4. For each child $v$ of $u$:
5.    - Precompute prefix sums $pref_v$ and suffix sums $suff_v$ of $dp[v]$.
6.    - Iterate rank $i \in [1, sz_u]$ and merged rank $k \in [1, sz_u + sz_v]$.
7.    - Interleave combinations $\binom{k-1}{i-1} \binom{new\_sz - k}{sz_u - i}$ multiplied by $pref_v[k-i]$ (if $u$ is max) or $suff_v[k-i+1]$ (if $u$ is min).
8. 5. Sum $dp[root]$ across all ranks and multiply by 2 modulo $998244353$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> adj(N);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> color(N, 0), parent(N, -1), order;
    vector<bool> visited(N, false);
    vector<int> stack = {0};
    visited[0] = true;

    while (!stack.empty()) {
        int u = stack.back();
        stack.pop_back();
        order.push_back(u);
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                color[v] = color[u] ^ 1;
                parent[v] = u;
                stack.push_back(v);
            }
        }
    }

    vector<vector<long long>> comb(N + 1, vector<long long>(N + 1, 0));
    for (int i = 0; i <= N; ++i) {
        comb[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
        }
    }

    vector<vector<long long>> dp(N);
    vector<int> sz(N, 1);

    for (int idx = N - 1; idx >= 0; --idx) {
        int u = order[idx];
        dp[u] = {0, 1}; // size 1, rank 1

        for (int v : adj[u]) {
            if (v == parent[u]) continue;

            bool u_is_max = (color[u] == 1);

            vector<long long> pref_v(sz[v] + 1, 0);
            for (int j = 1; j <= sz[v]; ++j) {
                pref_v[j] = (pref_v[j - 1] + dp[v][j]) % MOD;
            }
            vector<long long> suff_v(sz[v] + 2, 0);
            for (int j = sz[v]; j >= 1; --j) {
                suff_v[j] = (suff_v[j + 1] + dp[v][j]) % MOD;
            }

            int new_sz = sz[u] + sz[v];
            vector<long long> new_dp(new_sz + 1, 0);

            for (int i = 1; i <= sz[u]; ++i) {
                long long ways_u = dp[u][i];
                if (ways_u == 0) continue;

                for (int k = 1; k <= new_sz; ++k) {
                    int v_before = k - i;
                    int v_after = sz[v] - v_before;
                    if (v_before < 0 || v_after < 0) continue;

                    long long ways_interleave = (comb[k - 1][i - 1] * comb[new_sz - k][sz[u] - i]) % MOD;
                    long long sum_v = (u_is_max ? pref_v[v_before] : suff_v[v_before + 1]);

                    long long term = (ways_u * ways_interleave) % MOD;
                    term = (term * sum_v) % MOD;
                    new_dp[k] = (new_dp[k] + term) % MOD;
                }
            }
            dp[u] = move(new_dp);
            sz[u] = new_sz;
        }
    }

    long long ans1 = 0;
    for (int i = 1; i <= N; ++i) {
        ans1 = (ans1 + dp[0][i]) % MOD;
    }
    long long ans = (2 * ans1) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
