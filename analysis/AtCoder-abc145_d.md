# Problem Analysis: AtCoder-abc145_d — Knight

**Problem ID**: `AtCoder-abc145_d`  
**Contest**: `abc145`  
**Rating / Difficulty**: 1009  
**URL**: https://atcoder.jp/contests/abc145/tasks/abc145_d  
**VJudge Tag**: `[problem:AtCoder-abc145_d]`  
**Category File**: [`../categories/combinatorics/vector_linear_combination_combinations.md`](../categories/combinatorics/vector_linear_combination_combinations.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Linear Combinations`  
- **Topic (Skill)**: `2-Vector Linear Combination + Modular Binomial Combinatorics`  

---

## 1. Problem Statement & Key Idea
Starting at (0, 0), in each move you can move to (x + 1, y + 2) or (x + 2, y + 1). Find the number of distinct move sequences to reach (X, Y), modulo 10^9 + 7.

**Key Idea**: Let a be the number of (1, 2) moves and b be the number of (2, 1) moves. Then a + 2b = X and 2a + b = Y.

## 2. Core Observation & Invariant
Solving the 2x2 system: subtracting gives b - a = X - Y, adding gives 3(a + b) = X + Y. Hence (X + Y) must be divisible by 3. Solving: a = (2Y - X) / 3 and b = (2X - Y) / 3. If a < 0 or b < 0 or remainders are non-zero, reachable paths = 0. Otherwise, the number of paths is C(a + b, a) modulo 10^9 + 7.

## 3. Step-by-Step Algorithm
1. If (X + Y) % 3 != 0, output 0.
2. Compute a = (2 * Y - X) / 3 and b = (2 * X - Y) / 3.
3. If a < 0 or b < 0, output 0.
4. Compute C(a + b, a) modulo 10^9 + 7 using precomputed factorials and modular inverse.
5. Output the result.

## 4. Complexity Analysis
- **Time Complexity**: `O(X + Y)`
- **Space Complexity**: `O(X + Y)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

long long power_mod(long long base, long long exp) {
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
    return power_mod(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x, y;
    if (!(cin >> x >> y)) return 0;

    if ((x + y) % 3 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    long long a = (2 * y - x) / 3;
    long long b = (2 * x - y) / 3;

    if (a < 0 || b < 0) {
        cout << 0 << "\n";
        return 0;
    }

    long long total = a + b;
    vector<long long> fact(total + 1, 1);
    for (int i = 1; i <= total; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }

    long long ans = fact[total];
    ans = (ans * mod_inv(fact[a])) % MOD;
    ans = (ans * mod_inv(fact[b])) % MOD;

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Mapping 2D movement constraints to 2x2 integer linear equations and combinations.
- **Reusable Pattern**: `Solve linear system for move counts (a, b) -> output C(a + b, a).`
