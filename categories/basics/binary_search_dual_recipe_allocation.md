# Binary Search on Answer for Dual-Recipe Resource Allocation

**Domain**: `Basics`  
**Subtopic**: `Binary Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Answer for Dual-Recipe Resource Allocation**.

---

## Curated Problems

### `[problem:AtCoder-arc050_b]` — 花束
- **Rating / Difficulty**: 1838
- **Contest**: `arc050`
- **Analysis**: [`analysis/AtCoder-arc050_b.md`](../../analysis/AtCoder-arc050_b.md)
- **Key Idea**: Binary search on total bouquets K. If we make K bouquets, every bouquet needs at least 1 red and 1 blue (requiring R >= K and B >= K). The remaining R - K red flowers and B - K blue flowers can absorb extra requirements (x - 1 and y - 1).
- **Time Complexity**: `O(log(min(R, B)))`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long R, B, x, y;
    if (!(cin >> R >> B >> x >> y)) return 0;

    long long low = 0, high = min(R, B), ans = 0;

    while (low <= high) {
        long long K = low + (high - low) / 2;
        long long extra1 = (R - K) / (x - 1);
        long long extra2 = (B - K) / (y - 1);

        if (extra1 + extra2 >= K) {
            ans = K;
            low = K + 1;
        } else {
            high = K - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
