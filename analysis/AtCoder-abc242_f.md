# Problem Analysis: AtCoder-abc242_f — F. Black and White Rooks

**Problem ID**: `AtCoder-abc242_f`  
**Contest**: `abc242`  
**Rating / Difficulty**: 2268  
**URL**: https://atcoder.jp/contests/abc242/tasks/abc242_f  
**VJudge Tag**: `[problem:AtCoder-abc242_f]`  
**Category File**: [`../categories/combinatorics/pie_2d_chess_rook_placement.md`](../categories/combinatorics/pie_2d_chess_rook_placement.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Place $B$ black rooks and $W$ white rooks on an $N \times M$ grid ($N, M \le 50$) such that no black rook attacks any white rook (rooks attack horizontally/vertically unobstructed). Find the number of valid placements modulo 998244353.

## 2. Core Observation & Invariant
Because rooks of different colors attack along unobstructed lines, no row or column can contain both black and white rooks. Thus, black rooks occupy a subgrid of $r_1$ rows and $c_1$ columns, and white rooks occupy a subgrid of $r_2$ rows and $c_2$ columns, where the row subsets and column subsets are mutually disjoint: $r_1 + r_2 \le N$ and $c_1 + c_2 \le M$.
Let $f(R, C, K)$ denote the number of ways to place $K$ rooks on an $R \times C$ board such that every row and column has at least one rook. By 2D Principle of Inclusion and Exclusion (PIE): $f(R, C, K) = \sum_{i=0}^R \sum_{j=0}^C (-1)^{i+j} \binom{R}{i} \binom{C}{j} \binom{(R - i)(C - j)}{K}$. Precomputing $f$ and summing over disjoint row/col choices gives the total count.

## 3. Step-by-Step Algorithm
1. Precompute factorials and combinations up to $N \times M$.
2. Compute $f(r, c, B)$ and $f(r, c, W)$ for all $1 \le r \le N, 1 \le c \le M$ using 2D PIE over empty rows $i$ and empty columns $j$.
3. Iterate all row partition pairs $1 \le r_1, r_2$ with $r_1 + r_2 \le N$: compute row selection ways $\binom{N}{r_1} \binom{N - r_1}{r_2}$.
4. Iterate all column partition pairs $1 \le c_1, c_2$ with $c_1 + c_2 \le M$: compute column selection ways $\binom{M}{c_1} \binom{M - c_1}{c_2}$.
5. Accumulate product $\text{ways}_r \times \text{ways}_c \times f(r_1, c_1, B) \times f(r_2, c_2, W) \pmod{998244353}$.
6. Output the total sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 M^2)`
- **Space Complexity**: `O(N M)`

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

const int MAX_CELLS = 2600;
vector<long long> fact(MAX_CELLS), invFact(MAX_CELLS);

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAX_CELLS; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAX_CELLS - 1] = modInverse(fact[MAX_CELLS - 1]);
    for (int i = MAX_CELLS - 2; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    int n, m, b, w;
    if (!(cin >> n >> m >> b >> w)) return 0;

    vector<vector<long long>> f_b(n + 1, vector<long long>(m + 1, 0));
    vector<vector<long long>> f_w(n + 1, vector<long long>(m + 1, 0));

    for (int r = 1; r <= n; ++r) {
        for (int c = 1; c <= m; ++c) {
            if (r * c < b && r * c < w) continue;
            long long val_b = 0;
            long long val_w = 0;
            for (int i = 0; i <= r; ++i) {
                int sign_i = (i % 2 == 1 ? -1 : 1);
                for (int j = 0; j <= c; ++j) {
                    int sign = (j % 2 == 1 ? -sign_i : sign_i);
                    int rem_cells = (r - i) * (c - j);
                    long long ways = nCr(r, i) * nCr(c, j) % MOD;
                    if (rem_cells >= b) {
                        long long term_b = ways * nCr(rem_cells, b) % MOD;
                        val_b = (val_b + sign * term_b) % MOD;
                    }
                    if (rem_cells >= w) {
                        long long term_w = ways * nCr(rem_cells, w) % MOD;
                        val_w = (val_w + sign * term_w) % MOD;
                    }
                }
            }
            f_b[r][c] = (val_b % MOD + MOD) % MOD;
            f_w[r][c] = (val_w % MOD + MOD) % MOD;
        }
    }

    long long ans = 0;
    for (int r1 = 1; r1 <= n; ++r1) {
        for (int r2 = 1; r2 <= n - r1; ++r2) {
            long long ways_r = nCr(n, r1) * nCr(n - r1, r2) % MOD;
            for (int c1 = 1; c1 <= m; ++c1) {
                if (f_b[r1][c1] == 0) continue;
                for (int c2 = 1; c2 <= m - c1; ++c2) {
                    if (f_w[r2][c2] == 0) continue;
                    long long ways_c = nCr(m, c1) * nCr(m - c1, c2) % MOD;
                    long long term = ways_r * ways_c % MOD;
                    term = term * f_b[r1][c1] % MOD;
                    term = term * f_w[r2][c2] % MOD;
                    ans = (ans + term) % MOD;
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
