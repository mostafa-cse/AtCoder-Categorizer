# Prefix-Suffix Parity Split with Binary Search Insertion

**Domain**: `Data Structures`  
**Subtopic**: `Prefix & Suffix Arrays`  

This workbook contains curated, high-quality competitive programming problems teaching **Prefix-Suffix Parity Split with Binary Search Insertion**.

---

## Curated Problems

### [problem:AtCoder-abc181_e] — Transformable Teacher
- **Contest**: `abc181`
- **Rating / Difficulty**: 1193
- **Specific Skill**: Prefix-Suffix Parity Split with Binary Search Insertion
- **Individual Analysis**: [`../../analysis/AtCoder-abc181_e.md`](../../analysis/AtCoder-abc181_e.md)
- **Problem Statement Summary**: N students with heights H_1..H_N (N is odd). M transformation forms for teacher with heights W_1..W_M. Pair up all students and 1 teacher into (N+1)/2 pairs. Minimize the sum of absolute differences across pairs.
- **Core Insight**: If teacher pairs with student at even index i (0-indexed): elements before i pair as (H_0, H_1), (H_2, H_3)...; elements after i pair as (H_{i+1}, H_{i+2}), (H_{i+3}, H_{i+4})... Precompute prefix pair differences pref[i] and suffix pair differences suff[i]. For any teacher height W, find insertion point i via std::lower_bound in O(log N) and query pref + |H_i - W| + suff in O(1).
- **Complexity**: Time: `O(N log N + M log N)` | Space: `O(N)`
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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) {
        cin >> h[i];
    }
    sort(h.begin(), h.end());

    vector<long long> pref(n, 0);
    for (int i = 2; i < n; i += 2) {
        pref[i] = pref[i - 2] + (h[i - 1] - h[i - 2]);
    }

    vector<long long> suff(n, 0);
    for (int i = n - 3; i >= 0; i -= 2) {
        suff[i] = suff[i + 2] + (h[i + 2] - h[i + 1]);
    }

    long long min_diff = 4e18;

    for (int j = 0; j < m; ++j) {
        long long w;
        cin >> w;

        int pos = lower_bound(h.begin(), h.end(), w) - h.begin();
        if (pos % 2 == 1) pos--; // pair with even index

        long long cur = pref[pos] + abs(h[pos] - w) + suff[pos];
        min_diff = min(min_diff, cur);
    }

    cout << min_diff << "\n";
    return 0;
}
```
