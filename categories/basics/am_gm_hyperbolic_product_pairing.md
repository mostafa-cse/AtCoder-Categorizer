# AM-GM Hyperbolic Pairing for Strict Product Inequalities

**Domain**: `Basics`  
**Subtopic**: `AM-GM / Hyperbolic Bounding`  

This workbook contains curated, high-quality competitive programming problems teaching **AM-GM Hyperbolic Pairing for Strict Product Inequalities**.

---

## Curated Problems

### `[problem:AtCoder-arc094_b]` — Worst Case
- **Rating / Difficulty**: 1869
- **Contest**: `abc093`
- **Analysis**: [`analysis/AtCoder-arc094_b.md`](../../analysis/AtCoder-arc094_b.md)
- **Key Idea**: Let P = A * B. To maximize elements with x * y < P, pair scores around the square root C = floor(sqrt(P - 1)). By AM-GM, product x * y peaks when x approx y approx sqrt(P).
- **Time Complexity**: `O(1) per query`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <cmath>

using namespace std;

void solve() {
    long long a, b;
    cin >> a >> b;

    if (a == b) {
        cout << 2 * a - 2 << "\n";
        return;
    }

    long long P = a * b;
    long long c = sqrt(P - 1);
    while ((c + 1) * (c + 1) <= P - 1) c++;
    while (c * c > P - 1) c--;

    if (c * (c + 1) < P) {
        cout << 2 * c - 1 << "\n";
    } else {
        cout << 2 * c - 2 << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (cin >> q) {
        while (q--) solve();
    }
    return 0;
}
```
