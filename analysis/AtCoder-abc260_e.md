# Problem Analysis: AtCoder-abc260_e — At Least One

**Problem ID**: `AtCoder-abc260_e`  
**Contest**: `abc260`  
**Rating / Difficulty**: 1692  
**URL**: https://atcoder.jp/contests/abc260/tasks/abc260_e  
**VJudge Tag**: `[problem:AtCoder-abc260_e]`  
**Category File**: [`../categories/basics/two_pointers_multi_interval_coverage.md`](../categories/basics/two_pointers_multi_interval_coverage.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Two Pointers`  
- **Topic (Skill)**: `Two Pointers / Sliding Window on Multi-Interval Coverage`  

---

## 1. Problem Statement & Key Idea
N pairs of integers (A_i, B_i) with 1 <= A_i < B_i <= M. An integer sequence f(k) counts intervals [l, r] of length k = r - l + 1 such that for every pair i, the interval contains at least one of A_i or B_i. Compute f(k) for all k = 1..M.

**Key Insight**: Two pointers! For each left endpoint l (1 <= l <= M), find the minimum right endpoint r such that [l, r] contains at least one number from every pair.

## 2. Core Observation & Invariant
If [l, r] is the minimal valid interval for l, then for any R in [r, M], [l, R] is also valid! Its length is k = R - l + 1, so all lengths in [r - l + 1, M - l + 1] receive +1. Add +1 to this range using a difference array.

## 3. Step-by-Step Algorithm
1. Store which pairs contain value x in occ[x].
2. Use two pointers (l = 1, r = 1) and maintain covered_pairs count.
3. While covered_pairs < N and r <= M: add r, r++.
4. For l from 1 to M:
5.   While r <= M and covered_pairs < N: add r, r++.
6.   If covered_pairs == N:
7.     min_k = (r - 1) - l + 1, max_k = M - l + 1.
8.     diff[min_k]++, diff[max_k + 1]--;
9.   Remove l from window.
10. Prefix sum diff array and print f(1..M).

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> occ(m + 1);
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        occ[a].push_back(i);
        occ[b].push_back(i);
    }

    vector<int> pair_cnt(n, 0);
    int covered = 0;
    int r = 1;

    vector<int> diff(m + 2, 0);

    for (int l = 1; l <= m; ++l) {
        while (r <= m && covered < n) {
            for (int p : occ[r]) {
                if (pair_cnt[p] == 0) covered++;
                pair_cnt[p]++;
            }
            r++;
        }

        if (covered == n) {
            int min_len = (r - 1) - l + 1;
            int max_len = m - l + 1;
            diff[min_len]++;
            diff[max_len + 1]--;
        }

        // Remove l
        for (int p : occ[l]) {
            pair_cnt[p]--;
            if (pair_cnt[p] == 0) covered--;
        }
    }

    int cur = 0;
    for (int k = 1; k <= m; ++k) {
        cur += diff[k];
        cout << cur << (k == m ? "\n" : " ");
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Two pointers minimal valid right endpoint sweep mapped to length contribution difference arrays.
- **Reusable Pattern**: `Minimal Window Coverage: two pointers finds min r for each l, adds to length range via diff array.`
