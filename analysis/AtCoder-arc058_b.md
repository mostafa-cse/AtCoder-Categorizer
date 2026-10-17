# Problem Analysis: AtCoder-arc058_b — Iroha and a Grid

**Problem ID**: `AtCoder-arc058_b`  
**Contest**: `arc058`  
**Rating / Difficulty**: 1905  
**URL**: https://atcoder.jp/contests/arc058/tasks/arc058_b  
**VJudge Tag**: `[problem:AtCoder-arc058_b]`  
**Category File**: [`../categories/combinatorics/grid_paths_cutout_bottleneck_partition.md`](../categories/combinatorics/grid_paths_cutout_bottleneck_partition.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Grid Paths`  
- **Topic (Skill)**: `Grid Path Combinations with Rectangular Cutout via Bottleneck Diagonal Partition`  

---

## 1. Problem Statement & Key Idea
In an H x W grid, the bottom-left A x B subgrid (rows H-A+1..H, cols 1..B) cannot be entered. Find the number of paths from (1, 1) to (H, W) moving only right and down, modulo 10^9 + 7.

Every valid path must cross column B to column B + 1 at some row i in [1, H - A]. Since the step from (i, B) to (i, B + 1) is horizontal, each crossing row i defines a disjoint set of paths. The number of paths through row i is binom((i - 1) + (B - 1), i - 1) * binom((H - i) + (W - B - 1), H - i). Summing over all 1 <= i <= H - A gives the answer.

## 2. Core Observation & Invariant
Partitioning paths by the unique step across the vertical cut-line boundary decomposes the restricted grid into independent binomial products.

## 3. Step-by-Step Algorithm
1. Precompute factorials and inverse factorials up to H + W.
2. Iterate row i from 1 to H - A.
3. ways = binom(i - 1 + B - 1, i - 1) * binom(H - i + W - B - 1, H - i) % MOD.
4. ans = (ans + ways) % MOD.
5. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(H + W)`
- **Space Complexity**: `O(H + W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;
const int MAX = 200005;

long long fact[MAX], invFact[MAX];

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

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAX; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAX - 1] = modInverse(fact[MAX - 1]);
    for (int i = MAX - 2; i >= 1; i--) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int h, w, a, b;
    if (!(cin >> h >> w >> a >> b)) return 0;

    long long ans = 0;
    for (int i = 1; i <= h - a; ++i) {
        long long ways1 = nCr((i - 1) + (b - 1), i - 1);
        long long ways2 = nCr((h - i) + (w - b - 1), h - i);
        long long term = (ways1 * ways2) % MOD;
        ans = (ans + term) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Partitioning constrained grid walks by a minimal cut line of disjoint boundary transitions.
- **Reusable Pattern**: `Cutout Grid Walk: Sum over boundary crossing cells binom(start -> (i, B)) * binom((i, B+1) -> target).`
