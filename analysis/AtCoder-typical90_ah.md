# Problem Analysis: AtCoder-typical90_ah — There are few types of elements

**Problem ID**: `AtCoder-typical90_ah`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 034)  
**Rating / Difficulty**: 1250 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ah  
**VJudge Tag**: `[problem:AtCoder-typical90_ah]`  
**Category File**: [`../categories/data_structures/two_pointers_sliding_window.md`](../categories/data_structures/two_pointers_sliding_window.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Two Pointers / Sliding Window`  
- **Topic (Skill)**: `Two Pointers with Frequency Map / K-Distinct Subarray`  

---

## 1. Problem Statement & Key Idea
Given an array of length N (N <= 10^5) and integer K, find the maximum length of a contiguous subarray containing at most K distinct elements.

**Core Idea**: The subarray validity condition 'contains <= K distinct elements' is monotonic with respect to subsegments. Use Two Pointers (Sliding Window).

## 2. Core Observation & Invariant
Maintain a frequency hash map of elements in window [l, r]. Expand r; when map size exceeds K, advance l until map size <= K.

## 3. Step-by-Step Algorithm
1. Initialize l = 0, max_len = 0, map<int, int> freq.
2. For r from 0 to N - 1:
   - freq[A[r]]++
   - while freq.size() > K: freq[A[l]]--; if freq[A[l]] == 0 freq.erase(A[l]); l++
   - max_len = max(max_len, r - l + 1)
3. Output max_len.

## 4. Complexity Analysis
Time: O(N log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    map<int, int> freq;
    int max_len = 0;
    int l = 0;

    for (int r = 0; r < n; ++r) {
        freq[a[r]]++;
        while ((int)freq.size() > k) {
            freq[a[l]]--;
            if (freq[a[l]] == 0) {
                freq.erase(a[l]);
            }
            l++;
        }
        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Classic two-pointer sliding window maintaining distinct element count.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Two-pointer sliding window technique, dynamic frequency tracking, and shrinking left bound on constraint violation.
- **Reusable Pattern**: `Two Pointers with Frequency Map.`

---
Back to [Two Pointers with Frequency Map / K-Distinct Subarray](../categories/data_structures/two_pointers_sliding_window.md) | [Categories Directory](../categories/README.md)