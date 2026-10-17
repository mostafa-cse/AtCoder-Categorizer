# Cellular Automaton Modulo 3 Linearity via Pascal & Lucas' Theorem

**Domain**: `Math`  
**Subtopic**: `Lucas Theorem`  

This workbook contains curated, high-quality competitive programming problems teaching **Cellular Automaton Modulo 3 Linearity via Pascal & Lucas' Theorem**.

---

## Curated Problems

### `[problem:AtCoder-arc117_c]` — Tricolor Pyramid
- **Rating / Difficulty**: 1768
- **Contest**: `arc117`
- **Analysis**: [`analysis/AtCoder-arc117_c.md`](../../analysis/AtCoder-arc117_c.md)
- **Key Idea**: The transition function for colors x and y in Z_3 is f(x, y) = -(x + y) mod 3. Propagating this linear relation up N - 1 levels gives the apex color: (-1)^{N - 1} * sum_{i=0}^{N - 1} C(N - 1, i) * c_i mod 3.
- **Time Complexity**: `O(N log_3 N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int comb_small(int n, int r) {
    if (r < 0 || r > n) return 0;
    if (r == 0 || r == n) return 1;
    return n; // n=2, r=1 -> 2
}

int lucas(int n, int r) {
    int res = 1;
    while (n > 0 || r > 0) {
        int ni = n % 3;
        int ri = r % 3;
        if (ri > ni) return 0;
        res = (res * comb_small(ni, ri)) % 3;
        n /= 3;
        r /= 3;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    string s;
    cin >> s;

    auto char_to_val = [](char c) -> int {
        if (c == 'B') return 0;
        if (c == 'W') return 1;
        return 2; // 'R'
    };

    auto val_to_char = [](int v) -> char {
        if (v == 0) return 'B';
        if (v == 1) return 'W';
        return 'R';
    };

    long long sum_val = 0;
    for (int i = 0; i < n; ++i) {
        int coeff = lucas(n - 1, i);
        sum_val += coeff * char_to_val(s[i]);
    }

    sum_val %= 3;

    if ((n - 1) % 2 == 1) {
        sum_val = (3 - sum_val) % 3;
    }

    cout << val_to_char(sum_val) << "\n";
    return 0;
}
```
