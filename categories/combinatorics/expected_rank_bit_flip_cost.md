# Expected Permutation Rank / Contribution to Sum on Bit-Flip Costs

**Domain**: `Combinatorics`  
**Subtopic**: `Linearity of Expectation`  

This workbook contains curated, high-quality competitive programming problems teaching **Expected Permutation Rank / Contribution to Sum on Bit-Flip Costs**.

---

## Curated Problems

### `[problem:AtCoder-abc150_e]` — Change a Little Bit
- **Rating / Difficulty**: 1851
- **Contest**: `abc150`
- **Analysis**: [`analysis/AtCoder-abc150_e.md`](../../analysis/AtCoder-abc150_e.md)
- **Key Idea**: Sort C descending: C_1 >= C_2 >= ... >= C_N. In any pair (S, T), bit i differs with probability 1/2. When bit i differs, the expected number of elements among C_1..C_{i-1} that also differ is (i - 1) / 2. By linearity of expectation and symmetry, the total contribution of C_i over all 4^N pairs simplifies to C_i * 2^{2N - 2} * (i + 2) mod (10^9 + 7).
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> c(n);
    for (int i = 0; i < n; ++i) cin >> c[i];

    sort(c.rbegin(), c.rend());

    long long base_ways = power(2, 2LL * n - 2);
    long long ans = 0;

    for (int i = 1; i <= n; ++i) {
        long long term = c[i - 1] % MOD * base_ways % MOD * (i + 2) % MOD;
        ans = (ans + term) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
