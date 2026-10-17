# Problem Analysis: AtCoder-abc188_f — +1-1x2

**Problem ID**: `AtCoder-abc188_f`  
**Contest**: `abc188`  
**Rating / Difficulty**: 1865  
**URL**: https://atcoder.jp/contests/abc188/tasks/abc188_f  
**VJudge Tag**: `[problem:AtCoder-abc188_f]`  
**Category File**: [`../categories/basics/backward_parity_branching_memoization.md`](../categories/basics/backward_parity_branching_memoization.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Memoized Recursion`  
- **Topic (Skill)**: `Backward Parity Branching Recursion with Memoization from Target to Source`  

---

## 1. Problem Statement & Key Idea
Starting from X, reach Y using operations: +1 (cost 1), -1 (cost 1), or *2 (cost 1). Minimize total cost. (X, Y <= 10^{18}).

**Key Insight**: Work backward from Y to X: dividing by 2 is only allowed when the current number is even. If Y is odd, we can either add 1 or subtract 1 to make it even, then divide by 2. We can also reach X directly using only +1/-1 with cost |X - Y|.

## 2. Core Observation & Invariant
Branching backward visits at most O(log Y) distinct states. Memoize using std::map.

## 3. Step-by-Step Algorithm
1. Define solve(Y):
2.   if Y <= X: return X - Y;
3.   if memo contains Y: return memo[Y];
4.   res = Y - X; // direct +/-1 operations
5.   if Y % 2 == 0:
6.     res = min(res, solve(Y / 2) + 1);
7.   else:
8.     res = min(res, solve((Y + 1) / 2) + 2);
9.     res = min(res, solve((Y - 1) / 2) + 2);
10.   return memo[Y] = res;

## 4. Complexity Analysis
- **Time Complexity**: `O(log Y)`
- **Space Complexity**: `O(log Y)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

long long X;
map<long long, long long> memo;

long long solve(long long y) {
    if (y <= X) return X - y;
    if (memo.count(y)) return memo[y];

    long long res = y - X; // direct operations

    if (y % 2 == 0) {
        res = min(res, solve(y / 2) + 1);
    } else {
        res = min(res, solve((y + 1) / 2) + 2);
        res = min(res, solve((y - 1) / 2) + 2);
    }

    return memo[y] = res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long y;
    if (!(cin >> X >> y)) return 0;

    cout << solve(y) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Backward state space pruning on multiplicative search spaces with parity branching.
- **Reusable Pattern**: `Backward Multiplicative Recursion: Branch Y -> Y/2 (even) or (Y+/-1)/2 (odd) with memoization.`
