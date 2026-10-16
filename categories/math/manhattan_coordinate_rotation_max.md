# 45-degree Coordinate Rotation for Manhattan Maxima

**Domain**: `Math`  
**Subtopic**: `Manhattan & Chebyshev`  

This workbook contains curated, high-quality competitive programming problems teaching **45-degree Coordinate Rotation for Manhattan Maxima**.

---

## Curated Problems

### [problem:AtCoder-abc178_e] — Dist Max
- **Contest**: `abc178`
- **Rating / Difficulty**: 1054
- **Specific Skill**: 45-degree Coordinate Rotation for Manhattan Maxima
- **Individual Analysis**: [`../../analysis/AtCoder-abc178_e.md`](../../analysis/AtCoder-abc178_e.md)
- **Problem Statement Summary**: Given N points (x_i, y_i) in 2D plane (N <= 2 * 10^5). Find the maximum Manhattan distance |x_i - x_j| + |y_i - y_j| over all pairs.
- **Core Insight**: Let u_i = x_i + y_i and v_i = x_i - y_i. Then Manhattan distance between point i and point j is max(|u_i - u_j|, |v_i - v_j|). The maximum distance over all pairs is max(max(u) - min(u), max(v) - min(v)), computable in a single pass O(N)!
- **Complexity**: Time: `O(N)` | Space: `O(N)`
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
    if (!(cin >> n)) return 0;

    long long max_u = -4e18, min_u = 4e18;
    long long max_v = -4e18, min_v = 4e18;

    for (int i = 0; i < n; ++i) {
        long long x, y;
        cin >> x >> y;
        long long u = x + y;
        long long v = x - y;
        max_u = max(max_u, u);
        min_u = min(min_u, u);
        max_v = max(max_v, v);
        min_v = min(min_v, v);
    }

    cout << max(max_u - min_u, max_v - min_v) << "\n";
    return 0;
}
```
