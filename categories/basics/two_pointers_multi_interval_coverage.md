# Two Pointers / Sliding Window on Multi-Interval Coverage

**Domain**: `Basics`  
**Subtopic**: `Two Pointers`  

This workbook contains curated, high-quality competitive programming problems teaching **Two Pointers / Sliding Window on Multi-Interval Coverage**.

---

## Curated Problems

### `[problem:AtCoder-abc260_e]` — At Least One
- **Rating / Difficulty**: 1692
- **Contest**: `abc260`
- **Analysis**: [`analysis/AtCoder-abc260_e.md`](../../analysis/AtCoder-abc260_e.md)
- **Key Idea**: Two pointers! For each left endpoint l (1 <= l <= M), find the minimum right endpoint r such that [l, r] contains at least one number from every pair.
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> occ(m + 1);
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        occ[a].push_back(i);
        occ[b].push_back(i);
    }

    vector<int> pair_cnt(n, 0);
    int covered = 0;
    int r = 1;

    vector<int> diff(m + 2, 0);

    for (int l = 1; l <= m; ++l) {
        while (r <= m && covered < n) {
            for (int p : occ[r]) {
                if (pair_cnt[p] == 0) covered++;
                pair_cnt[p]++;
            }
            r++;
        }

        if (covered == n) {
            int min_len = (r - 1) - l + 1;
            int max_len = m - l + 1;
            diff[min_len]++;
            diff[max_len + 1]--;
        }

        // Remove l
        for (int p : occ[l]) {
            pair_cnt[p]--;
            if (pair_cnt[p] == 0) covered--;
        }
    }

    int cur = 0;
    for (int k = 1; k <= m; ++k) {
        cur += diff[k];
        cout << cur << (k == m ? "\n" : " ");
    }

    return 0;
}
```
