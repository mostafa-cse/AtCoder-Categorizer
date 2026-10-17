# Problem Analysis: AtCoder-abc149_f — Surrounded Nodes

**Problem ID**: `AtCoder-abc149_f`  
**Contest**: `abc149`  
**Rating / Difficulty**: 2208  
**URL**: https://atcoder.jp/contests/abc149/tasks/abc149_f  
**VJudge Tag**: `[problem:AtCoder-abc149_f]`  
**Category File**: [`../categories/math/surrounded_nodes_minimal_steiner_tree_expectation.md`](../categories/math/surrounded_nodes_minimal_steiner_tree_expectation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Linearity of expectation on tree nodes with complement probability of minimal Steiner tree containment.

## 2. Core Observation & Invariant
A vertex u is surrounded iff u not in S and u lies in the minimal connected subtree spanning S. Node u is on a path between two nodes in S iff at least two connected components of T \ {u} contain vertices from S. The complement is that at most one component contains vertices from S.

## 3. Step-by-Step Algorithm
1. 1. Run DFS to compute subtree sizes and component sizes for each node u.
2. 2. For node u, removing u leaves components of sizes sz_1, ..., sz_d (where sum sz_j = N - 1).
3. 3. Probability that at most one component contains a node from S is (1 + sum_{j=1}^d (2^{sz_j} - 1)) / 2^{N-1}.
4. 4. Node u is surrounded with probability 1/2 * (1 - (1 + sum (2^{sz_j} - 1)) / 2^{N-1}).
5. 5. Sum this expectation over all N vertices modulo 10^9+7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 1000000007;

ll power(ll base, ll exp) {
    ll res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

ll modInverse(ll n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> sz(N + 1, 0);
    vector<int> parent(N + 1, 0);

    function<void(int, int)> dfs_sz = [&](int u, int p) {
        parent[u] = p;
        sz[u] = 1;
        for (int v : adj[u]) {
            if (v != p) {
                dfs_sz(v, u);
                sz[u] += sz[v];
            }
        }
    };

    dfs_sz(1, 0);

    vector<ll> pow2(N + 1);
    pow2[0] = 1;
    for (int i = 1; i <= N; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    ll total_numer = 0;

    for (int u = 1; u <= N; ++u) {
        ll sum_comp = 0;
        for (int v : adj[u]) {
            int comp_sz = (v == parent[u]) ? (N - sz[u]) : sz[v];
            sum_comp = (sum_comp + (pow2[comp_sz] - 1 + MOD)) % MOD;
        }

        ll cur = (pow2[N - 1] - 1 - sum_comp) % MOD;
        if (cur < 0) cur += MOD;
        total_numer = (total_numer + cur) % MOD;
    }

    ll ans = (total_numer * modInverse(pow2[N])) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
