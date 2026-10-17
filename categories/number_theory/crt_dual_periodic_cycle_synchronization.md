# Dual Periodic Cycle Synchronization via Chinese Remainder Theorem on Interval Windows

**Domain**: `Number Theory`  
**Subtopic**: `Chinese Remainder Theorem`  

This workbook contains curated, high-quality competitive programming problems teaching **Dual Periodic Cycle Synchronization via Chinese Remainder Theorem on Interval Windows**.

---

## Curated Problems

### `[problem:AtCoder-abc193_e]` — Oversleeping
- **Rating / Difficulty**: 1948
- **Contest**: `abc193`
- **Analysis**: [`analysis/AtCoder-abc193_e.md`](../../analysis/AtCoder-abc193_e.md)
- **Key Idea**: For any pair of offsets t1 in [X, X + Y) and t2 in [P, P + Q), we have a system of two modular equations: t = t1 mod M_1 and t = t2 mod M_2. Since Y, Q <= 500, we can solve this using the Chinese Remainder Theorem (via Extended Euclidean Algorithm) across candidate pairs, finding the minimal non-negative solution.
- **Time Complexity**: `O(Y * Q * log(min(M1, M2)))`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <numeric>
#include <algorithm>

using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long d = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

pair<long long, long long> crt(long long r1, long long m1, long long r2, long long m2) {
    long long p, q;
    long long d = extgcd(m1, m2, p, q);
    if ((r2 - r1) % d != 0) return {0, -1};
    long long m = m1 / d * m2;
    long long tmp = (r2 - r1) / d % (m2 / d) * p % (m2 / d);
    long long r = (r1 + m1 * tmp) % m;
    if (r < 0) r += m;
    return {r, m};
}

void solve() {
    long long X, Y, P, Q;
    cin >> X >> Y >> P >> Q;

    long long M1 = 2 * X + 2 * Y;
    long long M2 = P + Q;

    long long ans = -1;

    for (long long t1 = X; t1 < X + Y; ++t1) {
        for (long long t2 = P; t2 < P + Q; ++t2) {
            auto [r, m] = crt(t1, M1, t2, M2);
            if (m != -1) {
                if (ans == -1 || r < ans) {
                    ans = r;
                }
            }
        }
    }

    if (ans == -1) {
        cout << "infinity\n";
    } else {
        cout << ans << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```
