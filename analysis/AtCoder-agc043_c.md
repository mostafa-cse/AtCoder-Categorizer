# Problem Analysis: AtCoder-agc043_c — C - Giant Graph

**Problem ID**: `AtCoder-agc043_c`  
**Contest**: `agc043`  
**Rating / Difficulty**: 2872  
**URL**: https://atcoder.jp/contests/agc043/tasks/agc043_c  
**VJudge Tag**: `[problem:AtCoder-agc043_c]`  
**Category File**: [`../categories/game_theory/tensor_product_graph_independent_set_grundy_xor.md`](../categories/game_theory/tensor_product_graph_independent_set_grundy_xor.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
Three graphs X, Y, Z on N vertices form a Cartesian product graph W with N^3 vertices (i, j, k) having exponential weights 10^{18(i+j+k)}. Find the maximum weight independent set in W modulo 998244353.

## 2. Core Observation & Invariant
Exponential weights force greedy lexicographical choice: a vertex is selected iff none of its higher-indexed neighbors are selected. Orienting edges u -> v for u < v creates a DAG, and the greedy independent set is precisely the kernel (P-positions / Grundy value 0) of the game on W. Since W is the independent sum of games on X, Y, Z, the Sprague-Grundy theorem gives g_W(i, j, k) = g_X(i) ^ g_Y(j) ^ g_Z(k) = 0. Factorizing weights into S_X, S_Y, S_Z by Grundy value allows summing over g_1 ^ g_2 ^ g_3 = 0 in O(G^2) time.

## 3. Step-by-Step Algorithm
1. 1. Orient edges in X, Y, Z from smaller index to larger index.
2. 2. Compute Grundy values g_X(u), g_Y(v), g_Z(w) in O(M) by scanning vertices backwards.
3. 3. Aggregate polynomial weights S_X[g] = sum_{g_X(i) = g} (10^18)^i mod 998244353, and similarly for S_Y, S_Z.
4. 4. Iterate over pairs (g_1, g_2) and accumulate S_X[g_1] * S_Y[g_2] * S_Z[g_1 ^ g_2] modulo 998244353.
5. 5. Output total sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M + G^2)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
const long long BASE = 716070898; // 10^18 % 998244353

int N, M1, M2, M3;

vector<int> get_grundy(int M) {
    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        if (u > v) swap(u, v);
        adj[u].push_back(v);
    }
    vector<int> g(N + 1, 0);
    vector<int> seen(N + 2, 0);
    for (int u = N; u >= 1; --u) {
        for (int v : adj[u]) {
            if (g[v] <= N + 1) seen[g[v]] = u;
        }
        int mex = 0;
        while (seen[mex] == u) mex++;
        g[u] = mex;
    }
    return g;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;
    cin >> M1;
    vector<int> gX = get_grundy(M1);
    cin >> M2;
    vector<int> gY = get_grundy(M2);
    cin >> M3;
    vector<int> gZ = get_grundy(M3);

    int max_g = 0;
    for (int i = 1; i <= N; ++i) {
        max_g = max(max_g, max({gX[i], gY[i], gZ[i]}));
    }
    int K = 1;
    while (K <= max_g) K <<= 1;

    vector<long long> SX(K, 0), SY(K, 0), SZ(K, 0);
    long long pw = 1;
    for (int i = 1; i <= N; ++i) {
        pw = (pw * BASE) % MOD;
        SX[gX[i]] = (SX[gX[i]] + pw) % MOD;
        SY[gY[i]] = (SY[gY[i]] + pw) % MOD;
        SZ[gZ[i]] = (SZ[gZ[i]] + pw) % MOD;
    }

    long long ans = 0;
    for (int g1 = 0; g1 < K; ++g1) {
        if (!SX[g1]) continue;
        for (int g2 = 0; g2 < K; ++g2) {
            if (!SY[g2]) continue;
            int g3 = g1 ^ g2;
            if (g3 < K && SZ[g3]) {
                long long term = (SX[g1] * SY[g2]) % MOD;
                term = (term * SZ[g3]) % MOD;
                ans = (ans + term) % MOD;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
