# Problem Analysis: AtCoder-arc087_b — FT Robot

**Problem ID**: `AtCoder-arc087_b`  
**Contest**: `abc082`  
**Rating / Difficulty**: 1508  
**URL**: https://atcoder.jp/contests/abc082/tasks/arc087_b  
**VJudge Tag**: `[problem:AtCoder-arc087_b]`  
**Category File**: [`../categories/dp/independent_xy_subset_sum_bitset.md`](../categories/dp/independent_xy_subset_sum_bitset.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Bitset DP`  
- **Topic (Skill)**: `Independent X/Y Coordinate Subset Sum Knapsack DP`  

---

## 1. Problem Statement & Key Idea
A robot starts at (0, 0) facing +X. A string S of 'F' (move forward 1) and 'T' (turn 90 degrees) is executed. Can the robot end at coordinate (X, Y)?

**Key Insight**: Turns alternate between moving along the X-axis and Y-axis! The first segment of 'F's must move +X. All subsequent segments can move in either positive or negative direction, independently for X and Y.

## 2. Core Observation & Invariant
Parse S into consecutive 'F' block lengths separated by 'T's. Blocks alternate: X, Y, X, Y, ... The problem decouples into two independent subset sum problems: can we choose signs for X-blocks to reach X, and signs for Y-blocks to reach Y? Solved with `std::bitset` in O(len^2 / 64).

## 3. Step-by-Step Algorithm
1. Parse S into segments of 'F' counts separated by 'T'.
2. First segment moves strictly in +X: target_X -= len[0].
3. Collect subsequent segments into moves_x and moves_y alternatingly.
4. Solve check(moves, target):
5.   Let S = sum(moves). If (target + S) < 0 or (target + S) % 2 != 0: return false.
6.   w = (target + S) / 2.
7.   Use bitset<16001> dp; dp[0] = 1.
8.   For each length m in moves: dp |= (dp << m).
9.   Return dp[w].
10. Print 'Yes' if check(moves_x, target_X) && check(moves_y, Y), else 'No'.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|^2 / 64)`
- **Space Complexity**: `O(|S|)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>

using namespace std;

const int OFFSET = 8000;

bool can_reach(const vector<int>& moves, int target) {
    bitset<16005> dp;
    dp[OFFSET] = 1;

    for (int d : moves) {
        dp = (dp << d) | (dp >> d);
    }

    if (abs(target) > 8000) return false;
    return dp[target + OFFSET];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int target_x, target_y;
    if (!(cin >> s >> target_x >> target_y)) return 0;

    vector<int> segments;
    int cur = 0;
    for (char c : s) {
        if (c == 'F') {
            cur++;
        } else {
            segments.push_back(cur);
            cur = 0;
        }
    }
    segments.push_back(cur);

    // First segment is fixed along +X
    target_x -= segments[0];

    vector<int> moves_x, moves_y;
    for (size_t i = 1; i < segments.size(); ++i) {
        if (segments[i] == 0) continue;
        if (i % 2 == 1) {
            moves_y.push_back(segments[i]);
        } else {
            moves_x.push_back(segments[i]);
        }
    }

    if (can_reach(moves_x, target_x) && can_reach(moves_y, target_y)) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Decoupling 2D orthogonal grid motions into independent 1D subset sum problems accelerated by bitsets.
- **Reusable Pattern**: `Orthogonal Motion Independence: split turns into X and Y steps, solve with bitset.`
