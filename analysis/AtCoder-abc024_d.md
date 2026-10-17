# Problem Analysis: AtCoder-abc024_d — 動的計画法

**Problem ID**: `AtCoder-abc024_d`  
**Contest**: `abc024`  
**Rating / Difficulty**: 2050  
**URL**: https://atcoder.jp/contests/abc024/tasks/abc024_d  
**VJudge Tag**: `[problem:AtCoder-abc024_d]`  
**Category File**: [`../categories/math/modular_inverse_parameter_reconstruction.md`](../categories/math/modular_inverse_parameter_reconstruction.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Number Theory`  
- **Topic (Skill)**: `Modular Inverse Parameter Reconstruction from Recurrence Matrix`  

---

## 1. Problem Statement & Key Idea
In a grid where cell (r, c) contains C(r + c, r) mod 10^9 + 7, you are given the values of three adjacent cells A = (r, c), B = (r + 1, c), and C = (r, c + 1). Find the integers r and c.

**Key Idea**: From the recurrence: B / A = (r + c + 1) / (r + 1) = 1 + c / (r + 1), and C / A = (r + c + 1) / (c + 1) = 1 + r / (c + 1). This yields a 2x2 linear system in r and c over Z / (10^9 + 7)Z. Cross-multiplying and solving directly produces exact formulas: r = (B * C - A * B) / (A * B + A * C - B * C) mod 10^9 + 7, and c = (B * C - A * C) / (A * B + A * C - B * C) mod 10^9 + 7, computable in O(log MOD).

## 2. Core Observation & Invariant
Adjacent values in the Pascal grid algebraically constrain the coordinates into a linear system solvable via modular division.

## 3. Step-by-Step Algorithm
1. Compute denominator D = (A * B + A * C - B * C) mod MOD.
2. Compute numerator_r = (B * C - A * B) mod MOD.
3. Compute numerator_c = (B * C - A * C) mod MOD.
4. r = numerator_r * inv(D) mod MOD.
5. c = numerator_c * inv(D) mod MOD.
6. Output r and c.

## 4. Complexity Analysis
- **Time Complexity**: `O(log MOD)`
- **Space Complexity**: `O(1)`

## 5. Core Algorithmic Skill & Learning Takeaway
Modular parameter inversion from discrete recurrence relations.

**Reusable Pattern**: Recurrence Inversion: Setting up coordinate ratios to derive closed-form modular fractions r = f(A,B,C) / g(A,B,C).

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>

using namespace std;

const long long MOD = 1e9 + 7;

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

    long long A, B, C;
    if (!(cin >> A >> B >> C)) return 0;

    // Denominator = (A * B + A * C - B * C) % MOD
    long long den = (A * B + A * C - B * C) % MOD;
    den = (den % MOD + MOD) % MOD;

    long long inv_den = mod_inv(den);

    // r = (B * C - A * B) / Den
    long long num_r = (B * C - A * B) % MOD;
    num_r = (num_r % MOD + MOD) % MOD;
    long long r = (num_r * inv_den) % MOD;

    // c = (B * C - A * C) / Den
    long long num_c = (B * C - A * C) % MOD;
    num_c = (num_c % MOD + MOD) % MOD;
    long long c = (num_c * inv_den) % MOD;

    cout << r << " " << c << "\n";
    return 0;
}
```
