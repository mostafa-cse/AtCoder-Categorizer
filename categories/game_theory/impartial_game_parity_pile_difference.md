# Impartial Game Parity / Modular Difference Invariant (|X - Y| <= 1)

**Domain**: `Game Theory`  
**Subtopic**: `Impartial Games`  

This workbook contains curated, high-quality competitive programming problems teaching **Impartial Game Parity / Modular Difference Invariant (|X - Y| <= 1)**.

---

## Curated Problems

### `[problem:AtCoder-arc072_b]` — Alice&Brown
- **Rating / Difficulty**: 1749
- **Contest**: `abc059`
- **Analysis**: [`analysis/AtCoder-arc072_b.md`](../../analysis/AtCoder-arc072_b.md)
- **Key Idea**: The difference between piles |X - Y| determines the game. Any state with |X - Y| <= 1 is a P-position (losing state). Any state with |X - Y| >= 2 is an N-position (winning state).
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x, y;
    if (!(cin >> x >> y)) return 0;

    if (abs(x - y) <= 1) {
        cout << "Brown\n";
    } else {
        cout << "Alice\n";
    }

    return 0;
}
```
