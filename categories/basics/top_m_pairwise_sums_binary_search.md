# Top-M Pairwise Sums via Threshold Binary Search and Prefix Accumulation

**Domain**: `Basics`  
**Subtopic**: `Binary Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Top-M Pairwise Sums via Threshold Binary Search and Prefix Accumulation**.

---

## Curated Problems

### `[problem:AtCoder-abc149_e]` — Handshake
- **Rating / Difficulty**: 1905
- **Contest**: `abc149`
- **Analysis**: [`analysis/AtCoder-abc149_e.md`](../../analysis/AtCoder-abc149_e.md)
- **Key Idea**: Binary search on the minimum pair sum threshold S such that at least M pairs have A_i + A_j >= S. For sorted array A, counting pairs with A_i + A_j >= S takes O(N) using two pointers/lower_bound. After finding the maximal S, sum all pairs with sum > S using prefix sums of A, and fill the remaining M - count(S + 1) pairs with exact value S.
- **Time Complexity**: `O(N log(max A))`
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
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    vector<long long> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + a[i];
    }

    auto count_pairs = [&](long long mid) -> long long {
        long long cnt = 0;
        for (int i = 0; i < n; ++i) {
            long long req = mid - a[i];
            int idx = lower_bound(a.begin(), a.end(), req) - a.begin();
            cnt += (n - idx);
        }
        return cnt;
    };

    long long low = 0, high = 2000000;
    long long best_mid = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_pairs(mid) >= m) {
            best_mid = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    long long total_sum = 0;
    long long total_pairs = 0;
    for (int i = 0; i < n; ++i) {
        long long req = best_mid + 1 - a[i];
        int idx = lower_bound(a.begin(), a.end(), req) - a.begin();
        long long count = n - idx;
        if (count > 0) {
            total_sum += a[i] * count + (pref[n] - pref[idx]);
            total_pairs += count;
        }
    }

    total_sum += (m - total_pairs) * best_mid;
    cout << total_sum << "\n";
    return 0;
}
```
