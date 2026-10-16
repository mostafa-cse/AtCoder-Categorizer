# Expected Value DP with Self-Loop Formula + Range Sum Acceleration

**Domain**: `Dynamic Programming`  
**Subtopic**: `Expected Value DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Expected Value DP with Self-Loop Formula + Range Sum Acceleration**.

---

## Curated Problems

### `[problem:AtCoder-abc263_e]` — Sugoroku 3
- **Rating / Difficulty**: 1659
- **Contest**: `abc263`
- **Analysis**: [`analysis/AtCoder-abc263_e.md`](../../analysis/AtCoder-abc263_e.md)
- **Key Idea**: At square i, rolling 0 causes a self-loop: E[i] = 1 + (1 / (A_i + 1)) * E[i] + (1 / (A_i + 1)) * sum_{j=1}^{A_i} E[i + j]. Solve the self-loop algebraically.
- **Time Complexity**: `O(N log(MOD))`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

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

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 1; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> E(n + 2, 0);
    vector<long long> suf(n + 2, 0);

    for (int i = n - 1; i >= 1; --i) {
        int r = min((long long)n, i + a[i]);
        long long sum_future = (suf[i + 1] - suf[r + 1] + MOD) % MOD;
        long long num = (a[i] + 1 + sum_future) % MOD;
        E[i] = (num * modInverse(a[i])) % MOD;
        suf[i] = (suf[i + 1] + E[i]) % MOD;
    }

    cout << E[1] << "\n";
    return 0;
}
```
