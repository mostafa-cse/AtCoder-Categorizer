# Min-Max Spread Optimization via Fixed Lower Bound and Segmented Greedy Extraction

**Domain**: `Basics`  
**Subtopic**: `Greedy / Two Pointers`  

This workbook contains curated, high-quality competitive programming problems teaching **Min-Max Spread Optimization via Fixed Lower Bound and Segmented Greedy Extraction**.

---

## Curated Problems

### `[problem:AtCoder-arc098_c]` — Range Minimum Queries
- **Rating / Difficulty**: 1951
- **Contest**: `arc098`
- **Analysis**: [`analysis/AtCoder-arc098_c.md`](../../analysis/AtCoder-arc098_c.md)
- **Key Idea**: Iterate over the minimum element X in Z (at most N choices from A). For a fixed X, any chosen element must be >= X, meaning elements < X cannot be inside any chosen window. This splits A into contiguous segments of elements >= X. For each segment of length L >= K, we can extract L - K + 1 elements; greedily choose the smallest L - K + 1 elements from each segment. If the total extractable elements across all segments is >= Q, take the Q-th smallest element Y from the merged pool, and update ans = min(ans, Y - X).
- **Time Complexity**: `O(N^2 log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, q;
    if (!(cin >> n >> k >> q)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int ans = INF;

    for (int i = 0; i < n; ++i) {
        int x = a[i];
        vector<int> pool;
        vector<int> cur_seg;

        for (int j = 0; j < n; ++j) {
            if (a[j] >= x) {
                cur_seg.push_back(a[j]);
            } else {
                if ((int)cur_seg.size() >= k) {
                    sort(cur_seg.begin(), cur_seg.end());
                    int extract_cnt = (int)cur_seg.size() - k + 1;
                    for (int m = 0; m < extract_cnt; ++m) {
                        pool.push_back(cur_seg[m]);
                    }
                }
                cur_seg.clear();
            }
        }
        if ((int)cur_seg.size() >= k) {
            sort(cur_seg.begin(), cur_seg.end());
            int extract_cnt = (int)cur_seg.size() - k + 1;
            for (int m = 0; m < extract_cnt; ++m) {
                pool.push_back(cur_seg[m]);
            }
        }

        if ((int)pool.size() >= q) {
            sort(pool.begin(), pool.end());
            ans = min(ans, pool[q - 1] - x);
        }
    }

    cout << ans << "\n";
    return 0;
}
```
