# Dual Partition Subset Sum via Bitset Optimization

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Dual Partition Subset Sum via Bitset Optimization**.

---

## Curated Problems

### [problem:AtCoder-abc204_d] — Cooking
- **Contest**: `abc204`
- **Rating / Difficulty**: 832
- **Specific Skill**: Dual Partition Subset Sum via Bitset Optimization
- **Individual Analysis**: [`../../analysis/AtCoder-abc204_d.md`](../../analysis/AtCoder-abc204_d.md)
- **Problem Statement Summary**: N dishes with cooking times T_1, ..., T_N are cooked using 2 identical ovens (N <= 100, sum T_i <= 10^5). Each oven bakes one dish at a time. Minimize the time until all dishes are finished.
- **Core Insight**: This is 0-1 Subset Sum Knapsack. Because sum(T) <= 10^5 and N <= 100, std::bitset<100005> enables ultra-fast O(N * sum(T) / 64) DP transitions: dp |= (dp << t).
- **Complexity**: Time: `O(N * sum(T) / 64)` | Space: `O(sum(T) / 64)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <bitset>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> t(n);
    int total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> t[i];
        total += t[i];
    }

    bitset<100005> dp;
    dp[0] = 1;

    for (int x : t) {
        dp |= (dp << x);
    }

    int target = (total + 1) / 2;
    for (int s = target; s <= total; ++s) {
        if (dp[s]) {
            cout << s << "\n";
            return 0;
        }
    }

    cout << total << "\n";
    return 0;
}
```
