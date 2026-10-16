# Prime Exponent Partitioning for Highly Composite Numbers

**Domain**: `Number Theory`  
**Subtopic**: `Divisor Counting`  

This workbook contains curated, high-quality competitive programming problems teaching **Prime Exponent Partitioning for Highly Composite Numbers**.

---

## Curated Problems

### [problem:AtCoder-abc114_d] — 756
- **Contest**: `abc114`
- **Rating / Difficulty**: 1337
- **Specific Skill**: Prime Exponent Partitioning for Highly Composite Numbers
- **Individual Analysis**: [`../../analysis/AtCoder-abc114_d.md`](../../analysis/AtCoder-abc114_d.md)
- **Problem Statement Summary**: Given N <= 100. Count the number of positive divisors of N! that have exactly 75 positive divisors.
- **Core Insight**: Factorizations of 75 into integers > 1: (1) 75 = (74 + 1) -> p^74; (2) 25 * 3 = (24 + 1)(2 + 1) -> p^24 * q^2; (3) 15 * 5 = (14 + 1)(4 + 1) -> p^14 * q^4; (4) 5 * 5 * 3 = (4 + 1)(4 + 1)(2 + 1) -> p^4 * q^4 * r^2. Compute prime factor exponents in N!, count primes with exponent >= 74, 24, 14, 4, 2, and apply inclusion/permutation counting.
- **Complexity**: Time: `O(N^2)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> exp(n + 1, 0);
    for (int i = 2; i <= n; ++i) {
        int temp = i;
        for (int p = 2; p <= n; ++p) {
            while (temp % p == 0) {
                exp[p]++;
                temp /= p;
            }
        }
    }

    auto count_at_least = [&](int k) {
        int cnt = 0;
        for (int p = 2; p <= n; ++p) {
            if (exp[p] >= k) cnt++;
        }
        return cnt;
    };

    long long ans = 0;

    // Case 1: p^74
    ans += count_at_least(74);

    // Case 2: p^24 * q^2
    ans += (long long)count_at_least(24) * (count_at_least(2) - 1);

    // Case 3: p^14 * q^4
    ans += (long long)count_at_least(14) * (count_at_least(4) - 1);

    // Case 4: p^4 * q^4 * r^2
    long long c4 = count_at_least(4);
    long long c2 = count_at_least(2);
    if (c4 >= 2 && c2 >= 3) {
        ans += (c4 * (c4 - 1) / 2) * (c2 - 2);
    }

    cout << ans << "\n";
    return 0;
}
```
