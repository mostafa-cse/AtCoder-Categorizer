# Problem Analysis: AtCoder-abc029_d — 1

**Problem ID**: `AtCoder-abc029_d`  
**Contest**: `abc029`  
**Rating / Difficulty**: 1393  
**URL**: https://atcoder.jp/contests/abc029/tasks/abc029_d  
**VJudge Tag**: `[problem:AtCoder-abc029_d]`  
**Category File**: [`../categories/dp/digit_dp_counting_occurrences.md`](../categories/dp/digit_dp_counting_occurrences.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP Counting Occurrences of Digit '1'`  

---

## 1. Problem Statement & Key Idea
Given an integer N (1 <= N <= 10^9). Find the total number of times the digit '1' is written when writing all integers from 1 to N.

**Key Idea**: Standard Digit DP where the state tracks the cumulative count of '1's placed.

## 2. Core Observation & Invariant
State: (idx, count_of_ones, is_tight). At position idx with upper bound limit = (tight ? S[idx] - '0' : 9): iterate digit d from 0 to limit. Recurse on idx + 1 with count_of_ones + (d == 1) and new tight flag.

## 3. Step-by-Step Algorithm
1. Convert N to string S.
2. Initialize memo[12][12][2] to -1.
3. Write solve(idx, cnt, tight):
4.   If idx == |S|: return cnt.
5.   If memo[idx][cnt][tight] != -1: return memo.
6.   Iterate d from 0 to limit: sum solve(idx + 1, cnt + (d == 1), tight && (d == limit)).
7.   Return memo[idx][cnt][tight] = sum.
8. Output solve(0, 0, true).

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|^2 * 10)`
- **Space Complexity**: `O(|S|^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

string s;
long long memo[15][15][2];

long long solve(int idx, int cnt, bool tight) {
    if (idx == (int)s.size()) return cnt;
    if (memo[idx][cnt][tight] != -1) return memo[idx][cnt][tight];

    int limit = (tight ? s[idx] - '0' : 9);
    long long total = 0;

    for (int d = 0; d <= limit; ++d) {
        total += solve(idx + 1, cnt + (d == 1 ? 1 : 0), tight && (d == limit));
    }

    return memo[idx][cnt][tight] = total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    s = to_string(n);
    memset(memo, -1, sizeof(memo));

    cout << solve(0, 0, true) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Digit DP cumulative feature summation across all integers up to N.
- **Reusable Pattern**: `Digit DP sum of occurrences: recurse with cnt + (d == target_digit).`
