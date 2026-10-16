# Problem Analysis: AtCoder-arc086_b — Non-decreasing

**Problem ID**: `AtCoder-arc086_b`  
**Contest**: `abc081`  
**Rating / Difficulty**: 1567  
**URL**: https://atcoder.jp/contests/abc081/tasks/arc086_b  
**VJudge Tag**: `[problem:AtCoder-arc086_b]`  
**Category File**: [`../categories/basics/constructive_cumulative_addition_dominant_extremum.md`](../categories/basics/constructive_cumulative_addition_dominant_extremum.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Constructive Algorithms`  
- **Topic (Skill)**: `Constructive Prefix/Suffix Cumulative Addition via Global Dominant Extremum`  

---

## 1. Problem Statement & Key Idea
Given an array A of length N (N <= 50). In one operation, choose indices x and y and set A[y] += A[x]. Make A non-decreasing in at most 2N operations.

**Key Insight**: Find the element with maximum absolute value |A[m]|. If A[m] >= 0, add A[m] to all elements to make them non-negative, then perform forward prefix cumulative additions. If A[m] < 0, add A[m] to all elements to make them non-positive, then perform backward suffix cumulative additions.

## 2. Core Observation & Invariant
Once all elements are non-negative, A[i] += A[i-1] for i = 2..N guarantees A[i] >= A[i-1] because A[i-1] >= 0. Similarly, once all elements are non-positive, A[i] += A[i+1] for i = N-1 down to 1 guarantees non-decreasing order. Each phase takes N - 1 operations, total <= 2N - 2 <= 2N operations.

## 3. Step-by-Step Algorithm
1. Find index m with maximum |A[m]|.
2. If A[m] == 0, already non-decreasing; output 0.
3. Record operations list ops.
4. If A[m] > 0:
5.   Add m to all i != m (N - 1 operations).
6.   For i = 2 to N: add (i - 1) to i: ops.push_back({i - 1, i}).
7. If A[m] < 0:
8.   Add m to all i != m (N - 1 operations).
9.   For i = N - 1 down to 1: add (i + 1) to i: ops.push_back({i + 1, i}).
10. Print ops.size(), then all operations.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    int max_idx = 1;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        if (abs(a[i]) > abs(a[max_idx])) {
            max_idx = i;
        }
    }

    vector<pair<int, int>> ops;

    if (a[max_idx] >= 0) {
        // Make all elements non-negative
        for (int i = 1; i <= n; ++i) {
            if (i != max_idx) {
                ops.push_back({max_idx, i});
            }
        }
        // Prefix sum sweep
        for (int i = 2; i <= n; ++i) {
            ops.push_back({i - 1, i});
        }
    } else {
        // Make all elements non-positive
        for (int i = 1; i <= n; ++i) {
            if (i != max_idx) {
                ops.push_back({max_idx, i});
            }
        }
        // Suffix sum sweep
        for (int i = n - 1; i >= 1; --i) {
            ops.push_back({i + 1, i});
        }
    }

    cout << ops.size() << "\n";
    for (const auto& op : ops) {
        cout << op.first << " " << op.second << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Sign homogenization using the dominant absolute extremum followed by cumulative monotonic sweeping.
- **Reusable Pattern**: `Make Non-Decreasing in 2N: add dominant element to all, then prefix/suffix cumulative sum.`
