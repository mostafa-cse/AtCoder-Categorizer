# Interval Union under Bounded Expansion via Sorted Gap Prefix Sums

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Binary Search / Prefix Sums`  

This workbook contains curated, high-quality competitive programming problems teaching **Interval Union under Bounded Expansion via Sorted Gap Prefix Sums**.

---

## Curated Problems

### `[problem:AtCoder-arc014_4]` — grepマスター
- **Rating / Difficulty**: 1904
- **Contest**: `arc014`
- **Analysis**: [`analysis/AtCoder-arc014_4.md`](../../analysis/AtCoder-arc014_4.md)
- **Key Idea**: Match intervals expand by X to the left and Y to the right (total expansion S = X + Y between adjacent matches). The gap between L_i and L_{i+1} is d_i = L_{i+1} - L_i - 1. The number of covered lines between them is min(d_i, S). Sort all gaps d_i; for each query S, binary search splits gaps into those <= S (sum from prefix sums) and those > S ((count) * S). Boundary matches expand by min(X, L_1 - 1) and min(Y, all - L_N).
- **Time Complexity**: `O(N log N + M log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long all;
    int n, m;
    if (!(cin >> all >> n >> m)) return 0;

    vector<long long> l(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i];
    }

    vector<long long> d(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        d[i] = l[i + 1] - l[i] - 1;
    }
    sort(d.begin(), d.end());

    vector<long long> pref(n, 0);
    for (int i = 0; i < n - 1; ++i) {
        pref[i + 1] = pref[i] + d[i];
    }

    for (int q = 0; q < m; ++q) {
        long long x, y;
        cin >> x >> y;

        long long left_ext = min(x, l[0] - 1);
        long long right_ext = min(y, all - l[n - 1]);
        long long s = x + y;

        int idx = upper_bound(d.begin(), d.end(), s) - d.begin();
        long long gap_sum = pref[idx] + (long long)(n - 1 - idx) * s;

        long long ans = n + left_ext + right_ext + gap_sum;
        cout << ans << "\n";
    }

    return 0;
}
```
