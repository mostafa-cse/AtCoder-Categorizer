# Bulk Simulation / Monotonic Invariant on Multi-Decrement Process

**Domain**: `Basics`  
**Subtopic**: `Simulation / Invariant`  

This workbook contains curated, high-quality competitive programming problems teaching **Bulk Simulation / Monotonic Invariant on Multi-Decrement Process**.

---

## Curated Problems

### `[problem:AtCoder-arc079_c]` — Decrease (Judge ver.)
- **Rating / Difficulty**: 1745
- **Contest**: `arc079`
- **Analysis**: [`analysis/AtCoder-arc079_c.md`](../../analysis/AtCoder-arc079_c.md)
- **Key Idea**: Each operation reduces the total sum of elements by 1. When multiple elements are >= N, we can simulate them in batches (bulk decrement) where each element i performs floor(A_i / N) operations simultaneously.
- **Time Complexity**: `O(rounds * N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long total_ops = 0;

    while (true) {
        bool finished = true;
        for (int i = 0; i < n; ++i) {
            if (a[i] >= n) {
                finished = false;
                break;
            }
        }
        if (finished) break;

        vector<long long> k(n, 0);
        long long batch_ops = 0;
        for (int i = 0; i < n; ++i) {
            k[i] = a[i] / n;
            batch_ops += k[i];
        }

        total_ops += batch_ops;

        for (int i = 0; i < n; ++i) {
            a[i] = a[i] - k[i] * n + (batch_ops - k[i]);
        }
    }

    cout << total_ops << "\n";
    return 0;
}
```
