# Problem Analysis: AtCoder-arc047_b — B - 同一円周上

**Problem ID**: `AtCoder-arc047_b`  
**Contest**: `arc047`  
**Rating / Difficulty**: 2455  
**URL**: https://atcoder.jp/contests/arc047/tasks/arc047_b  
**VJudge Tag**: `[problem:AtCoder-arc047_b]`  
**Category File**: [`../categories/geometry/equidistant_points_chebyshev_rotation.md`](../categories/geometry/equidistant_points_chebyshev_rotation.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)`  

---

## 1. Problem Statement & Key Idea
Find a lattice point $P = (P_x, P_y)$ with $|P_x|, |P_y| \le 10^9$ equidistant in Manhattan metric from all $N$ given points.

## 2. Core Observation & Invariant
Rotating coordinates by 45 degrees via $(u, v) = (x+y, x-y)$ converts Manhattan distance to $\ell_\infty$ Chebyshev distance $\max(|u_1 - u_2|, |v_1 - v_2|)$. A circle of radius $D$ in $\ell_\infty$ is the boundary of an axis-aligned square of side length $2D$. All points must lie on the boundary of $[U - D, U + D] \times [V - D, V + D]$. Thus $2D = \max(u_{\max} - u_{\min}, v_{\max} - v_{\min})$, and the center $(U, V)$ must be one of at most 4 candidates $(u_{\min}+D, u_{\max}-D) \times (v_{\min}+D, v_{\max}-D)$. Testing these 4 candidates in $O(N)$ identifies the valid center point.

## 3. Step-by-Step Algorithm
1. 1. If $N=1$, return $(x_1, y_1)$.
2. 2. Compute $u_i = x_i + y_i, v_i = x_i - y_i$, and their minimums and maximums.
3. 3. Let $d = \max(u_{\max} - u_{\min}, v_{\max} - v_{\min})$; if $d$ is odd, increment $d$. Let $D = d / 2$.
4. 4. Generate candidates for $(U, V)$ from $\{u_{\min}+D, u_{\max}-D\} \times \{v_{\min}+D, v_{\max}-D\}$.
5. 5. For each candidate with $U \equiv V \pmod 2$, recover $(P_x, P_y) = ((U+V)/2, (U-V)/2)$.
6. 6. Check if all original points have distance $D$ to $(P_x, P_y)$. Output the first valid point.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;
    vector<long long> X(N), Y(N);
    vector<long long> U(N), V(N);
    long long u_min = 4e18, u_max = -4e18;
    long long v_min = 4e18, v_max = -4e18;

    for (int i = 0; i < N; ++i) {
        cin >> X[i] >> Y[i];
        U[i] = X[i] + Y[i];
        V[i] = X[i] - Y[i];
        u_min = min(u_min, U[i]);
        u_max = max(u_max, U[i]);
        v_min = min(v_min, V[i]);
        v_max = max(v_max, V[i]);
    }

    if (N == 1) {
        cout << X[0] << " " << Y[0] << "\n";
        return 0;
    }

    long long d = max(u_max - u_min, v_max - v_min);
    if (d % 2 != 0) d++;
    long long D = d / 2;

    vector<long long> cand_U = {u_min + D, u_max - D};
    vector<long long> cand_V = {v_min + D, v_max - D};

    for (long long u : cand_U) {
        for (long long v : cand_V) {
            if ((u + v) % 2 != 0) continue;
            long long px = (u + v) / 2;
            long long py = (u - v) / 2;
            if (abs(px) > 1000000000LL || abs(py) > 1000000000LL) continue;

            long long d0 = abs(X[0] - px) + abs(Y[0] - py);
            bool ok = true;
            for (int i = 1; i < N; ++i) {
                if (abs(X[i] - px) + abs(Y[i] - py) != d0) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                cout << px << " " << py << "\n";
                return 0;
            }
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
