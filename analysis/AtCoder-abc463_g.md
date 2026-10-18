# Problem Analysis: AtCoder-abc463_g — G - Random Walk Distance

**Problem ID**: `AtCoder-abc463_g`  
**Contest**: `abc463`  
**Rating / Difficulty**: 2452  
**URL**: https://atcoder.jp/contests/abc463/tasks/abc463_g  
**VJudge Tag**: `[problem:AtCoder-abc463_g]`  
**Category File**: [`../categories/data_structures_ds/random_walk_distance_mos_algorithm.md`](../categories/data_structures_ds/random_walk_distance_mos_algorithm.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Mo's Algorithm`  

---

## 1. Problem Statement & Key Idea
Compute the expected distance $\mathbb{E}[|x' - X|]$ after an $N$-step 1D random walk across $T$ offline queries modulo 998244353.

## 2. Core Observation & Invariant
If $|X| \ge N$, the sign of $x' - X$ is constant, giving answer $|X|$. For $|X| < N$, letting $M = \lceil (N + X) / 2 \rceil$, algebraic expansion yields $\mathbb{E}[|x' - X|] = -X + 2^{-(N-1)} ((N + X) f(N, M) - 2 g(N, M))$, where $f(N, M) = \sum_{i=0}^{M-1} \binom{N}{i}$ and $g(N, M) = \sum_{i=0}^{M-1} i \binom{N}{i}$. Both $f$ and $g$ admit $O(1)$ transitions under $N \to N \pm 1$ and $M \to M \pm 1$, enabling Mo's Algorithm over the 2D query points $(N, M)$ in $O(N \sqrt{T})$ time.

## 3. Step-by-Step Algorithm
1. 1. If $|X| \ge N$, answer is directly $|X| \pmod{998244353}$.
2. 2. Otherwise, formulate query point $(N, M)$ with $M = \lfloor (N + X + 1) / 2 \rfloor$.
3. 3. Sort queries using Mo's Hilbert / block order with block size $B = \max(1, 200000 / \sqrt{T})$.
4. 4. Maintain current values of $f(N, M)$ and $g(N, M)$ using $O(1)$ binomial transitions:
5.    - $M \to M \pm 1$: add / subtract $\binom{N}{M}$ and $M \binom{N}{M}$.
6.    - $N \to N + 1$: $g_{next} = 2g + f - M \binom{N}{M-1}$, $f_{next} = 2f - \binom{N}{M-1}$.
7.    - $N \to N - 1$: $f_{prev} = (f + \binom{N-1}{M-1}) / 2$, $g_{prev} = (g - f_{prev} + M \binom{N-1}{M-1}) / 2$.
8. 5. Compute the expectation for each query and output in original order.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \sqrt{T} + T \log T)`
- **Space Complexity**: `O(N + T)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
const int INV2 = (MOD + 1) / 2;

const int MAX = 500000;
long long fact[MAX + 1];
long long inv[MAX + 1];
long long inv2_pow[MAX + 1];

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

void init() {
    fact[0] = 1;
    inv2_pow[0] = 1;
    for (int i = 1; i <= MAX; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
        inv2_pow[i] = (inv2_pow[i - 1] * INV2) % MOD;
    }
    inv[MAX] = power(fact[MAX], MOD - 2);
    for (int i = MAX - 1; i >= 0; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }
}

inline long long C(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD;
}

struct Query {
    int id;
    int n, m;
    long long X;
    int block;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    init();

    int T;
    if (!(cin >> T)) return 0;

    int B = max(1, (int)(200000 / sqrt(max(1, T))));

    vector<Query> queries;
    queries.reserve(T);
    vector<long long> ans(T);

    for (int i = 0; i < T; ++i) {
        int N;
        long long X;
        cin >> N >> X;
        if (X >= N) {
            ans[i] = (X % MOD + MOD) % MOD;
        } else if (X <= -N) {
            ans[i] = ((-X) % MOD + MOD) % MOD;
        } else {
            int M = (N + X + 1) / 2;
            queries.push_back({i, N, M, X, N / B});
        }
    }

    sort(queries.begin(), queries.end(), [](const Query &a, const Query &b) {
        if (a.block != b.block) return a.block < b.block;
        return (a.block & 1) ? a.m < b.m : a.m > b.m;
    });

    int cur_n = 1, cur_m = 1;
    long long cur_f = 1; // sum_{i=0}^{0} C(1, i) = 1
    long long cur_g = 0; // sum_{i=0}^{0} i * C(1, i) = 0

    for (const auto &q : queries) {
        int target_n = q.n;
        int target_m = q.m;

        // Move m
        while (cur_m < target_m) {
            cur_f = (cur_f + C(cur_n, cur_m)) % MOD;
            cur_g = (cur_g + (long long)cur_m * C(cur_n, cur_m)) % MOD;
            cur_m++;
        }
        while (cur_m > target_m) {
            cur_m--;
            cur_f = (cur_f - C(cur_n, cur_m) + MOD) % MOD;
            cur_g = (cur_g - (long long)cur_m * C(cur_n, cur_m) % MOD + MOD) % MOD;
        }

        // Move n
        while (cur_n < target_n) {
            long long comb = C(cur_n, cur_m - 1);
            cur_g = (2 * cur_g + cur_f - (long long)cur_m * comb % MOD + MOD) % MOD;
            cur_f = (2 * cur_f - comb + MOD) % MOD;
            cur_n++;
        }
        while (cur_n > target_n) {
            long long comb = C(cur_n - 1, cur_m - 1);
            long long next_f = (cur_f + comb) * INV2 % MOD;
            long long next_g = (cur_g - next_f + (long long)cur_m * comb % MOD + MOD) * INV2 % MOD;
            cur_f = next_f;
            cur_g = next_g;
            cur_n--;
        }

        long long term = ((target_n + q.X) % MOD * cur_f - 2 * cur_g) % MOD;
        term = (term + MOD) % MOD;
        long long res = (-q.X + term * inv2_pow[target_n - 1]) % MOD;
        res = (res + MOD) % MOD;
        ans[q.id] = res;
    }

    for (int i = 0; i < T; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
