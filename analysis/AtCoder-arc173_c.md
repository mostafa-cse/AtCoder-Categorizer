# Problem Analysis: AtCoder-arc173_c — Not Median

**Problem ID**: `AtCoder-arc173_c`  
**Contest**: `arc173`  
**Rating / Difficulty**: 2008  
**URL**: https://atcoder.jp/contests/arc173/tasks/arc173_c  
**VJudge Tag**: `[problem:AtCoder-arc173_c]`  
**Category File**: [`../categories/basics/alternating_sign_median_parity_breaking.md`](../categories/basics/alternating_sign_median_parity_breaking.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy / Two Pointers`  
- **Topic (Skill)**: `Alternating Sign Invariant and Median Parity Breaking Search`  

---

## 1. Problem Statement & Key Idea
Given a permutation P of length N. For each i in [1, N], find the minimum odd length >= 3 of a contiguous subsegment containing P_i such that P_i is NOT the median of that subsegment (or -1 if impossible).

**Key Idea**: For i = 1 and i = N, we can directly scan the adjacent prefix/suffix in O(N). For 2 <= i <= N - 1, if sgn(P_{i-1} - P_i) == sgn(P_{i+1} - P_i), the 3-element window [i-1, i+1] already has P_i not as median, so ans = 3. Otherwise, relative to P_i, signs strictly alternate. Let R be the smallest j > i where adjacent signs match, and L be the largest j < i where adjacent signs match. Inside [L, R], P_i is always the median. The shortest interval where P_i fails to be median must extend past L or past R, achievable with length 2 * (i - (L - 1)) + 1 (or 2 * (R + 1 - i) + 1). The naive search for L and R takes O(N) total across all such i.

## 2. Core Observation & Invariant
Alternating sign sequences maintain the median invariant; breaking this requires reaching the first adjacent sign agreement boundary.

## 3. Step-by-Step Algorithm
1. For i = 1 and i = N: scan odd lengths 3, 5, ... by expanding the single available side; check median sum != 0.
2. For i from 2 to N - 1:
3.   If sgn(P[i-1] - P[i]) == sgn(P[i+1] - P[i]): ans[i] = 3.
4.   Else:
5.     Scan left to find largest L < i with sgn(P[L-1] - P[i]) == sgn(P[L] - P[i]).
6.     Scan right to find smallest R > i with sgn(P[R] - P[i]) == sgn(P[R+1] - P[i]).
7.     Evaluate candidate lengths from L - 1 and R + 1; take the minimum valid odd length.
8. Print all ans[i].

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Alternating sign permutation analysis and local median violation searching.

**Reusable Pattern**: Median Violation on Permutations: Check length 3 first; if alternating, expand to the first consecutive identical sign boundary.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int sgn(int x) {
    return (x > 0) - (x < 0);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
    }

    vector<int> ans(n + 1, -1);

    auto check_window = [&](int l, int r, int target_val) {
        int sum_sgn = 0;
        for (int j = l; j <= r; ++j) {
            sum_sgn += sgn(p[j] - target_val);
        }
        return sum_sgn != 0;
    };

    // Endpoints i = 1 and i = n
    for (int i : {1, n}) {
        for (int len = 3; len <= n; len += 2) {
            int l = (i == 1 ? 1 : n - len + 1);
            int r = (i == 1 ? len : n);
            if (l >= 1 && r <= n && check_window(l, r, p[i])) {
                ans[i] = len;
                break;
            }
        }
    }

    // Interior points
    for (int i = 2; i <= n - 1; ++i) {
        if (sgn(p[i - 1] - p[i]) == sgn(p[i + 1] - p[i])) {
            ans[i] = 3;
            continue;
        }

        int cand = 1e9;

        // Search left for boundary
        int L = -1;
        for (int j = i - 1; j >= 2; --j) {
            if (sgn(p[j - 1] - p[i]) == sgn(p[j] - p[i])) {
                L = j;
                break;
            }
        }
        if (L != -1) {
            int l = L - 1;
            int r = ( (i - l + 1) % 2 != 0 ? i : i + 1 );
            if (r <= n) cand = min(cand, r - l + 1);
        }

        // Search right for boundary
        int R = -1;
        for (int j = i + 1; j <= n - 1; ++j) {
            if (sgn(p[j] - p[i]) == sgn(p[j + 1] - p[i])) {
                R = j;
                break;
            }
        }
        if (R != -1) {
            int r = R + 1;
            int l = ( (r - i + 1) % 2 != 0 ? i : i - 1 );
            if (l >= 1) cand = min(cand, r - l + 1);
        }

        if (cand < 1e9) ans[i] = cand;
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
