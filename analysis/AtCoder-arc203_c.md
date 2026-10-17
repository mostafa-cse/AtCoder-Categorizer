# Problem Analysis: AtCoder-arc203_c — Destruction of Walls

**Problem ID**: `AtCoder-arc203_c`  
**Contest**: `arc203`  
**Rating / Difficulty**: 2248  
**URL**: https://atcoder.jp/contests/arc203/tasks/arc203_c  
**VJudge Tag**: `[problem:AtCoder-arc203_c]`  
**Category File**: [`../categories/combinatorics/destruction_of_walls_grid_shortest_paths_detours.md`](../categories/combinatorics/destruction_of_walls_grid_shortest_paths_detours.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Factorials and Binomial Coefficients (nCr)`  
- **Topic (Skill)**: `Large Factorials and Binomial Coefficients`  

---

## 1. Problem Statement & Key Idea
Count the number of ways to demolish K walls in an H x W grid such that the top-left room can reach the bottom-right room, given K <= H + W.

## 2. Core Observation & Invariant
Any path from (1, 1) to (H, W) requires at least L = H + W - 2 walls. For K < L: 0 ways. For K = L: exactly C(L, H - 1) shortest paths. For K = L + 1: one shortest path plus 1 extra unused wall, C(L, H - 1) * (E - L). For K = L + 2 = H + W: paths have length L (with 2 extra walls, minus double-counted pairs forming a 1x1 square) plus simple detour paths of length H + W (moving once away from (H, W)).

## 3. Step-by-Step Algorithm
1. 1. Let L = H + W - 2, and total walls E = 2HW - H - W.
2. 2. If K < L: return 0.
3. 3. If K == L: return C(L, H - 1).
4. 4. If K == L + 1: return C(L, H - 1) * (E - L) mod 998244353.
5. 5. If K == L + 2:
6.    - Part A: C(L, H - 1) * C(E - L, 2) - C(H + W - 4, H - 2) * (H + W - 3).
7.    - Part B: Vertical detours (H - 1) * C(H + W - 2, H + 1) for W >= 3, plus horizontal detours (W - 1) * C(H + W - 2, W + 1) for H >= 3.
8.    - Return (Part A + Part B) mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(H + W + T)`
- **Space Complexity**: `O(H + W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;
const int MAX = 1000005;

long long fact[MAX], inv[MAX];

long long mod_pow(long long a, long long b) {
    long long res = 1;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[MAX - 1] = mod_pow(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
}

void solve() {
    long long H, W, K;
    cin >> H >> W >> K;

    long long L = H + W - 2;
    if (K < L) {
        cout << 0 << "\n";
        return;
    }
    if (K == L) {
        cout << nCr(L, H - 1) << "\n";
        return;
    }

    long long E = (2 * (H % MOD) * (W % MOD) - (H % MOD) - (W % MOD) % MOD + MOD) % MOD;

    if (K == L + 1) {
        long long rem = (E - (L % MOD) + MOD) % MOD;
        long long ans = (nCr(L, H - 1) * rem) % MOD;
        cout << ans << "\n";
        return;
    }

    if (K == L + 2) {
        long long rem = (E - (L % MOD) + MOD) % MOD;
        long long ways_rem2 = (rem * ((rem - 1 + MOD) % MOD)) % MOD * inv[2] % MOD;
        long long partA1 = (nCr(L, H - 1) * ways_rem2) % MOD;

        long long sub = (nCr(H + W - 4, H - 2) * ((H + W - 3) % MOD)) % MOD;
        long long partA = (partA1 - sub + MOD) % MOD;

        long long partB = 0;
        if (W >= 3 && H >= 2) {
            long long v_detour = ((H - 1) % MOD * nCr(H + W - 2, H + 1)) % MOD;
            partB = (partB + v_detour) % MOD;
        }
        if (H >= 3 && W >= 2) {
            long long h_detour = ((W - 1) % MOD * nCr(H + W - 2, W + 1)) % MOD;
            partB = (partB + h_detour) % MOD;
        }

        long long ans = (partA + partB) % MOD;
        cout << ans << "\n";
        return;
    }

    cout << 0 << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    int T;
    if (cin >> T) {
        while (T--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
