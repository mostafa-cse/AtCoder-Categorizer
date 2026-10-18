# Problem Analysis: AtCoder-arc171_d — D. Rolling Hash

**Problem ID**: `AtCoder-arc171_d`  
**Contest**: `arc171`  
**Rating / Difficulty**: 2377  
**URL**: https://atcoder.jp/contests/arc171/tasks/arc171_d  
**VJudge Tag**: `[problem:AtCoder-arc171_d]`  
**Category File**: [`../categories/graph_theory/rolling_hash_difference_graph_chromatic_number.md`](../categories/graph_theory/rolling_hash_difference_graph_chromatic_number.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Coloring`  
- **Topic (Skill)**: `Chromatic Number`  

---

## 1. Problem Statement & Key Idea
Determine if a sequence A exists such that M rolling hash subsegments are all non-zero mod prime P. Inverting powers of base B reduces hash(L..R) != 0 to y_R != y_{L-1} mod P on prefix hashes, which is graph coloring on N+1 <= 17 vertices. Testing if chromatic number chi(G) <= P via Fast Zeta Transform and inclusion-exclusion runs in O(N 2^N) time.

## 2. Core Observation & Invariant
The rolling hash condition hash(A[L..R]) != 0 mod P is equivalent to (H_R - H_{L-1} B^{R-L+1}) != 0 mod P. Multiplying by B^{-R} yields y_R != y_{L-1} mod P where y_k = H_k B^{-k} mod P. Since any prefix hash assignment is achievable, the problem is equivalent to proper vertex coloring of the difference graph on N+1 vertices with at most P colors.

## 3. Step-by-Step Algorithm
1. Number vertices 0 .. N (V = N + 1 <= 17). If P >= V, output Yes immediately.
2. Otherwise, add an undirected edge between L_i - 1 and R_i for each pair.
3. Precompute whether each subset of vertices forms an independent set in O(2^V) time.
4. Compute the number of independent subsets f(S) for each mask S using the Fast Zeta Transform (SOS DP) in O(V 2^V) time.
5. Evaluate the chromatic polynomial sum_{S} (-1)^{V - |S|} (f(S))^P modulo two large 30-bit primes to verify that the number of proper P-colorings is strictly positive.

## 4. Complexity Analysis
- **Time Complexity**: `O(N 2^N)`
- **Space Complexity**: `O(2^N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long P, B;
    int N, M;
    if (!(cin >> P >> B >> N >> M)) return 0;

    int V = N + 1;
    if (P >= V) {
        cout << "Yes\n";
        return 0;
    }

    vector<int> adj(V, 0);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        u--; // L_i - 1
        // v is R_i
        adj[u] |= (1 << v);
        adj[v] |= (1 << u);
    }

    int total_masks = 1 << V;
    vector<int> is_indep(total_masks, 0);
    is_indep[0] = 1;
    for (int mask = 1; mask < total_masks; ++mask) {
        int v = __builtin_ctz(mask);
        int prev = mask ^ (1 << v);
        if (is_indep[prev] && !(prev & adj[v])) {
            is_indep[mask] = 1;
        }
    }

    // Fast Zeta Transform on is_indep
    vector<long long> f(total_masks);
    for (int i = 0; i < total_masks; ++i) f[i] = is_indep[i];

    for (int i = 0; i < V; ++i) {
        for (int mask = 0; mask < total_masks; ++mask) {
            if (mask & (1 << i)) {
                f[mask] += f[mask ^ (1 << i)];
            }
        }
    }

    // Number of proper colorings with k colors is:
    // sum_{S} (-1)^{V - |S|} f(S)^k
    // Check modulo two primes:
    long long MOD1 = 998244353;
    long long MOD2 = 1000000007;

    auto power = [](long long base, long long exp, long long mod) {
        long long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    };

    long long sum1 = 0, sum2 = 0;
    for (int mask = 0; mask < total_masks; ++mask) {
        int sz = __builtin_popcount(mask);
        long long sign = ((V - sz) % 2 == 0) ? 1 : -1;

        long long term1 = power(f[mask] % MOD1, P, MOD1);
        long long term2 = power(f[mask] % MOD2, P, MOD2);

        sum1 = (sum1 + sign * term1) % MOD1;
        sum2 = (sum2 + sign * term2) % MOD2;
    }
    sum1 = (sum1 % MOD1 + MOD1) % MOD1;
    sum2 = (sum2 % MOD2 + MOD2) % MOD2;

    if (sum1 != 0 || sum2 != 0) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
