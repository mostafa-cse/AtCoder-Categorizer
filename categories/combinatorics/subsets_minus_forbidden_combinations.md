# Total Subsets minus Forbidden Combinations (Fermat Mod Inv)

**Domain**: `Combinatorics`  
**Subtopic**: `Modular Arithmetic`  

This workbook contains curated, high-quality competitive programming problems teaching **Total Subsets minus Forbidden Combinations (Fermat Mod Inv)**.

---

## Curated Problems

### [problem:AtCoder-abc156_d] — Bouquet
- **Contest**: `abc156`
- **Rating / Difficulty**: 1014
- **Specific Skill**: Total Subsets minus Forbidden Combinations (Fermat Mod Inv)
- **Individual Analysis**: [`../../analysis/AtCoder-abc156_d.md`](../../analysis/AtCoder-abc156_d.md)
- **Problem Statement Summary**: Given N flowers (N <= 10^9). Make a bouquet with at least 1 flower, but the number of flowers cannot be exactly a or b. Find the number of valid bouquets modulo 10^9 + 7.
- **Core Insight**: Answer is (2^N - 1 - C(N, a) - C(N, b)) mod (10^9 + 7). Because N <= 10^9, we cannot compute factorials up to N; however, a, b <= 2 * 10^5, so C(N, k) can be computed in O(k) steps using falling factorials: C(N, k) = prod_{i=0}^{k-1} (N - i) / k!.
- **Complexity**: Time: `O(a + b + log N)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

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

long long nCr_large_n(long long n, long long r) {
    if (r < 0 || r > n) return 0;
    long long num = 1;
    long long den = 1;
    for (long long i = 0; i < r; ++i) {
        num = (num * ((n - i) % MOD)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    return (num * mod_inv(den)) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, a, b;
    if (!(cin >> n >> a >> b)) return 0;

    long long total = (power_mod(2, n) - 1 + MOD) % MOD;
    long long nCa = nCr_large_n(n, a);
    long long nCb = nCr_large_n(n, b);

    long long ans = (total - nCa - nCb) % MOD;
    ans = (ans + MOD + MOD) % MOD;

    cout << ans << "\n";
    return 0;
}
```
