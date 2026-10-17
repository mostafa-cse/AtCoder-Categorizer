# Problem Analysis: AtCoder-abc193_e — Oversleeping

**Problem ID**: `AtCoder-abc193_e`  
**Contest**: `abc193`  
**Rating / Difficulty**: 1948  
**URL**: https://atcoder.jp/contests/abc193/tasks/abc193_e  
**VJudge Tag**: `[problem:AtCoder-abc193_e]`  
**Category File**: [`../categories/number_theory/crt_dual_periodic_cycle_synchronization.md`](../categories/number_theory/crt_dual_periodic_cycle_synchronization.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Chinese Remainder Theorem`  
- **Topic (Skill)**: `Dual Periodic Cycle Synchronization via Chinese Remainder Theorem on Interval Windows`  

---

## 1. Problem Statement & Key Idea
A train cycle has period M_1 = 2X + 2Y, visiting station at times t = t1 mod M_1 for t1 in [X, X + Y - 1]. Sleep cycle has period M_2 = P + Q, waking at t = t2 mod M_2 for t2 in [P, P + Q - 1]. Find the earliest time Takahashi can get off the train, or report infinity.

For any pair of offsets t1 in [X, X + Y) and t2 in [P, P + Q), we have a system of two modular equations: t = t1 mod M_1 and t = t2 mod M_2. Since Y, Q <= 500, we can solve this using the Chinese Remainder Theorem (via Extended Euclidean Algorithm) across candidate pairs, finding the minimal non-negative solution.

## 2. Core Observation & Invariant
Small window widths Y, Q <= 500 allow directly checking pairwise CRT solutions in O(Y * Q * log(M)).

## 3. Step-by-Step Algorithm
1. For each query, set M1 = 2X + 2Y and M2 = P + Q.
2. Iterate t1 from X to X + Y - 1 and t2 from P to P + Q - 1.
3. Solve CRT(t1, M1, t2, M2) using extgcd.
4. If valid solution r >= 0 exists, update ans = min(ans, r).
5. Output ans if found, else infinity.

## 4. Complexity Analysis
- **Time Complexity**: `O(Y * Q * log(min(M1, M2)))`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Synchronizing dual periodic events over interval windows using Chinese Remainder Theorem.
- **Reusable Pattern**: `Periodic Cycle Sync: CRT(t1 mod M1, t2 mod M2) finds earliest alignment over window pairs.`
