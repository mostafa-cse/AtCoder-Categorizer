# Sprague-Grundy Closed Form for Bounded-Move Nim: (X mod (L+R)) / L

**Domain**: `Game Theory`  
**Subtopic**: `Sprague-Grundy`  

This workbook contains curated, high-quality competitive programming problems teaching **Sprague-Grundy Closed Form for Bounded-Move Nim: (X mod (L+R)) / L**.

---

## Curated Problems

### `[problem:AtCoder-abc297_g]` — Constrained Nim 2
- **Rating / Difficulty**: 1834
- **Contest**: `abc297`
- **Analysis**: [`analysis/AtCoder-abc297_g.md`](../../analysis/AtCoder-abc297_g.md)
- **Key Idea**: The Sprague-Grundy theorem applies. For a single pile of size X with allowed moves in [L, R], the Grundy value satisfies a periodic step-function pattern: g(X) = floor((X % (L + R)) / L).
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long l, r;
    if (!(cin >> n >> l >> r)) return 0;

    long long xor_sum = 0;
    long long period = l + r;

    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        long long g = (a % period) / l;
        xor_sum ^= g;
    }

    if (xor_sum != 0) {
        cout << "First\n";
    } else {
        cout << "Second\n";
    }

    return 0;
}
```
