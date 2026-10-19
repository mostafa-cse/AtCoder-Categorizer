# Problem Analysis: AtCoder-abc280_g — G - Do Use Hexagon Grid 2

**Problem ID**: `AtCoder-abc280_g`  
**Contest**: `abc280`  
**Rating / Difficulty**: 2842  
**URL**: https://atcoder.jp/contests/abc280/tasks/abc280_g  
**VJudge Tag**: `[problem:AtCoder-abc280_g]`  
**Category File**: [`../categories/basics/hexagonal_coordinate_transformation_bounding_box_sweep.md`](../categories/basics/hexagonal_coordinate_transformation_bounding_box_sweep.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Two Pointers`  

---

## 1. Problem Statement & Key Idea
On a hexagonal grid, distance is d((i1, j1), (i2, j2)) = max(|i1 - i2|, |j1 - j2|, |(i1 - j1) - (i2 - j2)|). Given N points, count non-empty subsets where all pairwise distances are <= D modulo 998244353.

## 2. Core Observation & Invariant
Mapping (X, Y) -> (X, Y, X - Y) embeds the hexagonal metric into 3D Chebyshev space. By Helly's property for L_infinity balls, all pairwise distances are <= D iff all points fit in a bounding box [X, X+D] x [Y, Y+D] x [Z, Z+D]. Subsets are uniquely counted by their coordinate minima (X, Y, Z). For fixed X and Y, maintaining points in the Z-window [Z, Z+D] with two pointers allows evaluating PIE over the 8 boundary conditions in O(1) per step, yielding an O(N^3) total algorithm.

## 3. Step-by-Step Algorithm
1. 1. Transform points (X, Y) -> (X, Y, X - Y) and extract unique X and Y coordinates.
2. 2. Precompute powers of 2 modulo 998244353.
3. 3. Loop over unique X and filter points in [X, X + D]. Loop over unique Y and filter points in [Y, Y + D].
4. 4. Sort remaining candidates by z. Use two pointers [l, r) to slide the window [Z, Z + D].
5. 5. For each distinct Z = z_l, expand r to include z <= Z + D.
6. 6. Use PIE over 8 subsets of {x > X, y > Y, z > Z} to count valid non-empty subsets with exact minima X, Y, Z.
7. 7. Sum contributions modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

const int MOD = 998244353;

struct Point {
    ll x, y, z;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    ll d;
    if (!(cin >> n >> d)) return 0;

    vector<Point> pts(n);
    vector<ll> coords_x(n), coords_y(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].x >> pts[i].y;
        pts[i].z = pts[i].x - pts[i].y;
        coords_x[i] = pts[i].x;
        coords_y[i] = pts[i].y;
    }

    sort(coords_x.begin(), coords_x.end());
    coords_x.erase(unique(coords_x.begin(), coords_x.end()), coords_x.end());

    sort(coords_y.begin(), coords_y.end());
    coords_y.erase(unique(coords_y.begin(), coords_y.end()), coords_y.end());

    vector<long long> pow2(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    long long ans = 0;

    for (ll X : coords_x) {
        vector<Point> cand1;
        for (const auto& p : pts) {
            if (X <= p.x && p.x <= X + d) {
                cand1.push_back(p);
            }
        }
        if (cand1.empty()) continue;

        for (ll Y : coords_y) {
            vector<Point> cand2;
            for (const auto& p : cand1) {
                if (Y <= p.y && p.y <= Y + d) {
                    cand2.push_back(p);
                }
            }
            if (cand2.empty()) continue;

            sort(cand2.begin(), cand2.end(), [](const Point& a, const Point& b) {
                return a.z < b.z;
            });

            int K = (int)cand2.size();
            int r = 0;
            int c[4] = {0, 0, 0, 0};

            auto get_type = [&](const Point& p) -> int {
                return (p.x == X ? 1 : 0) | (p.y == Y ? 2 : 0);
            };

            int l = 0;
            while (l < K) {
                ll Z = cand2[l].z;
                int l_end = l;
                while (l_end < K && cand2[l_end].z == Z) {
                    l_end++;
                }

                while (r < K && cand2[r].z <= Z + d) {
                    c[get_type(cand2[r])]++;
                    r++;
                }

                int cz[4] = {0, 0, 0, 0};
                for (int idx = l; idx < l_end; ++idx) {
                    cz[get_type(cand2[idx])]++;
                }

                long long ways_box = 0;
                for (int mask = 0; mask < 8; ++mask) {
                    bool bx = (mask & 1) > 0;
                    bool by = (mask & 2) > 0;
                    bool bz = (mask & 4) > 0;
                    int sign = (__builtin_popcount(mask) % 2 == 1) ? -1 : 1;

                    int total_allowed = 0;
                    for (int t = 0; t < 4; ++t) {
                        if (bx && (t & 1)) continue;
                        if (by && (t & 2)) continue;
                        total_allowed += c[t];
                        if (bz) total_allowed -= cz[t];
                    }

                    long long term = pow2[total_allowed];
                    if (sign == 1) {
                        ways_box = (ways_box + term) % MOD;
                    } else {
                        ways_box = (ways_box - term + MOD) % MOD;
                    }
                }

                ans = (ans + ways_box) % MOD;

                for (int idx = l; idx < l_end; ++idx) {
                    c[get_type(cand2[idx])]--;
                }
                l = l_end;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
