# Modular Inverse Parameter Reconstruction from Recurrence Matrix

**Domain**: `Math`  
**Subtopic**: `Number Theory`  

This workbook contains curated, high-quality competitive programming problems teaching **Modular Inverse Parameter Reconstruction from Recurrence Matrix**.

---

## Curated Problems

### `[problem:AtCoder-abc024_d]` — 動的計画法
- **Rating / Difficulty**: 2050
- **Contest**: `abc024`
- **Analysis**: [`analysis/AtCoder-abc024_d.md`](../../analysis/AtCoder-abc024_d.md)
- **Key Idea**: From the recurrence: B / A = (r + c + 1) / (r + 1) = 1 + c / (r + 1), and C / A = (r + c + 1) / (c + 1) = 1 + r / (c + 1). This yields a 2x2 linear system in r and c over Z / (10^9 + 7)Z. Cross-multiplying and solving directly produces exact formulas: r = (B * C - A * B) / (A * B + A * C - B * C) mod 10^9 + 7, and c = (B * C - A * C) / (A * B + A * C - B * C) mod 10^9 + 7, computable in O(log MOD).
- **Time Complexity**: `O(log MOD)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
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
