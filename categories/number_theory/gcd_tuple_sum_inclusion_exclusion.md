# Inclusion-Exclusion Multiple Counting from K down to 1

**Domain**: `Number Theory`  
**Subtopic**: `Inclusion-Exclusion`  

This workbook contains curated, high-quality competitive programming problems teaching **Inclusion-Exclusion Multiple Counting from K down to 1**.

---

## Curated Problems

### `[problem:AtCoder-abc162_e]` — Sum of gcd of Tuples
- **Rating / Difficulty**: 1662
- **Contest**: `abc162`
- **Analysis**: [`analysis/AtCoder-abc162_e.md`](../../analysis/AtCoder-abc162_e.md)
- **Key Idea**: Count sequences with gcd EXACTLY equal to g. The number of sequences where each element is a multiple of g is floor(K / g)^N. Subtract counts for multiples 2g, 3g, ... by processing g from K down to 1.
- **Time Complexity**: `O(K log K)`
- **Space Complexity**: `O(K)`
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> cnt(k + 1, 0);
    long long ans = 0;

    for (int g = k; g >= 1; --g) {
        long long ways = power(k / g, n);
        for (int m = 2 * g; m <= k; m += g) {
            ways = (ways - cnt[m] + MOD) % MOD;
        }
        cnt[g] = ways;
        ans = (ans + 1LL * g * cnt[g]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
