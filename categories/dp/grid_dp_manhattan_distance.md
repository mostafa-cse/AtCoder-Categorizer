# 2D Grid DP Coordinate Manhattan Distance Transformation

**Domain**: `Dynamic Programming`  
**Subtopic**: `2D Grid DP`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Grid DP Coordinate Manhattan Distance Transformation**.

---

## Curated Problems

### `[problem:AtCoder-abc210_d]` — National Railway
- **Rating / Difficulty**: 1507
- **Contest**: `abc210`
- **Analysis**: [`analysis/AtCoder-abc210_d.md`](../../analysis/AtCoder-abc210_d.md)
- **Key Idea**: Remove the absolute value by orienting the relative position: either (i' <= i, j' <= j) or (i' <= i, j' >= j). The second case is solved by horizontally reversing the grid.
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

long long solve_directed(int h, int w, long long C, const vector<vector<long long>>& A) {
    vector<vector<long long>> dp(h, vector<long long>(w, INF));
    long long best = INF;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (r > 0) {
                dp[r][c] = min(dp[r][c], min(A[r - 1][c], dp[r - 1][c]) + C);
            }
            if (c > 0) {
                dp[r][c] = min(dp[r][c], min(A[r][c - 1], dp[r][c - 1]) + C);
            }
            if (dp[r][c] < INF) {
                best = min(best, A[r][c] + dp[r][c]);
            }
        }
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    long long C;
    if (!(cin >> h >> w >> C)) return 0;

    vector<vector<long long>> A(h, vector<long long>(w));
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            cin >> A[r][c];
        }
    }

    long long ans1 = solve_directed(h, w, C, A);

    // Flip horizontally
    for (int r = 0; r < h; ++r) {
        reverse(A[r].begin(), A[r].end());
    }

    long long ans2 = solve_directed(h, w, C, A);

    cout << min(ans1, ans2) << "\n";
    return 0;
}
```
