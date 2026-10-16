# Dual Binary Search on Two Sorted Arrays (Shrines & Temples)

**Domain**: `Basics`  
**Subtopic**: `Binary Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Dual Binary Search on Two Sorted Arrays (Shrines & Temples)**.

---

## Curated Problems

### [problem:AtCoder-abc119_d] — Lazy Faith
- **Contest**: `abc119`
- **Rating / Difficulty**: 1346
- **Specific Skill**: Dual Binary Search on Two Sorted Arrays (Shrines & Temples)
- **Individual Analysis**: [`../../analysis/AtCoder-abc119_d.md`](../../analysis/AtCoder-abc119_d.md)
- **Problem Statement Summary**: A line with A shrines at s_1 < ... < s_A and B temples at t_1 < ... < t_B. Q queries: start at x_i, visit at least 1 shrine and 1 temple. Find the minimum distance traveled.
- **Core Insight**: Using std::lower_bound in s and t, we find the 2 closest shrines and 2 closest temples, producing at most 2 x 2 = 4 candidate pairs (S, T). For a pair (S, T), distance from x is: min(abs(x - S), abs(x - T)) + abs(S - T). We test all 4 combinations in O(1)!
- **Complexity**: Time: `O((A + B + Q) log(A + B))` | Space: `O(A + B)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, q;
    if (!(cin >> a >> b >> q)) return 0;

    vector<long long> s(a + 2), t(b + 2);
    s[0] = -INF; s[a + 1] = INF;
    t[0] = -INF; t[b + 1] = INF;

    for (int i = 1; i <= a; ++i) cin >> s[i];
    for (int i = 1; i <= b; ++i) cin >> t[i];

    while (q--) {
        long long x;
        cin >> x;

        auto it_s = lower_bound(s.begin(), s.end(), x);
        long long s_r = *it_s;
        long long s_l = *(it_s - 1);

        auto it_t = lower_bound(t.begin(), t.end(), x);
        long long t_r = *it_t;
        long long t_l = *(it_t - 1);

        long long ans = INF;
        for (long long S : {s_l, s_r}) {
            for (long long T : {t_l, t_r}) {
                long long d = min(abs(x - S), abs(x - T)) + abs(S - T);
                ans = min(ans, d);
            }
        }

        cout << ans << "\n";
    }

    return 0;
}
```
