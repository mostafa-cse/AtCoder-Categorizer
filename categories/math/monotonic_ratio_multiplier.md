# Monotonic Ratio Ceiling Multiplier

**Domain**: `Math`  
**Subtopic**: `Greedy Multipliers`  

This workbook contains curated, high-quality competitive programming problems teaching **Monotonic Ratio Ceiling Multiplier**.

---

## Curated Problems

### [problem:AtCoder-arc062_a] — AtCoDeer and Election Report
- **Contest**: `abc046`
- **Rating / Difficulty**: 1346
- **Specific Skill**: Monotonic Ratio Ceiling Multiplier
- **Individual Analysis**: [`../../analysis/AtCoder-arc062_a.md`](../../analysis/AtCoder-arc062_a.md)
- **Problem Statement Summary**: Two candidates with vote ratios T_i : A_i reported N times. Current votes never decrease: cur_T >= prev_T and cur_A >= prev_A. At step i, votes must be in ratio T_i : A_i (i.e. cur_T = k * T_i, cur_A = k * A_i for some integer k >= 1). Minimize final total votes cur_T + cur_A.
- **Core Insight**: To satisfy both inequalities simultaneously, k must satisfy: k >= ceil(cur_T / T_i) = (cur_T + T_i - 1) / T_i, and k >= ceil(cur_A / A_i) = (cur_A + A_i - 1) / A_i. Setting k = max((cur_T + T_i - 1) / T_i, (cur_A + A_i - 1) / A_i) greedily minimizes votes at each step.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long cur_t, cur_a;
    cin >> cur_t >> cur_a;

    for (int i = 1; i < n; ++i) {
        long long t, a;
        cin >> t >> a;

        long long kt = (cur_t + t - 1) / t;
        long long ka = (cur_a + a - 1) / a;
        long long k = max(kt, ka);

        cur_t = k * t;
        cur_a = k * a;
    }

    cout << cur_t + cur_a << "\n";
    return 0;
}
```
