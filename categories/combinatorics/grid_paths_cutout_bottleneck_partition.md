# Grid Path Combinations with Rectangular Cutout via Bottleneck Diagonal Partition

**Domain**: `Combinatorics`  
**Subtopic**: `Grid Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Grid Path Combinations with Rectangular Cutout via Bottleneck Diagonal Partition**.

---

## Curated Problems

### `[problem:AtCoder-arc058_b]` — Iroha and a Grid
- **Rating / Difficulty**: 1905
- **Contest**: `arc058`
- **Analysis**: [`analysis/AtCoder-arc058_b.md`](../../analysis/AtCoder-arc058_b.md)
- **Key Idea**: Every valid path must cross column B to column B + 1 at some row i in [1, H - A]. Since the step from (i, B) to (i, B + 1) is horizontal, each crossing row i defines a disjoint set of paths. The number of paths through row i is binom((i - 1) + (B - 1), i - 1) * binom((H - i) + (W - B - 1), H - i). Summing over all 1 <= i <= H - A gives the answer.
- **Time Complexity**: `O(H + W)`
- **Space Complexity**: `O(H + W)`
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

    int h, w, a, b;
    if (!(cin >> h >> w >> a >> b)) return 0;

    long long ans = 0;
    for (int i = 1; i <= h - a; ++i) {
        long long ways1 = nCr((i - 1) + (b - 1), i - 1);
        long long ways2 = nCr((h - i) + (w - b - 1), h - i);
        long long term = (ways1 * ways2) % MOD;
        ans = (ans + term) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
