# 45-Degree Grid Rotation Decomposing 2D Random Walk into Independent 1D Walks

**Domain**: `Math`  
**Subtopic**: `Coordinate Rotation`  

This workbook contains curated, high-quality competitive programming problems teaching **45-Degree Grid Rotation Decomposing 2D Random Walk into Independent 1D Walks**.

---

## Curated Problems

### `[problem:AtCoder-abc011_4]` — 大ジャンプ
- **Rating / Difficulty**: 1843
- **Contest**: `abc011`
- **Analysis**: [`analysis/AtCoder-abc011_4.md`](../../analysis/AtCoder-abc011_4.md)
- **Key Idea**: Scale coordinates by D: x = X / D, y = Y / D. Rotate coordinate axes by 45 degrees: u = x + y, v = x - y. Each cardinal jump (+1, 0), (-1, 0), (0, +1), (0, -1) becomes (+1, +1), (-1, -1), (+1, -1), (-1, +1), which decomposes into two completely INDEPENDENT 1D random walks of length N along u and v.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

using namespace std;

double prob_1d(int n, int target) {
    if ((n + target) % 2 != 0) return 0.0;
    int k = (n + target) / 2;
    if (k < 0 || k > n) return 0.0;

    // Compute C(n, k) * (1/2)^n via incremental multiplication
    double p = 1.0;
    for (int i = 1; i <= n; ++i) {
        p *= 0.5;
    }
    for (int i = 1; i <= k; ++i) {
        p = p * (n - i + 1) / i;
    }
    return p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long d, X, Y;
    if (!(cin >> n >> d >> X >> Y)) return 0;

    if (X % d != 0 || Y % d != 0) {
        cout << fixed << setprecision(12) << 0.0 << "\n";
        return 0;
    }

    long long x = X / d;
    long long y = Y / d;

    long long u = x + y;
    long long v = x - y;

    if (abs(u) > n || abs(v) > n) {
        cout << fixed << setprecision(12) << 0.0 << "\n";
        return 0;
    }

    double pu = prob_1d(n, u);
    double pv = prob_1d(n, v);

    cout << fixed << setprecision(12) << pu * pv << "\n";
    return 0;
}
```
