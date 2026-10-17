# Problem Analysis: AtCoder-abc443_g — G. Another Mod of Linear Problem

**Problem ID**: `AtCoder-abc443_g`  
**Contest**: `abc443`  
**Rating / Difficulty**: 2268  
**URL**: https://atcoder.jp/contests/abc443/tasks/abc443_g  
**VJudge Tag**: `[problem:AtCoder-abc443_g]`  
**Category File**: [`../categories/number_theory/floor_sum_linear_modulo_inequality.md`](../categories/number_theory/floor_sum_linear_modulo_inequality.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Floor Sum`  
- **Topic (Skill)**: `Floor Sum and Mod Sum of Arithmetic Progression`  

---

## 1. Problem Statement & Key Idea
Given integers $N, M, A, B$ with $1 \le N \le M \le 10^9$ and $0 \le A, B < M$. Across $T \le 3 \times 10^5$ test cases, find the number of integers $0 \le k < N$ such that $(Ak + B) \bmod M > k$.

## 2. Core Observation & Invariant
Rewrite the inequality algebraically:
$(Ak + B) \bmod M > k \iff k + 1 \le Ak + B - M \lfloor \frac{Ak + B}{M} \rfloor \iff \lfloor \frac{Ak + B}{M} \rfloor \le \frac{(A - 1)k + (B - 1)}{M}$.
Since the LHS is an integer, this is equivalent to $\lfloor \frac{Ak + B}{M} \rfloor \le \lfloor \frac{(A - 1)k + (B - 1)}{M} \rfloor$.
Furthermore, the difference $\Delta(k) = \lfloor \frac{Ak + B}{M} \rfloor - \lfloor \frac{(A - 1)k + (B - 1)}{M} \rfloor$ only ever takes values in $\{0, 1\}$. The condition $\Delta(k) \le 0$ means $\Delta(k) = 0$. Hence, the number of valid $k$ is precisely $N - \sum_{k=0}^{N-1} \Delta(k) = N - \text{floor\_sum}(N, M, A, B) + \text{floor\_sum}(N, M, A - 1, B - 1)$. Using generalized floor division and Euclidean floor sum computes each query in $O(\log M)$ time.

## 3. Step-by-Step Algorithm
1. Implement generalized `floor_sum(n, m, a, b)` using Euclidean-like recursion supporting arbitrary integer $a, b$ via floor division.
2. For each testcase $(N, M, A, B)$:
3. Compute $ans = N - \text{floor\_sum}(N, M, A, B) + \text{floor\_sum}(N, M, A - 1, B - 1)$.
4. Output $ans$.

## 4. Complexity Analysis
- **Time Complexity**: `O(T \log M)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>

using namespace std;

inline long long floor_div(long long a, long long m) {
    long long res = a / m;
    long long rem = a % m;
    if (rem != 0 && ((a < 0) ^ (m < 0))) {
        res--;
    }
    return res;
}

inline long long floor_mod(long long a, long long m) {
    long long rem = a % m;
    if (rem < 0) rem += m;
    return rem;
}

long long floor_sum(long long n, long long m, long long a, long long b) {
    if (n == 0) return 0;
    long long a1 = floor_div(a, m);
    long long a2 = floor_mod(a, m);
    long long s = n * (n - 1) / 2 * a1;
    long long b1 = floor_div(b, m);
    long long b2 = floor_mod(b, m);
    if (a2 == 0) {
        return s + b1 * n;
    }
    long long k = (a2 * (n - 1) + b2) / m;
    return s + n * (k + b1) - floor_sum(k, a2, m, m + a2 - b2 - 1);
}

void solve() {
    long long n, m, a, b;
    if (!(cin >> n >> m >> a >> b)) return;
    long long ans = n - floor_sum(n, m, a, b) + floor_sum(n, m, a - 1, b - 1);
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
