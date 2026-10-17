# Grid Parity Lower Bound and Recursive Square Border Peeling Construction

**Domain**: `Miscellaneous`  
**Subtopic**: `Constructive Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Grid Parity Lower Bound and Recursive Square Border Peeling Construction**.

---

## Curated Problems

### `[problem:AtCoder-arc226_c]` — Square Corner Packing
- **Rating / Difficulty**: 2070
- **Contest**: `arc226`
- **Analysis**: [`analysis/AtCoder-arc226_c.md`](../../analysis/AtCoder-arc226_c.md)
- **Key Idea**: Each square corners operation consumes 0 or 2 cells in any row or column. Thus if W is odd, at least 1 cell per row cannot be painted (at least H unpainted cells). If H and W are even, 2x2 squares achieve HW/4 operations. If one is odd (say W odd, H even), 2x2 squares achieve H(W-1)/4 operations. If both H and W are odd: when H != W, peel 2 columns/rows of 2x2 squares until H == W; when H == W is odd, peel an outer border of thickness 2 containing one (H-1)x(H-1) square and 2x2 border squares, reducing H by 4.
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Op {
    int r, c, s;
};

void solve() {
    int H, W;
    cin >> H >> W;

    vector<Op> ops;

    auto peel = [&](auto& self, int r1, int c1, int h, int w) -> void {
        if (h <= 1 || w <= 1) return;

        if (h % 2 == 0 && w % 2 == 0) {
            for (int r = r1; r < r1 + h; r += 2) {
                for (int c = c1; c < c1 + w; c += 2) {
                    ops.push_back({r, c, 1});
                }
            }
            return;
        }

        if (h % 2 == 0 && w % 2 != 0) {
            for (int r = r1; r < r1 + h; r += 2) {
                for (int c = c1; c < c1 + w - 1; c += 2) {
                    ops.push_back({r, c, 1});
                }
            }
            return;
        }

        if (h % 2 != 0 && w % 2 == 0) {
            for (int r = r1; r < r1 + h - 1; r += 2) {
                for (int c = c1; c < c1 + w; c += 2) {
                    ops.push_back({r, c, 1});
                }
            }
            return;
        }

        if (h < w) {
            for (int r = r1; r < r1 + h - 1; r += 2) {
                ops.push_back({r, c1 + w - 2, 1});
            }
            self(self, r1, c1, h, w - 2);
            return;
        }
        if (h > w) {
            for (int c = c1; c < c1 + w - 1; c += 2) {
                ops.push_back({r1 + h - 2, c, 1});
            }
            self(self, r1, c1, h - 2, w);
            return;
        }

        if (h == 1) return;
        if (h == 3) {
            ops.push_back({r1, c1, 2});
            return;
        }

        ops.push_back({r1, c1, h - 1});

        for (int c = c1 + 1; c + 1 < c1 + h - 1; c += 2) {
            ops.push_back({r1, c, 1});
        }
        for (int c = c1 + 1; c + 1 < c1 + h - 1; c += 2) {
            ops.push_back({r1 + h - 2, c, 1});
        }
        for (int r = r1 + 2; r + 1 < r1 + h - 1; r += 2) {
            ops.push_back({r, c1, 1});
        }
        for (int r = r1 + 1; r + 1 < r1 + h - 2; r += 2) {
            ops.push_back({r, c1 + h - 2, 1});
        }

        self(self, r1 + 2, c1 + 2, h - 4, w - 4);
    };

    peel(peel, 1, 1, H, W);

    cout << ops.size() << "\n";
    for (auto& op : ops) {
        cout << op.r << " " << op.c << " " << op.s << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```
