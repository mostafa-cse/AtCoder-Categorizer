# Binary Search

**Domain**: `Basics`  
**Subtopic**: `Leveraging Monotonicity`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search**.

---

## Curated Problems

### `[problem:AtCoder-abc229_g]` — Longest Y
- **Rating / Difficulty**: 2121
- **Contest**: `abc229`
- **Analysis**: [`analysis/AtCoder-abc229_g.md`](../../analysis/AtCoder-abc229_g.md)
- **Key Idea**: Let the original indices of 'Y' be P_0 < P_1 < ... < P_{M-1}. Bringing a window of elements P[l..r] into a contiguous block requires cost sum_{i=l}^r |P_i - (center + i - mid)|. Setting Q_i = P_i - i transforms this into the classic 1D facility location problem: minimizing sum_{i=l}^r |Q_i - Q_{mid}|, where mid = (l + r) / 2. Using prefix sums of Q, the minimum swap cost for any window [l, r] can be evaluated in O(1). We binary search the maximum window length len in [1, M].
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    long long k;
    if (!(cin >> s >> k)) return 0;

    vector<long long> q;
    for (int i = 0; i < (int)s.size(); ++i) {
        if (s[i] == 'Y') {
            q.push_back(i - (int)q.size());
        }
    }

    int m = q.size();
    if (m == 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> pref(m + 1, 0);
    for (int i = 0; i < m; ++i) {
        pref[i + 1] = pref[i] + q[i];
    }

    auto get_cost = [&](int l, int r) {
        int mid = (l + r) / 2;
        long long median = q[mid];
        long long left_cost = 1LL * (mid - l + 1) * median - (pref[mid + 1] - pref[l]);
        long long right_cost = (pref[r + 1] - pref[mid + 1]) - 1LL * (r - mid) * median;
        return left_cost + right_cost;
    };

    int low = 1, high = m, ans = 1;
    while (low <= high) {
        int len = (low + high) / 2;
        bool ok = false;
        for (int i = 0; i + len - 1 < m; ++i) {
            if (get_cost(i, i + len - 1) <= k) {
                ok = true;
                break;
            }
        }
        if (ok) {
            ans = len;
            low = len + 1;
        } else {
            high = len - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
