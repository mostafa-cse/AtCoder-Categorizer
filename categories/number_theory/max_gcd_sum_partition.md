# Maximum GCD of Sum Partition / Divisor Feasibility

**Domain**: `Number Theory`  
**Subtopic**: `Divisors & GCD`  

This workbook contains curated, high-quality competitive programming problems teaching **Maximum GCD of Sum Partition / Divisor Feasibility**.

---

## Curated Problems

### [problem:AtCoder-abc112_d] — Partition
- **Contest**: `abc112`
- **Rating / Difficulty**: 1025
- **Specific Skill**: Maximum GCD of Sum Partition / Divisor Feasibility
- **Individual Analysis**: [`../../analysis/AtCoder-abc112_d.md`](../../analysis/AtCoder-abc112_d.md)
- **Problem Statement Summary**: Find positive integers a_1, ..., a_N such that sum a_i = M and gcd(a_1, ..., a_N) is maximized (N <= 10^5, M <= 10^9).
- **Core Insight**: Since each a_i >= 1, we have k_i >= 1, so sum k_i >= N. Thus, for g to be achievable, we must have M / g >= N, which is equivalent to g <= M / N. We simply find the maximum divisor g of M that satisfies g <= M / N.
- **Complexity**: Time: `O(sqrt(M))` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m;
    if (!(cin >> n >> m)) return 0;

    long long max_g = 1;
    for (long long d = 1; d * d <= m; ++d) {
        if (m % d == 0) {
            if (d <= m / n) {
                max_g = max(max_g, d);
            }
            long long other = m / d;
            if (other <= m / n) {
                max_g = max(max_g, other);
            }
        }
    }

    cout << max_g << "\n";
    return 0;
}
```
