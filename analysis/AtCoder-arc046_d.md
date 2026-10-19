# Problem Analysis: AtCoder-arc046_d — D - うさぎとマス目

**Problem ID**: `AtCoder-arc046_d`  
**Contest**: `arc046`  
**Rating / Difficulty**: 2852  
**URL**: https://atcoder.jp/contests/arc046/tasks/arc046_d  
**VJudge Tag**: `[problem:AtCoder-arc046_d]`  
**Category File**: [`../categories/graph_theory/torus_grid_hamiltonian_cycle_gcd.md`](../categories/graph_theory/torus_grid_hamiltonian_cycle_gcd.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Hamiltonian Path`  
- **Topic (Skill)**: `Hamiltonian Path and Cycle`  

---

## 1. Problem Statement & Key Idea
A rabbit starts at (0, 0) on an H x W torus grid and repeatedly moves either 1 step down or 1 step right (both wrap around). Find the number of valid move sequences of length HW that visit all HW squares exactly once (forming a Hamiltonian cycle) modulo 10^9+7.

## 2. Core Observation & Invariant
Since the rabbit visits all HW cells in HW steps, it visits each cell exactly once. Let R be the number of right moves and D be the number of down moves, with R + D = HW. The sequence of coordinates visited forms a single connected cycle of length HW on the torus if and only if gcd(R, W) = 1 and gcd(D, H) = 1. By Burnside's Lemma / cycle decomposition, any valid step choices must cover the torus grid evenly. This allows counting valid sequences using gcd factorization and modular binomial combinations.

## 3. Step-by-Step Algorithm
1. 1. Factorize H and W to identify prime factors.
2. 2. Iterate over possible step parameters or apply the torus GCD cycle theorem.
3. 3. Compute combinations using precomputed factorials modulo 10^9+7.
4. 4. Sum over valid paths and output the result.

## 4. Complexity Analysis
- **Time Complexity**: `O(H + W)`
- **Space Complexity**: `O(H + W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

static const long long MOD = 1000000007;

long long gcd(long long a, long long b) {
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

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

    long long H, W;
    if (!(cin >> H >> W)) return 0;

    long long d = gcd(H, W);

    vector<long long> fact(d + 1, 1), inv(d + 1, 1);
    for (int i = 1; i <= d; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[d] = modInverse(fact[d]);
    for (int i = d - 1; i >= 0; i--) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](long long n, long long r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    long long target = (H * W) / d;
    long long ans = 0;

    for (long long x = 0; x <= d; x++) {
        long long y = d - x;
        long long gw = (x > 0) ? gcd(W, x) : W;
        long long gh = (y > 0) ? gcd(H, y) : H;

        long long per_w = W / gw;
        long long per_h = H / gh;

        long long g_per = gcd(per_w, per_h);
        long long cur_lcm = (per_w / g_per) * per_h; // won't overflow if target <= HW/d

        if (cur_lcm == target) {
            ans = (ans + nCr(d, x)) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
