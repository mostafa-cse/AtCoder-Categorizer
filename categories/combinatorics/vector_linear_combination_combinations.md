# 2-Vector Linear Combination + Modular Binomial Combinatorics

**Domain**: `Combinatorics`  
**Subtopic**: `Linear Combinations`  

This workbook contains curated, high-quality competitive programming problems teaching **2-Vector Linear Combination + Modular Binomial Combinatorics**.

---

## Curated Problems

### [problem:AtCoder-abc145_d] — Knight
- **Contest**: `abc145`
- **Rating / Difficulty**: 1009
- **Specific Skill**: 2-Vector Linear Combination + Modular Binomial Combinatorics
- **Individual Analysis**: [`../../analysis/AtCoder-abc145_d.md`](../../analysis/AtCoder-abc145_d.md)
- **Problem Statement Summary**: Starting at (0, 0), in each move you can move to (x + 1, y + 2) or (x + 2, y + 1). Find the number of distinct move sequences to reach (X, Y), modulo 10^9 + 7.
- **Core Insight**: Solving the 2x2 system: subtracting gives b - a = X - Y, adding gives 3(a + b) = X + Y. Hence (X + Y) must be divisible by 3. Solving: a = (2Y - X) / 3 and b = (2X - Y) / 3. If a < 0 or b < 0 or remainders are non-zero, reachable paths = 0. Otherwise, the number of paths is C(a + b, a) modulo 10^9 + 7.
- **Complexity**: Time: `O(X + Y)` | Space: `O(X + Y)`
- **Verified C++ Implementation**:
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
