# Sparse Grid 3x3 Window Counting via Coordinate Hash Map

**Domain**: `Data Structures`  
**Subtopic**: `Hash Map`  

This workbook contains curated, high-quality competitive programming problems teaching **Sparse Grid 3x3 Window Counting via Coordinate Hash Map**.

---

## Curated Problems

### `[problem:AtCoder-arc061_b]` — Snuke's Coloring
- **Rating / Difficulty**: 1682
- **Contest**: `abc045`
- **Analysis**: [`analysis/AtCoder-arc061_b.md`](../../analysis/AtCoder-arc061_b.md)
- **Key Idea**: The total number of 3x3 subgrids is (H - 2) * (W - 2) ~ 10^18. However, at most 9 * N subgrids contain AT LEAST ONE black cell! Hash map maps each 3x3 center to its black cell count.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long h, w;
    int n;
    if (!(cin >> h >> w >> n)) return 0;

    map<pair<long long, long long>, int> cnt;

    for (int i = 0; i < n; ++i) {
        long long r, c;
        cin >> r >> c;
        for (int dr = -1; dr <= 1; ++dr) {
            for (int dc = -1; dc <= 1; ++dc) {
                long long cr = r + dr;
                long long cc = c + dc;
                if (cr >= 2 && cr <= h - 1 && cc >= 2 && cc <= w - 1) {
                    cnt[{cr, cc}]++;
                }
            }
        }
    }

    vector<long long> ans(10, 0);
    for (const auto& entry : cnt) {
        ans[entry.second]++;
    }

    long long total_subgrids = (h - 2) * (w - 2);
    ans[0] = total_subgrids - cnt.size();

    for (int j = 0; j <= 9; ++j) {
        cout << ans[j] << "\n";
    }

    return 0;
}
```
