# Greedy Sorting on Floating Point Recurrence

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Sorting on Floating Point Recurrence**.

---

## Curated Problems

### [problem:AtCoder-abc003_3] — AtCoder Programming Course
- **Contest**: `abc003`
- **Rating / Difficulty**: 824
- **Specific Skill**: Greedy Sorting on Floating Point Recurrence
- **Individual Analysis**: [`../../analysis/AtCoder-abc003_3.md`](../../analysis/AtCoder-abc003_3.md)
- **Problem Statement Summary**: Choose K videos out of N with ratings R_1, ..., R_N. Starting from rating 0, watching a video with rating R updates your rating to (current + R) / 2. Maximize the final rating.
- **Core Insight**: To maximize the weighted sum, we must choose the K largest ratings and watch them in strictly ascending order so that the largest values receive the largest coefficients (1/2, 1/4, etc.).
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<double> r(n);
    for (int i = 0; i < n; ++i) {
        cin >> r[i];
    }

    sort(r.begin(), r.end());

    double rate = 0.0;
    for (int i = n - k; i < n; ++i) {
        rate = (rate + r[i]) / 2.0;
    }

    cout << fixed << setprecision(9) << rate << "\n";
    return 0;
}
```
