# Contiguous Block Placement DP for Colored Particles on 1D Line

**Domain**: `Dynamic Programming`  
**Subtopic**: `Interval DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Contiguous Block Placement DP for Colored Particles on 1D Line**.

---

## Curated Problems

### `[problem:AtCoder-abc004_4]` — マーブル
- **Rating / Difficulty**: 1861
- **Contest**: `abc004`
- **Analysis**: [`analysis/AtCoder-abc004_4.md`](../../analysis/AtCoder-abc004_4.md)
- **Key Idea**: The optimal placement places all red marbles into a contiguous block [r_L, r_R], all green into [g_L, g_R], and all blue into [b_L, b_R] such that r_R < g_L and g_R < b_L. Iterate over green's center/start position, and place red and blue greedily closest to their origins.
- **Time Complexity**: `O(Range * (R + G + B))`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const long long INF = 1e18;

long long range_cost(int start, int len, int origin) {
    long long total = 0;
    for (int i = 0; i < len; ++i) {
        total += abs(start + i - origin);
    }
    return total;
}

long long best_left(int max_r, int len, int origin) {
    int ideal_start = origin - len / 2;
    int actual_start = min(ideal_start, max_r - len + 1);
    return range_cost(actual_start, len, origin);
}

long long best_right(int min_l, int len, int origin) {
    int ideal_start = origin - len / 2;
    int actual_start = max(ideal_start, min_l);
    return range_cost(actual_start, len, origin);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, G, B;
    if (!(cin >> R >> G >> B)) return 0;

    long long min_cost = INF;

    for (int g_start = -500; g_start <= 500; ++g_start) {
        int g_end = g_start + G - 1;
        long long cost_g = range_cost(g_start, G, 0);
        long long cost_r = best_left(g_start - 1, R, -100);
        long long cost_b = best_right(g_end + 1, B, 100);

        min_cost = min(min_cost, cost_g + cost_r + cost_b);
    }

    cout << min_cost << "\n";
    return 0;
}
```
