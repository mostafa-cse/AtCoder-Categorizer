# Problem Analysis: AtCoder-abc011_4 — 大ジャンプ

**Problem ID**: `AtCoder-abc011_4`  
**Contest**: `abc011`  
**Rating / Difficulty**: 1843  
**URL**: https://atcoder.jp/contests/abc011/tasks/abc011_4  
**VJudge Tag**: `[problem:AtCoder-abc011_4]`  
**Category File**: [`../categories/math/45degree_rotation_independent_random_walks.md`](../categories/math/45degree_rotation_independent_random_walks.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Coordinate Rotation`  
- **Topic (Skill)**: `45-Degree Grid Rotation Decomposing 2D Random Walk into Independent 1D Walks`  

---

## 1. Problem Statement & Key Idea
Starting from (0, 0), take N jumps of length D in 4 cardinal directions with equal probability 1/4. Find the probability of landing exactly on (X, Y).

**Key Insight**: Scale coordinates by D: x = X / D, y = Y / D. Rotate coordinate axes by 45 degrees: u = x + y, v = x - y. Each cardinal jump (+1, 0), (-1, 0), (0, +1), (0, -1) becomes (+1, +1), (-1, -1), (+1, -1), (-1, +1), which decomposes into two completely INDEPENDENT 1D random walks of length N along u and v.

## 2. Core Observation & Invariant
In each independent 1D walk, the number of +1 steps is (N + target) / 2. Probability of reaching target in N steps is C(N, (N + target)/2) * (1/2)^N. Total probability is P_1D(u) * P_1D(v).

## 3. Step-by-Step Algorithm
1. If X % D != 0 or Y % D != 0: print 0.0.
2. Let x = X / D, y = Y / D, u = x + y, v = x - y.
3. If (N + u) % 2 != 0 or (N + v) % 2 != 0: print 0.0.
4. Compute log-probabilities or normalized combinations C(N, k) / 2^N to avoid overflow.
5. Print P_u * P_v with 12 decimal places.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

using namespace std;

double prob_1d(int n, int target) {
    if ((n + target) % 2 != 0) return 0.0;
    int k = (n + target) / 2;
    if (k < 0 || k > n) return 0.0;

    // Compute C(n, k) * (1/2)^n via incremental multiplication
    double p = 1.0;
    for (int i = 1; i <= n; ++i) {
        p *= 0.5;
    }
    for (int i = 1; i <= k; ++i) {
        p = p * (n - i + 1) / i;
    }
    return p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long d, X, Y;
    if (!(cin >> n >> d >> X >> Y)) return 0;

    if (X % d != 0 || Y % d != 0) {
        cout << fixed << setprecision(12) << 0.0 << "\n";
        return 0;
    }

    long long x = X / d;
    long long y = Y / d;

    long long u = x + y;
    long long v = x - y;

    if (abs(u) > n || abs(v) > n) {
        cout << fixed << setprecision(12) << 0.0 << "\n";
        return 0;
    }

    double pu = prob_1d(n, u);
    double pv = prob_1d(n, v);

    cout << fixed << setprecision(12) << pu * pv << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Decoupling 2D Manhattan random walks into independent 1D walks via 45-degree rotation.
- **Reusable Pattern**: `45-Degree Coordinate Rotation: Map (x, y) -> (x+y, x-y) to make (dx, dy) independently (+/-1, +/-1).`
