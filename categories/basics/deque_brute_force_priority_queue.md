# Double-Ended Queue Brute Force Insertion/Deletion with Priority Queue

**Domain**: `Basics`  
**Subtopic**: `Complete Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Double-Ended Queue Brute Force Insertion/Deletion with Priority Queue**.

---

## Curated Problems

### [problem:AtCoder-abc128_d] — equeue
- **Contest**: `abc128`
- **Rating / Difficulty**: 1354
- **Specific Skill**: Double-Ended Queue Brute Force Insertion/Deletion with Priority Queue
- **Individual Analysis**: [`../../analysis/AtCoder-abc128_d.md`](../../analysis/AtCoder-abc128_d.md)
- **Problem Statement Summary**: N jewels in a row (values V_1..V_N, can be negative). You can perform K operations: pull from left, pull from right, or put a jewel back into the row. Maximize jewel value in hand.
- **Core Insight**: Because N <= 50 and K <= 100, we can iterate over all choices of A and B with A + B <= min(N, K). Collect all jewels pulled into a list, sort them ascending, and discard the most negative jewels up to min(A + B, K - (A + B)).
- **Complexity**: Time: `O(N^2 * N log N) <= 50^3 * 6 = 7.5 * 10^5 operations` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }

    long long max_sum = 0;

    for (int a = 0; a <= min(n, k); ++a) {
        for (int b = 0; a + b <= min(n, k); ++b) {
            vector<long long> pulled;
            for (int i = 0; i < a; ++i) pulled.push_back(v[i]);
            for (int i = 0; i < b; ++i) pulled.push_back(v[n - 1 - i]);

            sort(pulled.begin(), pulled.end());

            int drop_budget = k - (a + b);
            long long current_sum = 0;

            for (size_t i = 0; i < pulled.size(); ++i) {
                if (pulled[i] < 0 && drop_budget > 0) {
                    drop_budget--;
                } else {
                    current_sum += pulled[i];
                }
            }

            max_sum = max(max_sum, current_sum);
        }
    }

    cout << max_sum << "\n";
    return 0;
}
```
