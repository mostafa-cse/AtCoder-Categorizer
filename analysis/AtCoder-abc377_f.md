# Problem Analysis: AtCoder-abc377_f — Avoid Queen Attack

**Problem ID**: `AtCoder-abc377_f`  
**Contest**: `abc377`  
**Rating / Difficulty**: 2232  
**URL**: https://atcoder.jp/contests/abc377/tasks/abc377_f  
**VJudge Tag**: `[problem:AtCoder-abc377_f]`  
**Category File**: [`../categories/combinatorics/pie_queen_attack_avoidance_grid_intersections.md`](../categories/combinatorics/pie_queen_attack_avoidance_grid_intersections.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Count the number of empty squares not attacked by any of M <= 1000 queens in an N x N grid with N <= 10^9.

## 2. Core Observation & Invariant
Attacked squares form the union of <= M rows, <= M columns, <= M anti-diagonals (r + c = d), and <= M main-diagonals (r - c = d). The initial non-attacked count from row and column exclusions is (N - |R|) * (N - |C|). For each anti-diagonal, compute its total grid length and subtract previously accounted intersections with R and C. For each main-diagonal, compute its grid length and subtract intersections with R, C, and all anti-diagonals. Since line pairs intersect at most once, total intersections are O(M^2).

## 3. Step-by-Step Algorithm
1. 1. Collect distinct attacked rows R, columns C, anti-diagonals D_slash (r+c), and main-diagonals D_backslash (r-c).
2. 2. Initialize ans = (N - |R|) * (N - |C|).
3. 3. For each d in D_slash: find intersections with rows x in R and columns y in C that fall inside grid [1, N]; subtract (length(d) - |cross_x|) from ans.
4. 4. For each d in D_backslash: find intersections with rows x in R, columns y in C, and anti-diagonals e in D_slash (where (d+e)%2 == 0); subtract (length(d) - |cross_x|) from ans.
5. 5. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(M^2 log M)`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N;
    int M;
    if (!(cin >> N >> M)) return 0;

    set<long long> horizontal, vertical, diag_slash, diag_backslash;
    for (int i = 0; i < M; ++i) {
        long long r, c;
        cin >> r >> c;
        horizontal.insert(r);
        vertical.insert(c);
        diag_slash.insert(r + c);
        diag_backslash.insert(r - c);
    }

    long long ans = (N - (long long)horizontal.size()) * (N - (long long)vertical.size());

    // anti-diagonal: r + c = d
    for (long long d : diag_slash) {
        set<long long> cross_x;
        for (long long x : horizontal) {
            if (1 <= d - x && d - x <= N) {
                cross_x.insert(x);
            }
        }
        for (long long y : vertical) {
            if (1 <= d - y && d - y <= N) {
                cross_x.insert(d - y);
            }
        }
        long long length = 2 * min(d, N + 1) - d - 1;
        ans -= (length - (long long)cross_x.size());
    }

    // main-diagonal: r - c = d
    for (long long d : diag_backslash) {
        set<long long> cross_x;
        for (long long x : horizontal) {
            if (1 <= x - d && x - d <= N) {
                cross_x.insert(x);
            }
        }
        for (long long y : vertical) {
            if (1 <= d + y && d + y <= N) {
                cross_x.insert(d + y);
            }
        }
        for (long long e : diag_slash) {
            if ((d + e) % 2 == 0) {
                long long x = (d + e) / 2;
                long long y = (e - d) / 2;
                if (1 <= x && x <= N && 1 <= y && y <= N) {
                    cross_x.insert(x);
                }
            }
        }
        long long length = N - abs(d);
        ans -= (length - (long long)cross_x.size());
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
