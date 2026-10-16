# 2D Vertical Consecutive Run Prefix Sums for Diamond Pattern Matching

**Domain**: `Dynamic Programming`  
**Subtopic**: `2D Grid DP`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Vertical Consecutive Run Prefix Sums for Diamond Pattern Matching**.

---

## Curated Problems

### `[problem:AtCoder-abc018_3]` — Diamond Count
- **Rating / Difficulty**: 1553
- **Contest**: `abc018`
- **Analysis**: [`analysis/AtCoder-abc018_3.md`](../../analysis/AtCoder-abc018_3.md)
- **Key Idea**: For cell (r, c) to be a diamond center, for each column offset dx in [-(K-1), K-1], the vertical continuous span of 'o's above and below (r, c+dx) must be at least K - 1 - |dx|.
- **Time Complexity**: `O(R * C * K)`
- **Space Complexity**: `O(R * C)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, K;
    if (!(cin >> R >> C >> K)) return 0;

    vector<string> grid(R + 1);
    for (int r = 1; r <= R; ++r) {
        cin >> grid[r];
        grid[r] = " " + grid[r];
    }

    vector<vector<int>> up(R + 2, vector<int>(C + 2, 0));
    vector<vector<int>> down(R + 2, vector<int>(C + 2, 0));

    for (int c = 1; c <= C; ++c) {
        for (int r = 1; r <= R; ++r) {
            up[r][c] = (grid[r][c] == 'o' ? up[r - 1][c] + 1 : 0);
        }
        for (int r = R; r >= 1; --r) {
            down[r][c] = (grid[r][c] == 'o' ? down[r + 1][c] + 1 : 0);
        }
    }

    int count = 0;
    for (int r = K; r <= R - K + 1; ++r) {
        for (int c = K; c <= C - K + 1; ++c) {
            bool ok = true;
            for (int dx = -(K - 1); dx <= K - 1; ++dx) {
                int req = K - 1 - abs(dx);
                if (up[r][c + dx] <= req || down[r][c + dx] <= req) {
                    ok = false;
                    break;
                }
            }
            if (ok) count++;
        }
    }

    cout << count << "\n";
    return 0;
}
```
