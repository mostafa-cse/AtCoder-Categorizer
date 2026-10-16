# Binomial Coefficient Unimodality Maximization

**Domain**: `Math`  
**Subtopic**: `Combinatorics`  

This workbook contains curated, high-quality competitive programming problems teaching **Binomial Coefficient Unimodality Maximization**.

---

## Curated Problems

### [problem:AtCoder-arc095_b] — Binomial Coefficients
- **Contest**: `abc094`
- **Rating / Difficulty**: 867
- **Specific Skill**: Binomial Coefficient Unimodality Maximization
- **Individual Analysis**: [`../../analysis/AtCoder-arc095_b.md`](../../analysis/AtCoder-arc095_b.md)
- **Problem Statement Summary**: Given n distinct positive integers a_1, ..., a_n. Choose a pair (a_i, a_j) with a_i > a_j that maximizes the binomial coefficient C(a_i, a_j).
- **Core Insight**: C(n, r) is strictly increasing with n. Therefore, a_i must be the maximum element in the entire array: a_i = max(A). To maximize C(a_i, a_j), a_j should be chosen from the remaining elements to minimize |a_j - a_i / 2.0|.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
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

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());
    long long max_val = a[n - 1];

    long long best_r = a[0];
    double target = max_val / 2.0;

    for (int i = 0; i < n - 1; ++i) {
        if (abs(a[i] - target) < abs(best_r - target)) {
            best_r = a[i];
        }
    }

    cout << max_val << " " << best_r << "\n";
    return 0;
}
```
