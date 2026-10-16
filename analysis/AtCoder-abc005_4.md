# Problem Analysis: AtCoder-abc005_4 — Takoyaki Plate

**Problem ID**: `AtCoder-abc005_4`  
**Contest**: `abc005`  
**Rating / Difficulty**: 1447  
**URL**: https://atcoder.jp/contests/abc005/tasks/abc005_4  
**VJudge Tag**: `[problem:AtCoder-abc005_4]`  
**Category File**: [`../categories/dp/prefix_sum_2d_rectangle_envelope.md`](../categories/dp/prefix_sum_2d_rectangle_envelope.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `2D Prefix Sums`  
- **Topic (Skill)**: `2D Prefix Sums Subrectangle Optimization with Monotonic Envelope`  

---

## 1. Problem Statement & Key Idea
An N x N plate has takoyaki with deliciousness D[i][j]. You are given Q queries, each with an integer P. For each query, find the maximum deliciousness of a contiguous rectangular subgrid containing AT MOST P takoyaki (area <= P). N <= 50, Q <= N^2.

**Key Insight**: Precompute the sum of every possible subrectangle using 2D prefix sums. Record the maximum deliciousness for each area h * w, then compute a prefix-maximum envelope over area.

## 2. Core Observation & Invariant
Since N <= 50, the total number of subrectangles is O(N^4 / 4) ~ 1.5 * 10^6. We can evaluate all subrectangles in O(N^4), populate max_val[area], take prefix maxima, and answer each query in O(1).

## 3. Step-by-Step Algorithm
1. Compute 2D prefix sums pref[r][c] of D.
2. Initialize best[area] = 0 for area = 0..N*N.
3. Enumerate all pairs of rows (r1, r2) and columns (c1, c2):
4.   area = (r2 - r1 + 1) * (c2 - c1 + 1).
5.   sum = pref[r2][c2] - pref[r1-1][c2] - pref[r2][c1-1] + pref[r1-1][c1-1].
6.   best[area] = max(best[area], sum).
7. Compute prefix maxima: for area = 1..N*N: best[area] = max(best[area], best[area - 1]).
8. For each query P, output best[P].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^4 + Q)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> d(n + 1, vector<int>(n + 1, 0));
    vector<vector<int>> pref(n + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> d[i][j];
            pref[i][j] = d[i][j] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
        }
    }

    int max_area = n * n;
    vector<int> best(max_area + 1, 0);

    for (int r1 = 1; r1 <= n; ++r1) {
        for (int r2 = r1; r2 <= n; ++r2) {
            int h = r2 - r1 + 1;
            for (int c1 = 1; c1 <= n; ++c1) {
                for (int c2 = c1; c2 <= n; ++c2) {
                    int w = c2 - c1 + 1;
                    int area = h * w;
                    int sum = pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1];
                    best[area] = max(best[area], sum);
                }
            }
        }
    }

    for (int a = 1; a <= max_area; ++a) {
        best[a] = max(best[a], best[a - 1]);
    }

    int q;
    cin >> q;
    while (q--) {
        int p;
        cin >> p;
        cout << best[p] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Exhaustive subgrid evaluation via 2D prefix sums mapped to monotonic parameter upper envelopes.
- **Reusable Pattern**: `2D Subgrid Area Envelope: O(N^4) precomputation + prefix max for O(1) area-constrained queries.`
