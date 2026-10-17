# Permutation Cycle Decomposition and Multinomial Mismatch Counting

**Domain**: `Combinatorics`  
**Subtopic**: `Counting Principles`  

This workbook contains curated, high-quality competitive programming problems teaching **Permutation Cycle Decomposition and Multinomial Mismatch Counting**.

---

## Curated Problems

### `[problem:AtCoder-arc168_c]` — Swap Characters
- **Rating / Difficulty**: 2071
- **Contest**: `arc168`
- **Analysis**: [`analysis/AtCoder-arc168_c.md`](../../analysis/AtCoder-arc168_c.md)
- **Key Idea**: Any reachable string T has the same character frequencies as S. The mismatch positions decompose into 2-cycles (A<->B, B<->C, C<->A, taking 1 swap each) and 3-cycles (A->B->C->A and A->C->B->A, taking 2 swaps each). A minimal swap sequence never contains both 3-cycle directions (min(c1, c2) = 0). Iterating over all valid tuples (c1, c2, c_AB, c_BC, c_CA) with swaps <= K uniquely determines the mismatch counts between all character pairs. The number of strings with a given mismatch matrix is computed via multinomial coefficients.
- **Time Complexity**: `O(N + K^4)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

long long fact[250005], invFact[250005];

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

void precompute(int n) {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[n] = modInverse(fact[n]);
    for (int i = n - 1; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long multinomial(int n, int a, int b) {
    if (a < 0 || b < 0 || a + b > n) return 0;
    int c = n - a - b;
    long long res = fact[n];
    res = (res * invFact[a]) % MOD;
    res = (res * invFact[b]) % MOD;
    res = (res * invFact[c]) % MOD;
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    string s;
    cin >> s;

    precompute(n);

    int ca = 0, cb = 0, cc = 0;
    for (char ch : s) {
        if (ch == 'A') ca++;
        else if (ch == 'B') cb++;
        else cc++;
    }

    long long ans = 0;

    for (int c1 = 0; 2 * c1 <= k; ++c1) {
        for (int c2 = 0; 2 * c2 <= k; ++c2) {
            if (c1 > 0 && c2 > 0) continue;
            int rem_k = k - 2 * (c1 + c2);
            for (int cab = 0; cab <= rem_k; ++cab) {
                for (int cbc = 0; cab + cbc <= rem_k; ++cbc) {
                    for (int cca = 0; cab + cbc + cca <= rem_k; ++cca) {
                        int a_to_b = cab + c1;
                        int a_to_c = cca + c2;
                        int b_to_a = cab + c2;
                        int b_to_c = cbc + c1;
                        int c_to_a = cca + c1;
                        int c_to_b = cbc + c2;

                        if (a_to_b + a_to_c > ca) continue;
                        if (b_to_a + b_to_c > cb) continue;
                        if (c_to_a + c_to_b > cc) continue;

                        long long ways = multinomial(ca, a_to_b, a_to_c);
                        ways = (ways * multinomial(cb, b_to_a, b_to_c)) % MOD;
                        ways = (ways * multinomial(cc, c_to_a, c_to_b)) % MOD;

                        ans = (ans * ways) % MOD;
                    }
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```
