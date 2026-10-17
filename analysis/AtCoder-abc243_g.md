# Problem Analysis: AtCoder-abc243_g — Sqrt

**Problem ID**: `AtCoder-abc243_g`  
**Contest**: `abc243`  
**Rating / Difficulty**: 2032  
**URL**: https://atcoder.jp/contests/abc243/tasks/abc243_g  
**VJudge Tag**: `[problem:AtCoder-abc243_g]`  
**Category File**: [`../categories/dynamic_programming/two_level_sqrt_dp_prefix_aggregation.md`](../categories/dynamic_programming/two_level_sqrt_dp_prefix_aggregation.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Two-Level Square Root DP with Prefix Sum Value Aggregation`  

---

## 1. Problem Statement & Key Idea
T test cases. Given X <= 9 * 10^18. A sequence starts with X, where each subsequent element y satisfies 1 <= y <= floor(sqrt(prev)), terminating when a term is 1. Count the number of valid sequences.

**Key Idea**: Let f(n) be the number of sequences starting at n. f(1) = 1, and f(n) = sum_{y=1}^{floor(sqrt(n))} f(y). For X <= 9 * 10^18, let R = floor(sqrt(X)) <= 3 * 10^9. Then f(X) = sum_{y=1}^R f(y). In this sum, f(y) = sum_{z=1}^{floor(sqrt(y))} f(z). Notice floor(sqrt(y)) <= floor(sqrt(R)) <= 54,772! We precompute f(z) for all z <= 60,000 using prefix sums. Then for any y <= R, f(y) is a known prefix sum pref[floor(sqrt(y))]. Grouping values of floor(sqrt(y)) = z into intervals [z^2, min(R, (z+1)^2 - 1)], we compute f(X) in O(sqrt(R)) ~ 55,000 operations per test case.

## 2. Core Observation & Invariant
Iterating the square root map reduces 10^18 to 3 * 10^9 to 54,772, enabling two-level square root grouping into a single fast linear sweep.

## 3. Step-by-Step Algorithm
1. Precompute f(z) for z up to M = 60,000:
2.   f(1) = 1; for z = 2..M: f(z) = pref[isqrt(z)]; pref[z] = pref[z - 1] + f(z).
3. For each query X:
4.   Compute R = isqrt(X) using exact integer square root.
5.   Let K = isqrt(R).
6.   ans = 0.
7.   For z = 1 to K:
8.     count of y where isqrt(y) == z is min(R, (z + 1)^2 - 1) - z^2 + 1.
9.     ans += pref[z] * count.
10.   Output ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(M + T * sqrt(sqrt(X))) where M = 60,000`
- **Space Complexity**: `O(M)`

## 5. Core Algorithmic Skill & Learning Takeaway
Two-level square root decomposition and prefix sum range aggregation.

**Reusable Pattern**: Double Sqrt Recurrence: Precompute up to X^(1/4); group values of X^(1/2) by integer square root ranges.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
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
