# Problem Analysis: AtCoder-arc215_f — F - Scapus

**Problem ID**: `AtCoder-arc215_f`  
**Contest**: `arc215`  
**Rating / Difficulty**: 2972  
**URL**: https://atcoder.jp/contests/arc215/tasks/arc215_f  
**VJudge Tag**: `[problem:AtCoder-arc215_f]`  
**Category File**: [`../categories/graph_theory/tree_scapus_leaf_stripping_diameter_path_counting.md`](../categories/graph_theory/tree_scapus_leaf_stripping_diameter_path_counting.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Tree Diameter`  

---

## 1. Problem Statement & Key Idea
Given a tree T with N <= 2 * 10^5 vertices, count pairs of vertices (u, v) such that their distance is >= D and the induced subgraph of their path satisfies structural degree bounds, modulo 998244353.

## 2. Core Observation & Invariant
The core structural property of long paths in a tree is governed by tree diameter and repeated leaf-stripping. The minimal intersection of all diameter-like paths collapses to a central path P*. If P* has length >= 2, any valid pair must have endpoints in the two opposite branch subtrees of P*. If P* is a single vertex, valid pairs branch out in different subtrees of this central centroid/diameter midpoint. This reduces the path count to polynomial convolutions of subtree depth profiles, evaluated via NTT.

## 3. Step-by-Step Algorithm
1. 1. Repeatedly strip leaves of the tree to identify the minimal spine path P*.
2. 2. If P* is an edge or path of length >= 2: compute depth polynomials of terminal branch trees A and B, convolving A(x) and B(x) using NTT.
3. 3. If P* is a single vertex: collect depth polynomials P_i(x) for all child branches of P*, computing 1/2 ((sum P_i(x))^2 - sum P_i(x)^2) via NTT.
4. 4. Sum valid pair counts modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

// Two NTT primes for exact integer convolution up to ~10^18
namespace NTT {
    long long power(long long base, long long exp, long long mod) {
        long long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }

    long long modInverse(long long n, long long mod) {
        return power(n, mod - 2, mod);
    }

    void ntt(vector<long long>& a, bool invert, long long mod) {
        int n = a.size();
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) swap(a[i], a[j]);
        }
        long long g = 3;
        for (int len = 2; len <= n; len <<= 1) {
            long long wlen = power(g, (mod - 1) / len, mod);
            if (invert) wlen = modInverse(wlen, mod);
            for (int i = 0; i < n; i += len) {
                long long w = 1;
                for (int j = 0; j < len / 2; j++) {
                    long long u = a[i + j];
                    long long v = (a[i + j + len / 2] * w) % mod;
                    a[i + j] = (u + v >= mod ? u + v - mod : u + v);
                    a[i + j + len / 2] = (u - v < 0 ? u - v + mod : u - v);
                    w = (w * wlen) % mod;
                }
            }
        }
        if (invert) {
            long long n_inv = modInverse(n, mod);
            for (long long& x : a) x = (x * n_inv) % mod;
        }
    }

    vector<long long> convolve_mod(const vector<long long>& a, const vector<long long>& b, long long mod) {
        int n = 1;
        int target = (int)a.size() + (int)b.size() - 1;
        while (n < target) n <<= 1;
        vector<long long> fa(a.begin(), a.end()), fb(b.begin(), b.end());
        fa.resize(n, 0); fb.resize(n, 0);
        ntt(fa, false, mod);
        ntt(fb, false, mod);
        for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % mod;
        ntt(fa, true, mod);
        fa.resize(target);
        return fa;
    }

    vector<long long> convolve(const vector<long long>& a, const vector<long long>& b) {
        if (a.empty() || b.empty()) return {};
        long long MOD1 = 998244353;
        long long MOD2 = 1004535809;
        auto res1 = convolve_mod(a, b, MOD1);
        auto res2 = convolve_mod(a, b, MOD2);
        long long m1_inv_m2 = modInverse(MOD1, MOD2);
        int sz = res1.size();
        vector<long long> res(sz);
        for (int i = 0; i < sz; i++) {
            long long r1 = res1[i];
            long long r2 = res2[i];
            long long k = ((r2 - r1) % MOD2 + MOD2) % MOD2;
            k = (k * m1_inv_m2) % MOD2;
            res[i] = k * MOD1 + r1;
        }
        return res;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> deg(n + 1, 0);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    vector<bool> in_tree(n + 1, true);

    // Leaf stripping until maximum degree in remaining tree is <= 2
    while (true) {
        int max_deg = 0;
        for (int u = 1; u <= n; ++u) {
            if (in_tree[u]) {
                max_deg = max(max_deg, deg[u]);
            }
        }
        if (max_deg <= 2) break;

        vector<int> leaves;
        for (int u = 1; u <= n; ++u) {
            if (in_tree[u] && deg[u] <= 1) {
                leaves.push_back(u);
            }
        }
        for (int u : leaves) in_tree[u] = false;
        for (int u : leaves) {
            for (int v : adj[u]) {
                if (in_tree[v]) deg[v]--;
            }
        }
    }

    vector<int> P_star;
    for (int u = 1; u <= n; ++u) {
        if (in_tree[u]) P_star.push_back(u);
    }

    vector<long long> ans(n + 1, 0);

    if (P_star.size() == 1) {
        int u = P_star[0];
        vector<vector<long long>> branch_polys;
        int max_depth_all = 0;

        for (int v : adj[u]) {
            vector<int> d_counts;
            queue<pair<int, int>> q;
            q.push({v, 1});
            vector<bool> vis(n + 1, false);
            vis[u] = true;
            vis[v] = true;

            while (!q.empty()) {
                auto pr = q.front(); q.pop();
                int curr = pr.first, d = pr.second;
                if ((int)d_counts.size() <= d) d_counts.resize(d + 1, 0);
                d_counts[d]++;
                for (int nxt : adj[curr]) {
                    if (!vis[nxt]) {
                        vis[nxt] = true;
                        q.push({nxt, d + 1});
                    }
                }
            }

            vector<long long> poly(d_counts.begin(), d_counts.end());
            max_depth_all = max(max_depth_all, (int)poly.size());
            branch_polys.push_back(poly);
        }

        vector<long long> tot_poly(max_depth_all, 0);
        for (const auto& p : branch_polys) {
            for (size_t d = 0; d < p.size(); ++d) {
                tot_poly[d] += p[d];
            }
        }

        ans[1] = 1; // path containing only u
        for (size_t d = 1; d < tot_poly.size(); ++d) {
            if (d + 1 <= (size_t)n) {
                ans[d + 1] += tot_poly[d]; // paths starting at u and going down one branch
            }
        }

        // sum_{B1 < B2} P_B1 * P_B2 = 1/2 (tot_poly^2 - sum P_B^2)
        auto tot_sq = NTT::convolve(tot_poly, tot_poly);
        vector<long long> sum_sq(tot_sq.size(), 0);
        for (const auto& p : branch_polys) {
            auto p_sq = NTT::convolve(p, p);
            for (size_t d = 0; d < p_sq.size(); ++d) {
                sum_sq[d] += p_sq[d];
            }
        }

        for (size_t d = 0; d < tot_sq.size(); ++d) {
            long long cross = (tot_sq[d] - sum_sq[d]) / 2;
            if (d + 1 <= (size_t)n) {
                ans[d + 1] += cross;
            }
        }
    } else {
        // P_star has at least 2 vertices
        vector<int> endpoints;
        for (int u : P_star) {
            int deg_in_p = 0;
            for (int v : adj[u]) {
                if (in_tree[v]) deg_in_p++;
            }
            if (deg_in_p <= 1) endpoints.push_back(u);
        }

        int u = endpoints[0];
        int v = endpoints[1];

        int nbr_u = -1, nbr_v = -1;
        for (int w : adj[u]) if (in_tree[w]) nbr_u = w;
        for (int w : adj[v]) if (in_tree[w]) nbr_v = w;

        auto get_depth_poly = [&](int root, int blocked) {
            vector<int> d_counts;
            queue<pair<int, int>> q;
            q.push({root, 0});
            vector<bool> vis(n + 1, false);
            vis[blocked] = true;
            vis[root] = true;

            while (!q.empty()) {
                auto pr = q.front(); q.pop();
                int curr = pr.first, d = pr.second;
                if ((int)d_counts.size() <= d) d_counts.resize(d + 1, 0);
                d_counts[d]++;
                for (int nxt : adj[curr]) {
                    if (!vis[nxt]) {
                        vis[nxt] = true;
                        q.push({nxt, d + 1});
                    }
                }
            }
            return vector<long long>(d_counts.begin(), d_counts.end());
        };

        auto poly_u = get_depth_poly(u, nbr_u);
        auto poly_v = get_depth_poly(v, nbr_v);
        auto conv = NTT::convolve(poly_u, poly_v);

        int L = (int)P_star.size();
        for (size_t d = 0; d < conv.size(); ++d) {
            int k = L + d;
            if (k <= n) {
                ans[k] += conv[d];
            }
        }
    }

    for (int k = 1; k <= n; ++k) {
        cout << ans[k] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
