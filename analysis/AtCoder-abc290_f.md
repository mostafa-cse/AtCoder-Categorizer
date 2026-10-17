# Problem Analysis: AtCoder-abc290_f — F. Maximum Diameter

**Problem ID**: `AtCoder-abc290_f`  
**Contest**: `abc290`  
**Rating / Difficulty**: 2300  
**URL**: https://atcoder.jp/contests/abc290/tasks/abc290_f  
**VJudge Tag**: `[problem:AtCoder-abc290_f]`  
**Category File**: [`../categories/basics/stars_and_bars_tree_diameter_degree_sequences.md`](../categories/basics/stars_and_bars_tree_diameter_degree_sequences.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Stars and Bars`  

---

## 1. Problem Statement & Key Idea
Compute the sum of maximum possible tree diameters over all valid degree sequences of size $N$, modulo 998244353.

## 2. Core Observation & Invariant
For any valid tree degree sequence $d_1, \dots, d_N$ with $\sum d_i = 2N - 2$ having $k$ leaves ($d_i = 1$), the maximum possible diameter is achieved by arranging all $N - k$ internal vertices in a simple path, giving maximum diameter $N - k + 1$. Summing $(N - k + 1)$ across all valid degree sequences simplifies algebraically to $(N+1) \binom{2N-3}{N-1} - N \binom{2N-4}{N-2}$.

## 3. Step-by-Step Algorithm
1. 1. In any tree on $N$ vertices, the degree sequence satisfies $d_i \ge 1$ and $\sum d_i = 2N - 2$.
2. 2. A vertex $i$ is a leaf iff $d_i = 1$. The remaining $N - k$ vertices are internal vertices ($d_i \ge 2$).
3. 3. To maximize the diameter for a given degree sequence, arrange all internal vertices in a line (caterpillar tree). The longest path visits all $N - k$ internal vertices plus two endpoint leaves, giving diameter $(N - k - 1) + 2 = N - k + 1$.
4. 4. To sum $(N - k + 1)$ over all degree sequences, we count the number of compositions of $\sum (d_i - 1) = N - 2$ into $N$ non-negative parts:
5.    - Total degree sequences: $\binom{(N - 2) + N - 1}{N - 1} = \binom{2N - 3}{N - 1}$.
6.    - Each leaf corresponds to $d_i - 1 = 0$. By linearity of expectation, the expected number of non-zero entries (internal nodes) corresponds to $(N+1) \binom{2N-3}{N-1} - N \binom{2N-4}{N-2}$.
7. 5. Precompute factorials up to $2 \times 10^6$ to answer each query in $O(1)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + T)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;
static const int MAX = 2000005;

long long fact[MAX];
long long inv[MAX];

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

void precompute() {
    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i < MAX; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[MAX - 1] = power(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
}

void solve() {
    int N;
    if (!(cin >> N)) return;
    if (N == 2) {
        cout << 1 << "\n";
        return;
    }
    long long term1 = (1LL * (N + 1) * nCr(2 * N - 3, N - 1)) % MOD;
    long long term2 = (1LL * N * nCr(2 * N - 4, N - 2)) % MOD;
    long long ans = (term1 - term2 + MOD) % MOD;
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    precompute();
    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
