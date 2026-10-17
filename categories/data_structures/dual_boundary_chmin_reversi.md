# Dual Monotonic Coordinate Chmin Query / 2D Reversi Boundary Tracking

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Range Query / Segment Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Dual Monotonic Coordinate Chmin Query / 2D Reversi Boundary Tracking**.

---

## Curated Problems

### `[problem:AtCoder-abc179_f]` — Simplified Reversi
- **Rating / Difficulty**: 1713
- **Contest**: `abc179`
- **Analysis**: [`analysis/AtCoder-abc179_f.md`](../../analysis/AtCoder-abc179_f.md)
- **Key Idea**: The board's turning boundary is monotonic. When query 1 is placed at (1, x), the stones turn white down to row row_limit[x] - 1. When query 2 is placed at (x, 1), stones turn white right to column col_limit[x] - 1. A Fenwick tree / range chmin structure maintains limits for row and column coordinates.
- **Time Complexity**: `O(N + Q log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct FenwickChmin {
    int sz;
    vector<int> tree;
    FenwickChmin(int n, int init_val) : sz(n), tree(n + 1, init_val) {}
    void chmin(int i, int val) {
        for (; i <= sz; i += i & -i) {
            if (val < tree[i]) tree[i] = val;
        }
    }
    int query(int i) {
        int res = 1e9;
        for (; i > 0; i -= i & -i) {
            res = min(res, tree[i]);
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    long long black = (long long)(n - 2) * (n - 2);
    int min_r = n, min_c = n;

    vector<int> row_lim(n + 1, n);
    vector<int> col_lim(n + 1, n);

    while (q--) {
        int type, x;
        cin >> type >> x;
        if (type == 1) { // place at (1, x)
            if (x < min_c) {
                for (int r = x; r < min_c; ++r) {
                    col_lim[r] = min_r;
                }
                min_c = x;
            }
            black -= (col_lim[x] - 2);
        } else { // place at (x, 1)
            if (x < min_r) {
                for (int r = x; r < min_r; ++r) {
                    row_lim[r] = min_c;
                }
                min_r = x;
            }
            black -= (row_lim[x] - 2);
        }
    }

    cout << black << "\n";
    return 0;
}
```
