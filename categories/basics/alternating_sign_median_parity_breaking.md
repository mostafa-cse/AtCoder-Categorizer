# Alternating Sign Invariant and Median Parity Breaking Search

**Domain**: `Basics`  
**Subtopic**: `Greedy / Two Pointers`  

This workbook contains curated, high-quality competitive programming problems teaching **Alternating Sign Invariant and Median Parity Breaking Search**.

---

## Curated Problems

### `[problem:AtCoder-arc173_c]` — Not Median
- **Rating / Difficulty**: 2008
- **Contest**: `arc173`
- **Analysis**: [`analysis/AtCoder-arc173_c.md`](../../analysis/AtCoder-arc173_c.md)
- **Key Idea**: For i = 1 and i = N, we can directly scan the adjacent prefix/suffix in O(N). For 2 <= i <= N - 1, if sgn(P_{i-1} - P_i) == sgn(P_{i+1} - P_i), the 3-element window [i-1, i+1] already has P_i not as median, so ans = 3. Otherwise, relative to P_i, signs strictly alternate. Let R be the smallest j > i where adjacent signs match, and L be the largest j < i where adjacent signs match. Inside [L, R], P_i is always the median. The shortest interval where P_i fails to be median must extend past L or past R, achievable with length 2 * (i - (L - 1)) + 1 (or 2 * (R + 1 - i) + 1). The naive search for L and R takes O(N) total across all such i.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int sgn(int x) {
    return (x > 0) - (x < 0);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
    }

    vector<int> ans(n + 1, -1);

    auto check_window = [&](int l, int r, int target_val) {
        int sum_sgn = 0;
        for (int j = l; j <= r; ++j) {
            sum_sgn += sgn(p[j] - target_val);
        }
        return sum_sgn != 0;
    };

    // Endpoints i = 1 and i = n
    for (int i : {1, n}) {
        for (int len = 3; len <= n; len += 2) {
            int l = (i == 1 ? 1 : n - len + 1);
            int r = (i == 1 ? len : n);
            if (l >= 1 && r <= n && check_window(l, r, p[i])) {
                ans[i] = len;
                break;
            }
        }
    }

    // Interior points
    for (int i = 2; i <= n - 1; ++i) {
        if (sgn(p[i - 1] - p[i]) == sgn(p[i + 1] - p[i])) {
            ans[i] = 3;
            continue;
        }

        int cand = 1e9;

        // Search left for boundary
        int L = -1;
        for (int j = i - 1; j >= 2; --j) {
            if (sgn(p[j - 1] - p[i]) == sgn(p[j] - p[i])) {
                L = j;
                break;
            }
        }
        if (L != -1) {
            int l = L - 1;
            int r = ( (i - l + 1) % 2 != 0 ? i : i + 1 );
            if (r <= n) cand = min(cand, r - l + 1);
        }

        // Search right for boundary
        int R = -1;
        for (int j = i + 1; j <= n - 1; ++j) {
            if (sgn(p[j] - p[i]) == sgn(p[j + 1] - p[i])) {
                R = j;
                break;
            }
        }
        if (R != -1) {
            int r = R + 1;
            int l = ( (r - i + 1) % 2 != 0 ? i : i - 1 );
            if (l >= 1) cand = min(cand, r - l + 1);
        }

        if (cand < 1e9) ans[i] = cand;
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
