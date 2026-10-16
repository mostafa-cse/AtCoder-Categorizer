# Problem Analysis: AtCoder-typical90_ba — Discrete Dowsing

**Problem ID**: `AtCoder-typical90_ba`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 053)  
**Rating / Difficulty**: 2600 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ba  
**VJudge Tag**: `[problem:AtCoder-typical90_ba]`  
**Category File**: [`../categories/basics/fibonacci_search.md`](../categories/basics/fibonacci_search.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Ternary Search & Optimization`  
- **Topic (Skill)**: `Discrete Golden-Section / Fibonacci Search on Unimodal Functions`  

---

## 1. Problem Statement & Key Idea
Interactive problem: array A of length N (N <= 1500) strictly increases then strictly decreases (strictly unimodal). Find the maximum value of A using at most 15 queries.

**Core Idea**: Standard ternary search uses 2 queries per step, requiring 2 * log_{3/2}(1500) ≈ 36 queries (too many). Golden Section / Fibonacci Search reuses one previous query each step, requiring only 1 query per step!

## 2. Core Observation & Invariant
Fibonacci numbers satisfy F_{k+1} = F_k + F_{k-1}. Pad the array to F_{16} = 1597. In each step, test two interior points at distances F_{k-1} and F_k from the boundary. One point is always carried over from the previous step!

## 3. Step-by-Step Algorithm
1. Pad array to size F_{16} = 1597 with -1.
2. Maintain active interval [L, R] of length F_k.
3. Place probes at L + F_{k-2} and L + F_{k-1}.
4. Compare values and contract interval to F_{k-1}.
5. Return maximum probed value.

## 4. Complexity Analysis
Time: O(log_phi N) = 15 queries max, Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int memo[1605];

int query(int i, int n) {
    if (i < 1 || i > n) return -1;
    if (memo[i] != -1) return memo[i];
    cout << "? " << i << endl;
    int ans;
    cin >> ans;
    return memo[i] = ans;
}

void solve() {
    int n;
    cin >> n;

    fill(memo, memo + 1605, -1);

    // Fibonacci numbers: F_0 = 0, F_1 = 1, ...
    vector<int> fib = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597};
    int k = 16; // fib[16] = 987, fib[17] = 1597

    int left = 0;
    int m1 = left + fib[k - 2];
    int m2 = left + fib[k - 1];
    int v1 = query(m1, n);
    int v2 = query(m2, n);

    while (k > 3) {
        if (v1 < v2) {
            left = m1;
            m1 = m2;
            v1 = v2;
            m2 = left + fib[k - 2];
            v2 = query(m2, n);
        } else {
            m2 = m1;
            v2 = v1;
            m1 = left + fib[k - 3];
            v1 = query(m1, n);
        }
        k--;
    }

    int best = -1;
    for (int i = 1; i <= n; ++i) {
        if (memo[i] != -1) best = max(best, memo[i]);
    }
    cout << "! " << best << endl;
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
Fibonacci search reusing interior function evaluations on unimodal functions.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Fibonacci / Golden Section search, query budget minimization, and unimodal optimization.
- **Reusable Pattern**: `Fibonacci Search on Unimodal Arrays.`

---
Back to [Discrete Golden-Section / Fibonacci Search on Unimodal Functions](../categories/basics/fibonacci_search.md) | [Categories Directory](../categories/README.md)