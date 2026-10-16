# 2D Subgrid Median via Binary Search on Answer + 2D Prefix Sums

**Domain**: `Basics`  
**Subtopic**: `Binary Search on Answer`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Subgrid Median via Binary Search on Answer + 2D Prefix Sums**.

---

## Curated Problems

### `[problem:AtCoder-abc203_d]` — Pond
- **Rating / Difficulty**: 1622
- **Contest**: `abc203`
- **Analysis**: [`analysis/AtCoder-abc203_d.md`](../../analysis/AtCoder-abc203_d.md)
- **Key Idea**: Binary search on the answer X. A subgrid has median <= X iff the number of elements STRICTLY GREATER than X in the subgrid is at most floor(K^2 / 2).
- **Time Complexity**: `O(N^2 log(max A))`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<int>> a(n + 1, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> a[i][j];
        }
    }

    int lim = (k * k) / 2;
    int low = 0, high = 1e9;
    int ans = high;

    vector<vector<int>> pref(n + 1, vector<int>(n + 1, 0));

    auto check = [&](int x) -> bool {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                int val = (a[i][j] > x ? 1 : 0);
                pref[i][j] = val + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
            }
        }

        for (int i = k; i <= n; ++i) {
            for (int j = k; j <= n; ++j) {
                int count = pref[i][j] - pref[i - k][j] - pref[i][j - k] + pref[i - k][j - k];
                if (count <= lim) return true;
            }
        }
        return false;
    };

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
