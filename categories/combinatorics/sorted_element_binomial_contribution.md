# Combinatorial Contribution of Sorted Elements (Binomial Sums)

**Domain**: `Combinatorics`  
**Subtopic**: `Contribution Technique`  

This workbook contains curated, high-quality competitive programming problems teaching **Combinatorial Contribution of Sorted Elements (Binomial Sums)**.

---

## Curated Problems

### [problem:AtCoder-abc151_e] — Max-Min Sums
- **Contest**: `abc151`
- **Rating / Difficulty**: 1344
- **Specific Skill**: Combinatorial Contribution of Sorted Elements (Binomial Sums)
- **Individual Analysis**: [`../../analysis/AtCoder-abc151_e.md`](../../analysis/AtCoder-abc151_e.md)
- **Problem Statement Summary**: Given array A of N integers. For each subset S of size K, compute max(S) - min(S). Find the sum of this value across all subsets modulo 10^9 + 7.
- **Core Insight**: Sort A in ascending order: A_0 <= A_1 <= ... <= A_{N-1}. Element A_i is the maximum of a size-K subset if and only if all other K - 1 elements are chosen from the i smaller elements: exactly C(i, K - 1) subsets! Similarly, A_i is the minimum of a size-K subset if all other K - 1 elements are chosen from the N - 1 - i larger elements: exactly C(N - 1 - i, K - 1) subsets. Total is sum A_i * (C(i, K - 1) - C(N - 1 - i, K - 1)).
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1e9 + 7;

long long power_mod(long long base, long long exp) {
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
    return power_mod(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    vector<long long> fact(n + 1, 1), inv_fact(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv_fact[n] = mod_inv(fact[n]);
    for (int i = n - 1; i >= 0; --i) {
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n_val, int r_val) -> long long {
        if (r_val < 0 || r_val > n_val) return 0;
        return fact[n_val] * inv_fact[r_val] % MOD * inv_fact[n_val - r_val] % MOD;
    };

    long long total_ans = 0;
    for (int i = 0; i < n; ++i) {
        long long c_max = nCr(i, k - 1);
        long long c_min = nCr(n - 1 - i, k - 1);
        long long coeff = (c_max - c_min + MOD) % MOD;
        total_ans = (total_ans + (a[i] % MOD + MOD) % MOD * coeff) % MOD;
    }

    cout << total_ans << "\n";
    return 0;
}
```
