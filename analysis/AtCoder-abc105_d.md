# Problem Analysis: AtCoder-abc105_d — Candy Distribution

**Problem ID**: `AtCoder-abc105_d`  
**Contest**: `abc105`  
**Rating / Difficulty**: 1458  
**URL**: https://atcoder.jp/contests/abc105/tasks/abc105_d  
**VJudge Tag**: `[problem:AtCoder-abc105_d]`  
**Category File**: [`../categories/math/prefix_sum_modulo_frequency.md`](../categories/math/prefix_sum_modulo_frequency.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Prefix Sums`  
- **Topic (Skill)**: `Prefix Sum Modulo Frequency Matching`  

---

## 1. Problem Statement & Key Idea
Given N boxes of candies A_1, ..., A_N. Find the number of pairs (l, r) with 1 <= l <= r <= N such that sum_{i=l}^r A_i is divisible by M.

**Key Insight**: The subarray sum is pref[r] - pref[l-1]. It is divisible by M if and only if pref[r] = pref[l-1] (mod M). Count the frequency of each remainder.

## 2. Core Observation & Invariant
Each remainder r_mod with frequency cnt contributes C(cnt, 2) = cnt * (cnt - 1) / 2 valid pairs. Prepending pref[0] = 0 accounts for subarrays starting at index 1.

## 3. Step-by-Step Algorithm
1. Maintain frequency map remainder_count.
2. remainder_count[0] = 1.
3. pref = 0, ans = 0.
4. For each element x in A:
5.   pref = (pref + x) % M.
6.   ans += remainder_count[pref].
7.   remainder_count[pref]++.
8. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

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
    long long m;
    if (!(cin >> n >> m)) return 0;

    map<long long, long long> cnt;
    cnt[0] = 1;

    long long pref = 0;
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        pref = (pref + a) % m;
        ans += cnt[pref];
        cnt[pref]++;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Equivalence class matching on modular prefix sums.
- **Reusable Pattern**: `Subarray Divisible by M: map<long long, int> cnt; ans += cnt[pref % M]++;`
