# 2D Prefix Sums Subrectangle Optimization with Monotonic Envelope

**Domain**: `Dynamic Programming`  
**Subtopic**: `2D Prefix Sums`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Prefix Sums Subrectangle Optimization with Monotonic Envelope**.

---

## Curated Problems

### `[problem:AtCoder-abc005_4]` — Takoyaki Plate
- **Rating / Difficulty**: 1447
- **Contest**: `abc005`
- **Analysis**: [`analysis/AtCoder-abc005_4.md`](../../analysis/AtCoder-abc005_4.md)
- **Key Idea**: Precompute the sum of every possible subrectangle using 2D prefix sums. Record the maximum deliciousness for each area h * w, then compute a prefix-maximum envelope over area.
- **Time Complexity**: `O(N^4 + Q)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> d(n + 1, vector<int>(n + 1, 0));
    vector<vector<int>> pref(n + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> d[i][j];
            pref[i][j] = d[i][j] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
        }
    }

    int max_area = n * n;
    vector<int> best(max_area + 1, 0);

    for (int r1 = 1; r1 <= n; ++r1) {
        for (int r2 = r1; r2 <= n; ++r2) {
            int h = r2 - r1 + 1;
            for (int c1 = 1; c1 <= n; ++c1) {
                for (int c2 = c1; c2 <= n; ++c2) {
                    int w = c2 - c1 + 1;
                    int area = h * w;
                    int sum = pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1];
                    best[area] = max(best[area], sum);
                }
            }
        }
    }

    for (int a = 1; a <= max_area; ++a) {
        best[a] = max(best[a], best[a - 1]);
    }

    int q;
    cin >> q;
    while (q--) {
        int p;
        cin >> p;
        cout << best[p] << "\n";
    }

    return 0;
}
```
