# Constructive Prefix/Suffix Cumulative Addition via Global Dominant Extremum

**Domain**: `Basics`  
**Subtopic**: `Constructive Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Constructive Prefix/Suffix Cumulative Addition via Global Dominant Extremum**.

---

## Curated Problems

### `[problem:AtCoder-arc086_b]` — Non-decreasing
- **Rating / Difficulty**: 1567
- **Contest**: `abc081`
- **Analysis**: [`analysis/AtCoder-arc086_b.md`](../../analysis/AtCoder-arc086_b.md)
- **Key Idea**: Find the element with maximum absolute value |A[m]|. If A[m] >= 0, add A[m] to all elements to make them non-negative, then perform forward prefix cumulative additions. If A[m] < 0, add A[m] to all elements to make them non-positive, then perform backward suffix cumulative additions.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    int max_idx = 1;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        if (abs(a[i]) > abs(a[max_idx])) {
            max_idx = i;
        }
    }

    vector<pair<int, int>> ops;

    if (a[max_idx] >= 0) {
        // Make all elements non-negative
        for (int i = 1; i <= n; ++i) {
            if (i != max_idx) {
                ops.push_back({max_idx, i});
            }
        }
        // Prefix sum sweep
        for (int i = 2; i <= n; ++i) {
            ops.push_back({i - 1, i});
        }
    } else {
        // Make all elements non-positive
        for (int i = 1; i <= n; ++i) {
            if (i != max_idx) {
                ops.push_back({max_idx, i});
            }
        }
        // Suffix sum sweep
        for (int i = n - 1; i >= 1; --i) {
            ops.push_back({i + 1, i});
        }
    }

    cout << ops.size() << "\n";
    for (const auto& op : ops) {
        cout << op.first << " " << op.second << "\n";
    }

    return 0;
}
```
