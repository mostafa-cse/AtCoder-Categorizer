# Difference Array

**Domain**: `Basics`  
**Subtopic**: `More Techniques`  

This workbook contains curated, high-quality competitive programming problems teaching **Difference Array**.

---

## Curated Problems

### `[problem:AtCoder-arc077_c]` — guruguru
- **Rating / Difficulty**: 2117
- **Contest**: `arc077`
- **Analysis**: [`analysis/AtCoder-arc077_c.md`](../../analysis/AtCoder-arc077_c.md)
- **Key Idea**: For a transition from u to v of distance d = (v - u + M) mod M, setting the favorite button to x saves presses if x lies on the forward arc: savings start at 0 at u+1, increase with slope +1 up to v (where savings = d - 1), then drop to 0 at v+1. Because the savings function is piecewise linear, we can use second-order difference arrays (slope changes) to add the piecewise linear functions from all transitions in O(1) each, then integrate twice to find the maximum savings.
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long base_cost = 0;
    vector<long long> d2(2 * m + 5, 0);

    for (int i = 0; i < n - 1; ++i) {
        int from = a[i];
        int to = a[i + 1];
        long long dist = (to - from + m) % m;
        base_cost += dist;

        if (dist > 1) {
            int l = from + 2;
            int r = from + dist;
            d2[l] += 1;
            d2[r + 1] -= (dist);
            d2[r + 2] += (dist - 1);
        }
    }

    vector<long long> slope(2 * m + 5, 0);
    vector<long long> savings_extended(2 * m + 5, 0);

    long long cur_slope = 0;
    long long cur_savings = 0;
    for (int x = 1; x <= 2 * m; ++x) {
        cur_slope += d2[x];
        slope[x] = cur_slope;
        cur_savings += cur_slope;
        savings_extended[x] = cur_savings;
    }

    vector<long long> savings(m + 1, 0);
    for (int x = 1; x <= 2 * m; ++x) {
        int actual_x = (x - 1) % m + 1;
        savings[actual_x] += savings_extended[x];
    }

    long long max_savings = 0;
    for (int x = 1; x <= m; ++x) {
        max_savings = max(max_savings, savings[x]);
    }

    cout << base_cost - max_savings << "\n";
    return 0;
}
```
