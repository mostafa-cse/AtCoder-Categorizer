# Problem Analysis: AtCoder-typical90_ay — Typical Shop

**Problem ID**: `AtCoder-typical90_ay`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 051)  
**Rating / Difficulty**: 1750 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ay  
**VJudge Tag**: `[problem:AtCoder-typical90_ay]`  
**Category File**: [`../categories/basics/meet_in_the_middle.md`](../categories/basics/meet_in_the_middle.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Meet in the Middle`  
- **Topic (Skill)**: `Meet-in-the-Middle with Cardinality and Value Constraints`  

---

## 1. Problem Statement & Key Idea
N items (N <= 40) with price A_i. Choose exactly K items such that total price <= P. Count ways.

**Core Idea**: N = 40 is too large for 2^N brute force, but 2^(N/2) = 2^20 ≈ 10^6 is fast. Split items into two halves (Meet in the Middle).

## 2. Core Observation & Invariant
Group subsets of half 1 by item count: list1[c] stores prices. Group subsets of half 2 by count: list2[c]. For each count c, sort list2[K - c] and use std::upper_bound to count prices <= P - price1.

## 3. Step-by-Step Algorithm
1. Split A into left (size n1 = N/2) and right (size n2 = N - n1).
2. Enumerate 2^n1 subsets -> group by count of chosen items.
3. Enumerate 2^n2 subsets -> group by count, sort each group.
4. For each count c in 0..K: for price in group1[c]: binary search count in group2[K - c] with price <= P - price.
5. Output total ways.

## 4. Complexity Analysis
Time: O(2^(N/2) * (N/2) log(2^(N/2))), Space: O(2^(N/2)).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void enumerate(const vector<long long>& a, vector<vector<long long>>& groups) {
    int n = a.size();
    int total = 1 << n;
    for (int mask = 0; mask < total; ++mask) {
        int cnt = 0;
        long long sum = 0;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                cnt++;
                sum += a[i];
            }
        }
        groups[cnt].push_back(sum);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    long long p;
    if (!(cin >> n >> k >> p)) return 0;

    int n1 = n / 2;
    int n2 = n - n1;

    vector<long long> a1(n1), a2(n2);
    for (int i = 0; i < n1; ++i) cin >> a1[i];
    for (int i = 0; i < n2; ++i) cin >> a2[i];

    vector<vector<long long>> g1(n1 + 1), g2(n2 + 1);
    enumerate(a1, g1);
    enumerate(a2, g2);

    for (int i = 0; i <= n2; ++i) {
        sort(g2[i].begin(), g2[i].end());
    }

    long long ans = 0;
    for (int c1 = 0; c1 <= n1 && c1 <= k; ++c1) {
        int c2 = k - c1;
        if (c2 < 0 || c2 > n2) continue;
        for (long long sum1 : g1[c1]) {
            if (sum1 > p) continue;
            long long rem = p - sum1;
            auto it = upper_bound(g2[c2].begin(), g2[c2].end(), rem);
            ans += (it - g2[c2].begin());
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Meet-in-the-middle splitting 40 items into 20 + 20 with cardinality-indexed binary search.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Meet-in-the-middle technique, subset generation, and cardinality-indexed binary search lookups.
- **Reusable Pattern**: `Meet-in-the-Middle with Cardinality Grouping.`

---
Back to [Meet-in-the-Middle with Cardinality and Value Constraints](../categories/basics/meet_in_the_middle.md) | [Categories Directory](../categories/README.md)