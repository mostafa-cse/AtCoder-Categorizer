# Binary Search on Answer / Splash Damage Allocation

**Domain**: `Basics`  
**Subtopic**: `Binary Search on Answer`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Answer / Splash Damage Allocation**.

---

## Curated Problems

### `[problem:AtCoder-arc075_b]` — Widespread
- **Rating / Difficulty**: 1544
- **Contest**: `abc063`
- **Analysis**: [`analysis/AtCoder-arc075_b.md`](../../analysis/AtCoder-arc075_b.md)
- **Key Idea**: Binary search on the total explosions K. In K explosions, every monster automatically receives K * B splash damage. Additional center blasts on monster i add A - B damage each.
- **Time Complexity**: `O(N log(max H))`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long a, b;
    if (!(cin >> n >> a >> b)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) {
        cin >> h[i];
    }

    long long diff = a - b;
    long long low = 1, high = 1e9;
    long long ans = high;

    auto check = [&](long long k) -> bool {
        long long centers = 0;
        for (int i = 0; i < n; ++i) {
            long long rem = h[i] - k * b;
            if (rem > 0) {
                centers += (rem + diff - 1) / diff;
                if (centers > k) return false;
            }
        }
        return centers <= k;
    };

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
