# Max Row/Col Intersection Overlap Filtering

**Domain**: `Basics`  
**Subtopic**: `Grid Sweeping`  

This workbook contains curated, high-quality competitive programming problems teaching **Max Row/Col Intersection Overlap Filtering**.

---

## Curated Problems

### [problem:AtCoder-abc176_e] — Bomber
- **Contest**: `abc176`
- **Rating / Difficulty**: 1204
- **Specific Skill**: Max Row/Col Intersection Overlap Filtering
- **Individual Analysis**: [`../../analysis/AtCoder-abc176_e.md`](../../analysis/AtCoder-abc176_e.md)
- **Problem Statement Summary**: An H x W grid contains M targets. Placing a bomb at cell (r, c) destroys all targets in row r and column c. Find the maximum number of targets that can be destroyed.
- **Core Insight**: Let max_r = max_i count_row[i] and max_c = max_j count_col[j]. The answer is either max_r + max_c or max_r + max_c - 1. It equals max_r + max_c if and only if there exists SOME pair (r, c) such that count_row[r] == max_r and count_col[c] == max_c and cell (r, c) does NOT contain a target!
- **Complexity**: Time: `O(H + W + M)` | Space: `O(H + W + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, m;
    if (!(cin >> h >> w >> m)) return 0;

    vector<int> row_cnt(h + 1, 0), col_cnt(w + 1, 0);
    set<pair<int, int>> targets;

    for (int i = 0; i < m; ++i) {
        int r, c;
        cin >> r >> c;
        row_cnt[r]++;
        col_cnt[c]++;
        targets.insert({r, c});
    }

    int max_r = 0, max_c = 0;
    for (int r = 1; r <= h; ++r) max_r = max(max_r, row_cnt[r]);
    for (int c = 1; c <= w; ++c) max_c = max(max_c, col_cnt[c]);

    vector<int> best_r, best_c;
    for (int r = 1; r <= h; ++r) if (row_cnt[r] == max_r) best_r.push_back(r);
    for (int c = 1; c <= w; ++c) if (col_cnt[c] == max_c) best_c.push_back(c);

    if ((long long)best_r.size() * best_c.size() > m) {
        cout << max_r + max_c << "\n";
        return 0;
    }

    for (int r : best_r) {
        for (int c : best_c) {
            if (!targets.count({r, c})) {
                cout << max_r + max_c << "\n";
                return 0;
            }
        }
    }

    cout << max_r + max_c - 1 << "\n";
    return 0;
}
```
