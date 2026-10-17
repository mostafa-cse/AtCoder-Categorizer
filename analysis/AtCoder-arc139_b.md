# Problem Analysis: AtCoder-arc139_b — Make N

**Problem ID**: `AtCoder-arc139_b`  
**Contest**: `arc139`  
**Rating / Difficulty**: 1719  
**URL**: https://atcoder.jp/contests/arc139/tasks/arc139_b  
**VJudge Tag**: `[problem:AtCoder-arc139_b]`  
**Category File**: [`../categories/basics/knapsack_lcm_sqrt_threshold.md`](../categories/basics/knapsack_lcm_sqrt_threshold.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Square Root / Greedy`  
- **Topic (Skill)**: `Square Root / LCM Dominance Threshold on 2-Denomination Unbounded Knapsack`  

---

## 1. Problem Statement & Key Idea
Reach exactly N starting from 0 using operations: +1 costs X, +A costs Y, +B costs Z. Find the minimum cost. (T test cases, N, A, B <= 10^9).

**Key Insight**: Assume without loss of generality that A is more cost-effective than B (Y/A <= Z/B). By LCM/Pigeonhole, taking A copies of B can always be replaced by B copies of A with less or equal cost, so we never need >= A copies of B.

## 2. Core Observation & Invariant
If A >= sqrt(N), the number of A packages is at most N / A <= sqrt(N), so we can iterate over copies of A. If A < sqrt(N), the number of B packages is < A < sqrt(N), so we can iterate over copies of B. In both cases, O(sqrt(N)) iterations suffice.

## 3. Step-by-Step Algorithm
1. Normalize costs: Y = min(Y, A * X), Z = min(Z, B * X).
2. If Y * B > Z * A: swap(A, B) and swap(Y, Z) to ensure A is more cost-effective.
3. If A >= 30000: iterate count of A from 0 to N / A; fill remainder with B then 1s.
4. Else: iterate count of B from 0 to min(A - 1, N / B); fill remainder with A then 1s.
5. Print minimal cost found.

## 4. Complexity Analysis
- **Time Complexity**: `O(sqrt(N)) per test case`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

void solve() {
    long long n, a, b, x, y, z;
    cin >> n >> a >> b >> x >> y >> z;

    y = min(y, a * x);
    z = min(z, b * x);

    // Ensure package A has better or equal rate than package B
    if (y * b > z * a) {
        swap(a, b);
        swap(y, z);
    }

    long long min_cost = 4e18;

    if (a >= 30000) {
        for (long long k_a = 0; k_a * a <= n; ++k_a) {
            long long rem = n - k_a * a;
            long long k_b = rem / b;
            long long k_1 = rem % b;
            min_cost = min(min_cost, k_a * y + k_b * z + k_1 * x);
        }
    } else {
        long long max_kb = min(a - 1, n / b);
        for (long long k_b = 0; k_b <= max_kb; ++k_b) {
            long long rem = n - k_b * b;
            long long k_a = rem / a;
            long long k_1 = rem % a;
            min_cost = min(min_cost, k_a * y + k_b * z + k_1 * x);
        }
    }

    cout << min_cost << "\n";
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
- **Core Skill**: Bounding dual unbounded knapsack package counts using exchange argument and square-root branching.
- **Reusable Pattern**: `Unbounded 2-Package Knapsack: Ensure Y/A <= Z/B and iterate min(N/A, A) steps.`
