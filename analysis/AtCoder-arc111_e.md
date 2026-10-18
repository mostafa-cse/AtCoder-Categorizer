# Problem Analysis: AtCoder-arc111_e — E. Simple Math 3

**Problem ID**: `AtCoder-arc111_e`  
**Contest**: `arc111`  
**Rating / Difficulty**: 2541  
**URL**: https://atcoder.jp/contests/arc111/tasks/arc111_e  
**VJudge Tag**: `[problem:AtCoder-arc111_e]`  
**Category File**: [`../categories/number_theory/simple_math_3_floor_sum.md`](../categories/number_theory/simple_math_3_floor_sum.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Floor Sum`  
- **Topic (Skill)**: `Floor Sum and Mod Sum of Arithmetic Progression`  

---

## 1. Problem Statement & Key Idea
Given $A, B, C, D$, find the number of positive integers $i \ge 1$ such that the interval $[A + B i, A + C i]$ contains no multiple of $D$. Notice that if $(C - B) i \ge D$, the interval length is at least $D$, guaranteeing a multiple of $D$. Thus $i \le M = \lfloor (D - 1) / (C - B) \rfloor$. For $1 \le i \le M$, the interval has length $< D$, so it contains at most one multiple of $D$. The condition is violated if and only if $\lfloor (A + C i) / D \rfloor > \lfloor (A + B i - 1) / D \rfloor$, which is solved in $O(\log D)$ using floor_sum.

## 2. Core Observation & Invariant
Because the interval $[A + B i, A + C i]$ contains at most one multiple of $D$ for each $1 \le i \le M$, the total number of violating $i$ is exactly $\sum_{i=1}^M (\lfloor \frac{C i + A}{D} \rfloor - \lfloor \frac{B i + A - 1}{D} \rfloor)$. Since $A < D$ and $A \ge 1$, the terms at $i = 0$ are both 0. Thus the sum equals $\text{floor\_sum}(M + 1, D, C, A) - \text{floor\_sum}(M + 1, D, B, A - 1)$.

## 3. Step-by-Step Algorithm
1. 1. Compute upper bound $M = (D - 1) / (C - B)$.
2. 2. Compute $S_C = \text{floor\_sum}(M + 1, D, C, A)$ using the Euclidean-like floor sum algorithm.
3. 3. Compute $S_B = \text{floor\_sum}(M + 1, D, B, A - 1)$.
4. 4. Output $M - (S_C - S_B)$ for each testcase.

## 4. Complexity Analysis
- **Time Complexity**: `O(T \log D)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp

#include <iostream>

using namespace std;

// Floor sum: sum_{i=0}^{n-1} floor((a * i + b) / m)
long long floor_sum(long long n, long long m, long long a, long long b) {
    long long ans = 0;
    if (a >= m) {
        ans += (n - 1) * n / 2 * (a / m);
        a %= m;
    }
    if (b >= m) {
        ans += n * (b / m);
        b %= m;
    }

    long long y_max = (a * n + b) / m;
    long long x_max = (y_max * m - b);
    if (y_max == 0) return ans;
    ans += (n - (x_max + a - 1) / a) * y_max;
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a);
    return ans;
}

void solve() {
    long long A, B, C, D;
    if (!(cin >> A >> B >> C >> D)) return;

    long long diff = C - B;
    long long M = (D - 1) / diff;

    // sum_{i=1}^M [floor((C*i + A)/D) - floor((B*i + A - 1)/D)]
    // = floor_sum(M + 1, D, C, A) - floor_sum(M + 1, D, B, A - 1)
    // because at i = 0: floor(A/D) = 0 and floor((A-1)/D) = 0
    long long sum_c = floor_sum(M + 1, D, C, A);
    long long sum_b = floor_sum(M + 1, D, B, A - 1);
    long long multiples_count = sum_c - sum_b;

    long long ans = M - multiples_count;
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
