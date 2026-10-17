# Problem Analysis: AtCoder-abc186_f — Rook on Grid

**Problem ID**: `AtCoder-abc186_f`  
**Contest**: `abc186`  
**Rating / Difficulty**: 1833  
**URL**: https://atcoder.jp/contests/abc186/tasks/abc186_f  
**VJudge Tag**: `[problem:AtCoder-abc186_f]`  
**Category File**: [`../categories/data_structures/obstacle_grid_rook_sweep_line.md`](../categories/data_structures/obstacle_grid_rook_sweep_line.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Fenwick Tree Sweep-Line`  
- **Topic (Skill)**: `2D Obstacle Grid Sweep-Line with Fenwick Tree Deduplication`  

---

## 1. Problem Statement & Key Idea
An H x W grid has M obstacles. A rook starts at (1, 1) and can make at most 2 moves (down then right, or right then down) without jumping obstacles. Find the number of distinct reachable cells.

**Key Insight**: Cells reachable in 1 or 2 moves are: (1) down-then-right cells (r, c) where r <= min_row_obst[1] and c <= min_col_obst[r], and (2) right-then-down cells. Count all down-then-right cells, then add right-then-down cells not already included via Fenwick sweep-line.

## 2. Core Observation & Invariant
Right-then-down cells at (r, c) are not counted by down-then-right iff c > min_col_obst[r] while r <= min_row_obst[c]. This is a range query over columns answered in O(log W).

## 3. Step-by-Step Algorithm
1. Find first obstacle in each row (row_lim[r]) and column (col_lim[c]).
2. Sum row_lim[r] for all r <= col_lim[1].
3. Group columns by their col_lim[c].
4. Maintain Fenwick tree over columns c in [col_lim[1] + 1, W].
5. Sweep row r from 1 to H:
6.   Insert all columns whose col_lim[c] >= r into Fenwick tree.
7.   Query count of active columns c > row_lim[r].
8. Print total.

## 4. Complexity Analysis
- **Time Complexity**: `O((H + W + M) log W)`
- **Space Complexity**: `O(H + W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int sz;
    vector<int> tree;
    Fenwick(int n) : sz(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= sz; i += i & -i) tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    int query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, m;
    if (!(cin >> h >> w >> m)) return 0;

    vector<int> row_lim(h + 1, w);
    vector<int> col_lim(w + 1, h);

    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        row_lim[x] = min(row_lim[x], y - 1);
        col_lim[y] = min(col_lim[y], x - 1);
    }

    long long ans = 0;
    int max_r = col_lim[1];
    for (int r = 1; r <= max_r; ++r) {
        ans += row_lim[r];
    }

    vector<vector<int>> col_events(h + 2);
    for (int c = row_lim[1] + 1; c <= w; ++c) {
        col_events[col_lim[c]].push_back(c);
    }

    Fenwick ft(w);
    for (int c = row_lim[1] + 1; c <= w; ++c) {
        ft.add(c, 1);
    }

    for (int r = 1; r <= max_r; ++r) {
        ans += ft.query(row_lim[r] + 1, w);
        for (int c : col_events[r]) {
            ft.add(c, -1);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining coordinate-projection range limits with Fenwick tree sweep-line deduplication.
- **Reusable Pattern**: `2-Move Grid Sweep: Add primary L-paths then count secondary L-paths exceeding primary bounds via Fenwick.`
