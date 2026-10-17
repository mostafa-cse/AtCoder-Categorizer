# Problem Analysis: AtCoder-abc160_f — Distributing Integers

**Problem ID**: `AtCoder-abc160_f`  
**Contest**: `abc160`  
**Rating / Difficulty**: 2048  
**URL**: https://atcoder.jp/contests/abc160/tasks/abc160_f  
**VJudge Tag**: `[problem:AtCoder-abc160_f]`  
**Category File**: [`../categories/dynamic_programming/tree_rerooting_topological_linear_extensions.md`](../categories/dynamic_programming/tree_rerooting_topological_linear_extensions.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Tree DP`  
- **Topic (Skill)**: `Tree Rerooting DP on Topological Linear Extensions`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices. For each vertex k in 1 ... N, count permutations of 1 ... N where vertex k receives 1, and for each i >= 2, the vertex with label i is adjacent to some vertex with label < i. Output mod 10^9 + 7.

**Key Idea**: The condition means the set of labeled vertices is always connected. When rooted at vertex k, each child's label must be greater than its parent's label. This is the definition of a topological linear extension of a tree poset rooted at k, given by the formula N! / prod_{v=1}^N sz(v). To compute this for all N vertices in O(N), we use Tree Rerooting DP (All-Directions Tree DP). When rerooting from u to adjacent neighbor v, only the subtree sizes of u and v change: sz(u) becomes N - sz(v), and sz(v) becomes N. Thus ans(v) = ans(u) * sz(v) * inv(N - sz(v)) % MOD.

## 2. Core Observation & Invariant
Tree poset topological orderings depend solely on subtree sizes; moving the root adjusts only two subtree sizes in O(1).

## 3. Step-by-Step Algorithm
1. Root tree arbitrarily at vertex 1. Compute subtree sizes sz[u] via DFS 1.
2. Compute base answer for root 1: ans[1] = N! * prod_{v=1}^N inv(sz[v]) % MOD.
3. Run DFS 2 (rerooting pass) from u to neighbor v:
4.   ans[v] = ans[u] * sz[v] % MOD * inv(N - sz[v]) % MOD.
5.   Recursively visit all neighbors of v.
6. Output ans[k] for all k from 1 to N.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Tree rerooting DP on tree poset topological linear extensions (N! / prod sz).

**Reusable Pattern**: Tree Poset Rerooting: When transferring root from u to v, adjust answer by multiplying old sz[v] and dividing new sz[u].

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long mod_inv(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> fact(n + 1), inv(n + 1);
    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
        inv[i] = mod_inv(i);
    }

    vector<int> sz(n + 1, 0);

    auto dfs1 = [&](auto& self, int u, int p) -> void {
        sz[u] = 1;
        for (int v : adj[u]) {
            if (v != p) {
                self(self, v, u);
                sz[u] += sz[v];
            }
        }
    };

    dfs1(dfs1, 1, 0);

    // Compute ans[1] = N! / prod sz[v]
    long long ans1 = fact[n];
    for (int v = 1; v <= n; ++v) {
        ans1 = (ans1 * inv[sz[v]]) % MOD;
    }

    vector<long long> ans(n + 1);
    ans[1] = ans1;

    auto dfs2 = [&](auto& self, int u, int p) -> void {
        for (int v : adj[u]) {
            if (v != p) {
                // Reroot u -> v:
                // sz[v] was subtree size from u
                // in v's view, u becomes a child of size (n - sz[v])
                ans[v] = ans[u] * sz[v] % MOD * inv[n - sz[v]] % MOD;
                self(self, v, u);
            }
        }
    };

    dfs2(dfs2, 1, 0);

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
