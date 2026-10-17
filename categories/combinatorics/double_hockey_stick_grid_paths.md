# Double Hockey-Stick Identity on Grid Path Combinations

**Domain**: `Combinatorics`  
**Subtopic**: `Hockey-Stick Identity`  

This workbook contains curated, high-quality competitive programming problems teaching **Double Hockey-Stick Identity on Grid Path Combinations**.

---

## Curated Problems

### `[problem:AtCoder-abc154_f]` — Many Many Paths
- **Rating / Difficulty**: 1775
- **Contest**: `abc154`
- **Analysis**: [`analysis/AtCoder-abc154_f.md`](../../analysis/AtCoder-abc154_f.md)
- **Key Idea**: By the Hockey-Stick Identity, sum_{c=0}^C C(r + c, c) = C(r + C + 1, C). Summing over r gives sum_{r=0}^R C(r + C + 1, r) = C(R + C + 2, R) - 1. Thus, F(R, C) = sum_{r=0}^R sum_{c=0}^C C(r + c, r) = C(R + C + 2, R + 1) - 1.
- **Time Complexity**: `O(max(R, C))`
- **Space Complexity**: `O(max(R, C))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;
const int MAX_VAL = 2000005;

long long fact[MAX_VAL], inv[MAX_VAL];

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

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
}

long long F(int r, int c) {
    if (r < 0 || c < 0) return 0;
    return (nCr(r + c + 2, r + 1) - 1 + MOD) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i < MAX_VAL; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[MAX_VAL - 1] = power(fact[MAX_VAL - 1], MOD - 2);
    for (int i = MAX_VAL - 2; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    int r1, c1, r2, c2;
    if (!(cin >> r1 >> c1 >> r2 >> c2)) return 0;

    long long ans = (F(r2, c2) - F(r1 - 1, c2) - F(r2, c1 - 1) + F(r1 - 1, c1 - 1)) % MOD;
    ans = (ans + MOD) % MOD;

    cout << ans << "\n";
    return 0;
}
```
