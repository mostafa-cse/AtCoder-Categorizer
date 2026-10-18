# Problem Analysis: AtCoder-abc251_g — G. Intersection of Polygons

**Problem ID**: `AtCoder-abc251_g`  
**Contest**: `abc251`  
**Rating / Difficulty**: 2468  
**URL**: https://atcoder.jp/contests/abc251/tasks/abc251_g  
**VJudge Tag**: `[problem:AtCoder-abc251_g]`  
**Category File**: [`../categories/geometry/intersection_of_polygons_halfplane_duality.md`](../categories/geometry/intersection_of_polygons_halfplane_duality.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Polygons(2D)`  

---

## 1. Problem Statement & Key Idea
Determine whether each query point $(a, b)$ lies inside the intersection of $M$ translated convex $N$-gons $P + (u_i, v_i)$. A point $q \in P + v_i \iff q - v_i \in P$. Each CCW edge of $P$ defines a half-plane $A_k x + B_k y \ge C_k$. Substituting $q - v_i$ yields $A_k a + B_k b \ge C_k + (A_k u_i + B_k v_i)$. Taking the maximum over all $M$ shifts precomputes $M_k = \max_i (A_k u_i + B_k v_i)$, allowing $O(N)$ checks per query.

## 2. Core Observation & Invariant
The intersection of convex polygons is defined by the intersection of all their bounding half-planes. Since the translations only affect the constant term of each half-plane, the intersection of translated copies preserves the normal vectors $A_k, B_k$ and simply tightens the threshold to $\max_i (A_k u_i + B_k v_i)$.

## 3. Step-by-Step Algorithm
1. 1. For each of the $N$ edges of $P$, compute line coefficients $A_k = y_k - y_{k+1}$, $B_k = x_{k+1} - x_k$, and $C_k = x_{k+1} y_k - x_k y_{k+1}$.
2. 2. For each edge $k$, precompute $M_k = \max_{j=1}^M (A_k u_j + B_k v_j)$ in $O(NM)$ total time.
3. 3. For each of the $Q$ queries $(a, b)$, verify whether $A_k a + B_k b \ge C_k + M_k$ holds for all $k = 1 \dots N$.
4. 4. Output 'Yes' if all $N$ conditions hold, otherwise 'No'.

## 4. Complexity Analysis
- **Time Complexity**: `O(NM + NQ)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    long long A, B, C;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n), y(n);
    for (int i = 0; i < n; ++i) cin >> x[i] >> y[i];

    vector<Edge> edges(n);
    for (int i = 0; i < n; ++i) {
        int next = (i + 1) % n;
        edges[i].A = y[i] - y[next];
        edges[i].B = x[next] - x[i];
        edges[i].C = x[next] * y[i] - x[i] * y[next];
    }

    int m;
    cin >> m;
    vector<long long> u(m), v(m);
    for (int i = 0; i < m; ++i) cin >> u[i] >> v[i];

    vector<long long> max_val(n, -4e18);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            long long val = edges[i].A * u[j] + edges[i].B * v[j];
            if (val > max_val[i]) max_val[i] = val;
        }
    }

    int q;
    cin >> q;
    while (q--) {
        long long a, b;
        cin >> a >> b;
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            if (edges[i].A * a + edges[i].B * b < edges[i].C + max_val[i]) {
                ok = false;
                break;
            }
        }
        cout << (ok ? "Yes" : "No") << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
