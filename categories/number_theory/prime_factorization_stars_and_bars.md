# Prime Factorization Combinatorics / Stars and Bars

**Domain**: `Number Theory`  
**Subtopic**: `Prime Factorization`  

This workbook contains curated, high-quality competitive programming problems teaching **Prime Factorization Combinatorics / Stars and Bars**.

---

## Curated Problems

### `[problem:AtCoder-arc116_c]` — Multiple Sequences
- **Rating / Difficulty**: 1468
- **Contest**: `arc116`
- **Analysis**: [`analysis/AtCoder-arc116_c.md`](../../analysis/AtCoder-arc116_c.md)
- **Key Idea**: Iterate over the last element x = A_N (1 <= x <= M). For each prime factor p^e dividing x, the e prime factors must be distributed across the N positions in the sequence, which is independent for each prime.
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;
const int MAX = 300005;

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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    // Sieve for SPF
    vector<int> spf(m + 1);
    for (int i = 1; i <= m; ++i) spf[i] = i;
    for (int i = 2; i * i <= m; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= m; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }

    long long total_ans = 0;
    for (int x = 1; x <= m; ++x) {
        int temp = x;
        long long ways = 1;
        while (temp > 1) {
            int p = spf[temp];
            int e = 0;
            while (temp % p == 0) {
                e++;
                temp /= p;
            }
            ways = (ways * nCr(e + n - 1, n - 1)) % MOD;
        }
        total_ans = (total_ans + ways) % MOD;
    }

    cout << total_ans << "\n";
    return 0;
}
```
