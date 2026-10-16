# Stock Buy-Low Sell-High Count of Max Profit Pairs

**Domain**: `Basics`  
**Subtopic**: `Prefix Minima`  

This workbook contains curated, high-quality competitive programming problems teaching **Stock Buy-Low Sell-High Count of Max Profit Pairs**.

---

## Curated Problems

### [problem:AtCoder-arc063_b] — An Invisible Hand
- **Contest**: `abc047`
- **Rating / Difficulty**: 1376
- **Specific Skill**: Stock Buy-Low Sell-High Count of Max Profit Pairs
- **Individual Analysis**: [`../../analysis/AtCoder-arc063_b.md`](../../analysis/AtCoder-arc063_b.md)
- **Problem Statement Summary**: Given prices A_1..A_N in N cities. You can buy 1 apple at town i and sell at town j (j > i) to make profit A_j - A_i. Find the minimum number of town prices to change to reduce the maximum achievable profit.
- **Core Insight**: Maintain running minimum min_val as we scan j from 1 to N. The maximum profit ending at j is A_j - min_val. Count how many indices j achieve A_j - min_val == max_diff. Changing the price of town j disrupts this pair. Because the sell towns j for distinct maximal pairs cannot be simultaneously satisfied by a single alteration without changing their sell price, the answer is exactly the count of indices j achieving maximum profit!
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
    long long t;
    if (!(cin >> n >> t)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long min_val = a[0];
    long long max_profit = 0;

    for (int i = 1; i < n; ++i) {
        max_profit = max(max_profit, a[i] - min_val);
        min_val = min(min_val, a[i]);
    }

    min_val = a[0];
    int count = 0;
    for (int i = 1; i < n; ++i) {
        if (a[i] - min_val == max_profit) {
            count++;
        }
        min_val = min(min_val, a[i]);
    }

    cout << count << "\n";
    return 0;
}
```
