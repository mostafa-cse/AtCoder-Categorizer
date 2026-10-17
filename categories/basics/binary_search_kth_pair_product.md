# Binary Search on K-th Pair Product with Sign-Partitioned Two Pointers

**Domain**: `Basics`  
**Subtopic**: `Binary Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on K-th Pair Product with Sign-Partitioned Two Pointers**.

---

## Curated Problems

### `[problem:AtCoder-abc155_d]` — Pairs
- **Rating / Difficulty**: 1845
- **Contest**: `abc155`
- **Analysis**: [`analysis/AtCoder-abc155_d.md`](../../analysis/AtCoder-abc155_d.md)
- **Key Idea**: Binary search on product value P in [-10^{18}, 10^{18}]. To count pairs with A_i * A_j <= P, split array into negative, zero, and positive elements, and count valid pairs in O(N) using two pointers.
- **Time Complexity**: `O(N log(max_val) * log N)`
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
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    auto count_le = [&](long long x) -> long long {
        long long total = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] > 0) {
                int l = i + 1, r = n - 1, pos = i;
                while (l <= r) {
                    int mid = l + (r - l) / 2;
                    if (a[i] * a[mid] <= x) {
                        pos = mid;
                        l = mid + 1;
                    } else {
                        r = mid - 1;
                    }
                }
                total += (pos - i);
            } else if (a[i] < 0) {
                int l = i + 1, r = n - 1, pos = n;
                while (l <= r) {
                    int mid = l + (r - l) / 2;
                    if (a[i] * a[mid] <= x) {
                        pos = mid;
                        r = mid - 1;
                    } else {
                        l = mid + 1;
                    }
                }
                total += (n - pos);
            } else {
                if (x >= 0) {
                    total += (n - 1 - i);
                }
            }
        }
        return total;
    };

    long long low = -1e18, high = 1e18, ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_le(mid) >= k) {
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
