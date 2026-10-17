# Permutation Cycle Decomposition with Minimum-Capacity Catalyst Sorting

**Domain**: `Greedy`  
**Subtopic**: `Permutations / Cycles`  

This workbook contains curated, high-quality competitive programming problems teaching **Permutation Cycle Decomposition with Minimum-Capacity Catalyst Sorting**.

---

## Curated Problems

### `[problem:AtCoder-arc111_c]` — Too Heavy
- **Rating / Difficulty**: 1750
- **Contest**: `arc111`
- **Analysis**: [`analysis/AtCoder-arc111_c.md`](../../analysis/AtCoder-arc111_c.md)
- **Key Idea**: The permutation P decomposes into independent cycles. For any cycle of length >= 2, each person who does not have their own luggage must satisfy A_i > B_{P_i} initially. If this holds, the person with the smallest target luggage weight B_u can safely take their own luggage first and act as a catalyst.
- **Time Complexity**: `O(N log N)`
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

    vector<long long> a(n + 1), b(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];
    for (int i = 1; i <= n; ++i) cin >> b[i];

    vector<int> p(n + 1), pos(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
        pos[p[i]] = i;
    }

    for (int i = 1; i <= n; ++i) {
        if (p[i] != i && a[i] <= b[p[i]]) {
            cout << -1 << "\n";
            return 0;
        }
    }

    vector<int> order(n);
    for (int i = 0; i < n; ++i) order[i] = i + 1;
    sort(order.begin(), order.end(), [&](int x, int y) {
        return b[x] < b[y];
    });

    vector<pair<int, int>> swaps;
    for (int x : order) {
        if (p[x] == x) continue;
        int holder = pos[x];
        swaps.push_back({x, holder});

        // Swap luggage between x and holder
        int lug_x = p[x];
        int lug_h = p[holder]; // which is x

        p[x] = lug_h;
        p[holder] = lug_x;

        pos[lug_h] = x;
        pos[lug_x] = holder;
    }

    cout << swaps.size() << "\n";
    for (auto& s : swaps) {
        cout << s.first << " " << s.second << "\n";
    }

    return 0;
}
```
