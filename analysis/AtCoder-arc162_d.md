# Problem Analysis: AtCoder-arc162_d — D. Smallest Vertices

**Problem ID**: `AtCoder-arc162_d`  
**Contest**: `arc162`  
**Rating / Difficulty**: 2568  
**URL**: https://atcoder.jp/contests/arc162/tasks/arc162_d  
**VJudge Tag**: `[problem:AtCoder-arc162_d]`  
**Category File**: [`../categories/graph_theory/smallest_vertices_prufer_tree_counting.md`](../categories/graph_theory/smallest_vertices_prufer_tree_counting.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Counting`  
- **Topic (Skill)**: `Prufer Code`  

---

## 1. Problem Statement & Key Idea
Count the total number of good vertices ($f(v) = v$) across all directed rooted trees with vertex 1 as root and specified out-degrees $(d_1, \dots, d_N)$.

## 2. Core Observation & Invariant
Vertex $v$ satisfies $f(v) = v$ iff all vertices in its subtree belong to $\{v, v+1, \dots, N\}$. By Cayley's multinomial formula via Prüfer sequences, the number of trees where $\{v\} \cup S$ forms $v$'s subtree depends only on $|S| = m$ and $\sum_{u \in S} d_u = m - d_v$, with contribution $\frac{(m - 1)! (N - m - 2)!}{(d_1 - 1)! \prod_{i=2}^N d_i!} d_v$.

## 3. Step-by-Step Algorithm
1. 1. Precompute total tree count $T = \frac{(N - 2)!}{(d_1 - 1)! \prod_{i=2}^N d_i!}$. Vertex 1 is good in all $T$ trees.
2. 2. Maintain suffix DP $dp[m][s]$: number of subsets of $\{v+1, \dots, N\}$ with cardinality $m$ and degree sum $s$.
3. 3. Iterate $v$ from $N$ down to 2. If $d_v = 0$, $v$ contributes $T$. Else accumulate $dp[m][m - d_v] \times \text{coeff}(m, d_v)$.
4. 4. Insert $d_v$ into the DP table.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<int> d(N);
    for (int i = 0; i < N; ++i) cin >> d[i];

    vector<long long> fact(N + 1), invFact(N + 1);
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i <= N; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }

    long long denom = invFact[d[0] - 1];
    for (int i = 1; i < N; ++i) {
        denom = (denom * invFact[d[i]]) % MOD;
    }

    long long T = (fact[N - 2] * denom) % MOD;
    long long ans = T; // v = 1 is good in all T trees

    vector<vector<long long>> dp(N, vector<long long>(N, 0));
    dp[0][0] = 1;

    for (int v = N; v >= 2; --v) {
        int dv = d[v - 1];
        if (dv == 0) {
            ans = (ans + T) % MOD;
        } else {
            for (int m = dv; m < N; ++m) {
                int s = m - dv;
                if (s < N && dp[m][s] > 0) {
                    long long ways = dp[m][s];
                    long long coeff = (fact[m - 1] * fact[N - m - 2]) % MOD;
                    coeff = (coeff * denom) % MOD;
                    coeff = (coeff * dv) % MOD;
                    ans = (ans + ways * coeff) % MOD;
                }
            }
        }
        for (int m = N - 2; m >= 0; --m) {
            for (int s = N - 1 - dv; s >= 0; --s) {
                if (dp[m][s]) {
                    dp[m + 1][s + dv] = (dp[m + 1][s + dv] + dp[m][s]) % MOD;
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
