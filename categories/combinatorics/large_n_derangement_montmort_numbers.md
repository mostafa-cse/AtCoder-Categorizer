# Large N Derangement Counting via Combinations and Montmort Numbers

**Domain**: `Combinatorics`  
**Subtopic**: `Inclusion-Exclusion Principle`  

This workbook contains curated, high-quality competitive programming problems teaching **Large N Derangement Counting via Combinations and Montmort Numbers**.

---

## Curated Problems

### `[problem:AtCoder-arc009_3]` — 高橋君、24歳
- **Rating / Difficulty**: 2015
- **Contest**: `arc009`
- **Analysis**: [`analysis/AtCoder-arc009_3.md`](../../analysis/AtCoder-arc009_3.md)
- **Key Idea**: The problem asks for permutations of N elements with exactly K non-fixed points. First, choose the K elements to be deranged in C(N, K) ways. Second, arrange these K elements into a complete derangement in D_K ways (Montmort numbers). Total answer is C(N, K) * D_K mod 1777777777. Since N <= 10^18 and K <= 777777, C(N, K) is computed as (N * (N-1) * ... * (N-K+1)) / K! in O(K) time, and D_K is computed via D_i = (i - 1) * (D_{i-1} + D_{i-2}) mod M in O(K) time.
- **Time Complexity**: `O(K)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

using namespace std;

const long long MOD = 1777777777;

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

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    // 1. Compute C(N, K) % MOD
    long long num = 1;
    long long den = 1;
    for (long long i = 0; i < k; ++i) {
        num = (num * ((n - i) % MOD)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    long long c_nk = (num * mod_inv(den)) % MOD;

    // 2. Compute D_K % MOD (Montmort numbers)
    // D_0 = 1, D_1 = 0, D_i = (i - 1) * (D_{i-1} + D_{i-2}) % MOD
    long long d_prev2 = 1; // D_0
    long long d_prev1 = 0; // D_1
    long long d_cur = (k == 0 ? 1 : 0);

    for (long long i = 2; i <= k; ++i) {
        d_cur = ((i - 1) % MOD * (d_prev1 + d_prev2)) % MOD;
        d_prev2 = d_prev1;
        d_prev1 = d_cur;
    }

    long long ans = (c_nk * d_cur) % MOD;
    cout << ans << "\n";

    return 0;
}
```
