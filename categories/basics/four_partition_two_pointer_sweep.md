# 4-Partition Array Optimization via Monotonic Two-Pointer Sweep

**Domain**: `Basics`  
**Subtopic**: `Two Pointers`  

This workbook contains curated, high-quality competitive programming problems teaching **4-Partition Array Optimization via Monotonic Two-Pointer Sweep**.

---

## Curated Problems

### `[problem:AtCoder-arc100_b]` — Equal Cut
- **Rating / Difficulty**: 1801
- **Contest**: `abc102`
- **Analysis**: [`analysis/AtCoder-arc100_b.md`](../../analysis/AtCoder-arc100_b.md)
- **Key Idea**: Fix the middle cut m in [2, N - 2]. The left half A[1..m] needs to be cut into two parts (P, Q) to minimize |P - Q|, and the right half A[m+1..N] into (R, S) to minimize |R - S|. Because prefix sums are strictly increasing, as m advances, the optimal left cut l and optimal right cut r both move monotonically forward.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    vector<long long> pref(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        pref[i] = pref[i - 1] + a[i];
    }

    int l = 1, r = 3;
    long long min_diff = 4e18;

    for (int m = 2; m <= n - 2; ++m) {
        while (l + 1 < m && abs((pref[m] - pref[l + 1]) - pref[l + 1]) <= abs((pref[m] - pref[l]) - pref[l])) {
            l++;
        }
        while (r + 1 < n && abs((pref[n] - pref[r + 1]) - (pref[r + 1] - pref[m])) <= abs((pref[n] - pref[r]) - (pref[r] - pref[m]))) {
            r++;
        }

        long long P = pref[l];
        long long Q = pref[m] - pref[l];
        long long R = pref[r] - pref[m];
        long long S = pref[n] - pref[r];

        long long mx = max({P, Q, R, S});
        long long mn = min({P, Q, R, S});
        min_diff = min(min_diff, mx - mn);
    }

    cout << min_diff << "\n";
    return 0;
}
```
