# Grid Graph Bounded Step DP with Infinite Stay Greedy Extension

**Domain**: `Dynamic Programming`  
**Subtopic**: `Grid DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Grid Graph Bounded Step DP with Infinite Stay Greedy Extension**.

---

## Curated Problems

### `[problem:AtCoder-abc358_g]` — AtCoder Tour
- **Rating / Difficulty**: 1737
- **Contest**: `abc358`
- **Analysis**: [`analysis/AtCoder-abc358_g.md`](../../analysis/AtCoder-abc358_g.md)
- **Key Idea**: The maximum number of steps taken before settling to stay indefinitely at the highest-scoring cell is bounded by H * W <= 2500. Compute dp[t][r][c] = max score reaching (r, c) in t moves without staying, then add (K - t) * A_{r, c}.
- **Time Complexity**: `O(H * W * min(K, H * W))`
- **Space Complexity**: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;
const int dr[] = {0, 0, 1, -1};
const int dc[] = {1, -1, 0, 0};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    long long k;
    if (!(cin >> h >> w >> k)) return 0;

    int sr, sc;
    cin >> sr >> sc;
    --sr; --sc;

    vector<vector<long long>> a(h, vector<long long>(w));
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) cin >> a[i][j];
    }

    vector<vector<long long>> dp(h, vector<long long>(w, -INF));
    dp[sr][sc] = 0;

    long long ans = k * a[sr][sc];
    int max_steps = min((long long)h * w, k);

    for (int step = 1; step <= max_steps; ++step) {
        vector<vector<long long>> next_dp(h, vector<long long>(w, -INF));

        for (int r = 0; r < h; ++r) {
            for (int c = 0; c < w; ++c) {
                if (dp[r][c] == -INF) continue;
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < h && nc >= 0 && nc < w) {
                        next_dp[nr][nc] = max(next_dp[nr][nc], dp[r][c] + a[nr][nc]);
                    }
                }
            }
        }

        dp = move(next_dp);

        for (int r = 0; r < h; ++r) {
            for (int c = 0; c < w; ++c) {
                if (dp[r][c] != -INF) {
                    long long total = dp[r][c] + (k - step) * a[r][c];
                    ans = max(ans, total);
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```
