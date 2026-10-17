# Problem Analysis: AtCoder-abc146_e — Rem of Sum is Num

**Problem ID**: `AtCoder-abc146_e`  
**Contest**: `abc146`  
**Rating / Difficulty**: 1762  
**URL**: https://atcoder.jp/contests/abc146/tasks/abc146_e  
**VJudge Tag**: `[problem:AtCoder-abc146_e]`  
**Category File**: [`../categories/data_structures/prefix_sum_shift_sliding_window_map.md`](../categories/data_structures/prefix_sum_shift_sliding_window_map.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Sliding Window Hash`  
- **Topic (Skill)**: `Prefix Sum Shift Transformation (S_i - i) mod K with Sliding Window Map`  

---

## 1. Problem Statement & Key Idea
Given an array A of N integers and an integer K. Count pairs (l, r) such that 1 <= r - l + 1 < K and sum_{i=l}^r A_i = r - l + 1 (mod K).

**Key Insight**: The condition (S_r - S_{l-1}) = r - (l - 1) (mod K) rearranges to (S_r - r) = (S_{l-1} - (l - 1)) (mod K). Defining B_i = (S_i - i) mod K, we require B_r == B_{l-1} within a sliding window of length at most K - 1.

## 2. Core Observation & Invariant
Maintain a hash map of frequencies of B_{l-1} for the last K - 1 indices. For each r, add freq[B_r] to the answer, then add B_r to the map and remove the element that falls out of the sliding window.

## 3. Step-by-Step Algorithm
1. Compute prefix sums S_i.
2. Let B_i = ((S_i - i) % K + K) % K for i = 0..N.
3. Maintain frequency map of B in a window of size K - 1.
4. Insert B_0 with count 1.
5. For r = 1 to N:
6.   if r >= K: decrement count of B_{r - K} in map.
7.   ans += map[B_r].
8.   increment count of B_r in map.
9. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log K)`
- **Space Complexity**: `O(K)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n + 1);
    vector<long long> b(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    long long pref = 0;
    for (int i = 1; i <= n; ++i) {
        pref += a[i];
        b[i] = ((pref - i) % k + k) % k;
    }

    map<long long, int> freq;
    long long ans = 0;

    freq[0] = 1;

    for (int r = 1; r <= n; ++r) {
        if (r >= k) {
            freq[b[r - k]]--;
        }
        ans += freq[b[r]];
        freq[b[r]]++;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Rewriting modular range sum length conditions into transformed prefix invariants with sliding window size constraints.
- **Reusable Pattern**: `Transformed Prefix Invariant: (S_r - r) == (S_l - l) mod K in sliding window.`
