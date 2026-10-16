# Prefix Imbalance Minimum Cuts

**Domain**: `Math`  
**Subtopic**: `Prefix Invariants`  

This workbook contains curated, high-quality competitive programming problems teaching **Prefix Imbalance Minimum Cuts**.

---

## Curated Problems

### [problem:AtCoder-abc027_b] — Island Bridges
- **Contest**: `abc027`
- **Rating / Difficulty**: 855
- **Specific Skill**: Prefix Imbalance Minimum Cuts
- **Individual Analysis**: [`../../analysis/AtCoder-abc027_b.md`](../../analysis/AtCoder-abc027_b.md)
- **Problem Statement Summary**: N islands in a line have populations a_1, ..., a_N. You can build bridges between adjacent islands (i, i+1). Find the minimum number of bridges needed so that all connected islands can redistribute people equally.
- **Core Insight**: Consider the cut between island i and i+1. The first i islands currently have sum_{j=1}^i a_j people, but need i * avg people. If sum_{j=1}^i a_j != i * avg, people must cross between i and i+1, so a bridge is mandatory! Conversely, if sum_{j=1}^i a_j == i * avg, no people need to cross, so no bridge is needed.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    int total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total += a[i];
    }

    if (total % n != 0) {
        cout << -1 << "\n";
        return 0;
    }

    int avg = total / n;
    int bridges = 0;
    int pref = 0;

    for (int i = 0; i < n - 1; ++i) {
        pref += a[i];
        if (pref != (i + 1) * avg) {
            bridges++;
        }
    }

    cout << bridges << "\n";
    return 0;
}
```
