# Shortcut Distance Closed Form Enumeration

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Shortcut Distance Closed Form Enumeration**.

---

## Curated Problems

### [problem:AtCoder-abc160_d] — Line++
- **Contest**: `abc160`
- **Rating / Difficulty**: 879
- **Specific Skill**: Shortcut Distance Closed Form Enumeration
- **Individual Analysis**: [`../../analysis/AtCoder-abc160_d.md`](../../analysis/AtCoder-abc160_d.md)
- **Problem Statement Summary**: A graph has N vertices along a line with edges (i, i+1) for 1 <= i < N, plus an additional shortcut edge (X, Y) with X < Y. For each k in 1..N-1, count the number of pairs (i, j) with i < j whose shortest path distance is exactly k.
- **Core Insight**: Distance is min(j - i, |i - X| + 1 + |j - Y|). Since N <= 2000, we can evaluate all O(N^2) pairs in O(1) each and accumulate counts into a frequency array.
- **Complexity**: Time: `O(N^2)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x, y;
    if (!(cin >> n >> x >> y)) return 0;

    vector<int> ans(n, 0);

    for (int i = 1; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            int direct = j - i;
            int via_bridge = abs(i - x) + 1 + abs(j - y);
            int dist = min(direct, via_bridge);
            ans[dist]++;
        }
    }

    for (int k = 1; k < n; ++k) {
        cout << ans[k] << "\n";
    }

    return 0;
}
```
