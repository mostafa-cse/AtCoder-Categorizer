# Problem Analysis: AtCoder-abc321_g — G. Electric Circuit

**Problem ID**: `AtCoder-abc321_g`  
**Contest**: `abc321`  
**Rating / Difficulty**: 2439  
**URL**: https://atcoder.jp/contests/abc321/tasks/abc321_g  
**VJudge Tag**: `[problem:AtCoder-abc321_g]`  
**Category File**: [`../categories/dynamic_programming/electric_circuit_random_connections_bitmask_dp.md`](../categories/dynamic_programming/electric_circuit_random_connections_bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Find the expected number of connected components when $M$ cables randomly connect $M$ red terminals and $M$ blue terminals attached to $N \le 16$ circuit parts. By linearity of expectation, total components is $\sum_{S \subseteq V} [S \text{ is a connected component}]$. A subset $S$ forms an isolated connected component iff it has equal red and blue terminals ($cntR(S) = cntB(S) = k$), and its internal subgraph is connected ($c(S)$ ways).

## 2. Core Observation & Invariant
The number of internally connected configurations $c(S)$ is computed via standard subset DP: $c(S) = g(S) - \sum_{T \subset S, v \in T} c(T) g(S \setminus T)$, where $g(S) = (cntR(S))!$ if $cntR(S) == cntB(S)$, else 0.

## 3. Step-by-Step Algorithm
1. 1. Compute $cntR[mask]$ and $cntB[mask]$ for all $2^N$ subsets.
2. 2. Set $g[mask] = fact[cntR[mask]]$ if $cntR[mask] == cntB[mask]$, else 0.
3. 3. Compute $c[mask]$ by fixing the lowest bit $v \in mask$ and subtracting $c[T] \times g[mask \setminus T]$ over all proper submasks $T \subsetneq mask$ containing $v$.
4. 4. Sum $c[mask] \times g[full\_mask \setminus mask]$ over all non-empty subsets $mask$.
5. 5. Multiply by $(M!)^{-1} \pmod{998244353}$ to output the expected value.

## 4. Complexity Analysis
- **Time Complexity**: `O(3^N + M)`
- **Space Complexity**: `O(2^N)`

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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<int> R(M), B(M);
    for (int i = 0; i < M; ++i) { cin >> R[i]; R[i]--; }
    for (int i = 0; i < M; ++i) { cin >> B[i]; B[i]--; }

    vector<long long> fact(M + 1, 1);
    for (int i = 1; i <= M; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }

    vector<int> cntR(1 << N, 0), cntB(1 << N, 0);
    for (int r : R) cntR[1 << r]++;
    for (int b : B) cntB[1 << b]++;

    for (int mask = 1; mask < (1 << N); ++mask) {
        int lsb = mask & -mask;
        cntR[mask] = cntR[mask ^ lsb] + cntR[lsb];
        cntB[mask] = cntB[mask ^ lsb] + cntB[lsb];
    }

    vector<long long> g(1 << N, 0);
    for (int mask = 0; mask < (1 << N); ++mask) {
        if (cntR[mask] == cntB[mask]) {
            g[mask] = fact[cntR[mask]];
        }
    }

    vector<long long> c(1 << N, 0);
    for (int mask = 1; mask < (1 << N); ++mask) {
        if (g[mask] == 0) continue;
        int v_bit = mask & -mask;
        long long res = g[mask];
        int rem = mask ^ v_bit;
        for (int sub = rem; ; sub = (sub - 1) & rem) {
            int T = sub | v_bit;
            if (T != mask) {
                if (c[T] != 0 && g[mask ^ T] != 0) {
                    res = (res - c[T] * g[mask ^ T]) % MOD;
                }
            }
            if (sub == 0) break;
        }
        c[mask] = (res % MOD + MOD) % MOD;
    }

    long long total_components = 0;
    int full_mask = (1 << N) - 1;
    for (int mask = 1; mask < (1 << N); ++mask) {
        if (c[mask] != 0 && g[full_mask ^ mask] != 0) {
            long long term = (c[mask] * g[full_mask ^ mask]) % MOD;
            total_components = (total_components + term) % MOD;
        }
    }

    long long ans = (total_components * modInverse(fact[M])) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
