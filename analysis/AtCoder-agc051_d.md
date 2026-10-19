# Problem Analysis: AtCoder-agc051_d — D - C4

**Problem ID**: `AtCoder-agc051_d`  
**Contest**: `agc051`  
**Rating / Difficulty**: 2807  
**URL**: https://atcoder.jp/contests/agc051/tasks/agc051_d  
**VJudge Tag**: `[problem:AtCoder-agc051_d]`  
**Category File**: [`../categories/graph_theory/c4_eulerian_walks_best_theorem.md`](../categories/graph_theory/c4_eulerian_walks_best_theorem.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Counting`  
- **Topic (Skill)**: `BEST Theorem`  

---

## 1. Problem Statement & Key Idea
Count Eulerian walks in a 4-cycle graph with undirected edge multiplicities a, b, c, d modulo 998244353.

## 2. Core Observation & Invariant
By the BEST Theorem, the number of Eulerian circuits in a directed graph is given by t_w(G) * prod_v (deg_in(v) - 1)!, where t_w(G) is the number of directed spanning trees rooted at w. In a 4-cycle S-T-U-V-S, directing x edges from S to T uniquely fixes the orientations of all remaining edges (y, z, w) via degree balance at each vertex. The number of directed trees kappa(G, S) is evaluated algebraically via the Matrix Tree Theorem cofactor as (a-x)(b-y)(c-z) + (a-x)(b-y)w + (a-x)zw + yzw.

## 3. Step-by-Step Algorithm
1. 1. Verify parity feasibility: (a + b + c + d) must be even, and opposite edge differences must have matching parity.
2. 2. Iterate x (edges S -> T) from 0 to a.
3. 3. Compute required directed counts y, z, w from alternating balance.
4. 4. If 0 <= y <= b, 0 <= z <= c, 0 <= w <= d:
5.    a. Calculate tree count kappa = (a-x)(b-y)(c-z) + (a-x)(b-y)w + (a-x)zw + yzw.
6.    b. Multiply kappa by deg(S)! * prod_{v != S} (deg(v) - 1)! / (x!(a-x)! y!(b-y)! z!(c-z)! w!(d-w)!).
7. 5. Sum valid circuit counts modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(min(a, b, c, d))`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long a, b, c, d;
    if (!(cin >> a >> b >> c >> d)) return 0;

    if ((a - d) % 2 != 0 || (b - a) % 2 != 0 || (c - b) % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    int max_val = a + b + c + d + 10;
    vector<long long> fact(max_val, 1), inv(max_val, 1);
    for (int i = 1; i < max_val; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[max_val - 1] = power(fact[max_val - 1], MOD - 2);
    for (int i = max_val - 2; i >= 0; i--) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    long long ans = 0;
    for (long long x = 0; x <= a; x++) {
        long long y = x + (b - a) / 2;
        long long z = y + (c - b) / 2;
        long long w = z + (d - c) / 2;
        if (0 <= y && y <= b && 0 <= z && z <= c && 0 <= w && w <= d) {
            long long degS = x + (d - w);
            long long degT = (a - x) + y;
            long long degU = (b - y) + z;
            long long degV = (c - z) + w;

            if (degS == 0 || degT == 0 || degU == 0 || degV == 0) continue;

            long long kappa = ((a - x) % MOD * ((b - y) % MOD) % MOD * ((c - z) % MOD) % MOD +
                               (a - x) % MOD * ((b - y) % MOD) % MOD * (w % MOD) % MOD +
                               (a - x) % MOD * (z % MOD) % MOD * (w % MOD) % MOD +
                               (y % MOD) * (z % MOD) % MOD * (w % MOD) % MOD) % MOD;

            long long num = kappa * fact[degS] % MOD * fact[degT - 1] % MOD * fact[degU - 1] % MOD * fact[degV - 1] % MOD;
            long long den = inv[x] * inv[a - x] % MOD * inv[y] % MOD * inv[b - y] % MOD *
                            inv[z] % MOD * inv[c - z] % MOD * inv[w] % MOD * inv[d - w] % MOD;

            ans = (ans + num * den) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
