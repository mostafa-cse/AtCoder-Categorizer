# Adjacent Greedy Transition / Cost Comparison

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Adjacent Greedy Transition / Cost Comparison**.

---

## Curated Problems

### [problem:AtCoder-arc067_b] — Walk and Teleport
- **Contest**: `abc052`
- **Rating / Difficulty**: 1060
- **Specific Skill**: Adjacent Greedy Transition / Cost Comparison
- **Individual Analysis**: [`../../analysis/AtCoder-arc067_b.md`](../../analysis/AtCoder-arc067_b.md)
- **Problem Statement Summary**: N towns on a 1D line at coordinates X_1 < X_2 < ... < X_N. You start at X_1 and visit all towns in increasing order. Walking distance d costs d * A fatigue; teleporting to any town costs B fatigue. Find the minimum fatigue to visit all towns.
- **Core Insight**: Each step between adjacent towns i and i+1 is completely independent. For each segment, walking costs (X_{i+1} - X_i) * A, while teleporting costs B. The optimal choice is strictly min((X_{i+1} - X_i) * A, B).
- **Complexity**: Time: `O(N)` | Space: `O(N)`
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
    long long a, b;
    if (!(cin >> n >> a >> b)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) {
        cin >> x[i];
    }

    long long total = 0;
    for (int i = 0; i < n - 1; ++i) {
        long long walk = (x[i + 1] - x[i]) * a;
        total += min(walk, b);
    }

    cout << total << "\n";
    return 0;
}
```
