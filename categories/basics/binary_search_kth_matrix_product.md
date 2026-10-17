# Binary Search on Answer for K-th Matrix Product / Multi-Set Item

**Domain**: `Basics`  
**Subtopic**: `Binary Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Answer for K-th Matrix Product / Multi-Set Item**.

---

## Curated Problems

### `[problem:AtCoder-arc037_c]` — 億マス計算
- **Rating / Difficulty**: 1824
- **Contest**: `arc037`
- **Analysis**: [`analysis/AtCoder-arc037_c.md`](../../analysis/AtCoder-arc037_c.md)
- **Key Idea**: Binary search on the product value X in [1, 10^{18}]. For a fixed X, count pairs (i, j) with A_i * B_j <= X in O(N log N) using upper_bound on sorted B.
- **Time Complexity**: `O(N log N * log(max_ans))`
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

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];

    sort(b.begin(), b.end());

    long long low = 1, high = 1e18, ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        long long count = 0;

        for (int i = 0; i < n; ++i) {
            long long target = mid / a[i];
            auto it = upper_bound(b.begin(), b.end(), target);
            count += (it - b.begin());
        }

        if (count >= k) {
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
