# Prime Factorization + Stars and Bars on Exponents

**Domain**: `Number Theory`  
**Subtopic**: `Prime Factorization`  

This workbook contains curated, high-quality competitive programming problems teaching **Prime Factorization + Stars and Bars on Exponents**.

---

## Curated Problems

### `[problem:AtCoder-abc110_d]` — Factorization
- **Rating / Difficulty**: 1695
- **Contest**: `abc110`
- **Analysis**: [`analysis/AtCoder-abc110_d.md`](../../analysis/AtCoder-abc110_d.md)
- **Key Idea**: Prime factorize M = prod p_i^{e_i}. Because prime factorizations are unique, the exponent e_i of each prime p_i must be distributed across the N variables independently.
- **Time Complexity**: `O(sqrt(M) + log(MOD))`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
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

void precompute() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAX - 1] = power(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    long long ans = 1;
    long long temp = m;

    for (long long d = 2; d * d <= temp; ++d) {
        if (temp % d == 0) {
            int e = 0;
            while (temp % d == 0) {
                e++;
                temp /= d;
            }
            ans = (ans * nCr(e + n - 1, n - 1)) % MOD;
        }
    }

    if (temp > 1) {
        ans = (ans * nCr(1 + n - 1, n - 1)) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
