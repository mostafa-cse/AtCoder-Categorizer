# Large Grid Path Combinations via Modular Inverse Factorials

**Domain**: `Combinatorics`  
**Subtopic**: `Classic Combinatorics`  

This workbook contains curated, high-quality competitive programming problems teaching **Large Grid Path Combinations via Modular Inverse Factorials**.

---

## Curated Problems

### `[problem:AtCoder-abc034_c]` — Grid Paths
- **Rating / Difficulty**: 1440
- **Contest**: `abc034`
- **Analysis**: [`analysis/AtCoder-abc034_c.md`](../../analysis/AtCoder-abc034_c.md)
- **Key Idea**: The total number of right moves is W - 1 and down moves is H - 1. Total moves = (W - 1) + (H - 1). The answer is C(W + H - 2, W - 1) mod (10^9 + 7).
- **Time Complexity**: `O(W + H)`
- **Space Complexity**: `O(W + H)`
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
    for (int i = 1; i < MAX; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAX - 1] = modInverse(fact[MAX - 1]);
    for (int i = MAX - 2; i >= 1; --i) {
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

    int w, h;
    if (!(cin >> w >> h)) return 0;

    cout << nCr(w + h - 2, w - 1) << "\n";
    return 0;
}
```
