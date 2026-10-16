# Problem Analysis: AtCoder-arc017_3 — Minimalist

**Problem ID**: `AtCoder-arc017_3`  
**Contest**: `arc017`  
**Rating / Difficulty**: 1625  
**URL**: https://atcoder.jp/contests/arc017/tasks/arc017_3  
**VJudge Tag**: `[problem:AtCoder-arc017_3]`  
**Category File**: [`../categories/basics/meet_in_the_middle_exact_subset_sum.md`](../categories/basics/meet_in_the_middle_exact_subset_sum.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Meet-in-the-Middle`  
- **Topic (Skill)**: `Meet-in-the-Middle on Subset Sum N <= 32`  

---

## 1. Problem Statement & Key Idea
Given N items with weights w_i (N <= 32) and target capacity X <= 10^9. Find the number of subsets of items whose total weight is EXACTLY X.

**Key Insight**: Split the N items into two halves of size <= 16. Generate all 2^16 subset sums for the first half, sort them, and for each sum in the second half, count matching complements X - sum.

## 2. Core Observation & Invariant
2^32 is ~ 4 * 10^9 (impossible), but 2^16 is 65,536. Generating all subset sums for both halves and using two pointers or binary search (equal_range) takes O(2^(N/2) log(2^(N/2))) operations, running in < 0.1s.

## 3. Step-by-Step Algorithm
1. Split items into left half (size n1 = N/2) and right half (size n2 = N - n1).
2. Generate all 2^n1 subset sums for left half: sums1.
3. Generate all 2^n2 subset sums for right half: sums2.
4. Sort sums2 in ascending order.
5. ans = 0.
6. For each s in sums1:
7.   auto [it1, it2] = equal_range(sums2.begin(), sums2.end(), X - s);
8.   ans += (it2 - it1);
9. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^(N/2) * (N/2))`
- **Space Complexity**: `O(2^(N/2))`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void generate_sums(const vector<long long>& a, vector<long long>& sums) {
    sums.push_back(0);
    for (long long x : a) {
        int sz = sums.size();
        for (int i = 0; i < sz; ++i) {
            sums.push_back(sums[i] + x);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long X;
    if (!(cin >> n >> X)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int mid = n / 2;
    vector<long long> left_a(a.begin(), a.begin() + mid);
    vector<long long> right_a(a.begin() + mid, a.end());

    vector<long long> sums1, sums2;
    generate_sums(left_a, sums1);
    generate_sums(right_a, sums2);

    sort(sums2.begin(), sums2.end());

    long long count = 0;
    for (long long s : sums1) {
        auto [it1, it2] = equal_range(sums2.begin(), sums2.end(), X - s);
        count += (it2 - it1);
    }

    cout << count << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Meet-in-the-middle subset sum exact match counting using binary search range.
- **Reusable Pattern**: `Exact Subset Sum N <= 36: generate 2^(N/2) halves, sort second half, equal_range for complement.`
