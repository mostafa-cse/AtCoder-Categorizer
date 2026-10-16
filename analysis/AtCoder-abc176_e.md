# Problem Analysis: AtCoder-abc176_e — Bomber

**Problem ID**: `AtCoder-abc176_e`  
**Contest**: `abc176`  
**Rating / Difficulty**: 1204  
**URL**: https://atcoder.jp/contests/abc176/tasks/abc176_e  
**VJudge Tag**: `[problem:AtCoder-abc176_e]`  
**Category File**: [`../categories/basics/max_row_col_intersection.md`](../categories/basics/max_row_col_intersection.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Grid Sweeping`  
- **Topic (Skill)**: `Max Row/Col Intersection Overlap Filtering`  

---

## 1. Problem Statement & Key Idea
An H x W grid contains M targets. Placing a bomb at cell (r, c) destroys all targets in row r and column c. Find the maximum number of targets that can be destroyed.

**Key Idea**: The targets destroyed by placing a bomb at (r, c) is count_row[r] + count_col[c] - (1 if target at (r, c) else 0).

## 2. Core Observation & Invariant
Let max_r = max_i count_row[i] and max_c = max_j count_col[j]. The answer is either max_r + max_c or max_r + max_c - 1. It equals max_r + max_c if and only if there exists SOME pair (r, c) such that count_row[r] == max_r and count_col[c] == max_c and cell (r, c) does NOT contain a target!

## 3. Step-by-Step Algorithm
1. Count targets in each row and column; find max_r and max_c.
2. Collect all rows with count_row[r] == max_r into best_rows.
3. Collect all cols with count_col[c] == max_c into best_cols.
4. Store target coordinates in a hash set.
5. If best_rows.size() * best_cols.size() > M, by Pigeonhole Principle at least one pair contains no target -> answer is max_r + max_c.
6. Else, check all candidate pairs: if any pair has no target, answer is max_r + max_c; else max_r + max_c - 1.

## 4. Complexity Analysis
- **Time Complexity**: `O(H + W + M)`
- **Space Complexity**: `O(H + W + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, m;
    if (!(cin >> h >> w >> m)) return 0;

    vector<int> row_cnt(h + 1, 0), col_cnt(w + 1, 0);
    set<pair<int, int>> targets;

    for (int i = 0; i < m; ++i) {
        int r, c;
        cin >> r >> c;
        row_cnt[r]++;
        col_cnt[c]++;
        targets.insert({r, c});
    }

    int max_r = 0, max_c = 0;
    for (int r = 1; r <= h; ++r) max_r = max(max_r, row_cnt[r]);
    for (int c = 1; c <= w; ++c) max_c = max(max_c, col_cnt[c]);

    vector<int> best_r, best_c;
    for (int r = 1; r <= h; ++r) if (row_cnt[r] == max_r) best_r.push_back(r);
    for (int c = 1; c <= w; ++c) if (col_cnt[c] == max_c) best_c.push_back(c);

    if ((long long)best_r.size() * best_c.size() > m) {
        cout << max_r + max_c << "\n";
        return 0;
    }

    for (int r : best_r) {
        for (int c : best_c) {
            if (!targets.count({r, c})) {
                cout << max_r + max_c << "\n";
                return 0;
            }
        }
    }

    cout << max_r + max_c - 1 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bounding intersection checks on maximal marginal distributions.
- **Reusable Pattern**: `Max cross sum: max_r + max_c - (all top pairs covered by targets ? 1 : 0).`
