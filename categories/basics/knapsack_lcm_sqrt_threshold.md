# Square Root / LCM Dominance Threshold on 2-Denomination Unbounded Knapsack

**Domain**: `Basics`  
**Subtopic**: `Square Root / Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Square Root / LCM Dominance Threshold on 2-Denomination Unbounded Knapsack**.

---

## Curated Problems

### `[problem:AtCoder-arc139_b]` — Make N
- **Rating / Difficulty**: 1719
- **Contest**: `arc139`
- **Analysis**: [`analysis/AtCoder-arc139_b.md`](../../analysis/AtCoder-arc139_b.md)
- **Key Idea**: Assume without loss of generality that A is more cost-effective than B (Y/A <= Z/B). By LCM/Pigeonhole, taking A copies of B can always be replaced by B copies of A with less or equal cost, so we never need >= A copies of B.
- **Time Complexity**: `O(sqrt(N)) per test case`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

void solve() {
    long long n, a, b, x, y, z;
    cin >> n >> a >> b >> x >> y >> z;

    y = min(y, a * x);
    z = min(z, b * x);

    // Ensure package A has better or equal rate than package B
    if (y * b > z * a) {
        swap(a, b);
        swap(y, z);
    }

    long long min_cost = 4e18;

    if (a >= 30000) {
        for (long long k_a = 0; k_a * a <= n; ++k_a) {
            long long rem = n - k_a * a;
            long long k_b = rem / b;
            long long k_1 = rem % b;
            min_cost = min(min_cost, k_a * y + k_b * z + k_1 * x);
        }
    } else {
        long long max_kb = min(a - 1, n / b);
        for (long long k_b = 0; k_b <= max_kb; ++k_b) {
            long long rem = n - k_b * b;
            long long k_a = rem / a;
            long long k_1 = rem % a;
            min_cost = min(min_cost, k_a * y + k_b * z + k_1 * x);
        }
    }

    cout << min_cost << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```
