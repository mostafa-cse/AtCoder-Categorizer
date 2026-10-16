# Principle of Inclusion-Exclusion (PIE) on Keyboard Key Sets

**Domain**: `Combinatorics`  
**Subtopic**: `Inclusion-Exclusion`  

This workbook contains curated, high-quality competitive programming problems teaching **Principle of Inclusion-Exclusion (PIE) on Keyboard Key Sets**.

---

## Curated Problems

### `[problem:AtCoder-abc246_f]` — typewriter
- **Rating / Difficulty**: 1677
- **Contest**: `abc246`
- **Analysis**: [`analysis/AtCoder-abc246_f.md`](../../analysis/AtCoder-abc246_f.md)
- **Key Idea**: Principle of Inclusion-Exclusion (PIE) over the N rows of keys! A string is typeable using row i if all its letters belong to S_i (which gives |S_i|^L strings).
- **Time Complexity**: `O(2^N * N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

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

    int n;
    long long L;
    if (!(cin >> n >> L)) return 0;

    vector<int> row_mask(n, 0);
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        for (char c : s) {
            row_mask[i] |= (1 << (c - 'a'));
        }
    }

    int total_masks = 1 << n;
    long long ans = 0;

    for (int mask = 1; mask < total_masks; ++mask) {
        int common_keys = (1 << 26) - 1;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                common_keys &= row_mask[i];
            }
        }
        int cnt = __builtin_popcount(common_keys);
        long long ways = power(cnt, L);

        if (__builtin_popcount(mask) % 2 == 1) {
            ans = (ans + ways) % MOD;
        } else {
            ans = (ans - ways + MOD) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
