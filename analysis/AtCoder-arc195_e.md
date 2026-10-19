# Problem Analysis: AtCoder-arc195_e — E - Random Tree Distance

**Problem ID**: `AtCoder-arc195_e`  
**Contest**: `arc195`  
**Rating / Difficulty**: 2734  
**URL**: https://atcoder.jp/contests/arc195/tasks/arc195_e  
**VJudge Tag**: `[problem:AtCoder-arc195_e]`  
**Category File**: [`../categories/combinatorics/random_tree_distance_contribution.md`](../categories/combinatorics/random_tree_distance_contribution.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
A tree on N vertices rooted at 1 is formed by independently choosing parent P_i uniformly from 1..i-1 with edge weight A_i for each i in 2..N. There are (N - 1)! possible trees. For Q queries (u, v), find the sum of distances between u and v across all trees modulo 998244353.

## 2. Core Observation & Invariant
By linearity of expectation, E[d(u, v)] = E[depth(u)] + E[depth(v)] - 2 * E[depth(LCA(u, v))]. First, expected depths satisfy E_1 = 0 and E_v = A_v + (1 / (v-1)) * sum_{i=1}^{v-1} E_i for 2 <= v <= N, computable in O(N) using prefix sums. Second, remarkably, for u < v, the distribution of LCA(u, v) depends ONLY on u, not on v! Specifically, moving up from v, the first node <= u is uniformly distributed on 1..u with probability 1/u. This yields L_u = E[depth(LCA(u, v))] = (1 / u) * (E_u + sum_{i=1}^{u-1} L_i), computable in O(N). Each query is then answered in O(1) as (E_u + E_v - 2*L_u) * (N - 1)! mod 998244353.

## 3. Step-by-Step Algorithm
1. 1. Compute prefix sums and modular inverses 1..N modulo 998244353.
2. 2. Compute E_v for v = 2..N: E_v = A_v + inv(v-1) * sum_{i=1}^{v-1} E_i.
3. 3. Compute L_u for u = 1..N-1: L_u = inv(u) * (E_u + sum_{i=1}^{u-1} L_i).
4. 4. Compute factorial (N - 1)! modulo 998244353.
5. 5. For each query (u, v) with u < v, output (E_u + E_v - 2*L_u) * (N - 1)! modulo 998244353 in O(1).

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

long long power_mod(long long base, long long exp) {
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
    return power_mod(n, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    if (!(cin >> N >> Q)) return 0;

    vector<long long> A(N + 1, 0);
    for (int i = 2; i <= N; ++i) {
        cin >> A[i];
    }

    vector<long long> inv(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        inv[i] = mod_inv(i);
    }

    vector<long long> E(N + 1, 0);
    long long sum_E = 0;
    for (int v = 2; v <= N; ++v) {
        E[v] = (A[v] + sum_E % MOD * inv[v - 1]) % MOD;
        sum_E = (sum_E + E[v]) % MOD;
    }

    vector<long long> L(N + 1, 0);
    long long sum_L = 0;
    for (int u = 1; u < N; ++u) {
        L[u] = (E[u] + sum_L) % MOD * inv[u] % MOD;
        sum_L = (sum_L + L[u]) % MOD;
    }

    long long fact = 1;
    for (int i = 1; i < N; ++i) {
        fact = (fact * i) % MOD;
    }

    for (int q = 0; q < Q; ++q) {
        int u, v;
        cin >> u >> v;
        long long exp_d = (E[u] + E[v] - 2 * L[u]) % MOD;
        if (exp_d < 0) exp_d += MOD;
        long long ans = (exp_d * fact) % MOD;
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
