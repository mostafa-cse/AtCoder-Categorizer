# Problem Analysis: AtCoder-arc074_b — 3N Numbers

**Problem ID**: `AtCoder-arc074_b`  
**Contest**: `abc062`  
**Rating / Difficulty**: 1730  
**URL**: https://atcoder.jp/contests/abc062/tasks/arc074_b  
**VJudge Tag**: `[problem:AtCoder-arc074_b]`  
**Category File**: [`../categories/data_structures/dual_priority_queue_3n_split.md`](../categories/data_structures/dual_priority_queue_3n_split.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Priority Queue`  
- **Topic (Skill)**: `Dual Priority Queue Prefix/Suffix Optimization (3N Elements Partition)`  

---

## 1. Problem Statement & Key Idea
Given an array A of length 3N. Remove exactly N elements so that the sum of the first N remaining elements minus the sum of the last N remaining elements is maximized.

**Key Insight**: The split between the first N elements and the last N elements must occur at some boundary index k between N and 2N. Precompute L[k] = max sum of N elements from A[1..k] using a min-heap, and R[k] = min sum of N elements from A[k..3N] using a max-heap.

## 2. Core Observation & Invariant
Maximizing L[k] - R[k + 1] over all k in [N, 2N] gives the optimal answer in O(N log N).

## 3. Step-by-Step Algorithm
1. Maintain min-heap of size N for left prefix. Sweep k from 1 to 2N to populate L[k].
2. Maintain max-heap of size N for right suffix. Sweep k from 3N down to N + 1 to populate R[k].
3. Ans = max_{k=N..2N} (L[k] - R[k + 1]).
4. Print Ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_len = 3 * n;
    vector<long long> a(total_len + 1);
    for (int i = 1; i <= total_len; ++i) {
        cin >> a[i];
    }

    priority_queue<long long, vector<long long>, greater<long long>> min_pq;
    vector<long long> L(total_len + 1, 0);
    long long left_sum = 0;

    for (int i = 1; i <= total_len; ++i) {
        min_pq.push(a[i]);
        left_sum += a[i];
        if ((int)min_pq.size() > n) {
            left_sum -= min_pq.top();
            min_pq.pop();
        }
        if (i >= n) {
            L[i] = left_sum;
        }
    }

    priority_queue<long long> max_pq;
    vector<long long> R(total_len + 2, 0);
    long long right_sum = 0;

    for (int i = total_len; i >= 1; --i) {
        max_pq.push(a[i]);
        right_sum += a[i];
        if ((int)max_pq.size() > n) {
            right_sum -= max_pq.top();
            max_pq.pop();
        }
        if (i <= 2 * n + 1) {
            R[i] = right_sum;
        }
    }

    long long max_diff = -1e18;
    for (int k = n; k <= 2 * n; ++k) {
        max_diff = max(max_diff, L[k] - R[k + 1]);
    }

    cout << max_diff << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Prefix/suffix priority queue sweep for partition optimization.
- **Reusable Pattern**: `Dual Heap Partition: Min-heap for max top-K prefix and Max-heap for min top-K suffix.`
