# Circular Segment Decomposition DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Circular Segment Decomposition DP**.

---

## Curated Problems

### `[problem:AtCoder-abc285_e]` — Work or Rest
- **Rating / Difficulty**: 1466
- **Contest**: `abc285`
- **Analysis**: [`analysis/AtCoder-abc285_e.md`](../../analysis/AtCoder-abc285_e.md)
- **Key Idea**: By rotational symmetry, fix day 1 as a rest day. The remaining days are partitioned into contiguous blocks of workdays between rest days. The productivity of a block of length L depends solely on L.
- **Time Complexity**: `O(N^2)`
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

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    // val[L]: productivity of L consecutive workdays between two rest days
    vector<long long> val(n + 1, 0);
    for (int L = 1; L <= n; ++L) {
        long long sum = 0;
        for (int k = 1; k <= L; ++k) {
            sum += a[min(k, L - k + 1)];
        }
        val[L] = sum;
    }

    vector<long long> dp(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            dp[i] = max(dp[i], dp[j] + val[i - j - 1]);
        }
    }

    cout << dp[n] << "\n";
    return 0;
}
```
