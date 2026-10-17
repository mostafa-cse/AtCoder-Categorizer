# Problem Analysis: AtCoder-abc205_e — White and Black Balls

**Problem ID**: `AtCoder-abc205_e`  
**Contest**: `abc205`  
**Rating / Difficulty**: 2025  
**URL**: https://atcoder.jp/contests/abc205/tasks/abc205_e  
**VJudge Tag**: `[problem:AtCoder-abc205_e]`  
**Category File**: [`../categories/combinatorics/reflection_principle_shifted_diagonal_grid_walks.md`](../categories/combinatorics/reflection_principle_shifted_diagonal_grid_walks.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Catalan Numbers & Grid Walks`  
- **Topic (Skill)**: `Reflection Principle for Shifted Diagonal Grid Walks`  

---

## 1. Problem Statement & Key Idea
Arrange N white balls and M black balls in a line of length N + M such that in every prefix, (count of white balls) <= (count of black balls) + K. Output total valid arrangements mod 10^9 + 7.

**Key Idea**: Interpret as a grid walk from (0, 0) to (N, M) with right-steps (+1 white) and up-steps (+1 black). The condition requires x <= y + K, which means the path must never touch the forbidden line y = x - (K + 1). If N > M + K, the destination (N, M) itself violates the condition, so 0. Otherwise, by Andre's Reflection Principle, any path touching y = x - (K + 1) can be reflected across this line to a path starting at (0, 0) and ending at the reflected destination (M + K + 1, N - K - 1). Thus the invalid paths equal C(N + M, M + K + 1), giving total valid paths C(N + M, N) - C(N + M, M + K + 1).

## 2. Core Observation & Invariant
Grid walks avoiding a shifted diagonal boundary y = x - D are solved in O(1) by reflecting the destination point across the forbidden line.

## 3. Step-by-Step Algorithm
1. If N > M + K: return 0.
2. Precompute factorials and inverse factorials up to N + M mod 10^9 + 7.
3. Total unconstrained paths = C(N + M, N).
4. Reflected invalid paths = C(N + M, M + K + 1).
5. ans = (total - invalid + MOD) % MOD.
6. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. Core Algorithmic Skill & Learning Takeaway
Reflection Principle / Bertrand's ballot theorem for shifted diagonal boundaries.

**Reusable Pattern**: Shifted Diagonal Reflection: Valid paths avoiding y < x - K equals C(N+M, N) - C(N+M, M + K + 1).

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

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    if (n > m + k) {
        cout << 0 << "\n";
        return 0;
    }

    int max_val = n + m + 5;
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

    long long total = nCr(n + m, n);
    long long invalid = nCr(n + m, m + k + 1);

    long long ans = (total - invalid + MOD) % MOD;
    cout << ans << "\n";

    return 0;
}
```
