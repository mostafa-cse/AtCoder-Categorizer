# Problem Analysis: AtCoder-arc061_b — Snuke's Coloring

**Problem ID**: `AtCoder-arc061_b`  
**Contest**: `abc045`  
**Rating / Difficulty**: 1682  
**URL**: https://atcoder.jp/contests/abc045/tasks/arc061_b  
**VJudge Tag**: `[problem:AtCoder-arc061_b]`  
**Category File**: [`../categories/data_structures/sparse_grid_window_counting_hash.md`](../categories/data_structures/sparse_grid_window_counting_hash.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Hash Map`  
- **Topic (Skill)**: `Sparse Grid 3x3 Window Counting via Coordinate Hash Map`  

---

## 1. Problem Statement & Key Idea
An H x W grid (H, W <= 10^9) with N black cells (N <= 10^5), all other cells white. For each j in 0..9, find the number of 3x3 subgrids containing EXACTLY j black cells.

**Key Insight**: The total number of 3x3 subgrids is (H - 2) * (W - 2) ~ 10^18. However, at most 9 * N subgrids contain AT LEAST ONE black cell! Hash map maps each 3x3 center to its black cell count.

## 2. Core Observation & Invariant
Each black cell at (r, c) can only be inside 3x3 subgrids whose centers (cr, cc) satisfy r - 1 <= cr <= r + 1 and c - 1 <= cc <= c + 1 with 2 <= cr <= H - 1 and 2 <= cc <= W - 1. Increment black count for these <= 9 centers. The count of subgrids with 0 black cells is (H - 2)*(W - 2) - (number of centers in map).

## 3. Step-by-Step Algorithm
1. Maintain map<pair<int, int>, int> center_black_count.
2. For each black cell (r, c):
3.   For dr in {-1, 0, 1}, dc in {-1, 0, 1}:
4.     cr = r + dr, cc = c + dc.
5.     If 2 <= cr <= H - 1 and 2 <= cc <= W - 1:
6.       center_black_count[{cr, cc}]++;
7. Tally counts in freq[10].
8. freq[0] = (H - 2) * (W - 2) - center_black_count.size().
9. Print freq[0] through freq[9].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long h, w;
    int n;
    if (!(cin >> h >> w >> n)) return 0;

    map<pair<long long, long long>, int> cnt;

    for (int i = 0; i < n; ++i) {
        long long r, c;
        cin >> r >> c;
        for (int dr = -1; dr <= 1; ++dr) {
            for (int dc = -1; dc <= 1; ++dc) {
                long long cr = r + dr;
                long long cc = c + dc;
                if (cr >= 2 && cr <= h - 1 && cc >= 2 && cc <= w - 1) {
                    cnt[{cr, cc}]++;
                }
            }
        }
    }

    vector<long long> ans(10, 0);
    for (const auto& entry : cnt) {
        ans[entry.second]++;
    }

    long long total_subgrids = (h - 2) * (w - 2);
    ans[0] = total_subgrids - cnt.size();

    for (int j = 0; j <= 9; ++j) {
        cout << ans[j] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Sparse window contribution hashing on massive coordinate grids.
- **Reusable Pattern**: `Sparse Subgrid Counting: each point votes for its covering window centers in hash map.`
