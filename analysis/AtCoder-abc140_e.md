# Problem Analysis: AtCoder-abc140_e — Second Sum

**Problem ID**: `AtCoder-abc140_e`  
**Contest**: `abc140`  
**Rating / Difficulty**: 1873  
**URL**: https://atcoder.jp/contests/abc140/tasks/abc140_e  
**VJudge Tag**: `[problem:AtCoder-abc140_e]`  
**Category File**: [`../categories/data_structures/second_largest_contribution_ordered_set.md`](../categories/data_structures/second_largest_contribution_ordered_set.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Ordered Set / Predecessors`  
- **Topic (Skill)**: `Second Largest Element Contribution via Ordered Set Predecessors/Successors`  

---

## 1. Problem Statement & Key Idea
Given permutation P of length N. Find sum_{1 <= l < r <= N} X_{l, r}, where X_{l, r} is the second largest element in subarray P[l..r].

**Key Insight**: Process elements in descending order of value, inserting their indices into an active ordered set. When processing index i with value v, find the two predecessors (L_2, L_1) and two successors (R_1, R_2) in the set.

## 2. Core Observation & Invariant
Element v is the second largest in subarrays containing exactly one larger element on the left ((L_1 - L_2) * (R_1 - i) subarrays) or exactly one larger element on the right ((i - L_1) * (R_2 - R_1) subarrays).

## 3. Step-by-Step Algorithm
1. Store indices of values 1..N.
2. Initialize std::multiset with sentinels {0, 0, N + 1, N + 1}.
3. For v = N down to 1:
4.   i = pos[v].
5.   Find iterator it = set.lower_bound(i).
6.   R_1 = *it, R_2 = *next(it).
7.   L_1 = *prev(it), L_2 = *prev(prev(it)).
8.   count = (L_1 - L_2) * (R_1 - i) + (i - L_1) * (R_2 - R_1).
9.   ans += v * count.
10.   set.insert(i).
11. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> pos(n + 1);
    for (int i = 1; i <= n; ++i) {
        int p;
        cin >> p;
        pos[p] = i;
    }

    multiset<int> s;
    s.insert(0); s.insert(0);
    s.insert(n + 1); s.insert(n + 1);

    long long ans = 0;

    for (int v = n; v >= 1; --v) {
        int i = pos[v];
        auto it = s.lower_bound(i);
        long long r1 = *it;
        long long r2 = *next(it);
        long long l1 = *prev(it);
        long long l2 = *prev(prev(it));

        long long ways = (l1 - l2) * (r1 - i) + (i - l1) * (r2 - r1);
        ans += (long long)v * ways;

        s.insert(i);
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Inverting subarray queries into element contribution sums using dynamic order-statistic bounds.
- **Reusable Pattern**: `Second-Largest Contribution: (L1 - L2)*(R1 - i) + (i - L1)*(R2 - R1) using ordered set.`
