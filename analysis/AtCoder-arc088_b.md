# Problem Analysis: AtCoder-arc088_b — Wide Flip

**Problem ID**: `AtCoder-arc088_b`  
**Contest**: `abc083`  
**Rating / Difficulty**: 1646  
**URL**: https://atcoder.jp/contests/abc083/tasks/arc088_b  
**VJudge Tag**: `[problem:AtCoder-arc088_b]`  
**Category File**: [`../categories/basics/central_boundary_interval_flips.md`](../categories/basics/central_boundary_interval_flips.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Ad-Hoc / Observations`  
- **Topic (Skill)**: `Central Boundary Invariant on Reversible Interval Flips`  

---

## 1. Problem Statement & Key Idea
Given a binary string S of length N. You can choose any substring of length at least K and flip all its bits. Find the maximum possible integer K such that S can be transformed into an all-'0's or all-'1's string.

**Key Insight**: Flipping substrings of length >= K can flip any prefix [0..r] or suffix [l..N-1] as long as length >= K. If adjacent characters S[i] != S[i+1], an operation must differentiate between them, which requires K <= max(i + 1, N - (i + 1)).

## 2. Core Observation & Invariant
Every mismatch between S[i] and S[i+1] imposes the constraint K <= max(i + 1, N - 1 - i). The optimal K is precisely the minimum of max(i + 1, N - 1 - i) over all adjacent pairs where S[i] != S[i+1].

## 3. Step-by-Step Algorithm
1. If all characters in S are identical, output N.
2. ans = N.
3. For i from 0 to N - 2:
4.   If S[i] != S[i + 1]:
5.     ans = min(ans, max(i + 1, n - 1 - i)).
6. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    int ans = n;

    for (int i = 0; i < n - 1; ++i) {
        if (s[i] != s[i + 1]) {
            int bound = max(i + 1, n - 1 - i);
            ans = min(ans, bound);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Identifying critical boundary constraints on range-inversion operations.
- **Reusable Pattern**: `Range Inversion Bound: K = min_{S[i] != S[i+1]} max(i + 1, N - 1 - i).`
