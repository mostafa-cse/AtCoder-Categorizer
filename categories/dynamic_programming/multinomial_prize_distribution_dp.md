# Knapsack and Basic Dynamic Programming

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Knapsack and Basic Dynamic Programming**.

---

## Curated Problems

### `[problem:AtCoder-abc243_f]` — Lottery
- **Rating / Difficulty**: 2125
- **Contest**: `abc243`
- **Analysis**: [`analysis/AtCoder-abc243_f.md`](../../analysis/AtCoder-abc243_f.md)
- **Key Idea**: The probability of drawing prize i exactly c_i times is K! * prod_{i=1}^N (p_i^{c_i} / c_i!). To count states with exactly M non-zero counts c_i and sum c_i = K, we define dp[cnt][drawn] = sum of prod (p_i^{c_i} / c_i!) using cnt distinct prizes and drawn total draws. At prize i, we either skip it (c = 0), or pick c in [1, K - drawn] items, multiplying by p_i^c / c!. Finally, multiply dp[M][K] by K!.
- **Time Complexity**: `O(N * M * K^2)`
- **Space Complexity**: `O(M * K)`
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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> w(n);
    long long sum_w = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i];
        sum_w = (sum_w + w[i]) % MOD;
    }

    long long inv_sum = modInverse(sum_w);
    vector<long long> p(n);
    for (int i = 0; i < n; ++i) {
        p[i] = (w[i] * inv_sum) % MOD;
    }

    vector<long long> fact(k + 1, 1), invFact(k + 1, 1);
    for (int i = 1; i <= k; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[k] = modInverse(fact[k]);
    for (int i = k - 1; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;

    vector<vector<long long>> dp(m + 1, vector<long long>(k + 1, 0));
    dp[0][0] = 1;

    for (int i = 0; i < n; ++i) {
        vector<vector<long long>> next_dp = dp;
        for (int cnt = 0; cnt < m; ++cnt) {
            for (int drawn = 0; drawn < k; ++drawn) {
                if (!dp[cnt][drawn]) continue;

                long long p_pow = p[i];
                for (int c = 1; drawn + c <= k; ++c) {
                    long long term = (p_pow * invFact[c]) % MOD;
                    next_dp[cnt + 1][drawn + c] = (next_dp[cnt + 1][drawn + c] + dp[cnt][drawn] * term) % MOD;
                    p_pow = (p_pow * p[i]) % MOD;
                }
            }
        }
        dp = next_dp;
    }

    long long ans = (dp[m][k] * fact[k]) % MOD;
    cout << ans << "\n";
    return 0;
}
```
