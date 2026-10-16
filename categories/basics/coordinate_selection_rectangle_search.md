# 2D Coordinate Selection O(N^4) Search for K Points

**Domain**: `Basics`  
**Subtopic**: `Exhaustive Search`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Coordinate Selection O(N^4) Search for K Points**.

---

## Curated Problems

### `[problem:AtCoder-abc075_d]` — Axis-Parallel Rectangle
- **Rating / Difficulty**: 1470
- **Contest**: `abc075`
- **Analysis**: [`analysis/AtCoder-abc075_d.md`](../../analysis/AtCoder-abc075_d.md)
- **Key Idea**: The optimal rectangle has its four sides aligned with the coordinates of some subset of the given points. Enumerate all pairs of x-coordinates and all pairs of y-coordinates.
- **Time Complexity**: `O(N^5) with small constant, runs in < 0.2s`
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

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> x(n), y(n);
    vector<long long> x_vals, y_vals;

    for (int i = 0; i < n; ++i) {
        cin >> x[i] >> y[i];
        x_vals.push_back(x[i]);
        y_vals.push_back(y[i]);
    }

    sort(x_vals.begin(), x_vals.end());
    sort(y_vals.begin(), y_vals.end());

    unsigned long long min_area = ~0ULL;

    for (int xi = 0; xi < n; ++xi) {
        for (int xj = xi + 1; xj < n; ++xj) {
            long long x1 = x_vals[xi];
            long long x2 = x_vals[xj];

            for (int yi = 0; yi < n; ++yi) {
                for (int yj = yi + 1; yj < n; ++yj) {
                    long long y1 = y_vals[yi];
                    long long y2 = y_vals[yj];

                    int count = 0;
                    for (int p = 0; p < n; ++p) {
                        if (x[p] >= x1 && x[p] <= x2 && y[p] >= y1 && y[p] <= y2) {
                            count++;
                        }
                    }

                    if (count >= k) {
                        unsigned long long area = (unsigned long long)(x2 - x1) * (y2 - y1);
                        if (area < min_area) {
                            min_area = area;
                        }
                    }
                }
            }
        }
    }

    cout << min_area << "\n";
    return 0;
}
```
