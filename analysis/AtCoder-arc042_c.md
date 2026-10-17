# Problem Analysis: AtCoder-arc042_c — おやつ

**Problem ID**: `AtCoder-arc042_c`  
**Contest**: `arc042`  
**Rating / Difficulty**: 1746  
**URL**: https://atcoder.jp/contests/arc042/tasks/arc042_c  
**VJudge Tag**: `[problem:AtCoder-arc042_c]`  
**Category File**: [`../categories/dp/descending_sort_knapsack_exempt_heaviest.md`](../categories/dp/descending_sort_knapsack_exempt_heaviest.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Knapsack DP`  
- **Topic (Skill)**: `Descending Sort Relaxation on Knapsack Boundary (Exempt Heaviest Item)`  

---

## 1. Problem Statement & Key Idea
Given N snacks with weight a_i and deliciousness b_i. You can choose snacks such that: removing the single heaviest snack chosen leaves the remaining snacks with total weight <= L. Maximize total deliciousness. (N, L <= 5000).

**Key Insight**: Sort snacks by weight descending: a_1 >= a_2 >= ... >= a_N. If snack i is the heaviest item in the chosen subset, all other chosen snacks must come from {i+1, ..., N} and their sum of weights must be <= L.

## 2. Core Observation & Invariant
Process snacks in descending order of weight. For snack i, answer candidate is b_i + max_{w <= L} dp[w]. Then insert snack i into the 0-1 knapsack DP of capacity L.

## 3. Step-by-Step Algorithm
1. Sort items by weight descending.
2. Initialize dp[L + 1] = 0.
3. ans = 0.
4. For each item (a_i, b_i):
5.   max_rest = max_{w <= L} dp[w].
6.   ans = max(ans, b_i + max_rest).
7.   For w = L down to a_i:
8.     dp[w] = max(dp[w], dp[w - a_i] + b_i).
9. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * L)`
- **Space Complexity**: `O(L)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    int a, b;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, l;
    if (!(cin >> n >> l)) return 0;

    vector<Item> items(n);
    for (int i = 0; i < n; ++i) {
        cin >> items[i].a >> items[i].b;
    }

    sort(items.begin(), items.end(), [](const Item& x, const Item& y) {
        return x.a > y.a;
    });

    vector<int> dp(l + 1, 0);
    int max_ans = 0;

    for (int i = 0; i < n; ++i) {
        int best_prev = 0;
        for (int w = 0; w <= l; ++w) {
            best_prev = max(best_prev, dp[w]);
        }
        max_ans = max(max_ans, items[i].b + best_prev);

        for (int w = l; w >= items[i].a; --w) {
            dp[w] = max(dp[w], dp[w - items[i].a] + items[i].b);
        }
    }

    cout << max_ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Relaxed knapsack boundary conditions solved by descending sort order.
- **Reusable Pattern**: `Exempt Extreme Item Knapsack: Sort descending, treat item i as exempt extreme, update 1D DP.`
