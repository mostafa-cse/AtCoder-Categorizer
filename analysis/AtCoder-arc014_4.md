# Problem Analysis: AtCoder-arc014_4 — grepマスター

**Problem ID**: `AtCoder-arc014_4`  
**Contest**: `arc014`  
**Rating / Difficulty**: 1904  
**URL**: https://atcoder.jp/contests/arc014/tasks/arc014_4  
**VJudge Tag**: `[problem:AtCoder-arc014_4]`  
**Category File**: [`../categories/data_structures/interval_union_sorted_gap_prefix_sums.md`](../categories/data_structures/interval_union_sorted_gap_prefix_sums.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Binary Search / Prefix Sums`  
- **Topic (Skill)**: `Interval Union under Bounded Expansion via Sorted Gap Prefix Sums`  

---

## 1. Problem Statement & Key Idea
Given N matched line positions L_1 < L_2 < ... < L_N in an all-line file. Answer M queries (X, Y): each match displays [L_i - X, L_i + Y] clamped to [1, all]. Output the number of uniquely displayed lines.

Match intervals expand by X to the left and Y to the right (total expansion S = X + Y between adjacent matches). The gap between L_i and L_{i+1} is d_i = L_{i+1} - L_i - 1. The number of covered lines between them is min(d_i, S). Sort all gaps d_i; for each query S, binary search splits gaps into those <= S (sum from prefix sums) and those > S ((count) * S). Boundary matches expand by min(X, L_1 - 1) and min(Y, all - L_N).

## 2. Core Observation & Invariant
Sorting gaps once in O(N log N) allows answering each query in O(log N).

## 3. Step-by-Step Algorithm
1. Compute gaps d_i = L_{i+1} - L_i - 1 for i = 1..N-1.
2. Sort gaps and compute prefix sums.
3. For each query (X, Y): S = X + Y.
4. idx = upper_bound(d.begin(), d.end(), S) - d.begin().
5. ans = N + min(X, L_1 - 1) + min(Y, all - L_N) + pref[idx] + (N - 1 - idx) * S.
6. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + M log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long all;
    int n, m;
    if (!(cin >> all >> n >> m)) return 0;

    vector<long long> l(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i];
    }

    vector<long long> d(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        d[i] = l[i + 1] - l[i] - 1;
    }
    sort(d.begin(), d.end());

    vector<long long> pref(n, 0);
    for (int i = 0; i < n - 1; ++i) {
        pref[i + 1] = pref[i] + d[i];
    }

    for (int q = 0; q < m; ++q) {
        long long x, y;
        cin >> x >> y;

        long long left_ext = min(x, l[0] - 1);
        long long right_ext = min(y, all - l[n - 1]);
        long long s = x + y;

        int idx = upper_bound(d.begin(), d.end(), s) - d.begin();
        long long gap_sum = pref[idx] + (long long)(n - 1 - idx) * s;

        long long ans = n + left_ext + right_ext + gap_sum;
        cout << ans << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Binary search on sorted gap differences to evaluate bounded interval unions in logarithmic time.
- **Reusable Pattern**: `Interval Union on Points: sum(min(gap_i, S)) answered via binary search on sorted gaps.`
