# Two-Level Square Root DP with Prefix Sum Value Aggregation

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `DP Optimizations`  

This workbook contains curated, high-quality competitive programming problems teaching **Two-Level Square Root DP with Prefix Sum Value Aggregation**.

---

## Curated Problems

### `[problem:AtCoder-abc243_g]` — Sqrt
- **Rating / Difficulty**: 2032
- **Contest**: `abc243`
- **Analysis**: [`analysis/AtCoder-abc243_g.md`](../../analysis/AtCoder-abc243_g.md)
- **Key Idea**: Let f(n) be the number of sequences starting at n. f(1) = 1, and f(n) = sum_{y=1}^{floor(sqrt(n))} f(y). For X <= 9 * 10^18, let R = floor(sqrt(X)) <= 3 * 10^9. Then f(X) = sum_{y=1}^R f(y). In this sum, f(y) = sum_{z=1}^{floor(sqrt(y))} f(z). Notice floor(sqrt(y)) <= floor(sqrt(R)) <= 54,772! We precompute f(z) for all z <= 60,000 using prefix sums. Then for any y <= R, f(y) is a known prefix sum pref[floor(sqrt(y))]. Grouping values of floor(sqrt(y)) = z into intervals [z^2, min(R, (z+1)^2 - 1)], we compute f(X) in O(sqrt(R)) ~ 55,000 operations per test case.
- **Time Complexity**: `O(M + T * sqrt(sqrt(X))) where M = 60,000`
- **Space Complexity**: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <cstdint>

using namespace std;

const int MAX_M = 60000;
uint64_t f[MAX_M + 1];
uint64_t pref[MAX_M + 1];

uint64_t isqrt(uint64_t n) {
    uint64_t r = sqrt(n);
    while ((r + 1) * (r + 1) <= n) r++;
    while (r * r > n) r--;
    return r;
}

void precompute() {
    f[1] = 1;
    pref[1] = 1;
    for (uint64_t z = 2; z <= MAX_M; ++z) {
        uint64_t s = isqrt(z);
        f[z] = pref[s];
        pref[z] = pref[z - 1] + f[z];
    }
}

void solve() {
    uint64_t x;
    cin >> x;

    uint64_t r = isqrt(x);
    uint64_t k = isqrt(r);

    uint64_t ans = 0;
    for (uint64_t z = 1; z <= k; ++z) {
        uint64_t low = z * z;
        uint64_t high = min(r, (z + 1) * (z + 1) - 1);
        uint64_t cnt = high - low + 1;
        ans += pref[z] * cnt;
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
```
