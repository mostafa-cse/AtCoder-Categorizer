# 2D Rectilinear Area Decomposition into 1D Coordinate Gaps

**Domain**: `Math`  
**Subtopic**: `Combinatorics`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Rectilinear Area Decomposition into 1D Coordinate Gaps**.

---

## Curated Problems

### `[problem:AtCoder-arc071_b]` — ###
- **Rating / Difficulty**: 1641
- **Contest**: `abc058`
- **Analysis**: [`analysis/AtCoder-arc071_b.md`](../../analysis/AtCoder-arc071_b.md)
- **Key Idea**: The area of a rectangle formed by (x_i, x_j) and (y_k, y_l) is (x_j - x_i) * (y_l - y_k). The sum over all pairs decomposes into (sum_{i < j} (x_j - x_i)) * (sum_{k < l} (y_l - y_k)).
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> x(n), y(m);
    for (int i = 0; i < n; ++i) cin >> x[i];
    for (int j = 0; j < m; ++j) cin >> y[j];

    long long sum_x = 0;
    for (int i = 0; i < n - 1; ++i) {
        long long delta = (x[i + 1] - x[i]) % MOD;
        long long count = 1LL * (i + 1) * (n - 1 - i) % MOD;
        sum_x = (sum_x + delta * count) % MOD;
    }

    long long sum_y = 0;
    for (int j = 0; j < m - 1; ++j) {
        long long delta = (y[j + 1] - y[j]) % MOD;
        long long count = 1LL * (j + 1) * (m - 1 - j) % MOD;
        sum_y = (sum_y + delta * count) % MOD;
    }

    long long total = (sum_x * sum_y) % MOD;
    cout << total << "\n";
    return 0;
}
```
