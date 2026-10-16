# Problem Analysis: AtCoder-abc114_c — 755

**Problem ID**: `AtCoder-abc114_c`  
**Contest**: `abc114`  
**Rating / Difficulty**: 1045  
**URL**: https://atcoder.jp/contests/abc114/tasks/abc114_c  
**VJudge Tag**: `[problem:AtCoder-abc114_c]`  
**Category File**: [`../categories/basics/digit_recursion_3branch_dfs.md`](../categories/basics/digit_recursion_3branch_dfs.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Recursion & Backtracking`  
- **Topic (Skill)**: `Digit Recursion / 3-Branch DFS Enumeration`  

---

## 1. Problem Statement & Key Idea
A '755 number' is a positive integer <= N whose decimal representation contains only the digits 7, 5, 3, and contains each of 7, 5, and 3 at least once. Count all 755 numbers <= N (N <= 10^9).

**Key Idea**: Because N <= 10^9, any candidate number has at most 9 digits. The total numbers using only digits 3, 5, 7 with up to 9 digits is sum_{d=1}^9 3^d = (3^{10} - 3) / 2 = 29,523.

## 2. Core Observation & Invariant
Since the search space is fewer than 30,000 numbers, we can generate all candidate numbers recursively via 3-way branching DFS: append 3, 5, or 7, tracking whether 3, 5, and 7 have appeared using bitmask flags.

## 3. Step-by-Step Algorithm
1. Run DFS(val, mask):
2. If val > N, return 0.
3. int ans = (mask == 7 ? 1 : 0) (where mask bit 0 is 3, bit 1 is 5, bit 2 is 7).
4. ans += DFS(val * 10 + 3, mask | 1).
5. ans += DFS(val * 10 + 5, mask | 2).
6. ans += DFS(val * 10 + 7, mask | 4).
7. Return ans; start from DFS(0, 0).

## 4. Complexity Analysis
- **Time Complexity**: `O(3^D) where D <= 9`
- **Space Complexity**: `O(D)`

## 5. Complete C++ Solution
```cpp
#include <iostream>

using namespace std;

long long n;

int dfs(long long val, int mask) {
    if (val > n) return 0;
    int count = (mask == 7 ? 1 : 0);

    count += dfs(val * 10 + 3, mask | 1);
    count += dfs(val * 10 + 5, mask | 2);
    count += dfs(val * 10 + 7, mask | 4);

    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    cout << dfs(0, 0) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Complete search over small restricted-digit search spaces via recursion.
- **Reusable Pattern**: `Restricted-alphabet generation: 3-branch DFS with bitmask tracking.`
