# Problem Analysis: AtCoder-tenka1_2018_e — E. Equilateral

**Problem ID**: `AtCoder-tenka1_2018_e`  
**Contest**: `tenka1-2018`  
**Rating / Difficulty**: 2459  
**URL**: https://atcoder.jp/contests/tenka1-2018/tasks/tenka1_2018_e  
**VJudge Tag**: `[problem:AtCoder-tenka1_2018_e]`  
**Category File**: [`../categories/miscellaneous/equilateral_triangles_chebyshev_rotation.md`](../categories/miscellaneous/equilateral_triangles_chebyshev_rotation.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Manhattan <> Chebyshev`  

---

## 1. Problem Statement & Key Idea
Count triples of points with equal pairwise Manhattan distances. Manhattan distance rotates 45 degrees into Chebyshev distance $\max(|u_i - u_j|, |v_i - v_j|)$ with $u = r + c, v = r - c + W$. In Chebyshev distance, pairwise distances $D$ must be even, and any equilateral triangle consists of two points lying along an axis-aligned boundary of size $D$ and a third point on the parallel opposite boundary $[v_1, v_2]$ or $[u_1, u_2]$. Range queries count candidate points, while subtracting L-shaped 3-corner overlaps avoids overcounting.

## 2. Core Observation & Invariant
Any equilateral triangle in Chebyshev metric cannot have all three pairwise distances along the same axis. Therefore, at least two points share the same $u$ or same $v$. Triangles with a flat horizontal side are queried via 2D prefix sums over vertical ranges; triangles with a flat vertical side are queried similarly. Triangles forming three corners of an axis-aligned square (L-shapes) are counted twice and subtracted.

## 3. Step-by-Step Algorithm
1. 1. Map each '#' coin at $(r, c)$ to rotated coordinates $u = r + c, v = r - c + W$.
2. 2. Compute 2D prefix sums over the grid.
3. 3. Group points by $u$ and sort by $v$; group points by $v$ and sort by $u$.
4. 4. For each horizontal pair $(u, v_1, v_2)$ with $D = v_2 - v_1$, query points on $u - D$ and $u + D$ in range $[v_1, v_2]$, recording L-shape matches at corners.
5. 5. For each vertical pair $(v, u_1, u_2)$ with $D = u_2 - u_1$, query points on $v - D$ and $v + D$ in range $[u_1, u_2]$.
6. 6. Return $ans_u + ans_v - L\_shapes$.

## 4. Complexity Analysis
- **Time Complexity**: `O((H + W)^2)`
- **Space Complexity**: `O((H + W)^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int MAXC = 605;
int pref[MAXC][MAXC];

int query_sum(int r1, int c1, int r2, int c2) {
    if (r1 > r2 || c1 > c2) return 0;
    r1 = max(0, r1); c1 = max(0, c1);
    r2 = min(MAXC - 1, r2); c2 = min(MAXC - 1, c2);
    if (r1 > r2 || c1 > c2) return 0;
    int res = pref[r2][c2];
    if (r1 > 0) res -= pref[r1 - 1][c2];
    if (c1 > 0) res -= pref[r2][c1 - 1];
    if (r1 > 0 && c1 > 0) res += pref[r1 - 1][c1 - 1];
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    vector<string> S(H);
    for (int i = 0; i < H; ++i) cin >> S[i];

    vector<vector<int>> grid(MAXC, vector<int>(MAXC, 0));
    vector<pair<int, int>> pts;

    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            if (S[r][c] == '#') {
                int u = r + c;
                int v = r - c + W;
                grid[u][v] = 1;
                pts.push_back({u, v});
            }
        }
    }

    for (int i = 0; i < MAXC; ++i) {
        for (int j = 0; j < MAXC; ++j) {
            pref[i][j] = grid[i][j];
            if (i > 0) pref[i][j] += pref[i - 1][j];
            if (j > 0) pref[i][j] += pref[i][j - 1];
            if (i > 0 && j > 0) pref[i][j] -= pref[i - 1][j - 1];
        }
    }

    vector<vector<int>> at_u(MAXC), at_v(MAXC);
    for (auto& p : pts) {
        at_u[p.first].push_back(p.second);
        at_v[p.second].push_back(p.first);
    }
    for (int i = 0; i < MAXC; ++i) {
        sort(at_u[i].begin(), at_u[i].end());
        sort(at_v[i].begin(), at_v[i].end());
    }

    long long ans_u = 0;
    long long L_shapes = 0;

    // Pairs sharing same u
    for (int u = 0; u < MAXC; ++u) {
        int sz = at_u[u].size();
        for (int i = 0; i < sz; ++i) {
            for (int j = i + 1; j < sz; ++j) {
                int D = at_u[u][j] - at_u[u][i];
                int v1 = at_u[u][i], v2 = at_u[u][j];

                // Check opposite sides at u - D and u + D
                if (u - D >= 0) {
                    ans_u += query_sum(u - D, v1, u - D, v2);
                    if (grid[u - D][v1]) L_shapes++;
                    if (grid[u - D][v2]) L_shapes++;
                }
                if (u + D < MAXC) {
                    ans_u += query_sum(u + D, v1, u + D, v2);
                    if (grid[u + D][v1]) L_shapes++;
                    if (grid[u + D][v2]) L_shapes++;
                }
            }
        }
    }

    long long ans_v = 0;
    // Pairs sharing same v
    for (int v = 0; v < MAXC; ++v) {
        int sz = at_v[v].size();
        for (int i = 0; i < sz; ++i) {
            for (int j = i + 1; j < sz; ++j) {
                int D = at_v[v][j] - at_v[v][i];
                int u1 = at_v[v][i], u2 = at_v[v][j];

                // Check opposite sides at v - D and v + D
                if (v - D >= 0) {
                    ans_v += query_sum(u1, v - D, u2, v - D);
                }
                if (v + D < MAXC) {
                    ans_v += query_sum(u1, v + D, u2, v + D);
                }
            }
        }
    }

    long long ans = ans_u + ans_v - L_shapes;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
