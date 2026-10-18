# Problem Analysis: AtCoder-abc333_g — G. Nearest Fraction

**Problem ID**: `AtCoder-abc333_g`  
**Contest**: `abc333`  
**Rating / Difficulty**: 2536  
**URL**: https://atcoder.jp/contests/abc333/tasks/abc333_g  
**VJudge Tag**: `[problem:AtCoder-abc333_g]`  
**Category File**: [`../categories/miscellaneous/nearest_fraction_stern_brocot_tree.md`](../categories/miscellaneous/nearest_fraction_stern_brocot_tree.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Stern-Brocot Tree and Rational Approximation`  

---

## 1. Problem Statement & Key Idea
Given a real number $r \in [0, 1]$ with up to 18 decimal places and an integer $N \le 10^{18}$, find a reduced fraction $p / q$ with $0 \le p \le q \le N$ and $\gcd(p, q) = 1$ that minimizes $|r - p / q|$. In case of a tie, choose the smaller fraction.

## 2. Core Observation & Invariant
The best rational approximations of a real number are found via continued fractions or descending the Stern-Brocot Tree. The Stern-Brocot Tree maintains a bracket $(\frac{p_1}{q_1}, \frac{p_2}{q_2})$ containing $r$, starting with $\frac{0}{1}$ and $\frac{1}{1}$. The mediant $\frac{p_1 + p_2}{q_1 + q_2}$ is compared against $r$. To handle $N \le 10^{18}$ in logarithmic time, accelerated leaps (Euclidean division on continued fraction quotients) jump multiple mediants at once.

## 3. Step-by-Step Algorithm
1. 1. Represent $r$ as an exact integer fraction $A / B$ where $B = 10^k$ and $k$ is the number of decimal digits of $r$.
2. 2. Initialize Stern-Brocot brackets $L = (0, 1)$ and $R = (1, 1)$.
3. 3. Loop while true:
4.    - Compare mediant $M = (L.p + R.p, L.q + R.q)$ with $r = A / B$.
5.    - If $M == r$: if $M.q \le N$, return $M$.
6.    - If $r > M$: jump along right branch by $k = \lfloor \frac{A \cdot R.q - B \cdot R.p}{B \cdot L.p - A \cdot L.q} \rfloor$ steps. If $L.q + k \cdot R.q > N$, truncate $k$ to maximum feasible $\le N$, check closest between $L$ and boundary candidate, and terminate.
7.    - Symmetrically for $r < M$: jump along left branch by $k$ steps.
8. 4. Compare the final candidates with $q \le N$ using 128-bit cross-multiplication $|A \cdot q - B \cdot p|$ to find the exact nearest fraction.

## 4. Complexity Analysis
- **Time Complexity**: `O(\log N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

typedef __int128_t int128;

int128 abs128(int128 x) {
    return x < 0 ? -x : x;
}

bool better(int128 p1, int128 q1, int128 p2, int128 q2, int128 X, int128 Y) {
    int128 diff1 = abs128(p1 * Y - q1 * X) * q2;
    int128 diff2 = abs128(p2 * Y - q2 * X) * q1;
    if (diff1 < diff2) return true;
    if (diff1 > diff2) return false;
    return p1 * q2 < p2 * q1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string r_str;
    long long N_in;
    if (!(cin >> r_str >> N_in)) return 0;

    int128 N = N_in;
    size_t dot_pos = r_str.find('.');
    string dec = r_str.substr(dot_pos + 1);
    int D = dec.size();

    int128 X = 0;
    for (char c : dec) X = X * 10 + (c - '0');

    int128 Y = 1;
    for (int i = 0; i < D; ++i) Y *= 10;

    int128 a = 0, b = 1;
    int128 c = 1, d = 1;

    int128 best_p = 0, best_q = 1;

    auto update = [&](int128 p, int128 q) {
        if (q >= 1 && q <= N) {
            if (better(p, q, best_p, best_q, X, Y)) {
                best_p = p;
                best_q = q;
            }
        }
    };

    update(0, 1);
    update(1, 1);

    while (true) {
        int128 med_num = a + c;
        int128 med_den = b + d;

        if (med_den > N) {
            if (d <= N) {
                int128 k = (N - b) / d;
                if (k > 0) update(a + k * c, b + k * d);
            }
            if (b <= N) {
                int128 k = (N - d) / b;
                if (k > 0) update(k * a + c, k * b + d);
            }
            break;
        }

        if (med_num * Y < med_den * X) {
            int128 num = b * X - a * Y;
            int128 den = c * Y - d * X;
            int128 k = num / den;
            if (b + k * d > N) {
                k = (N - b) / d;
                if (k > 0) update(a + k * c, b + k * d);
                break;
            }
            update(a + k * c, b + k * d);
            a += k * c;
            b += k * d;
        } else if (med_num * Y > med_den * X) {
            int128 num = c * Y - d * X;
            int128 den = b * X - a * Y;
            int128 k = num / den;
            if (k * b + d > N) {
                k = (N - d) / b;
                if (k > 0) update(k * a + c, k * b + d);
                break;
            }
            update(k * a + c, k * b + d);
            c += k * a;
            d += k * b;
        } else {
            update(med_num, med_den);
            break;
        }
    }

    long long out_p = (long long)best_p;
    long long out_q = (long long)best_q;
    cout << out_p << " " << out_q << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
