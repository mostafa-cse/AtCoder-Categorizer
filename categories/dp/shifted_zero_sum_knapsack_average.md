# Subset Average Equals A via Shifted Zero-Sum Knapsack DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Subset Average Equals A via Shifted Zero-Sum Knapsack DP**.

---

## Curated Problems

### `[problem:AtCoder-arc060_a]` — Tak and Cards
- **Rating / Difficulty**: 1583
- **Contest**: `abc044`
- **Analysis**: [`analysis/AtCoder-arc060_a.md`](../../analysis/AtCoder-arc060_a.md)
- **Key Idea**: The average of a subset equals A iff sum_{i in S} x_i = |S| * A iff sum_{i in S} (x_i - A) = 0. Shift each card value by -A: y_i = x_i - A. The problem becomes counting non-empty subsets with sum = 0.
- **Time Complexity**: `O(N^2 * max(X))`
- **Space Complexity**: `O(N * max(X))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int OFFSET = 2500;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a;
    if (!(cin >> n >> a)) return 0;

    vector<long long> dp(2 * OFFSET + 1, 0);
    dp[OFFSET] = 1;

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        int y = x - a;
        vector<long long> next_dp = dp;

        for (int s = 0; s <= 2 * OFFSET; ++s) {
            if (dp[s] > 0) {
                int ns = s + y;
                if (ns >= 0 && ns <= 2 * OFFSET) {
                    next_dp[ns] += dp[s];
                }
            }
        }
        dp = move(next_dp);
    }

    cout << dp[OFFSET] - 1 << "\n";
    return 0;
}
```
