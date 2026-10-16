# Problem Analysis: AtCoder-abc106_d — AtCoder Express 2

**Problem ID**: `AtCoder-abc106_d`  
**Contest**: `abc106`  
**Rating / Difficulty**: 1319  
**URL**: https://atcoder.jp/contests/abc106/tasks/abc106_d  
**VJudge Tag**: `[problem:AtCoder-abc106_d]`  
**Category File**: [`../categories/data_structures/interval_2d_prefix_sums.md`](../categories/data_structures/interval_2d_prefix_sums.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `2D Prefix Sums`  
- **Topic (Skill)**: `2D Prefix Sums on Interval Endpoints [L, R]`  

---

## 1. Problem Statement & Key Idea
M train lines, where train i runs between cities L_i and R_i (1 <= L_i <= R_i <= N <= 500). Q queries: count train lines running strictly inside interval [p, q] (i.e. p <= L_i and R_i <= q).

**Key Idea**: Treat each interval [L_i, R_i] as a 2D integer point (L_i, R_i) in the N x N plane.

## 2. Core Observation & Invariant
A train line lies entirely within [p, q] if and only if its left endpoint satisfies p <= L and its right endpoint satisfies R <= q. In the 2D plane, this corresponds to querying the number of points in the bounding box [p, N] x [1, q], solved in O(1) using standard 2D prefix sums!

## 3. Step-by-Step Algorithm
1. Initialize grid cnt[N+1][N+1] with 0; for each train (l, r), cnt[l][r]++.
2. Compute 2D prefix sum table pref[r][c] = cnt[r][c] + pref[r-1][c] + pref[r][c-1] - pref[r-1][c-1].
3. For each query (p, q): query box [p..q, p..q]: count = pref[q][q] - pref[p-1][q] - pref[q][p-1] + pref[p-1][p-1].
4. Print count for each query.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 + Q)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<int>> grid(n + 1, vector<int>(n + 1, 0));
    for (int i = 0; i < m; ++i) {
        int l, r;
        cin >> l >> r;
        grid[l][r]++;
    }

    vector<vector<int>> pref(n + 1, vector<int>(n + 1, 0));
    for (int r = 1; r <= n; ++r) {
        for (int c = 1; c <= n; ++c) {
            pref[r][c] = grid[r][c] + pref[r - 1][c] + pref[r][c - 1] - pref[r - 1][c - 1];
        }
    }

    while (q--) {
        int p, q_end;
        cin >> p >> q_end;
        int ans = pref[q_end][q_end] - pref[p - 1][q_end] - pref[q_end][p - 1] + pref[p - 1][p - 1];
        cout << ans << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Mapping 1D interval inclusion to 2D range sum box queries.
- **Reusable Pattern**: `Interval inclusion [p, q]: 2D box query on (L, R) in [p..q] x [p..q].`
