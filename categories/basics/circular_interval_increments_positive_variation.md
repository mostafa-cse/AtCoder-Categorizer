# Basic Constructive Algorithms

**Domain**: `Basics`  
**Subtopic**: `Greedy and Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Basic Constructive Algorithms**.

---

## Curated Problems

### `[problem:AtCoder-arc136_c]` — Circular Addition
- **Rating / Difficulty**: 2137
- **Contest**: `arc136`
- **Analysis**: [`analysis/AtCoder-arc136_c.md`](../../analysis/AtCoder-arc136_c.md)
- **Key Idea**: Each interval increment on a circle increases the maximum element by at most 1, so answer >= max_i A_i. Also, each interval increment contributes at most 1 to the sum of positive adjacent differences sum_{i=1}^N max(0, A_i - A_{i-1}) (wrapping around). Thus answer >= sum_{i=1}^N max(0, A_i - A_{i-1}). It can be shown that this theoretical lower bound is always tight: ans = max(max_i A_i, sum_{i=1}^N max(0, A_i - A_{i-1})).
- **Time Complexity**: `O(N)`
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
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    long long sum_pos_diff = 0;
    for (int i = 0; i < n; ++i) {
        int prev_idx = (i - 1 + n) % n;
        if (a[i] > a[prev_idx]) {
            sum_pos_diff += (a[i] - a[prev_idx]);
        }
    }

    long long ans = max(max_val, sum_pos_diff);
    cout << ans << "\n";
    return 0;
}
```
