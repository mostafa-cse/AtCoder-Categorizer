# Problem Analysis: AtCoder-arc100_b — Equal Cut

**Problem ID**: `AtCoder-arc100_b`  
**Contest**: `abc102`  
**Rating / Difficulty**: 1801  
**URL**: https://atcoder.jp/contests/abc102/tasks/arc100_b  
**VJudge Tag**: `[problem:AtCoder-arc100_b]`  
**Category File**: [`../categories/basics/four_partition_two_pointer_sweep.md`](../categories/basics/four_partition_two_pointer_sweep.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Two Pointers`  
- **Topic (Skill)**: `4-Partition Array Optimization via Monotonic Two-Pointer Sweep`  

---

## 1. Problem Statement & Key Idea
Given an array A of N positive integers. Cut A at 3 points into 4 contiguous non-empty subarrays with sums P, Q, R, S. Minimize max(P, Q, R, S) - min(P, Q, R, S).

**Key Insight**: Fix the middle cut m in [2, N - 2]. The left half A[1..m] needs to be cut into two parts (P, Q) to minimize |P - Q|, and the right half A[m+1..N] into (R, S) to minimize |R - S|. Because prefix sums are strictly increasing, as m advances, the optimal left cut l and optimal right cut r both move monotonically forward.

## 2. Core Observation & Invariant
Maintain two pointers l and r. For each m, advance l while |pref[l] - (pref[m] - pref[l])| decreases, and similarly advance r. Running in O(1) amortized per m gives O(N) overall.

## 3. Step-by-Step Algorithm
1. Compute prefix sums pref[1..N].
2. Initialize l = 1, r = 3, min_diff = INF.
3. For m = 2 to N - 2:
4.   While l + 1 < m and abs(pref[l + 1] - (pref[m] - pref[l + 1])) <= abs(pref[l] - (pref[m] - pref[l])):
5.     l++;
6.   While r + 1 < N and abs((pref[r + 1] - pref[m]) - (pref[N] - pref[r + 1])) <= abs((pref[r] - pref[m]) - (pref[N] - pref[r])):
7.     r++;
8.   Compute P = pref[l], Q = pref[m] - pref[l], R = pref[r] - pref[m], S = pref[N] - pref[r].
9.   min_diff = min(min_diff, max({P, Q, R, S}) - min({P, Q, R, S})).
10. Print min_diff.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    vector<long long> pref(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        pref[i] = pref[i - 1] + a[i];
    }

    int l = 1, r = 3;
    long long min_diff = 4e18;

    for (int m = 2; m <= n - 2; ++m) {
        while (l + 1 < m && abs((pref[m] - pref[l + 1]) - pref[l + 1]) <= abs((pref[m] - pref[l]) - pref[l])) {
            l++;
        }
        while (r + 1 < n && abs((pref[n] - pref[r + 1]) - (pref[r + 1] - pref[m])) <= abs((pref[n] - pref[r]) - (pref[r] - pref[m]))) {
            r++;
        }

        long long P = pref[l];
        long long Q = pref[m] - pref[l];
        long long R = pref[r] - pref[m];
        long long S = pref[n] - pref[r];

        long long mx = max({P, Q, R, S});
        long long mn = min({P, Q, R, S});
        min_diff = min(min_diff, mx - mn);
    }

    cout << min_diff << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Multi-partition optimization via independent monotonic prefix two-pointer sweep.
- **Reusable Pattern**: `4-Way Partition Sweep: Fix middle cut and maintain monotonic left/right halving pointers.`
