# Problem Analysis: AtCoder-abc204_d — Cooking

**Problem ID**: `AtCoder-abc204_d`  
**Contest**: `abc204`  
**Rating / Difficulty**: 832  
**URL**: https://atcoder.jp/contests/abc204/tasks/abc204_d  
**VJudge Tag**: `[problem:AtCoder-abc204_d]`  
**Category File**: [`../categories/dp/dual_partition_subset_sum_bitset.md`](../categories/dp/dual_partition_subset_sum_bitset.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Dual Partition Subset Sum via Bitset Optimization`  

---

## 1. Problem Statement & Key Idea
N dishes with cooking times T_1, ..., T_N are cooked using 2 identical ovens (N <= 100, sum T_i <= 10^5). Each oven bakes one dish at a time. Minimize the time until all dishes are finished.

**Key Idea**: If oven 1 cooks a subset of dishes taking time s, oven 2 takes sum(T) - s. The completion time is max(s, sum(T) - s). We want to find a reachable subset sum s >= ceil(sum(T) / 2) minimizing s.

## 2. Core Observation & Invariant
This is 0-1 Subset Sum Knapsack. Because sum(T) <= 10^5 and N <= 100, std::bitset<100005> enables ultra-fast O(N * sum(T) / 64) DP transitions: dp |= (dp << t).

## 3. Step-by-Step Algorithm
1. Calculate total_time = sum(T_i).
2. Initialize bitset<100005> dp; dp[0] = 1.
3. For each dish time t: dp |= (dp << t).
4. Find smallest s >= (total_time + 1) / 2 such that dp[s] == 1.
5. Output s.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * sum(T) / 64)`
- **Space Complexity**: `O(sum(T) / 64)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <bitset>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> t(n);
    int total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> t[i];
        total += t[i];
    }

    bitset<100005> dp;
    dp[0] = 1;

    for (int x : t) {
        dp |= (dp << x);
    }

    int target = (total + 1) / 2;
    for (int s = target; s <= total; ++s) {
        if (dp[s]) {
            cout << s << "\n";
            return 0;
        }
    }

    cout << total << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Subset sum reachability optimization using bitset shifts.
- **Reusable Pattern**: `Bitset knapsack reachability: dp |= (dp << weight).`
