# Problem Analysis: AtCoder-abc003_4 — AtCoder社の冬

**Problem ID**: `AtCoder-abc003_4`  
**Contest**: `abc003`  
**Rating / Difficulty**: 2033  
**URL**: https://atcoder.jp/contests/abc003/tasks/abc003_4  
**VJudge Tag**: `[problem:AtCoder-abc003_4]`  
**Category File**: [`../categories/combinatorics/four_boundary_subgrid_inclusion_exclusion.md`](../categories/combinatorics/four_boundary_subgrid_inclusion_exclusion.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion-Exclusion Principle`  
- **Topic (Skill)**: `4-Boundary Subgrid Bounding Box Inclusion-Exclusion`  

---

## 1. Problem Statement & Key Idea
An R x C grid contains D desks and L laptops placed in an X x Y subgrid such that the bounding box of the D + L items exactly matches the X x Y subgrid. Find the number of valid placements mod 10^9 + 7.

**Key Idea**: There are (R - X + 1) * (C - Y + 1) choices for the X x Y subgrid. Within an X x Y subgrid, the items must span all 4 boundaries: top row, bottom row, left column, right column. By the Principle of Inclusion-Exclusion over the 4 boundaries, there are 2^4 = 16 boundary subsets. For a subset leaving t top rows, b bottom rows, l left columns, r right columns empty, the available subgrid size is x * y = (X - t - b) * (Y - l - r). The number of placements is C(x * y, D) * C(x * y - D, L) with sign (-1)^(boundaries empty).

## 2. Core Observation & Invariant
Exact bounding box containment is standardly solved by 2^4 inclusion-exclusion over the four bounding edges.

## 3. Step-by-Step Algorithm
1. Calculate subgrid placements = (R - X + 1) * (C - Y + 1) mod MOD.
2. Iterate mask from 0 to 15 (bits: 0: top empty, 1: bottom empty, 2: left empty, 3: right empty):
3.   dx = X - (mask & 1) - ((mask >> 1) & 1).
4.   dy = Y - ((mask >> 2) & 1) - ((mask >> 3) & 1).
5.   If dx < 0 or dy < 0: continue.
6.   slots = dx * dy.
7.   if slots < D + L: ways = 0;
8.   else ways = C(slots, D) * C(slots - D, L) % MOD.
9.   Add or subtract ways based on __builtin_parity(mask).
10. Multiply by subgrid placements mod MOD and print.

## 4. Complexity Analysis
- **Time Complexity**: `O(X * Y + 16)`
- **Space Complexity**: `O(X * Y)`

## 5. Core Algorithmic Skill & Learning Takeaway
4-boundary Inclusion-Exclusion for exact rectangular bounding boxes.

**Reusable Pattern**: 4-Wall Inclusion-Exclusion: sum_{mask=0}^{15} (-1)^popcount(mask) C(dx * dy, items).

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

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

long long mod_inv(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, X, Y, D, L;
    if (!(cin >> R >> C >> X >> Y >> D >> L)) return 0;

    int max_val = X * Y + 5;
    vector<long long> fact(max_val), inv(max_val);
    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i < max_val; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[max_val - 1] = mod_inv(fact[max_val - 1]);
    for (int i = max_val - 2; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    long long subgrid_ways = 0;

    for (int mask = 0; mask < 16; ++mask) {
        int t = (mask & 1);
        int b = ((mask >> 1) & 1);
        int l = ((mask >> 2) & 1);
        int r = ((mask >> 3) & 1);

        int dx = X - t - b;
        int dy = Y - l - r;

        if (dx < 0 || dy < 0) continue;
        int slots = dx * dy;
        if (slots < D + L) continue;

        long long ways = (nCr(slots, D) * nCr(slots - D, L)) % MOD;
        if (__builtin_parity(mask)) {
            subgrid_ways = (subgrid_ways - ways + MOD) % MOD;
        } else {
            subgrid_ways = (subgrid_ways + ways) % MOD;
        }
    }

    long long total_positions = (1LL * (R - X + 1) * (C - Y + 1)) % MOD;
    long long ans = (subgrid_ways * total_positions) % MOD;

    cout << ans << "\n";
    return 0;
}
```
