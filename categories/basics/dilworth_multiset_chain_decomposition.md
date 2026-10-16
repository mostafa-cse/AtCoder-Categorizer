# Dilworth's Theorem / Minimum Decreasing Chains via Multiset Greedy

**Domain**: `Basics`  
**Subtopic**: `Dilworth / Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Dilworth's Theorem / Minimum Decreasing Chains via Multiset Greedy**.

---

## Curated Problems

### [problem:AtCoder-abc134_e] — Sequence Decomposing
- **Contest**: `abc134`
- **Rating / Difficulty**: 1320
- **Specific Skill**: Dilworth's Theorem / Minimum Decreasing Chains via Multiset Greedy
- **Individual Analysis**: [`../../analysis/AtCoder-abc134_e.md`](../../analysis/AtCoder-abc134_e.md)
- **Problem Statement Summary**: Given an array A of N integers. Color elements such that every monochromatic subsequence is strictly increasing. Minimize the number of colors used.
- **Core Insight**: Greedy maintenance of chain tail values: process elements left-to-right. For element A_i, to extend an existing increasing chain, we want to find an existing chain whose tail value is STRICTLY LESS than A_i. To be greedy, pick the largest such tail value < A_i! If no such chain exists, start a new chain with tail A_i. Store tail values in std::multiset or sorted vector.
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    multiset<int> tails;

    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;

        auto it = tails.lower_bound(a);
        if (it != tails.begin()) {
            --it;
            tails.erase(it);
        }
        tails.insert(a);
    }

    cout << tails.size() << "\n";
    return 0;
}
```
