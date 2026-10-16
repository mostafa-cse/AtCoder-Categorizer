# Binary Search on Answer with Capped Work Allocations min(A_i, P)

**Domain**: `Basics`  
**Subtopic**: `Binary Search on Answer`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Answer with Capped Work Allocations min(A_i, P)**.

---

## Curated Problems

### `[problem:AtCoder-abc227_d]` — Project Planning
- **Rating / Difficulty**: 1643
- **Contest**: `abc227`
- **Analysis**: [`analysis/AtCoder-abc227_d.md`](../../analysis/AtCoder-abc227_d.md)
- **Key Idea**: Binary search on the total number of projects P. Department i can contribute at most 1 employee per project, so it contributes at most min(A_i, P) employees. Forming P projects is feasible iff sum_{i=1}^N min(A_i, P) >= K * P.
- **Time Complexity**: `O(N log(sum A))`
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
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long sum_a = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        sum_a += a[i];
    }

    long long low = 1, high = sum_a / k;
    long long ans = 0;

    auto check = [&](long long p) -> bool {
        long long total = 0;
        for (int i = 0; i < n; ++i) {
            total += min(a[i], p);
        }
        return total >= (__int128)k * p;
    };

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
