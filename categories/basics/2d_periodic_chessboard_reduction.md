# 2D Periodic Chessboard Coordinate Reduction and 2D Prefix Sums

**Domain**: `Basics`  
**Subtopic**: `2D Prefix Sums`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Periodic Chessboard Coordinate Reduction and 2D Prefix Sums**.

---

## Curated Problems

### `[problem:AtCoder-arc089_b]` — Checker
- **Rating / Difficulty**: 1797
- **Contest**: `abc086`
- **Analysis**: [`analysis/AtCoder-arc089_b.md`](../../analysis/AtCoder-arc089_b.md)
- **Key Idea**: The chessboard pattern has period 2K in both X and Y dimensions. A white point at (x, y) is equivalent to a black point at (x, y + K). Fold all points modulo 2K: (x % 2K, y % 2K). Then use 2D prefix sums to evaluate all (2K) x (2K) shift offsets in O(K^2).
- **Time Complexity**: `O(N + K^2)`
- **Space Complexity**: `O(K^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    int k2 = 2 * k;
    vector<vector<int>> cnt(k2, vector<int>(k2, 0));

    for (int i = 0; i < n; ++i) {
        int x, y;
        char c;
        cin >> x >> y >> c;
        if (c == 'W') y += k;
        cnt[x % k2][y % k2]++;
    }

    vector<vector<int>> pref(2 * k2 + 1, vector<int>(2 * k2 + 1, 0));
    for (int i = 0; i < 2 * k2; ++i) {
        for (int j = 0; j < 2 * k2; ++j) {
            pref[i + 1][j + 1] = cnt[i % k2][j % k2] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j];
        }
    }

    auto get_sum = [&](int x1, int y1, int x2, int y2) -> int {
        return pref[x2][y2] - pref[x1][y2] - pref[x2][y1] + pref[x1][y1];
    };

    int max_ans = 0;
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            int black_count = get_sum(i, j, i + k, j + k) +
                              get_sum(i + k, j + k, i + 2 * k, j + 2 * k);
            max_ans = max(max_ans, max(black_count, n - black_count));
        }
    }

    cout << max_ans << "\n";
    return 0;
}
```
