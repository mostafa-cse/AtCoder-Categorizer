# Problem Analysis: AtCoder-arc092_c — E. Both Sides Merger

**Problem ID**: `AtCoder-arc092_c`  
**Contest**: `arc092`  
**Rating / Difficulty**: 2361  
**URL**: https://atcoder.jp/contests/arc092/tasks/arc092_c  
**VJudge Tag**: `[problem:AtCoder-arc092_c]`  
**Category File**: [`../categories/basics/same_parity_merger_constructive.md`](../categories/basics/same_parity_merger_constructive.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Array merging via neighbor replacement preserves relative index parity. Any achievable value is a non-empty sum of same-parity elements; greedy parity selection and $O(N)$ constructive trimming and collapsing deterministically yields the maximum sum.

## 2. Core Observation & Invariant
Choosing an internal element replaces it with the sum of its neighbors and deletes both neighbors, preserving the index parity of all remaining elements. Thus, any final single element is a sum of a non-empty subset of elements with identical original index parity (all odd or all even). The maximum sum is achieved by taking all positive elements of the superior parity (or the single maximum element if all are negative).

## 3. Step-by-Step Algorithm
1. Compare sum of positive elements at odd indices vs even indices (or max single element if all $\le 0$). Mark the chosen subset of kept elements.
2. Repeatedly delete elements beyond the last kept element and before the first kept element using endpoint deletions.
3. In the trimmed array (where index 1 is kept and all kept elements are at odd indices), repeatedly reduce the array: if index 3 is kept, choose index 2 (merging 1 and 3); if index 3 is not kept, choose index 3 (merging 2 and 4 to delete 3). Continue until length 1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    long long max_val = -2e18;
    int max_idx = -1;
    for (int i = 1; i <= n; i++) {
        if (a[i] > max_val) {
            max_val = a[i];
            max_idx = i;
        }
    }

    int best_parity = -1;
    long long best_sum = -2e18;
    vector<int> chosen;

    if (max_val <= 0) {
        best_sum = max_val;
        chosen.push_back(max_idx);
    } else {
        long long sum_odd = 0, sum_even = 0;
        vector<int> odd_pos, even_pos;
        for (int i = 1; i <= n; i++) {
            if (a[i] > 0) {
                if (i % 2 == 1) {
                    sum_odd += a[i];
                    odd_pos.push_back(i);
                } else {
                    sum_even += a[i];
                    even_pos.push_back(i);
                }
            }
        }
        if (sum_odd >= sum_even) {
            best_sum = sum_odd;
            chosen = odd_pos;
        } else {
            best_sum = sum_even;
            chosen = even_pos;
        }
    }

    vector<bool> keep(n + 1, false);
    for (int idx : chosen) keep[idx] = true;

    vector<int> ops;
    int cur_len = n;

    // 1. Delete elements after the last chosen
    int last_chosen = chosen.back();
    while (cur_len > last_chosen) {
        ops.push_back(cur_len);
        cur_len--;
    }

    // 2. Delete elements before the first chosen
    int first_chosen = chosen.front();
    for (int i = 1; i < first_chosen; i++) {
        ops.push_back(1);
        cur_len--;
    }

    // Build the current list of boolean keep
    vector<int> cur_keep;
    for (int i = first_chosen; i <= last_chosen; i++) {
        cur_keep.push_back(keep[i] ? 1 : 0);
    }

    // Now index 0 is kept, and all kept elements have even indices in 0-based indexing
    while (cur_keep.size() > 1) {
        if (cur_keep[2] == 1) {
            // Merge index 0 and index 2: choose 1 (1-based index 2)
            ops.push_back(2);
            cur_keep.erase(cur_keep.begin());
            cur_keep.erase(cur_keep.begin() + 1);
        } else {
            // Choose index 2 (1-based index 3)
            ops.push_back(3);
            cur_keep.erase(cur_keep.begin() + 1);
            cur_keep.erase(cur_keep.begin() + 2);
        }
    }

    cout << best_sum << "\n";
    cout << ops.size() << "\n";
    for (int op : ops) cout << op << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
