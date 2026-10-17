# Principle of Inclusion-Exclusion on Constrained Sequence Derangements

**Domain**: `Combinatorics`  
**Subtopic**: `Inclusion-Exclusion`  

This workbook contains curated, high-quality competitive programming problems teaching **Principle of Inclusion-Exclusion on Constrained Sequence Derangements**.

---

## Curated Problems

### `[problem:AtCoder-abc172_e]` — NEQ
- **Rating / Difficulty**: 1880
- **Contest**: `abc172`
- **Analysis**: [`analysis/AtCoder-abc172_e.md`](../../analysis/AtCoder-abc172_e.md)
- **Key Idea**: The number of choices for A is P(M, N) = M! / (M - N)!. For any fixed sequence A, the number of valid sequences B is identical by symmetry. Using Principle of Inclusion-Exclusion, select k positions where B_i == A_i: C(N, k) ways. The remaining N - k elements of B are chosen from the M - k remaining values: P(M - k, N - k) ways.
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> fact(m + 1), inv(m + 1);
    fact[0] = inv[0] = 1;
    for (int i = 1; i <= m; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[m] = power(fact[m], MOD - 2);
    for (int i = m - 1; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int total, int r) -> long long {
        if (r < 0 || r > total) return 0;
        return fact[total] * inv[r] % MOD * inv[total - r] % MOD;
    };

    auto nPr = [&](int total, int r) -> long long {
        if (r < 0 || r > total) return 0;
        return fact[total] * inv[total - r] % MOD;
    };

    long long ways_b = 0;
    for (int k = 0; k <= n; ++k) {
        long long term = nCr(n, k) * nPr(m - k, n - k) % MOD;
        if (k % 2 == 1) {
            ways_b = (ways_b - term + MOD) % MOD;
        } else {
            ways_b = (ways_b + term) % MOD;
        }
    }

    long long ans = nPr(m, n) * ways_b % MOD;
    cout << ans << "\n";
    return 0;
}
```
