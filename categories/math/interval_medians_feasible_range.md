# Interval Medians Feasible Range [Min Median, Max Median]

**Domain**: `Math`  
**Subtopic**: `Median Optimization`  

This workbook contains curated, high-quality competitive programming problems teaching **Interval Medians Feasible Range [Min Median, Max Median]**.

---

## Curated Problems

### [problem:AtCoder-abc169_e] — Count Median
- **Contest**: `abc169`
- **Rating / Difficulty**: 1353
- **Specific Skill**: Interval Medians Feasible Range [Min Median, Max Median]
- **Individual Analysis**: [`../../analysis/AtCoder-abc169_e.md`](../../analysis/AtCoder-abc169_e.md)
- **Problem Statement Summary**: N integers X_1..X_N where each X_i is chosen from integer interval [A_i, B_i]. Find the number of possible distinct values of the median of X_1..X_N.
- **Core Insight**: Sort A and B independently. (1) If N is odd: the median is an integer. Min median is A[N/2], max median is B[N/2]. Every integer in [min, max] is achievable, giving B[N/2] - A[N/2] + 1 values. (2) If N is even: the median is (X_{N/2 - 1} + X_{N/2}) / 2. Min sum is A[N/2 - 1] + A[N/2], max sum is B[N/2 - 1] + B[N/2]. Every integer sum in between is achievable (each step of 0.5 in median), giving max_sum - min_sum + 1 values.
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
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

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> b[i];
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    if (n % 2 == 1) {
        long long min_med = a[n / 2];
        long long max_med = b[n / 2];
        cout << max_med - min_med + 1 << "\n";
    } else {
        long long min_sum = a[n / 2 - 1] + a[n / 2];
        long long max_sum = b[n / 2 - 1] + b[n / 2];
        cout << max_sum - min_sum + 1 << "\n";
    }

    return 0;
}
```
