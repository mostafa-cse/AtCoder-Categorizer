# 2-adic Valuation & Odd Multiple LCM Condition

**Domain**: `Number Theory`  
**Subtopic**: `LCM & Divisibility`  

This workbook contains curated, high-quality competitive programming problems teaching **2-adic Valuation & Odd Multiple LCM Condition**.

---

## Curated Problems

### `[problem:AtCoder-abc150_d]` — Semi Common Multiple
- **Rating / Difficulty**: 1534
- **Contest**: `abc150`
- **Analysis**: [`analysis/AtCoder-abc150_d.md`](../../analysis/AtCoder-abc150_d.md)
- **Key Idea**: X = (A_i / 2) * (2p + 1). Thus, X must be an ODD multiple of each a'_i = A_i / 2. This requires all a'_i to have the exact same 2-adic valuation (power of 2).
- **Time Complexity**: `O(N log(max A))`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    int common_ctz = -1;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] /= 2;
        int c = __builtin_ctzll(a[i]);
        if (common_ctz == -1) common_ctz = c;
        else if (common_ctz != c) {
            cout << 0 << "\n";
            return 0;
        }
    }

    long long L = 1;
    for (int i = 0; i < n; ++i) {
        long long g = gcd(L, a[i]);
        __int128 next_L = (__int128)L * (a[i] / g);
        if (next_L > m) {
            cout << 0 << "\n";
            return 0;
        }
        L = next_L;
    }

    cout << (m / L + 1) / 2 << "\n";
    return 0;
}
```
