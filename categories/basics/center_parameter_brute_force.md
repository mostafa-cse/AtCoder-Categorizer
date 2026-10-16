# Center Parameter Brute Force with Positive Reference Anchor

**Domain**: `Basics`  
**Subtopic**: `Complete Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Center Parameter Brute Force with Positive Reference Anchor**.

---

## Curated Problems

### [problem:AtCoder-abc112_c] — Pyramid
- **Contest**: `abc112`
- **Rating / Difficulty**: 1147
- **Specific Skill**: Center Parameter Brute Force with Positive Reference Anchor
- **Individual Analysis**: [`../../analysis/AtCoder-abc112_c.md`](../../analysis/AtCoder-abc112_c.md)
- **Problem Statement Summary**: A pyramid has center (C_X, C_Y) and height H (0 <= C_X, C_Y <= 100, H >= 1). Height at (x, y) is max(0, H - |x - C_X| - |y - C_Y|). Given N observations (x_i, y_i, h_i), find (C_X, C_Y, H).
- **Core Insight**: For any fixed candidate (cx, cy), pick an observation with h_i > 0. Since h_i > 0, the equation h_i = H - |x_i - cx| - |y_i - cy| holds without truncation, uniquely fixing H = h_i + |x_i - cx| + |y_i - cy|! Then verify this H against all other N observations in O(N).
- **Complexity**: Time: `O(101^2 * N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y, h;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    int pos_idx = -1;
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].x >> pts[i].y >> pts[i].h;
        if (pts[i].h > 0) pos_idx = i;
    }

    for (int cx = 0; cx <= 100; ++cx) {
        for (int cy = 0; cy <= 100; ++cy) {
            long long H = pts[pos_idx].h + abs(pts[pos_idx].x - cx) + abs(pts[pos_idx].y - cy);
            bool ok = true;
            for (int i = 0; i < n; ++i) {
                long long expected = max(0LL, H - abs(pts[i].x - cx) - abs(pts[i].y - cy));
                if (pts[i].h != expected) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                cout << cx << " " << cy << " " << H << "\n";
                return 0;
            }
        }
    }

    return 0;
}
```
