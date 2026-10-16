# Problem Analysis: AtCoder-abc227_d — Project Planning

**Problem ID**: `AtCoder-abc227_d`  
**Contest**: `abc227`  
**Rating / Difficulty**: 1643  
**URL**: https://atcoder.jp/contests/abc227/tasks/abc227_d  
**VJudge Tag**: `[problem:AtCoder-abc227_d]`  
**Category File**: [`../categories/basics/binary_search_capped_work_allocation.md`](../categories/basics/binary_search_capped_work_allocation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search on Answer`  
- **Topic (Skill)**: `Binary Search on Answer with Capped Work Allocations min(A_i, P)`  

---

## 1. Problem Statement & Key Idea
N departments with A_i employees. Each project requires exactly K employees from K DIFFERENT departments. Find the maximum number of projects that can be formed.

**Key Insight**: Binary search on the total number of projects P. Department i can contribute at most 1 employee per project, so it contributes at most min(A_i, P) employees. Forming P projects is feasible iff sum_{i=1}^N min(A_i, P) >= K * P.

## 2. Core Observation & Invariant
By Hall's marriage / max flow structure, the condition sum min(A_i, P) >= K * P is both necessary and sufficient. The check function is strictly monotonic in P.

## 3. Step-by-Step Algorithm
1. Binary search on P in range [1, (sum A) / K].
2. Define check(P):
3.   total_slots = 0.
4.   For each a in A: total_slots += min(a, P).
5.   Return total_slots >= K * P.
6. Find maximum P with check(P) == true.
7. Print P.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(sum A))`
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

    vector<long long> a(n);
    long long sum_a = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        sum_a += a[i];
    }

    long long low = 1, high = sum_a / k;
    long long ans = 0;

    auto check = [&](long long p) -> bool {
        long long total = 0;
        for (int i = 0; i < n; ++i) {
            total += min(a[i], p);
        }
        return total >= (__int128)k * p;
    };

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy work allocation feasibility with capacity capping min(A_i, P).
- **Reusable Pattern**: `Project Planning Feasibility: check(P) := sum min(A_i, P) >= K * P.`
