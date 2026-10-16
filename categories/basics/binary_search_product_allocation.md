# Monotonic Binary Search on Multiplicative Work Allocation

**Domain**: `Basics`  
**Subtopic**: `Binary Search on Answer`  

This workbook contains curated, high-quality competitive programming problems teaching **Monotonic Binary Search on Multiplicative Work Allocation**.

---

## Curated Problems

### `[problem:AtCoder-abc144_e]` — Gluttony
- **Rating / Difficulty**: 1449
- **Contest**: `abc144`
- **Analysis**: [`analysis/AtCoder-abc144_e.md`](../../analysis/AtCoder-abc144_e.md)
- **Key Idea**: Rearrangement inequality dictates pairing smallest A_i with largest F_i. Then binary search on the minimum achievable maximum product X.
- **Time Complexity**: `O(N log(max(A * F)))`
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

    vector<long long> a(n), f(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> f[i];

    sort(a.begin(), a.end());
    sort(f.rbegin(), f.rend());

    long long low = 0, high = 1e12;
    long long ans = high;

    auto check = [&](long long x) -> bool {
        long long ops = 0;
        for (int i = 0; i < n; ++i) {
            long long target_a = x / f[i];
            if (a[i] > target_a) {
                ops += (a[i] - target_a);
                if (ops > k) return false;
            }
        }
        return ops <= k;
    };

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
