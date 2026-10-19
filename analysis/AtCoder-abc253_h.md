# Problem Analysis: AtCoder-abc253_h — Ex - We Love Forest

**Problem ID**: `AtCoder-abc253_h`  
**Contest**: `abc253`  
**Rating / Difficulty**: 2758  
**URL**: https://atcoder.jp/contests/abc253/tasks/abc253_h  
**VJudge Tag**: `[problem:AtCoder-abc253_h]`  
**Category File**: [`../categories/dynamic_programming_dp/we_love_forest_subset_convolution.md`](../categories/dynamic_programming_dp/we_love_forest_subset_convolution.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Subset Convolution`  

---

## 1. Problem Statement & Key Idea
Starting with an empty graph on N vertices (N <= 14), we add an edge chosen uniformly at random from a multiset of M edges N-1 times. For each K in 1..N-1, find the probability modulo 998244353 that the graph is a forest after the K-th operation.

## 2. Core Observation & Invariant
The probability that the graph is a forest with K edges is g_K(V) * K! / M^K, where g_K(V) is the number of forests with K edges on vertex set V. For each subset S, the number of spanning trees f(S) on the induced subgraph is given by the Matrix Tree Theorem via the determinant of the (|S|-1) x (|S|-1) Laplacian matrix. The number of forests g_i(S) with i edges satisfies the subset convolution DP: g_i(S) = sum_{v in T subset S} f(T) * g_{i - (|T| - 1)}(S \ T), where v is a fixed canonical vertex (e.g. lsb(S)) to avoid overcounting components.

## 3. Step-by-Step Algorithm
1. 1. For each of the 2^N subsets S, compute f(S) as the determinant of its Laplacian matrix using Gaussian elimination.
2. 2. Initialize DP table g[0][0] = 1.
3. 3. For each mask S, fix v = lsb(S), iterate over submasks T of S containing v, and transition g_i(S) += f(T) * g_{i - (|T|-1)}(S \ T).
4. 4. For each K in 1..N-1, compute ans_K = g_K(full) * K! * (1 / M)^K mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 * 2^N + N * 3^N)`
- **Space Complexity**: `O(N * 2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

long long mat_det(vector<vector<long long>>& A, int n) {
    long long det = 1;
    for (int i = 0; i < n; ++i) {
        int pivot = -1;
        for (int r = i; r < n; ++r) {
            if (A[r][i] != 0) {
                pivot = r;
                break;
            }
        }
        if (pivot == -1) return 0;
        if (pivot != i) {
            swap(A[i], A[pivot]);
            det = (MOD - det) % MOD;
        }
        det = (det * A[i][i]) % MOD;
        long long inv = modInverse(A[i][i]);
        for (int r = i + 1; r < n; ++r) {
            if (A[r][i] != 0) {
                long long factor = (A[r][i] * inv) % MOD;
                for (int c = i; c < n; ++c) {
                    A[r][c] = (A[r][c] - factor * A[i][c]) % MOD;
                    if (A[r][c] < 0) A[r][c] += MOD;
                }
            }
        }
    }
    return det;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n, vector<int>(n, 0));
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u][v]++;
        adj[v][u]++;
    }

    int total_masks = 1 << n;
    vector<long long> f(total_masks, 0);

    for (int mask = 1; mask < total_masks; ++mask) {
        vector<int> verts;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) verts.push_back(i);
        }
        int sz = (int)verts.size();
        if (sz == 1) {
            f[mask] = 1;
            continue;
        }

        vector<vector<long long>> L(sz - 1, vector<long long>(sz - 1, 0));
        for (int i = 0; i < sz - 1; ++i) {
            int u = verts[i];
            long long deg = 0;
            for (int j = 0; j < sz; ++j) {
                int v = verts[j];
                if (u != v) {
                    int cnt = adj[u][v];
                    deg += cnt;
                    if (j < sz - 1) {
                        L[i][j] = (MOD - cnt % MOD) % MOD;
                    }
                }
            }
            L[i][i] = deg % MOD;
        }
        f[mask] = mat_det(L, sz - 1);
    }

    // g[mask] has size sz
    vector<vector<long long>> g(total_masks);
    g[0] = {1};

    for (int mask = 1; mask < total_masks; ++mask) {
        int sz = 0;
        int temp = mask;
        while (temp) {
            sz += (temp & 1);
            temp >>= 1;
        }
        g[mask].assign(sz, 0);

        int v = mask & -mask; // lsb vertex
        int rem = mask ^ v;
        int sub = rem;

        while (true) {
            int T = v | sub;
            long long f_T = f[T];
            if (f_T != 0) {
                int T_sz = 0;
                int temp_T = T;
                while (temp_T) {
                    T_sz += (temp_T & 1);
                    temp_T >>= 1;
                }
                int edges_T = T_sz - 1;
                int rem_mask = mask ^ T;
                const auto& g_rem = g[rem_mask];
                for (size_t rem_i = 0; rem_i < g_rem.size(); ++rem_i) {
                    if (g_rem[rem_i] != 0) {
                        int total_i = edges_T + (int)rem_i;
                        g[mask][total_i] = (g[mask][total_i] + f_T * g_rem[rem_i]) % MOD;
                    }
                }
            }
            if (sub == 0) break;
            sub = (sub - 1) & rem;
        }
    }

    vector<long long> fact(n, 1);
    for (int i = 1; i < n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }

    int full = total_masks - 1;
    long long inv_M = modInverse(m);
    long long inv_M_pow = 1;

    for (int k = 1; k < n; ++k) {
        inv_M_pow = (inv_M_pow * inv_M) % MOD;
        long long ways = g[full][k];
        long long ans_k = (ways * fact[k]) % MOD;
        ans_k = (ans_k * inv_M_pow) % MOD;
        cout << ans_k << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
