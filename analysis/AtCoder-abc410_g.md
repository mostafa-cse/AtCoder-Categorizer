# Problem Analysis: AtCoder-abc410_g — Longest Chord Chain

**Problem ID**: `AtCoder-abc410_g`  
**Contest**: `abc410`  
**Rating / Difficulty**: 2242  
**URL**: https://atcoder.jp/contests/abc410/tasks/abc410_g  
**VJudge Tag**: `[problem:AtCoder-abc410_g]`  
**Category File**: [`../categories/dp/longest_chord_chain_nested_intervals_lis.md`](../categories/dp/longest_chord_chain_nested_intervals_lis.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Longest Increasing Subsequence (LIS)`  

---

## 1. Problem Statement & Key Idea
Select a subset of pairwise non-intersecting circle chords such that a single newly added chord can intersect as many of them as possible.

## 2. Core Observation & Invariant
A single chord cuts the circle into two arcs and intersects a set of pairwise non-intersecting chords iff their intervals are mutually strictly nested: I_1 subset I_2 subset ... subset I_k. Each given chord (a, b) with a < b corresponds to two circular intervals: [a, b] and [b, a + 2N]. A set of chords can be intersected simultaneously iff their chosen intervals form a nested chain. Sorting all 2N intervals by right endpoint R in descending order (with ties broken by L ascending) reduces finding the maximum nested chain to finding the Longest Increasing Subsequence (LIS) on the left endpoints L.

## 3. Step-by-Step Algorithm
1. 1. For each of the N chords (a, b) with a < b, generate intervals [a, b] and [b, a + 2N].
2. 2. Sort the 2N intervals primarily by R descending, secondarily by L ascending.
3. 3. Compute the LIS on the sequence of left endpoints L using binary search (lower_bound).
4. 4. The length of the LIS is the maximum number of intersecting chords.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    // Each chord (a, b) with a < b produces two intervals: [a, b] and [b, a + 2n]
    vector<pair<int, int>> intervals;
    intervals.reserve(2 * n);

    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        if (a > b) swap(a, b);
        intervals.push_back({a, b});
        intervals.push_back({b, a + 2 * n});
    }

    // Sort by second (R) descending.
    // If second is equal, sort by first (L) ascending so we cannot pick two intervals with the same R!
    sort(intervals.begin(), intervals.end(), [](const pair<int, int>& x, const pair<int, int>& y) {
        if (x.second != y.second) return x.second > y.second;
        return x.first < y.first;
    });

    // LIS on first (L)
    // For nested intervals: I_k contains I_{k+1} means R_k > R_{k+1} and L_k < L_{k+1}.
    // Since R is decreasing, we need L to be strictly increasing!
    vector<int> lis;
    for (const auto& interval : intervals) {
        int l = interval.first;
        auto it = lower_bound(lis.begin(), lis.end(), l);
        if (it != lis.end()) {
            *it = l;
        } else {
            lis.push_back(l);
        }
    }

    cout << lis.size() << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
