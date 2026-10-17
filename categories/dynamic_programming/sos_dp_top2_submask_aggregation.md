# Sum Over Subsets DP (SOS DP)

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Bit Related DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Sum Over Subsets DP (SOS DP)**.

---

## Curated Problems

### `[problem:AtCoder-arc100_c]` — Or Plus Max
- **Rating / Difficulty**: 2111
- **Contest**: `arc100`
- **Analysis**: [`analysis/AtCoder-arc100_c.md`](../../analysis/AtCoder-arc100_c.md)
- **Key Idea**: The condition (u OR v) <= K is relaxed to considering all subsets where u and v are submasks of mask, which ensures (u OR v) is a submask of mask. For any bitmask, the maximum pair sum is obtained by the top two largest elements among all submasks! We use SOS DP (Fast Zeta Transform) to compute the pair (max1, max2) for every mask in O(N * 2^N). Then, answer for K is the prefix maximum of (max1 + max2) for all masks <= K.
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(2^N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Top2 {
    int max1, max2;
    void update(int val) {
        if (val > max1) {
            max2 = max1;
            max1 = val;
        } else if (val > max2) {
            max2 = val;
        }
    }
};

Top2 merge(const Top2& a, const Top2& b) {
    Top2 res = a;
    res.update(b.max1);
    res.update(b.max2);
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total = 1 << n;
    vector<Top2> dp(total, {-1, -1});
    for (int i = 0; i < total; ++i) {
        int a;
        cin >> a;
        dp[i].max1 = a;
    }

    for (int j = 0; j < n; ++j) {
        for (int mask = 0; mask < total; ++mask) {
            if ((mask >> j) & 1) {
                dp[mask] = merge(dp[mask], dp[mask ^ (1 << j)]);
            }
        }
    }

    int cur_max = 0;
    for (int k = 1; k < total; ++k) {
        cur_max = max(cur_max, dp[k].max1 + dp[k].max2);
        cout << cur_max << "\n";
    }

    return 0;
}
```
