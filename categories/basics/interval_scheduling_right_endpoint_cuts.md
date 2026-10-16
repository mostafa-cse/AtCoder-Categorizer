# Interval Scheduling / Right-Endpoint Greedy Cuts

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Interval Scheduling / Right-Endpoint Greedy Cuts**.

---

## Curated Problems

### [problem:AtCoder-abc103_d] — Islands War
- **Contest**: `abc103`
- **Rating / Difficulty**: 1278
- **Specific Skill**: Interval Scheduling / Right-Endpoint Greedy Cuts
- **Individual Analysis**: [`../../analysis/AtCoder-abc103_d.md`](../../analysis/AtCoder-abc103_d.md)
- **Problem Statement Summary**: N islands in a row with N - 1 bridges between adjacent islands. M disputes: dispute i requires island a_i and b_i to NOT be connected. Find the minimum bridges to remove.
- **Core Insight**: Sort disputes by their right endpoint b_i in ascending order. Greedily cut the rightmost bridge in the interval: bridge b_i - 1. Cutting as far right as possible maximizes the number of subsequent disputes that are also severed by the same cut!
- **Complexity**: Time: `O(M log M)` | Space: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Dispute {
    int a, b;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Dispute> d(m);
    for (int i = 0; i < m; ++i) {
        cin >> d[i].a >> d[i].b;
    }

    sort(d.begin(), d.end(), [](const Dispute& x, const Dispute& y) {
        return x.b < y.b;
    });

    int cuts = 0;
    int last_cut = -1;

    for (const auto& disp : d) {
        if (disp.a > last_cut) {
            cuts++;
            last_cut = disp.b - 1;
        }
    }

    cout << cuts << "\n";
    return 0;
}
```
