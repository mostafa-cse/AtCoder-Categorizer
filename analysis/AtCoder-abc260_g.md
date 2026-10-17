# Problem Analysis: AtCoder-abc260_g — G. Scalene Triangle Area

**Problem ID**: `AtCoder-abc260_g`  
**Contest**: `abc260`  
**Rating / Difficulty**: 2339  
**URL**: https://atcoder.jp/contests/abc260/tasks/abc260_g  
**VJudge Tag**: `[problem:AtCoder-abc260_g]`  
**Category File**: [`../categories/basics/scalene_triangle_imos_2d_difference.md`](../categories/basics/scalene_triangle_imos_2d_difference.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `2D Prefix Sum`  
- **Topic (Skill)**: `2D Prefix Sum`  

---

## 1. Problem Statement & Key Idea
Count how many pieces cover each query square in a scalene triangle region. Triangular coverage regions have vertical and slope-2 diagonal boundaries, computed via 2D imos difference arrays in $O(N(N + M) + Q)$.

## 2. Core Observation & Invariant
The region covered by a piece at $(s, t)$ is a right triangle where on each row $u \in [s, s + M - 1]$, the covered columns form an interval $[t, t + 2M - 1 - 2(u - s)]$. The start boundary is vertical (constant $t$), while the end boundary is a diagonal with direction $(\Delta u = 1, \Delta v = -2)$.

## 3. Step-by-Step Algorithm
1. Mark $+1$ and $-1$ on the vertical boundary in array $V$ at $(s, t)$ and $(s + M, t)$.
2. Mark $-1$ and $+1$ on the diagonal boundary in array $\delta$ at $(s, t + 2M)$ and $(s + M, t)$.
3. Propagate diagonal differences along direction $(+1, -2)$, accumulate vertical sums into horizontal difference array $H$, and perform horizontal prefix sums in $O(N(N + M))$ time to answer queries in $O(1)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N(N + M) + Q)`
- **Space Complexity**: `O(N(N + M))`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }

    int max_u = n + m + 5;
    int max_v = n + 2 * m + 5;

    vector<vector<int>> V(max_u, vector<int>(max_v, 0));
    vector<vector<int>> delta(max_u, vector<int>(max_v, 0));

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            if (s[r][c] == 'O') {
                V[r][c] += 1;
                V[r + m][c] -= 1;
                delta[r][c + 2 * m] -= 1;
                delta[r + m][c] += 1;
            }
        }
    }

    vector<vector<int>> D(max_u, vector<int>(max_v, 0));
    for (int u = 0; u < max_u; ++u) {
        for (int v = max_v - 1; v >= 0; --v) {
            int prev = (u > 0 && v + 2 < max_v) ? D[u - 1][v + 2] : 0;
            D[u][v] = prev + delta[u][v];
        }
    }

    vector<vector<int>> H(max_u, vector<int>(max_v, 0));
    for (int v = 0; v < max_v; ++v) {
        int run_v = 0;
        for (int u = 0; u < max_u; ++u) {
            run_v += V[u][v];
            H[u][v] = run_v + D[u][v];
        }
    }

    vector<vector<int>> Ans(n, vector<int>(n, 0));
    for (int u = 0; u < n; ++u) {
        int run_h = 0;
        for (int v = 0; v < max_v; ++v) {
            run_h += H[u][v];
            if (v < n) {
                Ans[u][v] = run_h;
            }
        }
    }

    int q;
    if (!(cin >> q)) return 0;

    for (int i = 0; i < q; ++i) {
        int x, y;
        cin >> x >> y;
        --x; --y;
        cout << Ans[x][y] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
