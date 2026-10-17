# Problem Analysis: AtCoder-arc134_d — Concatenate Subsequences

**Problem ID**: `AtCoder-arc134_d`  
**Contest**: `arc134`  
**Rating / Difficulty**: 1998  
**URL**: https://atcoder.jp/contests/arc134/tasks/arc134_d  
**VJudge Tag**: `[problem:AtCoder-arc134_d]`  
**Category File**: [`../categories/basics/two_phase_greedy_concatenated_subsequence.md`](../categories/basics/two_phase_greedy_concatenated_subsequence.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Lexicographical Minimal Concatenated Subsequence via Two-Phase Greedy Selection`  

---

## 1. Problem Statement & Key Idea
Given arrays a_1..a_N and b_1..b_N. Choose a non-empty index sequence i_1 < ... < i_k to form sequence x = (a_{i_1}..a_{i_k}, b_{i_1}..b_{i_k}). Find the lexicographically smallest x.

The first element of x must be the global minimum of a: m = min(a). If there exists any index i with a_i = m such that b_i <= m, then selecting ONLY this single index i yields (m, b_i) with b_i <= m, which is strictly smaller than any sequence starting with (m, >m). If no such index exists, we must select ALL occurrences of m. Let the minimum b among all chosen indices be min_b. We can then greedily append subsequent elements j with a_j < min_b, or if a_j == min_b, only if the resulting b_j maintains lexicographical superiority.

## 2. Core Observation & Invariant
Single-element shortcut (m, b_i <= m) beats multi-element sequences; otherwise mandatory selection of all minimums sets the upper bound on subsequent choices.

## 3. Step-by-Step Algorithm
1. Find global min m = min(a).
2. Check if any i with a[i] == m has b[i] <= m. If so, choose the one with smallest b[i] and print [m, b[i]].
3. Otherwise, collect all indices with a[i] == m.
4. Let min_b = min(b[i] for selected i).
5. For subsequent indices j > last_idx: if a[j] < min_b, greedily select j.
6. Handle border case where a[j] == min_b by checking if first differing b is smaller than min_b.
7. Print concatenated sequence a_indices followed by b_indices.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
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

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n), b(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];

    int min_a = *min_element(a.begin(), a.end());

    int best_single_b = 2e9;
    for (int i = 0; i < n; ++i) {
        if (a[i] == min_a && b[i] <= min_a) {
            best_single_b = min(best_single_b, b[i]);
        }
    }

    if (best_single_b <= min_a) {
        cout << min_a << " " << best_single_b << "\n";
        return 0;
    }

    vector<int> idx;
    for (int i = 0; i < n; ++i) {
        if (a[i] == min_a) {
            idx.push_back(i);
        }
    }

    int min_b = 2e9;
    for (int i : idx) {
        min_b = min(min_b, b[i]);
    }

    // Determine whether to accept a[j] == min_b
    bool take_equal = false;
    for (int i : idx) {
        if (b[i] != min_b) {
            take_equal = (b[i] < min_b);
            break;
        }
    }

    int cur_idx = idx.back();
    for (int i = cur_idx + 1; i < n; ++i) {
        if (a[i] < min_b || (a[i] == min_b && take_equal)) {
            if (idx.empty() || a[i] >= a[idx.back()]) {
                idx.push_back(i);
            }
        }
    }

    vector<int> ans;
    for (int i : idx) ans.push_back(a[i]);
    for (int i : idx) ans.push_back(b[i]);

    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << (i + 1 == (int)ans.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Two-phase lexicographical greedy optimization with boundary shortcuts.
- **Reusable Pattern**: `Concatenated Subsequence Greedy: Check single-element shortcut (m, b_i <= m); else collect all minimums.`
