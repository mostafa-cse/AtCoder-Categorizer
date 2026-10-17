# Problem Analysis: AtCoder-arc098_c — Range Minimum Queries

**Problem ID**: `AtCoder-arc098_c`  
**Contest**: `arc098`  
**Rating / Difficulty**: 1951  
**URL**: https://atcoder.jp/contests/arc098/tasks/arc098_c  
**VJudge Tag**: `[problem:AtCoder-arc098_c]`  
**Category File**: [`../categories/basics/min_max_spread_fixed_lower_bound.md`](../categories/basics/min_max_spread_fixed_lower_bound.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy / Two Pointers`  
- **Topic (Skill)**: `Min-Max Spread Optimization via Fixed Lower Bound and Segmented Greedy Extraction`  

---

## 1. Problem Statement & Key Idea
Given array A of length N. In each step, choose an interval of length K, take its minimum, and remove it from A. Repeat Q times. Minimize max(Z) - min(Z) where Z is the multiset of Q removed elements.

Iterate over the minimum element X in Z (at most N choices from A). For a fixed X, any chosen element must be >= X, meaning elements < X cannot be inside any chosen window. This splits A into contiguous segments of elements >= X. For each segment of length L >= K, we can extract L - K + 1 elements; greedily choose the smallest L - K + 1 elements from each segment. If the total extractable elements across all segments is >= Q, take the Q-th smallest element Y from the merged pool, and update ans = min(ans, Y - X).

## 2. Core Observation & Invariant
Fixing the lower bound decomposes the interval selection constraint into independent contiguous segments where greedy choice is optimal.

## 3. Step-by-Step Algorithm
1. For each candidate minimum value X in A:
2.   Split A into contiguous segments of elements >= X.
3.   For each segment with length L >= K:
4.     Sort elements and add the smallest L - K + 1 elements to pool.
5.   If pool.size() >= Q:
6.     Sort pool and update ans = min(ans, pool[Q - 1] - X).
7. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, q;
    if (!(cin >> n >> k >> q)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int ans = INF;

    for (int i = 0; i < n; ++i) {
        int x = a[i];
        vector<int> pool;
        vector<int> cur_seg;

        for (int j = 0; j < n; ++j) {
            if (a[j] >= x) {
                cur_seg.push_back(a[j]);
            } else {
                if ((int)cur_seg.size() >= k) {
                    sort(cur_seg.begin(), cur_seg.end());
                    int extract_cnt = (int)cur_seg.size() - k + 1;
                    for (int m = 0; m < extract_cnt; ++m) {
                        pool.push_back(cur_seg[m]);
                    }
                }
                cur_seg.clear();
            }
        }
        if ((int)cur_seg.size() >= k) {
            sort(cur_seg.begin(), cur_seg.end());
            int extract_cnt = (int)cur_seg.size() - k + 1;
            for (int m = 0; m < extract_cnt; ++m) {
                pool.push_back(cur_seg[m]);
            }
        }

        if ((int)pool.size() >= q) {
            sort(pool.begin(), pool.end());
            ans = min(ans, pool[q - 1] - x);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Fixing the lower bound in min-max spread problems to enable greedy segment extraction.
- **Reusable Pattern**: `Fixed Lower Bound Sweep: Iterate X in A, segment elements >= X, extract greedily, take Q-th element.`
