# Bipartite Matching / Greedy Sweepline on 2D Coordinates

**Domain**: `Graph Theory`  
**Subtopic**: `Bipartite Matching`  

This workbook contains curated, high-quality competitive programming problems teaching **Bipartite Matching / Greedy Sweepline on 2D Coordinates**.

---

## Curated Problems

### [problem:AtCoder-arc092_a] — 2D Plane 2N Points
- **Contest**: `abc091`
- **Rating / Difficulty**: 1268
- **Specific Skill**: Bipartite Matching / Greedy Sweepline on 2D Coordinates
- **Individual Analysis**: [`../../analysis/AtCoder-arc092_a.md`](../../analysis/AtCoder-arc092_a.md)
- **Problem Statement Summary**: N red points (a_i, b_i) and N blue points (c_i, d_i). A red point can be paired with a blue point if a_i < c_j and b_i < d_j. Maximize the number of disjoint pairs (N <= 100).
- **Core Insight**: For a blue point (c, d), any red point with a < c and b < d is eligible. To preserve flexibility for subsequent blue points (which have even larger c), greedily pair with the eligible red point that has the MAXIMUM y-coordinate b!
- **Complexity**: Time: `O(N^2)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> red(n), blue(n);
    for (int i = 0; i < n; ++i) cin >> red[i].x >> red[i].y;
    for (int i = 0; i < n; ++i) cin >> blue[i].x >> blue[i].y;

    sort(blue.begin(), blue.end(), [](const Point& p1, const Point& p2) {
        return p1.x < p2.x;
    });

    vector<bool> used(n, false);
    int pairs = 0;

    for (int j = 0; j < n; ++j) {
        int best_i = -1;
        int max_y = -1;

        for (int i = 0; i < n; ++i) {
            if (!used[i] && red[i].x < blue[j].x && red[i].y < blue[j].y) {
                if (red[i].y > max_y) {
                    max_y = red[i].y;
                    best_i = i;
                }
            }
        }

        if (best_i != -1) {
            used[best_i] = true;
            pairs++;
        }
    }

    cout << pairs << "\n";
    return 0;
}
```
