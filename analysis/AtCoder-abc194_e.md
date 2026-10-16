# Problem Analysis: AtCoder-abc194_e — Mex Min

**Problem ID**: `AtCoder-abc194_e`  
**Contest**: `abc194`  
**Rating / Difficulty**: 1088  
**URL**: https://atcoder.jp/contests/abc194/tasks/abc194_e  
**VJudge Tag**: `[problem:AtCoder-abc194_e]`  
**Category File**: [`../categories/data_structures/sliding_window_mex_min.md`](../categories/data_structures/sliding_window_mex_min.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Sliding Window`  
- **Topic (Skill)**: `Sliding Window Frequency Tracking / Minimum Missing Non-Negative`  

---

## 1. Problem Statement & Key Idea
Given an array A of length N and integer M. For each contiguous subarray of length M, compute its MEX (minimum excluded non-negative integer). Find the minimum MEX across all subarrays of length M (M <= N <= 1.5 * 10^6).

**Key Idea**: An integer x can be the MEX of a subarray if and only if x does not appear in that subarray.

## 2. Core Observation & Invariant
Instead of recalculating MEX in O(M), observe that an integer x is NEVER the MEX of any length-M window if every two consecutive occurrences of x (including imaginary boundaries at index -1 and index N) are at distance <= M. Conversely, if there exists two consecutive occurrences of x separated by gap > M, then a window of length M fits completely between them without containing x, making x a valid candidate MEX! The answer is the smallest x that has a gap > M.

## 3. Step-by-Step Algorithm
1. For each value x from 0 to N: store positions where x appears, with sentinel at -1 and N.
2. Iterate x from 0 to N: check if any gap pos[k] - pos[k-1] > M.
3. The first x with a gap > M is the minimum possible MEX across all windows.
4. Print x.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> pos(n + 1);
    for (int i = 0; i <= n; ++i) {
        pos[i].push_back(-1);
    }

    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        if (a <= n) {
            pos[a].push_back(i);
        }
    }

    for (int i = 0; i <= n; ++i) {
        pos[i].push_back(n);
    }

    for (int x = 0; x <= n; ++x) {
        for (size_t k = 1; k < pos[x].size(); ++k) {
            if (pos[x][k] - pos[x][k - 1] > m) {
                cout << x << "\n";
                return 0;
            }
        }
    }

    cout << n << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Inverting sliding window MEX tracking into element gap interval analysis.
- **Reusable Pattern**: `MEX containment gap: value x is absent in some length-M window iff max gap between occurrences > M.`
