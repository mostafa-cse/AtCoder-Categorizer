# Dual Priority Queue Prefix/Suffix Optimization (3N Elements Partition)

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Priority Queue`  

This workbook contains curated, high-quality competitive programming problems teaching **Dual Priority Queue Prefix/Suffix Optimization (3N Elements Partition)**.

---

## Curated Problems

### `[problem:AtCoder-arc074_b]` — 3N Numbers
- **Rating / Difficulty**: 1730
- **Contest**: `abc062`
- **Analysis**: [`analysis/AtCoder-arc074_b.md`](../../analysis/AtCoder-arc074_b.md)
- **Key Idea**: The split between the first N elements and the last N elements must occur at some boundary index k between N and 2N. Precompute L[k] = max sum of N elements from A[1..k] using a min-heap, and R[k] = min sum of N elements from A[k..3N] using a max-heap.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_len = 3 * n;
    vector<long long> a(total_len + 1);
    for (int i = 1; i <= total_len; ++i) {
        cin >> a[i];
    }

    priority_queue<long long, vector<long long>, greater<long long>> min_pq;
    vector<long long> L(total_len + 1, 0);
    long long left_sum = 0;

    for (int i = 1; i <= total_len; ++i) {
        min_pq.push(a[i]);
        left_sum += a[i];
        if ((int)min_pq.size() > n) {
            left_sum -= min_pq.top();
            min_pq.pop();
        }
        if (i >= n) {
            L[i] = left_sum;
        }
    }

    priority_queue<long long> max_pq;
    vector<long long> R(total_len + 2, 0);
    long long right_sum = 0;

    for (int i = total_len; i >= 1; --i) {
        max_pq.push(a[i]);
        right_sum += a[i];
        if ((int)max_pq.size() > n) {
            right_sum -= max_pq.top();
            max_pq.pop();
        }
        if (i <= 2 * n + 1) {
            R[i] = right_sum;
        }
    }

    long long max_diff = -1e18;
    for (int k = n; k <= 2 * n; ++k) {
        max_diff = max(max_diff, L[k] - R[k + 1]);
    }

    cout << max_diff << "\n";
    return 0;
}
```
