# Problem Analysis: AtCoder-abc202_f — F. Integer Convex Hull

**Problem ID**: `AtCoder-abc202_f`  
**Contest**: `abc202`  
**Rating / Difficulty**: 2905  
**URL**: https://atcoder.jp/contests/abc202/tasks/abc202_f  
**VJudge Tag**: `[problem:AtCoder-abc202_f]`  
**Category File**: [`../categories/dynamic_programming/convex_hull_integer_area_parity_dp.md`](../categories/dynamic_programming/convex_hull_integer_area_parity_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Convex Hulls`  

---

## 1. Problem Statement & Key Idea
Given N points in general position in the 2D plane, count the number of subsets S of size >= 3 whose convex hull conv(S) has an integer area, modulo 10^9 + 7.

## 2. Core Observation & Invariant
By Pick's theorem, 2 * Area of any integer polygon is an integer, so the area is an integer iff 2 * Area == 0 (mod 2). Fix the bottom-leftmost vertex P0 of the convex hull. Sort all other points radially around P0. A convex polygon rooted at P0 is formed by a counter-clockwise sequence of points P0 -> P_i1 -> P_i2 -> ... -> P0. Points strictly inside the polygon can be either included or excluded in S arbitrarily without affecting conv(S), contributing a factor of 2^{interior points}. The quantity 2 * Area (mod 2) accumulates additively as cross products of successive triangles.

## 3. Step-by-Step Algorithm
1. 1. For each point P0, consider all points with higher Y coordinate (or same Y and higher X) and sort them angularly around P0.
2. 2. Precompute the number of points strictly inside triangle (P0, Pu, Pv) for all pairs (u, v).
3. 3. Run DP: dp[u][v][parity] = sum of 2^{interior} weights for convex paths ending with edge Pu -> Pv with current 2*Area parity.
4. 4. Transition: extend to Pw if (P0, Pv, Pw) is CCW and (Pu, Pv, Pw) turns left.
5. 5. Close the polygon to P0: if parity + cross_product(Pv, P0) == 0 (mod 2), add to answer.
6. 6. Sum over all choices of root P0 modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^4)`
- **Space Complexity**: `O(N^3)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long ll;

const int MOD = 1000000007;

struct Point {
    ll x, y;
};

ll cross(Point o, Point a, Point b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

bool in_triangle(Point o, Point a, Point b, Point p) {
    ll c1 = cross(o, a, p);
    ll c2 = cross(a, b, p);
    ll c3 = cross(b, o, p);
    return (c1 > 0 && c2 > 0 && c3 > 0);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<Point> pts(N);
    for (int i = 0; i < N; ++i) {
        cin >> pts[i].x >> pts[i].y;
    }

    vector<ll> pw2(N + 1, 1);
    for (int i = 1; i <= N; ++i) {
        pw2[i] = (pw2[i - 1] * 2) % MOD;
    }

    sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
        if (a.y != b.y) return a.y < b.y;
        return a.x < b.x;
    });

    ll total_ans = 0;

    for (int i = 0; i < N; ++i) {
        Point o = pts[i];
        vector<Point> rem;
        for (int j = i + 1; j < N; ++j) {
            rem.push_back(pts[j]);
        }
        int M = rem.size();
        if (M < 2) continue;

        sort(rem.begin(), rem.end(), [&](const Point& a, const Point& b) {
            ll c = cross(o, a, b);
            if (c != 0) return c > 0;
            ll da = (a.x - o.x) * (a.x - o.x) + (a.y - o.y) * (a.y - o.y);
            ll db = (b.x - o.x) * (b.x - o.x) + (b.y - o.y) * (b.y - o.y);
            return da < db;
        });

        vector<vector<ll>> w(M, vector<ll>(M, 0));
        vector<vector<int>> par(M, vector<int>(M, 0));

        for (int j = 0; j < M; ++j) {
            for (int k = j + 1; k < M; ++k) {
                int cnt = 0;
                for (int p = 0; p < N; ++p) {
                    if (in_triangle(o, rem[j], rem[k], pts[p])) {
                        cnt++;
                    }
                }
                w[j][k] = pw2[cnt];
                ll c = abs(cross(o, rem[j], rem[k]));
                par[j][k] = c % 2;
            }
        }

        // dp[k][j][parity]: chain ending at edge rem[j] -> rem[k]
        vector<vector<vector<ll>>> dp(M, vector<vector<ll>>(M, vector<ll>(2, 0)));
        for (int j = 0; j < M; ++j) {
            for (int k = j + 1; k < M; ++k) {
                dp[k][j][par[j][k]] = w[j][k];
            }
        }

        for (int k = 0; k < M; ++k) {
            for (int j = 0; j < k; ++j) {
                for (int p = 0; p < 2; ++p) {
                    ll val = dp[k][j][p];
                    if (!val) continue;

                    for (int l = k + 1; l < M; ++l) {
                        if (cross(rem[j], rem[k], rem[l]) > 0) {
                            int np = (p + par[k][l]) % 2;
                            ll nw = (val * w[k][l]) % MOD;
                            dp[l][k][np] = (dp[l][k][np] + nw) % MOD;
                        }
                    }
                }
            }
        }

        for (int k = 0; k < M; ++k) {
            for (int j = 0; j < k; ++j) {
                total_ans = (total_ans + dp[k][j][0]) % MOD;
            }
        }
    }

    cout << total_ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
