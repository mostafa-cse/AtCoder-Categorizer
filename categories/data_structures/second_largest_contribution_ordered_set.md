# Second Largest Element Contribution via Ordered Set Predecessors/Successors

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Ordered Set / Predecessors`  

This workbook contains curated, high-quality competitive programming problems teaching **Second Largest Element Contribution via Ordered Set Predecessors/Successors**.

---

## Curated Problems

### `[problem:AtCoder-abc140_e]` — Second Sum
- **Rating / Difficulty**: 1873
- **Contest**: `abc140`
- **Analysis**: [`analysis/AtCoder-abc140_e.md`](../../analysis/AtCoder-abc140_e.md)
- **Key Idea**: Process elements in descending order of value, inserting their indices into an active ordered set. When processing index i with value v, find the two predecessors (L_2, L_1) and two successors (R_1, R_2) in the set.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> pos(n + 1);
    for (int i = 1; i <= n; ++i) {
        int p;
        cin >> p;
        pos[p] = i;
    }

    multiset<int> s;
    s.insert(0); s.insert(0);
    s.insert(n + 1); s.insert(n + 1);

    long long ans = 0;

    for (int v = n; v >= 1; --v) {
        int i = pos[v];
        auto it = s.lower_bound(i);
        long long r1 = *it;
        long long r2 = *next(it);
        long long l1 = *prev(it);
        long long l2 = *prev(prev(it));

        long long ways = (l1 - l2) * (r1 - i) + (i - l1) * (r2 - r1);
        ans += (long long)v * ways;

        s.insert(i);
    }

    cout << ans << "\n";
    return 0;
}
```
