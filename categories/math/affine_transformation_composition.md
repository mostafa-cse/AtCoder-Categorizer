# 2D Affine Transformation Matrix Composition

**Domain**: `Math`  
**Subtopic**: `Linear Algebra`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Affine Transformation Matrix Composition**.

---

## Curated Problems

### `[problem:AtCoder-abc189_e]` — Rotate and Flip
- **Rating / Difficulty**: 1526
- **Contest**: `abc189`
- **Analysis**: [`analysis/AtCoder-abc189_e.md`](../../analysis/AtCoder-abc189_e.md)
- **Key Idea**: Every operation is a 2D affine transformation. Composition of any sequence of these transformations can be maintained in O(1) prefix table form as X' = sx * (orig_coord) + cx, Y' = sy * (orig_coord) + cy.
- **Time Complexity**: `O(N + M + Q)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Affine {
    // x' = x_src == 0 ? sx * x + cx : sx * y + cx
    // y' = y_src == 1 ? sy * y + cy : sy * x + cy
    int x_src; // 0 for x, 1 for y
    int y_src; // 0 for x, 1 for y
    long long sx, sy;
    long long cx, cy;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> pts(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> pts[i].first >> pts[i].second;
    }

    int m;
    cin >> m;

    vector<Affine> pref(m + 1);
    pref[0] = {0, 1, 1, 1, 0, 0};

    for (int i = 1; i <= m; ++i) {
        int type;
        cin >> type;
        Affine prev = pref[i - 1];

        if (type == 1) {
            // (x, y) -> (y, -x)
            pref[i] = {prev.y_src, prev.x_src, prev.sy, -prev.sx, prev.cy, -prev.cx};
        } else if (type == 2) {
            // (x, y) -> (-y, x)
            pref[i] = {prev.y_src, prev.x_src, -prev.sy, prev.sx, -prev.cy, prev.cx};
        } else if (type == 3) {
            // (x, y) -> (2p - x, y)
            long long p;
            cin >> p;
            pref[i] = {prev.x_src, prev.y_src, -prev.sx, prev.sy, 2 * p - prev.cx, prev.cy};
        } else if (type == 4) {
            // (x, y) -> (x, 2p - y)
            long long p;
            cin >> p;
            pref[i] = {prev.x_src, prev.y_src, prev.sx, -prev.sy, prev.cx, 2 * p - prev.cy};
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int b, a_idx;
        cin >> b >> a_idx;
        long long orig[2] = {pts[a_idx].first, pts[a_idx].second};
        Affine trans = pref[b];

        long long res_x = trans.sx * orig[trans.x_src] + trans.cx;
        long long res_y = trans.sy * orig[trans.y_src] + trans.cy;

        cout << res_x << " " << res_y << "\n";
    }

    return 0;
}
```
