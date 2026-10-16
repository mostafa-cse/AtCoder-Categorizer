# Problem Analysis: AtCoder-typical90_bl — Uplift

**Problem ID**: `AtCoder-typical90_bl`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 064)  
**Rating / Difficulty**: 800 (★3)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bl  
**VJudge Tag**: `[problem:AtCoder-typical90_bl]`  
**Category File**: [`../categories/data_structures/difference_arrays_imos.md`](../categories/data_structures/difference_arrays_imos.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Prefix Sums & Difference Arrays`  
- **Topic (Skill)**: `Difference Array Local Perturbation for O(1) Range Update Inconvenience`  

---

## 1. Problem Statement & Key Idea
Array A of length N. Total inconvenience is sum_{i=1}^{N-1} |A_{i+1} - A_i|. Q queries: add V to range [L, R]. Print total inconvenience after each query.

**Core Idea**: Range addition [L, R] by V changes only TWO adjacent differences: D_{L-1} and D_R in the difference array D_i = A_{i+1} - A_i.

## 2. Core Observation & Invariant
Update total inconvenience in O(1) time per query by subtracting |D_old| and adding |D_new| at indices L-1 and R.

## 3. Step-by-Step Algorithm
1. Compute D_i = A_{i+1} - A_i and initial total_inconvenience = sum |D_i|.
2. For each query (L, R, V):
   - If L > 1: subtract |D_{L-1}|, D_{L-1} += V, add |D_{L-1}|.
   - If R < N: subtract |D_R|, D_R -= V, add |D_R|.
   - Print total_inconvenience.

## 4. Complexity Analysis
Time: O(N + Q), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<long long> d(n + 1, 0);
    long long total = 0;
    for (int i = 1; i < n; ++i) {
        d[i] = a[i + 1] - a[i];
        total += abs(d[i]);
    }

    while (q--) {
        int l, r;
        long long v;
        cin >> l >> r >> v;

        if (l > 1) {
            total -= abs(d[l - 1]);
            d[l - 1] += v;
            total += abs(d[l - 1]);
        }
        if (r < n) {
            total -= abs(d[r]);
            d[r] -= v;
            total += abs(d[r]);
        }

        cout << total << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Difference array local perturbation update in O(1).

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Maintaining global objective functions under range additions via difference array boundary perturbation.
- **Reusable Pattern**: `Difference Array Boundary Perturbation.`

---
Back to [Difference Array Local Perturbation for O(1) Range Update Inconvenience](../categories/data_structures/difference_arrays_imos.md) | [Categories Directory](../categories/README.md)