# Stars and Bars Empty Boxes Combinatorics

**Domain**: `Combinatorics`  
**Subtopic**: `Stars and Bars`  

This workbook contains curated, high-quality competitive programming problems teaching **Stars and Bars Empty Boxes Combinatorics**.

---

## Curated Problems

### `[problem:AtCoder-abc156_e]` — Roaming
- **Rating / Difficulty**: 1514
- **Contest**: `abc156`
- **Analysis**: [`analysis/AtCoder-abc156_e.md`](../../analysis/AtCoder-abc156_e.md)
- **Key Idea**: Each move can create at most one empty room. Thus, after at most K moves, the number of empty rooms z satisfies 0 <= z <= min(N - 1, K).
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;
const int MAX = 400005;

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
    long long k;
    if (!(cin >> n >> k)) return 0;

    long long max_z = min((long long)n - 1, k);
    long long ans = 0;

    for (int z = 0; z <= max_z; ++z) {
        long long ways = nCr(n, z) * nCr(n - 1, n - z - 1) % MOD;
        ans = (ans + ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
