# Problem Analysis: AtCoder-abc146_f — Sugoroku

**Problem ID**: `AtCoder-abc146_f`  
**Contest**: `abc146`  
**Rating / Difficulty**: 1545  
**URL**: https://atcoder.jp/contests/abc146/tasks/abc146_f  
**VJudge Tag**: `[problem:AtCoder-abc146_f]`  
**Category File**: [`../categories/basics/greedy_reverse_bfs_lexicographical_jumps.md`](../categories/basics/greedy_reverse_bfs_lexicographical_jumps.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy Algorithms`  
- **Topic (Skill)**: `Greedy Reverse BFS / Range Minimum for Lexicographical Jumps`  

---

## 1. Problem Statement & Key Idea
A board with N squares (0 to N). S[i] == '1' is game over; '0' is safe. From square i, you can jump to i + d for 1 <= d <= M. Reach N in the minimum number of moves, and among those, find the LEXICOGRAPHICALLY SMALLEST sequence of die rolls. Output -1 if unreachable.

**Key Insight**: To achieve the lexicographically smallest sequence of forward jumps, work BACKWARDS from N! At each step from current position curr, jump backwards as FAR as possible (up to M steps) to a valid square.

## 2. Core Observation & Invariant
Greedily making the largest possible backward jump pushes earlier steps as small as possible in forward order. This guarantees the lexicographically first sequence of moves with zero extra state overhead.

## 3. Step-by-Step Algorithm
1. Start at curr = N. Initialize move sequence moves.
2. While curr > 0:
3.   Find the smallest index prev in [max(0, curr - M), curr - 1] such that S[prev] == '0'.
4.   If no safe square exists in range, output -1.
5.   Record step (curr - prev) into moves.
6.   curr = prev.
7. Reverse moves and print.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    string s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<int> rolls;
    int curr = n;

    while (curr > 0) {
        int best_prev = -1;
        int min_reach = max(0, curr - m);

        for (int prev = min_reach; prev < curr; ++prev) {
            if (s[prev] == '0') {
                best_prev = prev;
                break;
            }
        }

        if (best_prev == -1) {
            cout << -1 << "\n";
            return 0;
        }

        rolls.push_back(curr - best_prev);
        curr = best_prev;
    }

    reverse(rolls.begin(), rolls.end());
    for (size_t i = 0; i < rolls.size(); ++i) {
        cout << rolls[i] << (i + 1 == rolls.size() ? "\n" : " ");
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Backward greedy simulation to achieve lexicographical optimality for forward sequences.
- **Reusable Pattern**: `Lexicographical Forward Moves: backward greedy maximal jump simulation.`
