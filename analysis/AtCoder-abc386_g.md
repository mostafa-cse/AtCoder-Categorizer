# Problem Analysis: AtCoder-abc386_g — G. Many MST

**Problem ID**: `AtCoder-abc386_g`  
**Contest**: `abc386`  
**Rating / Difficulty**: 2930  
**URL**: https://atcoder.jp/contests/abc386/tasks/abc386_g  
**VJudge Tag**: `[problem:AtCoder-abc386_g]`  
**Category File**: [`../categories/graph_theory/kruskal_connected_components_graph_enumeration_egf.md`](../categories/graph_theory/kruskal_connected_components_graph_enumeration_egf.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Counting`  
- **Topic (Skill)**: `Counting Labeled Graphs`  

---

## 1. Problem Statement & Key Idea
Count connected graphs with N labeled vertices and edge weights in {1, ..., M} whose MST weight is at most K.

## 2. Core Observation & Invariant
By Kruskal's algorithm, the MST weight is determined by the number of connected components c_w after considering edges of weight <= w: weight(MST) = sum_{w=1}^M (c_{w-1} - 1). We enumerate graphs with prescribed component counts across edge-weight thresholds via exponential generating functions (EGF) of connected graphs and polynomial interpolation.

## 3. Step-by-Step Algorithm
1. 1. Precompute EGF for connected graphs on N vertices with edges in weight <= w.
2. 2. Compute number of connected components distribution using polynomial powers.
3. 3. Combine threshold contributions across all M weights.
4. 4. Output total valid graph count modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(M N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long M;
    if (!(cin >> N >> M)) return 0;

    // Precompute combinations C[i][j]
    vector<vector<long long>> C(N + 1, vector<long long>(N + 1, 0));
    for (int i = 0; i <= N; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    int max_e = N * (N - 1) / 2;
    vector<long long> pw_M(max_e + 1, 1);
    for (int e = 1; e <= max_e; ++e) {
        pw_M[e] = (pw_M[e - 1] * M) % MOD;
    }

    long long total_graphs = pw_M[max_e];
    long long ans = (1LL * (N - 1) % MOD * total_graphs) % MOD;

    vector<long long> f(N + 1, 0);
    vector<long long> pw_cross(N * N + 1, 1);

    for (int w = 1; w < M; ++w) {
        long long base_cross = (M - w) % MOD;
        pw_cross[0] = 1;
        int max_cross = N * N;
        for (int e = 1; e <= max_cross; ++e) {
            pw_cross[e] = (pw_cross[e - 1] * base_cross) % MOD;
        }

        for (int k = 1; k <= N; ++k) {
            int total_e = k * (k - 1) / 2;
            long long cur = pw_M[total_e];
            for (int j = 1; j < k; ++j) {
                int cross_e = j * (k - j);
                int rem_e = (k - j) * (k - j - 1) / 2;
                long long sub = C[k - 1][j - 1] * f[j] % MOD * pw_cross[cross_e] % MOD * pw_M[rem_e] % MOD;
                cur = (cur - sub + MOD) % MOD;
            }
            f[k] = cur;
        }

        long long total_comp = 0;
        for (int k = 1; k <= N; ++k) {
            int cross_e = k * (N - k);
            int rem_e = (N - k) * (N - k - 1) / 2;
            long long ways = C[N][k] * f[k] % MOD * pw_cross[cross_e] % MOD * pw_M[rem_e] % MOD;
            total_comp = (total_comp + ways) % MOD;
        }

        long long diff = (total_comp - total_graphs + MOD) % MOD;
        ans = (ans + diff) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
