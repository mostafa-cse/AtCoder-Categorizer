# Substring Bounded Sequence Counting via Symbol Fusion and Slot Restriction

**Domain**: `Combinatorics`  
**Subtopic**: `Stars and Bars & Bounded Compositions`  

This workbook contains curated, high-quality competitive programming problems teaching **Substring Bounded Sequence Counting via Symbol Fusion and Slot Restriction**.

---

## Curated Problems

### `[problem:AtCoder-abc266_g]` — Yet Another RGB Sequence
- **Rating / Difficulty**: 2045
- **Contest**: `abc266`
- **Analysis**: [`analysis/AtCoder-abc266_g.md`](../../analysis/AtCoder-abc266_g.md)
- **Key Idea**: Fuse the K occurrences of 'RG' into a single new character 'X'. We now arrange: K copies of 'X', R - K copies of 'R', G - K copies of 'G', and B copies of 'B', with the restriction that NO remaining 'R' is immediately followed by a remaining 'G'. First, arrange the B 'B's, K 'X's, and R - K 'R's in (B + R)! / (B! * K! * (R - K)!) ways. Second, insert the G - K remaining 'G's into the available slots. Since a 'G' cannot immediately follow an 'R', the valid slots are: before the first element, and after any non-'R' element (i.e. after any 'B' or 'X'). There are exactly 1 + B + K valid slots. Placing G - K identical 'G's into 1 + B + K slots is given by Stars and Bars: C(G + B, G - K).
- **Time Complexity**: `O(R + G + B)`
- **Space Complexity**: `O(R + G + B)`
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

long long mod_inv(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, g, b, k;
    if (!(cin >> r >> g >> b >> k)) return 0;

    if (k > r || k > g) {
        cout << 0 << "\n";
        return 0;
    }

    int total_len = r + g + b + 5;
    vector<long long> fact(total_len), inv(total_len);
    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i < total_len; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[total_len - 1] = mod_inv(fact[total_len - 1]);
    for (int i = total_len - 2; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    // 1. Arrange B 'B's, K 'X's, and (R - K) 'R's:
    long long ways1 = fact[b + r] * inv[b] % MOD * inv[k] % MOD * inv[r - k] % MOD;

    // 2. Distribute (G - K) 'G's into (1 + B + K) available slots:
    // C((G - K) + (1 + B + K) - 1, G - K) = C(G + B, G - K)
    long long ways2 = nCr(g + b, g - k);

    long long ans = (ways1 * ways2) % MOD;
    cout << ans << "\n";

    return 0;
}
```
