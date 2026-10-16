# Composition of Clamping Intervals [L, R] with Linear Shift

**Domain**: `Math`  
**Subtopic**: `Linear Algebra`  

This workbook contains curated, high-quality competitive programming problems teaching **Composition of Clamping Intervals [L, R] with Linear Shift**.

---

## Curated Problems

### `[problem:AtCoder-abc196_e]` — Filters
- **Rating / Difficulty**: 1650
- **Contest**: `abc196`
- **Analysis**: [`analysis/AtCoder-abc196_e.md`](../../analysis/AtCoder-abc196_e.md)
- **Key Idea**: The composition of addition, max, and min operations is always a piecewise linear function characterized by a single horizontal shift and clamping bounds: f(x) = min(high, max(low, x + add)).
- **Time Complexity**: `O(N + Q)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long add = 0;
    long long low = -INF;
    long long high = INF;

    for (int i = 0; i < n; ++i) {
        long long a;
        int t;
        cin >> a >> t;

        if (t == 1) {
            add += a;
            low += a;
            high += a;
        } else if (t == 2) {
            low = max(low, a);
            high = max(high, a);
        } else if (t == 3) {
            high = min(high, a);
            low = min(low, a);
        }
    }

    int q;
    cin >> q;
    while (q--) {
        long long x;
        cin >> x;
        long long res = min(high, max(low, x + add));
        cout << res << "\n";
    }

    return 0;
}
```
