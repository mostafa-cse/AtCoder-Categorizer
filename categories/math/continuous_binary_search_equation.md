# Binary Search on Continuous Function f(t) = At + B sin(Ct) = 100

**Domain**: `Math`  
**Subtopic**: `Binary Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Continuous Function f(t) = At + B sin(Ct) = 100**.

---

## Curated Problems

### [problem:AtCoder-abc026_d] — Takahashi and Equation
- **Contest**: `abc026`
- **Rating / Difficulty**: 1406
- **Specific Skill**: Binary Search on Continuous Function f(t) = At + B sin(Ct) = 100
- **Individual Analysis**: [`../../analysis/AtCoder-abc026_d.md`](../../analysis/AtCoder-abc026_d.md)
- **Problem Statement Summary**: Given A, B, C. Find a real number t >= 0 such that f(t) = A*t + B*sin(C*PI*t) = 100.
- **Core Insight**: Because f(t) is continuous and passes from 0 to > 100, the Intermediate Value Theorem guarantees at least one root. Binary search / bisection method over 100 iterations on interval [0, 200] achieves machine epsilon precision.
- **Complexity**: Time: `O(100) iterations` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    double pi = acos(-1.0);
    double low = 0.0, high = 200.0;

    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) / 2.0;
        double val = a * mid + b * sin(c * pi * mid);
        if (val < 100.0) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(15) << (low + high) / 2.0 << "\n";
    return 0;
}
```
