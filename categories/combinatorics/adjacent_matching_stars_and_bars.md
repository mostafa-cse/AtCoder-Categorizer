# Adjacent Matching Constraints Combinatorics

**Domain**: `Combinatorics`  
**Subtopic**: `Stars and Bars`  

This workbook contains curated, high-quality competitive programming problems teaching **Adjacent Matching Constraints Combinatorics**.

---

## Curated Problems

### `[problem:AtCoder-abc167_e]` — Colorful Blocks
- **Rating / Difficulty**: 1442
- **Contest**: `abc167`
- **Analysis**: [`analysis/AtCoder-abc167_e.md`](../../analysis/AtCoder-abc167_e.md)
- **Key Idea**: Iterate over the exact number of matching adjacent pairs j (0 <= j <= K). Choose which j positions match, color the first block with M choices, and each subsequent block with either 1 choice (if matching) or M - 1 choices (if different).
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;
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

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    long long ans = 0;
    for (int j = 0; j <= k; ++j) {
        long long ways = nCr(n - 1, j) * m % MOD;
        ways = (ways * power(m - 1, n - 1 - j)) % MOD;
        ans = (ans + ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
