# Problem Analysis: AtCoder-abc229_g — Longest Y

**Problem ID**: `AtCoder-abc229_g`  
**Contest**: `abc229`  
**Rating / Difficulty**: 2121  
**URL**: https://atcoder.jp/contests/abc229/tasks/abc229_g  
**VJudge Tag**: `[problem:AtCoder-abc229_g]`  
**Category File**: [`../categories/basics/coordinate_transformation_median_alignment.md`](../categories/basics/coordinate_transformation_median_alignment.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Binary Search`  

---

## 1. Problem Statement & Key Idea
Given a string S containing 'Y' and '.', and an integer K, find the maximum number of contiguous 'Y's that can be formed using at most K adjacent swaps.

**Key Insight**: Let the original indices of 'Y' be P_0 < P_1 < ... < P_{M-1}. Bringing a window of elements P[l..r] into a contiguous block requires cost sum_{i=l}^r |P_i - (center + i - mid)|. Setting Q_i = P_i - i transforms this into the classic 1D facility location problem: minimizing sum_{i=l}^r |Q_i - Q_{mid}|, where mid = (l + r) / 2. Using prefix sums of Q, the minimum swap cost for any window [l, r] can be evaluated in O(1). We binary search the maximum window length len in [1, M].

## 2. Core Observation & Invariant
Coordinate shift Q_i = P_i - i reduces contiguous clustering swap cost to sum of absolute deviations around the median, evaluated in O(1) via prefix sums.

## 3. Step-by-Step Algorithm
1. Extract indices P of 'Y'. If none, output 0.
2. Define Q_i = P_i - i and compute prefix sums of Q.
3. Binary search the window length len in [1, M]:
4.   For each starting index i with i + len - 1 < M:
5.     mid = i + len / 2.
6.     Compute left deviation: len_left * Q[mid] - sum(Q[i..mid]).
7.     Compute right deviation: sum(Q[mid+1..r]) - len_right * Q[mid].
8.     If total cost <= K, length len is achievable.
9. Output the maximum feasible window length.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Coordinate transformation P_i - i and median prefix sum evaluation for adjacent swap clustering.
- **Reusable Pattern**: Transforming contiguous block clustering costs into L1 median deviations on Q_i = P_i - i.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    long long k;
    if (!(cin >> s >> k)) return 0;

    vector<long long> q;
    for (int i = 0; i < (int)s.size(); ++i) {
        if (s[i] == 'Y') {
            q.push_back(i - (int)q.size());
        }
    }

    int m = q.size();
    if (m == 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> pref(m + 1, 0);
    for (int i = 0; i < m; ++i) {
        pref[i + 1] = pref[i] + q[i];
    }

    auto get_cost = [&](int l, int r) {
        int mid = (l + r) / 2;
        long long median = q[mid];
        long long left_cost = 1LL * (mid - l + 1) * median - (pref[mid + 1] - pref[l]);
        long long right_cost = (pref[r + 1] - pref[mid + 1]) - 1LL * (r - mid) * median;
        return left_cost + right_cost;
    };

    int low = 1, high = m, ans = 1;
    while (low <= high) {
        int len = (low + high) / 2;
        bool ok = false;
        for (int i = 0; i + len - 1 < m; ++i) {
            if (get_cost(i, i + len - 1) <= k) {
                ok = true;
                break;
            }
        }
        if (ok) {
            ans = len;
            low = len + 1;
        } else {
            high = len - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
