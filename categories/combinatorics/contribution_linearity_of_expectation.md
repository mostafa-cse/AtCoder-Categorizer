# Contribution to the Sum and Linearity of Expectation

**Domain**: `Combinatorics`  
**Subtopic**: `Counting Principles`  

This workbook contains curated, high-quality competitive programming problems teaching **Contribution to the Sum and Linearity of Expectation**.

---

## Curated Problems

### `[problem:AtCoder-arc114_c]` — Sequence Scores
- **Rating / Difficulty**: 2056
- **Contest**: `arc114`
- **Analysis**: [`analysis/AtCoder-arc114_c.md`](../../analysis/AtCoder-arc114_c.md)
- **Key Idea**: An element A_i = v requires a new operation unless there exists a prior j < i with A_j = v such that all intermediate elements A_k > v for k in (j, i). If such j exists, A_i can be merged into the operation that created A_j. Thus f(A) = N - (number of saved indices). By linearity of expectation, we sum the probability of saving over all pairs (j, i) with distance d = i - j: A_j = A_i = v has 1 choice, intermediate d-1 elements must be > v ((M - v) choices each), and the remaining N - 1 - d elements have M choices each.
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    long long total_all = (1LL * n % MOD) * power(m, n) % MOD;
    long long total_saved = 0;
    vector<long long> pow_t(m, 1);

    for (int d = 1; d <= n - 1; ++d) {
        long long sum_t = 0;
        for (int t = 0; t < m; ++t) {
            sum_t = (sum_t + pow_t[t]) % MOD;
            pow_t[t] = (pow_t[t] * t) % MOD;
        }
        long long ways = (1LL * (n - d) % MOD) * power(m, n - 1 - d) % MOD;
        ways = (ways * sum_t) % MOD;
        total_saved = (total_saved + ways) % MOD;
    }

    long long ans = (total_all - total_saved + MOD) % MOD;
    cout << ans << "\n";
    return 0;
}
```
