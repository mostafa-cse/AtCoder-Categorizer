# Binary Search on Average / Dinkelbach Fractional Programming

**Domain**: `Basics`  
**Subtopic**: `Binary Search on Answer`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Average / Dinkelbach Fractional Programming**.

---

## Curated Problems

### `[problem:AtCoder-abc034_d]` — Salt Water
- **Rating / Difficulty**: 1549
- **Contest**: `abc034`
- **Analysis**: [`analysis/AtCoder-abc034_d.md`](../../analysis/AtCoder-abc034_d.md)
- **Key Idea**: Binary search on target concentration X. A mixture has concentration >= X iff sum_{chosen} w_i * (p_i - X) >= 0.
- **Time Complexity**: `O(N log N * 100)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> w(n);
    vector<double> p(n);

    for (int i = 0; i < n; ++i) {
        cin >> w[i] >> p[i];
    }

    double low = 0.0, high = 100.0;
    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) / 2.0;

        vector<double> gain(n);
        for (int i = 0; i < n; ++i) {
            gain[i] = w[i] * (p[i] - mid);
        }

        sort(gain.rbegin(), gain.rend());

        double top_k_sum = 0;
        for (int i = 0; i < k; ++i) {
            top_k_sum += gain[i];
        }

        if (top_k_sum >= 0) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(12) << low << "\n";
    return 0;
}
```
