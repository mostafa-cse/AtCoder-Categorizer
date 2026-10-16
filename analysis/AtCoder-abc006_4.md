# Problem Analysis: AtCoder-abc006_4 — Playing Cards Insertion Sort

**Problem ID**: `AtCoder-abc006_4`  
**Contest**: `abc006`  
**Rating / Difficulty**: 1696  
**URL**: https://atcoder.jp/contests/abc006/tasks/abc006_4  
**VJudge Tag**: `[problem:AtCoder-abc006_4]`  
**Category File**: [`../categories/dp/minimum_insertions_lis.md`](../categories/dp/minimum_insertions_lis.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Longest Increasing Subsequence (LIS)`  
- **Topic (Skill)**: `Minimum Card Insertions = N - LIS(A) via Patience Sorting`  

---

## 1. Problem Statement & Key Idea
Given N cards with a permutation of numbers 1..N. In one operation, you can take any card and insert it at any position. Find the minimum operations to sort the cards in ascending order.

**Key Insight**: Any card that is NOT moved must maintain its relative order with other unmoved cards, meaning the unmoved cards must form an increasing subsequence. To minimize moved cards, maximize unmoved cards: min operations = N - LIS(A).

## 2. Core Observation & Invariant
Classic Longest Increasing Subsequence (LIS). Finding LIS(A) in O(N log N) using patience sorting / binary search (`std::lower_bound`) gives the exact answer N - LIS(A).

## 3. Step-by-Step Algorithm
1. Initialize tails array for patience sorting.
2. For each card x in permutation A:
3.   auto it = lower_bound(tails.begin(), tails.end(), x);
4.   If it == tails.end(): tails.push_back(x);
5.   Else: *it = x;
6. Print N - tails.size().

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
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
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> tails;
    for (int x : a) {
        auto it = lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) {
            tails.push_back(x);
        } else {
            *it = x;
        }
    }

    cout << n - tails.size() << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Reduction of insertion sort moves to Longest Increasing Subsequence complement.
- **Reusable Pattern**: `Minimum Insertion Moves: N - LIS(A) via lower_bound patience sorting.`
