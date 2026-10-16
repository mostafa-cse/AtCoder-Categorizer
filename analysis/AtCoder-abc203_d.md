# Problem Analysis: AtCoder-abc203_d — Pond

**Problem ID**: `AtCoder-abc203_d`  
**Contest**: `abc203`  
**Rating / Difficulty**: 1622  
**URL**: https://atcoder.jp/contests/abc203/tasks/abc203_d  
**VJudge Tag**: `[problem:AtCoder-abc203_d]`  
**Category File**: [`../categories/basics/binary_search_2d_subgrid_median.md`](../categories/basics/binary_search_2d_subgrid_median.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search on Answer`  
- **Topic (Skill)**: `2D Subgrid Median via Binary Search on Answer + 2D Prefix Sums`  

---

## 1. Problem Statement & Key Idea
An N x N grid of heights. Find the minimum median among all K x K subgrids. The median of a K x K subgrid is the (floor(K^2 / 2) + 1)-th largest element.

**Key Insight**: Binary search on the answer X. A subgrid has median <= X iff the number of elements STRICTLY GREATER than X in the subgrid is at most floor(K^2 / 2).

## 2. Core Observation & Invariant
For a fixed candidate X, construct a binary matrix B where B[i][j] = (A[i][j] > X ? 1 : 0). A K x K subgrid has sum of B <= floor(K^2 / 2) iff its median <= X. Check all (N - K + 1)^2 subgrids in O(N^2) using 2D prefix sums.

## 3. Step-by-Step Algorithm
1. Binary search on X in [0, 10^9].
2. Define check(X):
3.   Build 2D prefix sum of B where B[i][j] = (A[i][j] > X).
4.   For each (r, c) such that r + K - 1 <= N and c + K - 1 <= N:
5.     count_greater = subgrid_sum(r, c, r + K - 1, c + K - 1).
6.     If count_greater <= K*K / 2: return true.
7.   Return false.
8. Output minimal X with check(X) == true.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 log(max A))`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<vector<int>> a(n + 1, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> a[i][j];
        }
    }

    int lim = (k * k) / 2;
    int low = 0, high = 1e9;
    int ans = high;

    vector<vector<int>> pref(n + 1, vector<int>(n + 1, 0));

    auto check = [&](int x) -> bool {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                int val = (a[i][j] > x ? 1 : 0);
                pref[i][j] = val + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
            }
        }

        for (int i = k; i <= n; ++i) {
            for (int j = k; j <= n; ++j) {
                int count = pref[i][j] - pref[i - k][j] - pref[i][j - k] + pref[i - k][j - k];
                if (count <= lim) return true;
            }
        }
        return false;
    };

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
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
- **Core Skill**: Median query reduction to 2D binary indicator threshold counting.
- **Reusable Pattern**: `Subgrid Median Binary Search: indicator B[i][j] = (A[i][j] > X), check subgrid_sum <= K^2/2.`
