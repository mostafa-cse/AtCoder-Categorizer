# Coprime / Divisor Multiple Counting with Extreme Quotient Exclusions

**Domain**: `Number Theory`  
**Subtopic**: `Inclusion-Exclusion`  

This workbook contains curated, high-quality competitive programming problems teaching **Coprime / Divisor Multiple Counting with Extreme Quotient Exclusions**.

---

## Curated Problems

### `[problem:AtCoder-abc206_e]` — Divide Both
- **Rating / Difficulty**: 1745
- **Contest**: `abc206`
- **Analysis**: [`analysis/AtCoder-abc206_e.md`](../../analysis/AtCoder-abc206_e.md)
- **Key Idea**: Count pairs with gcd(x, y) = g > 1 using backward multiple counting from R down to 2. The condition x / g > 1 means x cannot be equal to g itself. If g >= L, we must subtract pairs where x = g.
- **Time Complexity**: `O(R log R)`
- **Space Complexity**: `O(R)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    vector<long long> f(R + 1, 0);
    long long ans = 0;

    for (long long g = R; g >= 2; --g) {
        long long m = (R / g) - ((L - 1) / g);
        long long pairs = m * (m - 1) / 2;

        for (long long k = 2 * g; k <= R; k += g) {
            pairs -= f[k];
        }
        f[g] = pairs;

        long long invalid = 0;
        if (g >= L) {
            invalid = m - 1; // pairs where x = g and y = k*g (k >= 2)
        }
        ans += (f[g] - invalid);
    }

    cout << ans * 2 << "\n";
    return 0;
}
```
