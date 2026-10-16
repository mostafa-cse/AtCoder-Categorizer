# Problem Analysis: AtCoder-arc098_b — Xor Sum 2

**Problem ID**: `AtCoder-arc098_b`  
**Contest**: `abc098`  
**Rating / Difficulty**: 1404  
**URL**: https://atcoder.jp/contests/abc098/tasks/arc098_b  
**VJudge Tag**: `[problem:AtCoder-arc098_b]`  
**Category File**: [`../categories/basics/bitwise_disjoint_two_pointers.md`](../categories/basics/bitwise_disjoint_two_pointers.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Two Pointers`  
- **Topic (Skill)**: `Two Pointers Bitwise Disjoint Subarray Counting (Sum == XOR)`  

---

## 1. Problem Statement & Key Idea
Given an array A of N non-negative integers. Count the number of pairs (l, r) with 1 <= l <= r <= N such that sum_{i=l}^r A_i == XOR_{i=l}^r A_i.

**Key Idea**: For any set of integers, sum A_i == XOR A_i if and only if NO two numbers have a 1 at the same bit position (all numbers are pairwise bitwise disjoint!).

## 2. Core Observation & Invariant
Because binary addition without carry is equivalent to XOR, the condition is monotonic: if A[l..r] has no bit collisions, any sub-interval also has no collisions. Two pointers: maintain running_xor = XOR_{i=l}^r A_i. For each l, expand r while (running_xor & A[r]) == 0. All subarrays starting at l and ending at any k in [l, r - 1] are valid (count is r - l).

## 3. Step-by-Step Algorithm
1. Initialize r = 0, running_xor = 0, total_valid = 0.
2. For l = 0 to N - 1:
3.   While r < N and (running_xor & A[r]) == 0: running_xor ^= A[r], r++.
4.   total_valid += (r - l).
5.   running_xor ^= A[l].
6. Print total_valid.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long ans = 0;
    long long cur_xor = 0;
    int r = 0;

    for (int l = 0; l < n; ++l) {
        while (r < n && (cur_xor & a[r]) == 0) {
            cur_xor ^= a[r];
            r++;
        }
        ans += (r - l);
        cur_xor ^= a[l];
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Recognizing bitwise disjointness as a monotonic two pointers invariant.
- **Reusable Pattern**: `Sum == XOR condition: (running_xor & A[r]) == 0 monotonic two pointers.`
