# Problem Analysis: AtCoder-arc063_b — An Invisible Hand

**Problem ID**: `AtCoder-arc063_b`  
**Contest**: `abc047`  
**Rating / Difficulty**: 1376  
**URL**: https://atcoder.jp/contests/abc047/tasks/arc063_b  
**VJudge Tag**: `[problem:AtCoder-arc063_b]`  
**Category File**: [`../categories/basics/stock_max_profit_pair_counting.md`](../categories/basics/stock_max_profit_pair_counting.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Prefix Minima`  
- **Topic (Skill)**: `Stock Buy-Low Sell-High Count of Max Profit Pairs`  

---

## 1. Problem Statement & Key Idea
Given prices A_1..A_N in N cities. You can buy 1 apple at town i and sell at town j (j > i) to make profit A_j - A_i. Find the minimum number of town prices to change to reduce the maximum achievable profit.

**Key Idea**: The maximum profit of a single transaction is max_diff = max_{j > i} (A_j - A_i). To reduce this maximum profit, every pair achieving this maximum profit must be disrupted.

## 2. Core Observation & Invariant
Maintain running minimum min_val as we scan j from 1 to N. The maximum profit ending at j is A_j - min_val. Count how many indices j achieve A_j - min_val == max_diff. Changing the price of town j disrupts this pair. Because the sell towns j for distinct maximal pairs cannot be simultaneously satisfied by a single alteration without changing their sell price, the answer is exactly the count of indices j achieving maximum profit!

## 3. Step-by-Step Algorithm
1. Scan j from 1 to N, maintaining min_val = min(A[0..j-1]).
2. Compute max_profit = max_j (A_j - min_val).
3. Count how many j achieve A_j - min_val == max_profit.
4. Print the count.

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
    long long t;
    if (!(cin >> n >> t)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long min_val = a[0];
    long long max_profit = 0;

    for (int i = 1; i < n; ++i) {
        max_profit = max(max_profit, a[i] - min_val);
        min_val = min(min_val, a[i]);
    }

    min_val = a[0];
    int count = 0;
    for (int i = 1; i < n; ++i) {
        if (a[i] - min_val == max_profit) {
            count++;
        }
        min_val = min(min_val, a[i]);
    }

    cout << count << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Prefix minimum running difference and disjoint bottleneck counting.
- **Reusable Pattern**: `Stock max profit pairs: count j where A[j] - pref_min == max_diff.`
