# Periodic Round Invariant Modulo (X + Y) on Multi-Pile Pebble Game

**Domain**: `Game Theory`  
**Subtopic**: `Impartial Games`  

This workbook contains curated, high-quality competitive programming problems teaching **Periodic Round Invariant Modulo (X + Y) on Multi-Pile Pebble Game**.

---

## Curated Problems

### `[problem:AtCoder-arc143_c]` — Piles of Pebbles
- **Rating / Difficulty**: 1805
- **Contest**: `arc143`
- **Analysis**: [`analysis/AtCoder-arc143_c.md`](../../analysis/AtCoder-arc143_c.md)
- **Key Idea**: Whenever a pile has >= X + Y pebbles, any move of X by Takahashi can be countered by Aoki taking Y from the same pile, and vice versa. Thus, each pile size A_i can be reduced modulo (X + Y).
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
    long long x, y;
    if (!(cin >> n >> x >> y)) return 0;

    vector<long long> a(n);
    bool can_tak = false;
    bool can_aoki_only = false;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        long long r = a[i] % (x + y);
        if (r >= x) can_tak = true;
        if (r >= y && r < x) can_aoki_only = true;
    }

    if (x <= y) {
        if (can_tak) cout << "First\n";
        else cout << "Second\n";
    } else {
        if (can_tak && !can_aoki_only) cout << "First\n";
        else cout << "Second\n";
    }

    return 0;
}
```
