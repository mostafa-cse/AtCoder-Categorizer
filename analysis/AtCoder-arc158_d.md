# Problem Analysis: AtCoder-arc158_d — D. Equation

**Problem ID**: `AtCoder-arc158_d`  
**Contest**: `arc158`  
**Rating / Difficulty**: 2893  
**URL**: https://atcoder.jp/contests/arc158/tasks/arc158_d  
**VJudge Tag**: `[problem:AtCoder-arc158_d]`  
**Category File**: [`../categories/miscellaneous/homogeneous_degree_scaling_randomized.md`](../categories/miscellaneous/homogeneous_degree_scaling_randomized.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Randomized`  
- **Topic (Skill)**: `Randomized Algorithms`  

---

## 1. Problem Statement & Key Idea
Given n and prime p, find three distinct integers x, y, z in [1, p-1] satisfying (x+y+z)(x^n+y^n+z^n)(x^{2n}+y^{2n}+z^{2n}) = x^{3n}+y^{3n}+z^{3n} modulo p.

## 2. Core Observation & Invariant
Both sides of the equation are homogeneous polynomials: LHS has degree 1 + n + 2n = 3n + 1, while RHS has degree 3n. If we choose distinct random non-zero (x_0, y_0, z_0) and scale them by factor k, LHS becomes k^{3n+1} LHS_0 and RHS becomes k^{3n} RHS_0. Equating LHS and RHS gives k = RHS_0 / LHS_0 mod p. As long as LHS_0 != 0 and RHS_0 != 0, this yields a valid scaling factor k in O(log p) time.

## 3. Step-by-Step Algorithm
1. 1. Pick three distinct integers x_0, y_0, z_0 in [1, p-1] uniformly at random.
2. 2. Compute power sums s_1, s_n, s_{2n}, s_{3n} modulo p.
3. 3. Evaluate LHS_0 = s_1 * s_n * s_{2n} mod p and RHS_0 = s_{3n} mod p.
4. 4. If LHS_0 != 0 and RHS_0 != 0, compute k = RHS_0 * (LHS_0)^{-1} mod p.
5. 5. If k * x_0, k * y_0, k * z_0 mod p are all distinct and non-zero, output them; otherwise retry.

## 4. Complexity Analysis
- **Time Complexity**: `O(log p) expected`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

using namespace std;

long long power(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (__int128)res * base % mod;
        base = (__int128)base * base % mod;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n, long long mod) {
    return power(n, mod - 2, mod);
}

void solve(mt19937_64& rng) {
    long long n, p;
    if (!(cin >> n >> p)) return;

    uniform_int_distribution<long long> dist(1, p - 1);

    while (true) {
        long long x = dist(rng);
        long long y = dist(rng);
        while (y == x) y = dist(rng);
        long long z = dist(rng);
        while (z == x || z == y) z = dist(rng);

        long long s1 = (x + y + z) % p;
        long long sn = (power(x, n, p) + power(y, n, p) + power(z, n, p)) % p;
        long long s2n = (power(x, 2 * n, p) + power(y, 2 * n, p) + power(z, 2 * n, p)) % p;

        long long lhs0 = (__int128)s1 * sn % p * s2n % p;
        long long rhs0 = (power(x, 3 * n, p) + power(y, 3 * n, p) + power(z, 3 * n, p)) % p;

        if (lhs0 != 0 && rhs0 != 0) {
            long long k = rhs0 * modInverse(lhs0, p) % p;
            long long nx = (__int128)x * k % p;
            long long ny = (__int128)y * k % p;
            long long nz = (__int128)z * k % p;

            vector<long long> ans = {nx, ny, nz};
            sort(ans.begin(), ans.end());

            if (ans[0] > 0 && ans[0] < ans[1] && ans[1] < ans[2]) {
                cout << ans[0] << " " << ans[1] << " " << ans[2] << "\n";
                return;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    mt19937_64 rng(1337);

    int t;
    if (cin >> t) {
        while (t--) {
            solve(rng);
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
