# Problem Analysis: AtCoder-arc037_c — 億マス計算

**Problem ID**: `AtCoder-arc037_c`  
**Contest**: `arc037`  
**Rating / Difficulty**: 1824  
**URL**: https://atcoder.jp/contests/arc037/tasks/arc037_c  
**VJudge Tag**: `[problem:AtCoder-arc037_c]`  
**Category File**: [`../categories/basics/binary_search_kth_matrix_product.md`](../categories/basics/binary_search_kth_matrix_product.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search`  
- **Topic (Skill)**: `Binary Search on Answer for K-th Matrix Product / Multi-Set Item`  

---

## 1. Problem Statement & Key Idea
Given two arrays A and B of length N (N <= 30000). Matrix C has C_{i, j} = A_i * B_j. Find the K-th smallest element among all N^2 elements of C.

**Key Insight**: Binary search on the product value X in [1, 10^{18}]. For a fixed X, count pairs (i, j) with A_i * B_j <= X in O(N log N) using upper_bound on sorted B.

## 2. Core Observation & Invariant
Sorting B takes O(N log N). In each step of binary search, sum_{i=1}^N upper_bound(B, X / A_i) counts valid elements in O(N log N). Total operations: 60 * 30000 * 15 ~ 2.7 * 10^7.

## 3. Step-by-Step Algorithm
1. Sort array B.
2. low = 1, high = 10^18, ans = high.
3. While low <= high:
4.   mid = low + (high - low) / 2.
5.   count = 0.
6.   For i = 0 to N - 1:
7.     count += upper_bound(B, mid / A_i) - B.begin().
8.   if count >= K: ans = mid, high = mid - 1.
9.   else low = mid + 1.
10. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N * log(max_ans))`
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
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];

    sort(b.begin(), b.end());

    long long low = 1, high = 1e18, ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        long long count = 0;

        for (int i = 0; i < n; ++i) {
            long long target = mid / a[i];
            auto it = upper_bound(b.begin(), b.end(), target);
            count += (it - b.begin());
        }

        if (count >= k) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting Cartesian product elements <= X via binary search on answer with sorted array upper bounds.
- **Reusable Pattern**: `K-th Matrix Element Search: Binary search value X + sum upper_bound(B, X / A_i).`
