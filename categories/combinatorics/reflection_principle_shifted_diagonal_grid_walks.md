# Reflection Principle for Shifted Diagonal Grid Walks

**Domain**: `Combinatorics`  
**Subtopic**: `Catalan Numbers & Grid Walks`  

This workbook contains curated, high-quality competitive programming problems teaching **Reflection Principle for Shifted Diagonal Grid Walks**.

---

## Curated Problems

### `[problem:AtCoder-abc205_e]` — White and Black Balls
- **Rating / Difficulty**: 2025
- **Contest**: `abc205`
- **Analysis**: [`analysis/AtCoder-abc205_e.md`](../../analysis/AtCoder-abc205_e.md)
- **Key Idea**: Interpret as a grid walk from (0, 0) to (N, M) with right-steps (+1 white) and up-steps (+1 black). The condition requires x <= y + K, which means the path must never touch the forbidden line y = x - (K + 1). If N > M + K, the destination (N, M) itself violates the condition, so 0. Otherwise, by Andre's Reflection Principle, any path touching y = x - (K + 1) can be reflected across this line to a path starting at (0, 0) and ending at the reflected destination (M + K + 1, N - K - 1). Thus the invalid paths equal C(N + M, M + K + 1), giving total valid paths C(N + M, N) - C(N + M, M + K + 1).
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

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

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    if (n > m + k) {
        cout << 0 << "\n";
        return 0;
    }

    int max_val = n + m + 5;
    vector<long long> fact(max_val), inv(max_val);
    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i < max_val; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[max_val - 1] = mod_inv(fact[max_val - 1]);
    for (int i = max_val - 2; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    long long total = nCr(n + m, n);
    long long invalid = nCr(n + m, m + k + 1);

    long long ans = (total - invalid + MOD) % MOD;
    cout << ans << "\n";

    return 0;
}
```
