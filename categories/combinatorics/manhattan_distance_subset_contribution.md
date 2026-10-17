# Manhattan Pairwise Distance Contribution over Subsets via Dimension Decoupling

**Domain**: `Combinatorics`  
**Subtopic**: `Linearity of Expectation`  

This workbook contains curated, high-quality competitive programming problems teaching **Manhattan Pairwise Distance Contribution over Subsets via Dimension Decoupling**.

---

## Curated Problems

### `[problem:AtCoder-abc127_e]` — Cell Distance
- **Rating / Difficulty**: 1938
- **Contest**: `abc127`
- **Analysis**: [`analysis/AtCoder-abc127_e.md`](../../analysis/AtCoder-abc127_e.md)
- **Key Idea**: By Linearity of Expectation / Contribution to Sum, any fixed pair of cells (A, B) appears in exactly binom(NM - 2, K - 2) choices of K cells. Manhattan distance |r_1 - r_2| + |c_1 - c_2| decouples into row differences and column differences. For rows, each pair of rows (r_1, r_2) has M cells each, contributing |r_1 - r_2| * M^2. Symmetrically for columns, each pair contributes |c_1 - c_2| * N^2. Sum both and multiply by binom(NM - 2, K - 2).
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N * M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

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

    long long n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    long long total_dist = 0;

    long long m2 = (m * m) % MOD;
    for (long long d = 1; d < n; ++d) {
        long long count = (n - d) * m2 % MOD;
        total_dist = (total_dist + d * count) % MOD;
    }

    long long n2 = (n * n) % MOD;
    for (long long d = 1; d < m; ++d) {
        long long count = (m - d) * n2 % MOD;
        total_dist = (total_dist + d * count) % MOD;
    }

    long long ways = nCr(n * m - 2, k - 2);
    long long ans = (total_dist * ways) % MOD;

    cout << ans << "\n";
    return 0;
}
```
