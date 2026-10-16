# 2D Point Rotation around Center via Complex Numbers

**Domain**: `Geometry`  
**Subtopic**: `Rotations & Complex Plane`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Point Rotation around Center via Complex Numbers**.

---

## Curated Problems

### [problem:AtCoder-abc197_d] — Opposite
- **Contest**: `abc197`
- **Rating / Difficulty**: 831
- **Specific Skill**: 2D Point Rotation around Center via Complex Numbers
- **Individual Analysis**: [`../../analysis/AtCoder-abc197_d.md`](../../analysis/AtCoder-abc197_d.md)
- **Problem Statement Summary**: In a regular N-gon (N is even), vertex 0 has coordinates (x_0, y_0) and opposite vertex N/2 has coordinates (x_{N/2}, y_{N/2}). Find the coordinates of vertex 1: (x_1, y_1).
- **Core Insight**: Using complex numbers: z_1 = z_M + (z_0 - z_M) * e^(i * theta). This eliminates trigonometry casework and provides clean, numerically stable coordinate calculation.
- **Complexity**: Time: `O(1)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    double x0, y0, xh, yh;
    if (!(cin >> n >> x0 >> y0 >> xh >> yh)) return 0;

    double cx = (x0 + xh) / 2.0;
    double cy = (y0 + yh) / 2.0;

    double pi = acos(-1.0);
    double theta = 2.0 * pi / n;

    double vx = x0 - cx;
    double vy = y0 - cy;

    double rx = vx * cos(theta) - vy * sin(theta);
    double ry = vx * sin(theta) + vy * cos(theta);

    cout << fixed << setprecision(10) << cx + rx << " " << cy + ry << "\n";
    return 0;
}
```
