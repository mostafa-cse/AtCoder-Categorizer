# DP over Amidakuji Horizontal Bars via Non-Adjacent Bitmasks

**Domain**: `Dynamic Programming`  
**Subtopic**: `Bitmask DP`  

This workbook contains curated, high-quality competitive programming problems teaching **DP over Amidakuji Horizontal Bars via Non-Adjacent Bitmasks**.

---

## Curated Problems

### `[problem:AtCoder-abc113_d]` — Number of Amidakuji
- **Rating / Difficulty**: 1597
- **Contest**: `abc113`
- **Analysis**: [`analysis/AtCoder-abc113_d.md`](../../analysis/AtCoder-abc113_d.md)
- **Key Idea**: Each horizontal level corresponds to a bitmask of length W - 1 representing where rungs are placed. A mask is valid iff (mask & (mask << 1)) == 0. A rung at bit c swaps line c and c + 1.
- **Time Complexity**: `O(H * 2^(W-1) * W)`
- **Space Complexity**: `O(W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, k;
    if (!(cin >> h >> w >> k)) return 0;

    // Line k is 1-indexed; convert to 0-indexed
    k--;

    // Precompute valid masks of width w - 1
    int total_masks = 1 << (w - 1);
    vector<int> valid_masks;
    for (int mask = 0; mask < total_masks; ++mask) {
        if (!(mask & (mask << 1))) {
            valid_masks.push_back(mask);
        }
    }

    vector<long long> dp(w, 0);
    dp[0] = 1;

    for (int step = 0; step < h; ++step) {
        vector<long long> next_dp(w, 0);
        for (int mask : valid_masks) {
            for (int col = 0; col < w; ++col) {
                if (!dp[col]) continue;

                int dest = col;
                if (col > 0 && (mask & (1 << (col - 1)))) {
                    dest = col - 1;
                } else if (col < w - 1 && (mask & (1 << col))) {
                    dest = col + 1;
                }

                next_dp[dest] = (next_dp[dest] + dp[col]) % MOD;
            }
        }
        dp = move(next_dp);
    }

    cout << dp[k] << "\n";
    return 0;
}
```
