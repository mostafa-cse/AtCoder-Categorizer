# Problem Analysis: AtCoder-abc315_g — G. Ai + Bj + Ck = X (1 <= i, j, k <= N)

**Problem ID**: `AtCoder-abc315_g`  
**Contest**: `abc315`  
**Rating / Difficulty**: 2315  
**URL**: https://atcoder.jp/contests/abc315/tasks/abc315_g  
**VJudge Tag**: `[problem:AtCoder-abc315_g]`  
**Category File**: [`../categories/number_theory/linear_diophantine_3var_bounded_solutions.md`](../categories/number_theory/linear_diophantine_3var_bounded_solutions.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Euclidean Algorithm`  
- **Topic (Skill)**: `Extended Euclid`  

---

## 1. Problem Statement & Key Idea
Given $N, A, B, C, X$, count the number of triples $(i, j, k)$ with $1 \le i, j, k \le N$ satisfying $A i + B j + C k = X$.

## 2. Core Observation & Invariant
For each fixed $i \in [1, N]$, the equation $B j + C k = X - A i$ is a 2-variable linear Diophantine equation whose solutions form an arithmetic progression $j = j_0 + t \cdot (C / g)$.

## 3. Step-by-Step Algorithm
1. Precompute $g = \gcd(B, C)$ and the base modular inverse $B' j_0 \equiv 1 \pmod{C'}$ via Extended Euclid.
2. Iterate over $i \in [1, N]$. For each $Y = X - A i$, verify divisibility by $g$, compute the particular residue $j \equiv j_{\text{rem}} \pmod{C'}$, and intersect the feasibility intervals $1 \le j \le N$ and $1 \le k \le N$ in $O(1)$ time, yielding an $O(N)$ total algorithm.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, a, b, c, x;
    if (!(cin >> n >> a >> b >> c >> x)) return 0;

    long long j0, k0;
    long long g = extgcd(b, c, j0, k0);

    long long bp = b / g;
    long long cp = c / g;

    j0 = (j0 % cp + cp) % cp;

    long long ans = 0;
    for (long long i = 1; i <= n; ++i) {
        long long y = x - a * i;
        if (y <= 0) continue;
        if (y % g != 0) continue;

        long long yp = y / g;

        long long rem = (j0 * (yp % cp)) % cp;
        if (rem == 0) rem += cp;

        long long L = max(1LL, (yp - n * cp + bp - 1) / bp);
        long long R = min(n, (yp - cp) / bp);

        if (L > R) continue;

        long long r_target = rem % cp;
        long long first = L + ((r_target - L % cp + cp) % cp);
        if (first <= R) {
            ans += (R - first) / cp + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
