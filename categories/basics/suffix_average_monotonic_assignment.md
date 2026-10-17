# Convex Monotonic Variable Assignment via Suffix Average Efficiency

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Convex Monotonic Variable Assignment via Suffix Average Efficiency**.

---

## Curated Problems

### `[problem:AtCoder-arc128_c]` — Max Dot
- **Rating / Difficulty**: 1810
- **Contest**: `arc128`
- **Analysis**: [`analysis/AtCoder-arc128_c.md`](../../analysis/AtCoder-arc128_c.md)
- **Key Idea**: By difference transformation y_i = x_i - x_{i - 1} >= 0, the sum condition becomes sum (N - i + 1) y_i = S, and the objective becomes sum (sum_{j=i}^N A_j) y_i. The marginal efficiency of variable y_i is the suffix average sum_{j=i}^N A_j / (N - i + 1).
- **Time Complexity**: `O(N^2) or O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long M, S;
    if (!(cin >> n >> M >> S)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> suf(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        suf[i] = suf[i + 1] + a[i];
    }

    double max_ans = 0.0;

    for (int k = 1; k <= n; ++k) {
        if ((long long)k * M >= S) {
            double avg = (double)S / k;
            double score = suf[n - k] * avg;
            max_ans = max(max_ans, score);
        } else {
            long long rem_s = S - (long long)k * M;
            double base_score = suf[n - k] * (double)M;

            for (int j = 1; j <= n - k; ++j) {
                if ((long long)j * M >= rem_s) {
                    double avg = (double)rem_s / j;
                    double score = base_score + (suf[n - k - j] - suf[n - k]) * avg;
                    max_ans = max(max_ans, score);
                }
            }
        }
    }

    cout << fixed << setprecision(12) << max_ans << "\n";
    return 0;
}
```
