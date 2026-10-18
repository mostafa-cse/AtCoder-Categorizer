# Problem Analysis: AtCoder-abc224_g — G. Roll or Increment

**Problem ID**: `AtCoder-abc224_g`  
**Contest**: `abc224`  
**Rating / Difficulty**: 2374  
**URL**: https://atcoder.jp/contests/abc224/tasks/abc224_g  
**VJudge Tag**: `[problem:AtCoder-abc224_g]`  
**Category File**: [`../categories/math/threshold_reroll_expected_value.md`](../categories/math/threshold_reroll_expected_value.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Find the minimum expected cost to reach target $T$ on an $N$-sided die with increment cost $A$ and reroll cost $B$. Optimal stopping strategy rerolls iff distance to $T$ exceeds threshold $k$; the expected cost $E(k) = \frac{NB}{k+1} + \frac{Ak}{2}$ is minimized via convex optimization in $O(1)$.

## 2. Core Observation & Invariant
From any state $X$, the decision to reroll or increment depends only on distance $T - X$. If $X > T$, rerolling is mandatory. If $X < T$, the optimal policy increments if $T - X \le k$ and rerolls otherwise, leading to expected reroll cost $E(k) = \frac{NB}{k+1} + \frac{Ak}{2}$, which is strictly convex in threshold $k$.

## 3. Step-by-Step Algorithm
1. The expected cost $E(k)$ of a reroll policy with threshold $k$ is $E(k) = \frac{NB}{k+1} + \frac{Ak}{2}$ for $k \in [0, \min(T - 1, N - 1)]$.
2. Find the optimal integer $k^*$ minimizing $E(k)$ near $k \approx \sqrt{2NB/A} - 1$.
3. From start state $S$: if $S == T$, answer is 0; if $S > T$, answer is $E(k^*)$; if $S < T$, answer is $\min((T - S)A, E(k^*))$ in $O(1)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed << setprecision(16);

    long long n, s, t, a, b;
    if (!(cin >> n >> s >> t >> a >> b)) return 0;

    if (s == t) {
        cout << 0.0 << "\n";
        return 0;
    }

    // Find best k in [0, min(t - 1, n - 1)]
    long long max_k = min(t - 1, n - 1);

    auto get_E = [&](long long k) -> double {
        return (double)n * b / (k + 1) + (double)a * k / 2.0;
    };

    // k around sqrt(2 * n * b / a) - 1
    double opt_k_real = sqrt(2.0 * n * b / a) - 1.0;
    long long center = max(0LL, min(max_k, (long long)opt_k_real));

    double best_E = 1e25;
    for (long long k = max(0LL, center - 5); k <= min(max_k, center + 5); k++) {
        best_E = min(best_E, get_E(k));
    }

    if (s > t) {
        cout << best_E << "\n";
    } else {
        double inc_cost = (double)(t - s) * a;
        cout << min(inc_cost, best_E) << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
