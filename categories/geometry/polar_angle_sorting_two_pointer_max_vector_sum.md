# Polar Angle Sorting and Two-Pointer Sliding Window for Maximum Vector Subset Sum

**Domain**: `Geometry`  
**Subtopic**: `Angular Sweep & Polar Sorting`  

This workbook contains curated, high-quality competitive programming problems teaching **Polar Angle Sorting and Two-Pointer Sliding Window for Maximum Vector Subset Sum**.

---

## Curated Problems

### `[problem:AtCoder-abc139_f]` — Engines
- **Rating / Difficulty**: 2034
- **Contest**: `abc139`
- **Analysis**: [`analysis/AtCoder-abc139_f.md`](../../analysis/AtCoder-abc139_f.md)
- **Key Idea**: If the optimal sum vector points in direction theta, any vector v contributing positively to the dot product v * S must satisfy v * S > 0, meaning it lies in the open half-plane centered at angle theta. Thus, the optimal subset of vectors always forms a contiguous angular interval of span < pi. By sorting all vectors by polar angle theta = atan2(y, x), duplicating the array cyclically, and using a two-pointer sliding window of angular width <= pi, the maximum vector sum is found in O(N log N).
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

const double PI = acos(-1.0);

struct Vec {
    double x, y;
    double ang;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Vec> vecs;
    for (int i = 0; i < n; ++i) {
        double x, y;
        cin >> x >> y;
        if (x != 0 || y != 0) {
            vecs.push_back({x, y, atan2(y, x)});
        }
    }

    if (vecs.empty()) {
        cout << fixed << setprecision(15) << 0.0 << "\n";
        return 0;
    }

    sort(vecs.begin(), vecs.end(), [](const Vec& a, const Vec& b) {
        return a.ang < b.ang;
    });

    int m = vecs.size();
    for (int i = 0; i < m; ++i) {
        vecs.push_back({vecs[i].x, vecs[i].y, vecs[i].ang + 2.0 * PI});
    }

    double max_norm = 0.0;

    // Two pointers over range [0, 2m - 1]
    int r = 0;
    double cur_x = 0.0, cur_y = 0.0;

    for (int l = 0; l < m; ++l) {
        while (r < l + m && vecs[r].ang - vecs[l].ang < PI - 1e-9) {
            cur_x += vecs[r].x;
            cur_y += vecs[r].y;
            max_norm = max(max_norm, hypot(cur_x, cur_y));
            r++;
        }
        max_norm = max(max_norm, hypot(cur_x, cur_y));
        cur_x -= vecs[l].x;
        cur_y -= vecs[l].y;
    }

    cout << fixed << setprecision(15) << max_norm << "\n";
    return 0;
}
```
