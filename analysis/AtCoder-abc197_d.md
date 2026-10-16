# Problem Analysis: AtCoder-abc197_d — Opposite

**Problem ID**: `AtCoder-abc197_d`  
**Contest**: `abc197`  
**Rating / Difficulty**: 831  
**URL**: https://atcoder.jp/contests/abc197/tasks/abc197_d  
**VJudge Tag**: `[problem:AtCoder-abc197_d]`  
**Category File**: [`../categories/geometry/point_rotation_complex.md`](../categories/geometry/point_rotation_complex.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Rotations & Complex Plane`  
- **Topic (Skill)**: `2D Point Rotation around Center via Complex Numbers`  

---

## 1. Problem Statement & Key Idea
In a regular N-gon (N is even), vertex 0 has coordinates (x_0, y_0) and opposite vertex N/2 has coordinates (x_{N/2}, y_{N/2}). Find the coordinates of vertex 1: (x_1, y_1).

**Key Idea**: The center of the regular N-gon is the midpoint between opposite vertices 0 and N/2: M = (p_0 + p_{N/2}) / 2. Vertex 1 is obtained by rotating vertex 0 around center M counterclockwise by angle theta = 2 * PI / N.

## 2. Core Observation & Invariant
Using complex numbers: z_1 = z_M + (z_0 - z_M) * e^(i * theta). This eliminates trigonometry casework and provides clean, numerically stable coordinate calculation.

## 3. Step-by-Step Algorithm
1. Compute center coordinates: cx = (x0 + x_half) / 2.0, cy = (y0 + y_half) / 2.0.
2. Compute angle theta = 2.0 * PI / N.
3. Shift vector: vx = x0 - cx, vy = y0 - cy.
4. Rotate vector: rx = vx * cos(theta) - vy * sin(theta), ry = vx * sin(theta) + vy * cos(theta).
5. Output cx + rx and cy + ry with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Point rotation around an arbitrary center using 2D rotation matrix / complex numbers.
- **Reusable Pattern**: `Rotate point P around center C: C + R(theta) * (P - C).`
