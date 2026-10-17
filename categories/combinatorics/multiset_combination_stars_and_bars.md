# Multiset Combination with Repetition: C(n + k - 1, k)

**Domain**: `Combinatorics`  
**Subtopic**: `Stars and Bars`  

This workbook contains curated, high-quality competitive programming problems teaching **Multiset Combination with Repetition: C(n + k - 1, k)**.

---

## Curated Problems

### `[problem:AtCoder-abc021_d]` — 多重ループ
- **Rating / Difficulty**: 1704
- **Contest**: `abc021`
- **Analysis**: [`analysis/AtCoder-abc021_d.md`](../../analysis/AtCoder-abc021_d.md)
- **Key Idea**: The number of non-decreasing sequences of length k with values from {1, ..., n} is equivalent to selecting k elements from n options with repetition (multiset combination), which is given by C(n + k - 1, k).
- **Time Complexity**: `O(n + k)`
- **Space Complexity**: `O(n + k)`
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

    int n, k;
    if (!(cin >> n >> k)) return 0;

    int max_val = n + k;
    vector<long long> fact(max_val + 1), inv(max_val + 1);
    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i <= max_val; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[max_val] = modInverse(fact[max_val]);
    for (int i = max_val - 1; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n_elem, int r_elem) -> long long {
        if (r_elem < 0 || r_elem > n_elem) return 0;
        return fact[n_elem] * inv[r_elem] % MOD * inv[n_elem - r_elem] % MOD;
    };

    cout << nCr(n + k - 1, k) << "\n";
    return 0;
}
```
