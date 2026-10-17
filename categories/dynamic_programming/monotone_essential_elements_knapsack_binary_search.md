# Monotone Essential Elements via 0-1 Knapsack DP and Binary Search

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Monotone Essential Elements via 0-1 Knapsack DP and Binary Search**.

---

## Curated Problems

### `[problem:AtCoder-arc070_b]` — No Need
- **Rating / Difficulty**: 2015
- **Contest**: `abc056`
- **Analysis**: [`analysis/AtCoder-arc070_b.md`](../../analysis/AtCoder-arc070_b.md)
- **Key Idea**: An element a_i is needed iff there exists a subset of the OTHER elements with sum in [K - a_i, K - 1]. Monotonicity property: if a is sorted in ascending order, if a_i is not needed, then every a_j <= a_i is also not needed! Thus the set of not needed elements forms a prefix a_1, ..., a_m. We binary search on m. To test if a_m is needed, we run 0-1 knapsack on the other elements up to capacity K - 1 and check if any sum in [K - a_m, K - 1] is reachable in O(N K).
- **Time Complexity**: `O(N * K * log N)`
- **Space Complexity**: `O(K)`
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
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    auto is_needed = [&](int idx) {
        if (a[idx] >= k) return true;

        vector<bool> dp(k, false);
        dp[0] = true;

        for (int i = 0; i < n; ++i) {
            if (i == idx) continue;
            long long val = a[i];
            if (val >= k) continue;

            for (long long s = k - 1; s >= val; --s) {
                if (dp[s - val]) dp[s] = true;
            }
        }

        long long low_bound = max(0LL, k - a[idx]);
        for (long long s = low_bound; s < k; ++s) {
            if (dp[s]) return true;
        }
        return false;
    };

    int low = 0, high = n - 1, ans = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (!is_needed(mid)) {
            ans = mid + 1;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
