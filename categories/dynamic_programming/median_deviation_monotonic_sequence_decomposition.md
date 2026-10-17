# Slope Trick

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `More Tricks`  

This workbook contains curated, high-quality competitive programming problems teaching **Slope Trick**.

---

## Curated Problems

### `[problem:AtCoder-arc123_d]` — Inc, Dec - Decomposition
- **Rating / Difficulty**: 2143
- **Contest**: `arc123`
- **Analysis**: [`analysis/AtCoder-arc123_d.md`](../../analysis/AtCoder-arc123_d.md)
- **Key Idea**: The monotonicity constraints B_i - B_{i-1} >= 0 and C_{i-1} - C_i >= 0 imply B_i - B_{i-1} >= max(0, A_i - A_{i-1}). To minimize total absolute values, the optimal step increments are exactly B_i - B_{i-1} = max(0, A_i - A_{i-1}). Expressing B_i = x + P_i and C_i = A_i - P_i - x for prefix increments P_i, the objective becomes sum (|x + P_i| + |x - (A_i - P_i)|). This is the sum of L1 distances from x to 2N fixed points, which is minimized when x is the median of the 2N points.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> p(n, 0);
    for (int i = 1; i <= n - 1; ++i) {
        p[i] = p[i - 1] + max(0LL, a[i] - a[i - 1]);
    }

    vector<long long> z;
    for (int i = 0; i < n; ++i) {
        z.push_back(-p[i]);
        z.push_back(a[i] - p[i]);
    }

    sort(z.begin(), z.end());
    long long median = z[n];

    long long ans = 0;
    for (long long pt : z) {
        ans += abs(median - pt);
    }

    cout << ans << "\n";
    return 0;
}
```
