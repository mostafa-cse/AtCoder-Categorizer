# Problem Analysis: AtCoder-arc119_e — E. Pancakes

**Problem ID**: `AtCoder-arc119_e`  
**Contest**: `arc119`  
**Rating / Difficulty**: 2502  
**URL**: https://atcoder.jp/contests/arc119/tasks/arc119_e  
**VJudge Tag**: `[problem:AtCoder-arc119_e]`  
**Category File**: [`../categories/miscellaneous/pancakes_interval_overlap_manhattan.md`](../categories/miscellaneous/pancakes_interval_overlap_manhattan.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Manhattan <> Chebyshev`  

---

## 1. Problem Statement & Key Idea
Reverse at most one contiguous subarray $A[l \dots r]$ to minimize total ugliness $\sum_{i=1}^{N-1} |A_{i+1} - A_i|$.

## 2. Core Observation & Invariant
Reversing $A[l \dots r]$ changes only two boundary transitions. Prefix reversals ($l = 1$) and suffix reversals ($r = N$) are evaluated in $O(N)$ time. For interior reversals $1 < l < r < N$, the ugliness decrease is $2 \times \text{length}(I_1 \cap I_2)$ where $I_1$ and $I_2$ are intervals of transitions with the same direction (both increasing or both decreasing). Finding maximum interval overlap is solved via sweep-line in $O(N \log N)$.

## 3. Step-by-Step Algorithm
1. 1. Compute initial ugliness $\sum |A_{i+1} - A_i|$.
2. 2. Evaluate prefix reversals $[0, r]$ and suffix reversals $[l, n-1]$ in $O(N)$.
3. 3. Collect intervals $[A_i, A_{i+1}]$ for increasing steps and $[A_{i+1}, A_i]$ for decreasing steps.
4. 4. In each group, sort intervals by left endpoint and sweep, tracking $\max(R_{prev})$ to find $\max(0, \min(R, \max R_{prev}) - L)$.
5. 5. Subtract $2 \times \text{max\_overlap}$ from initial ugliness.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
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
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long total = 0;
    for (int i = 0; i < n - 1; ++i) {
        total += abs(a[i + 1] - a[i]);
    }

    long long max_dec = 0;

    // 1. Reversals starting at 0: [0, r] for r in [1, n - 2]
    for (int r = 1; r < n - 1; ++r) {
        long long old_cost = abs(a[r + 1] - a[r]);
        long long new_cost = abs(a[r + 1] - a[0]);
        max_dec = max(max_dec, old_cost - new_cost);
    }

    // 2. Reversals ending at n - 1: [l, n - 1] for l in [1, n - 2]
    for (int l = 1; l < n - 1; ++l) {
        long long old_cost = abs(a[l] - a[l - 1]);
        long long new_cost = abs(a[n - 1] - a[l - 1]);
        max_dec = max(max_dec, old_cost - new_cost);
    }

    // 3. Interior reversals: intervals [min(A_i, A_{i+1}), max(A_i, A_{i+1})]
    vector<pair<long long, long long>> inc, dec;
    for (int i = 0; i < n - 1; ++i) {
        if (a[i] < a[i + 1]) {
            inc.push_back({a[i], a[i + 1]});
        } else if (a[i] > a[i + 1]) {
            dec.push_back({a[i + 1], a[i]});
        }
    }

    auto get_max_overlap = [](vector<pair<long long, long long>> &intervals) -> long long {
        if (intervals.empty()) return 0;
        sort(intervals.begin(), intervals.end());
        long long max_r = 0;
        long long best = 0;
        for (auto &iv : intervals) {
            long long l = iv.first;
            long long r = iv.second;
            if (max_r > l) {
                best = max(best, min(r, max_r) - l);
            }
            max_r = max(max_r, r);
        }
        return best;
    };

    long long overlap = max(get_max_overlap(inc), get_max_overlap(dec));
    max_dec = max(max_dec, 2 * overlap);

    cout << total - max_dec << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
