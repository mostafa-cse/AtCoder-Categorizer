# Centroid Invariant Distance Ratio for 2D Similarity Transformations

**Domain**: `Geometry`  
**Subtopic**: `Centroid Invariant`  

This workbook contains curated, high-quality competitive programming problems teaching **Centroid Invariant Distance Ratio for 2D Similarity Transformations**.

---

## Curated Problems

### `[problem:AtCoder-abc022_d]` — Big Bang
- **Rating / Difficulty**: 1857
- **Contest**: `abc022`
- **Analysis**: [`analysis/AtCoder-abc022_d.md`](../../analysis/AtCoder-abc022_d.md)
- **Key Idea**: Translation and rotation preserve distances from the centroid (center of mass). The scaling factor P scales the distance of every point from its respective centroid by exactly P. Thus, P = max_{i} dist(B_i, G_B) / max_{i} dist(A_i, G_A).
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Point {
    double x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> a(n), b(n);
    double sum_ax = 0, sum_ay = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i].x >> a[i].y;
        sum_ax += a[i].x;
        sum_ay += a[i].y;
    }

    double sum_bx = 0, sum_by = 0;
    for (int i = 0; i < n; ++i) {
        cin >> b[i].x >> b[i].y;
        sum_bx += b[i].x;
        sum_by += b[i].y;
    }

    Point ga = {sum_ax / n, sum_ay / n};
    Point gb = {sum_bx / n, sum_by / n};

    double max_da = 0;
    for (int i = 0; i < n; ++i) {
        max_da = max(max_da, hypot(a[i].x - ga.x, a[i].y - ga.y));
    }

    double max_db = 0;
    for (int i = 0; i < n; ++i) {
        max_db = max(max_db, hypot(b[i].x - gb.x, b[i].y - gb.y));
    }

    cout << fixed << setprecision(12) << max_db / max_da << "\n";
    return 0;
}
```
