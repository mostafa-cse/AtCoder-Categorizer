# Problem Analysis: AtCoder-abc196_e — Filters

**Problem ID**: `AtCoder-abc196_e`  
**Contest**: `abc196`  
**Rating / Difficulty**: 1650  
**URL**: https://atcoder.jp/contests/abc196/tasks/abc196_e  
**VJudge Tag**: `[problem:AtCoder-abc196_e]`  
**Category File**: [`../categories/math/clamping_interval_composition.md`](../categories/math/clamping_interval_composition.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Composition of Clamping Intervals [L, R] with Linear Shift`  

---

## 1. Problem Statement & Key Idea
N filter operations on an integer x: 1) x = x + a; 2) x = max(x, a); 3) x = min(x, a). Answer Q queries: value of input x after applying all N operations in order.

**Key Insight**: The composition of addition, max, and min operations is always a piecewise linear function characterized by a single horizontal shift and clamping bounds: f(x) = min(high, max(low, x + add)).

## 2. Core Observation & Invariant
Initialize add = 0, low = -INF, high = INF. Type 1 shifts add, low, and high. Type 2 updates low = max(low, a) and high = max(high, a). Type 3 updates high = min(high, a) and low = min(low, a). Each query is evaluated in O(1).

## 3. Step-by-Step Algorithm
1. Initialize add = 0, low = -INF, high = INF.
2. For each operation (a, t):
3.   If t == 1: add += a, low += a, high += a.
4.   If t == 2: low = max(low, a), high = max(high, a).
5.   If t == 3: high = min(high, a), low = min(low, a).
6. For each query x:
7.   res = min(high, max(low, x + add)).
8.   Print res.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long add = 0;
    long long low = -INF;
    long long high = INF;

    for (int i = 0; i < n; ++i) {
        long long a;
        int t;
        cin >> a >> t;

        if (t == 1) {
            add += a;
            low += a;
            high += a;
        } else if (t == 2) {
            low = max(low, a);
            high = max(high, a);
        } else if (t == 3) {
            high = min(high, a);
            low = min(low, a);
        }
    }

    int q;
    cin >> q;
    while (q--) {
        long long x;
        cin >> x;
        long long res = min(high, max(low, x + add));
        cout << res << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Continuous function composition preserving clamped linear envelopes.
- **Reusable Pattern**: `Affine Clamping Composition: f(x) = clamp(x + add, low, high).`
