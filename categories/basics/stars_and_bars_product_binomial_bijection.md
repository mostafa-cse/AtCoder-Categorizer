# Stars and Bars

**Domain**: `Basics`  
**Subtopic**: `Basic Counting`  

This workbook contains curated, high-quality competitive programming problems teaching **Stars and Bars**.

---

## Curated Problems

### `[problem:AtCoder-arc110_d]` — Binomial Coefficient is Fun
- **Rating / Difficulty**: 2075
- **Contest**: `arc110`
- **Analysis**: [`analysis/AtCoder-arc110_d.md`](../../analysis/AtCoder-arc110_d.md)
- **Key Idea**: Consider a row of M balls. Let S = sum_{i=1}^N A_i. The product prod binom(B_i, A_i) asks us to partition a prefix of length sum B_i <= M into N segments of lengths B_1, ..., B_N, and choose A_i items from the i-th segment. By introducing a slack variable B_{N+1} = M - sum B_i, this corresponds to partitioning M items into N+1 bins and choosing A_i items from bin i (for 1 <= i <= N). This is combinatorially isomorphic to choosing N delimiters and S chosen elements from a total sequence of M + N positions! Therefore, the entire sum collapses into a single binomial coefficient: binom(M + N, S + N).
- **Time Complexity**: `O(N + sum A_i)`
- **Space Complexity**: `O(1)`
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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m;
    if (!(cin >> n >> m)) return 0;

    long long sumA = 0;
    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        sumA += a;
    }

    if (sumA > m) {
        cout << 0 << "\n";
        return 0;
    }

    long long top = n + m;
    long long k = sumA + n;

    long long num = 1, den = 1;
    for (long long i = 0; i < k; ++i) {
        num = (num * ((top - i) % MOD)) % MOD;
        den = (den * ((i + 1) % MOD)) % MOD;
    }

    long long ans = (num * modInverse(den)) % MOD;
    cout << ans << "\n";

    return 0;
}
```
