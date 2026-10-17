# Min Sum of Pairwise Differences on Intervals via Median Pairing

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Min Sum of Pairwise Differences on Intervals via Median Pairing**.

---

## Curated Problems

### `[problem:AtCoder-arc147_c]` — Min Diff Sum
- **Rating / Difficulty**: 1704
- **Contest**: `arc147`
- **Analysis**: [`analysis/AtCoder-arc147_c.md`](../../analysis/AtCoder-arc147_c.md)
- **Key Idea**: For sorted coordinates x_1 <= x_2 <= ... <= x_N, the sum of differences can be decomposed into sum_{k=1}^{floor(N/2)} (N - 2k + 1) * (x_{N - k + 1} - x_k). To minimize this, pair the largest L_i with the smallest R_j greedily.
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

    vector<long long> L(n), R(n);
    for (int i = 0; i < n; ++i) {
        cin >> L[i] >> R[i];
    }

    sort(L.rbegin(), L.rend());
    sort(R.begin(), R.end());

    long long ans = 0;
    for (int k = 0; k < n / 2; ++k) {
        long long weight = n - 1 - 2LL * k;
        if (L[k] > R[k]) {
            ans += weight * (L[k] - R[k]);
        }
    }

    cout << ans << "\n";
    return 0;
}
```
