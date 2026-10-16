# 1D L1-Norm / Absolute Deviation Median Minimization

**Domain**: `Math`  
**Subtopic**: `Median Optimization`  

This workbook contains curated, high-quality competitive programming problems teaching **1D L1-Norm / Absolute Deviation Median Minimization**.

---

## Curated Problems

### [problem:AtCoder-arc100_a] — Linear Approximation
- **Contest**: `abc102`
- **Rating / Difficulty**: 1089
- **Specific Skill**: 1D L1-Norm / Absolute Deviation Median Minimization
- **Individual Analysis**: [`../../analysis/AtCoder-arc100_a.md`](../../analysis/AtCoder-arc100_a.md)
- **Problem Statement Summary**: Given an array A of N integers. Find an integer b that minimizes sum_{i=1}^N |A_i - (b + i)|.
- **Core Insight**: The value b that minimizes the sum of absolute deviations sum |C_i - b| is the median of array C! Sort C in ascending order and set b = C[N / 2].
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> c(n);
    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        c[i] = a - (i + 1);
    }

    sort(c.begin(), c.end());
    long long b = c[n / 2];

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += abs(c[i] - b);
    }

    cout << ans << "\n";
    return 0;
}
```
