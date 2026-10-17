# Problem Analysis: AtCoder-abc161_e — Yutori

**Problem ID**: `AtCoder-abc161_e`  
**Contest**: `abc161`  
**Rating / Difficulty**: 1760  
**URL**: https://atcoder.jp/contests/abc161/tasks/abc161_e  
**VJudge Tag**: `[problem:AtCoder-abc161_e]`  
**Category File**: [`../categories/basics/mandatory_days_left_right_greedy.md`](../categories/basics/mandatory_days_left_right_greedy.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Mandatory Task Identification via Leftmost vs Rightmost Greedy Schedules`  

---

## 1. Problem Statement & Key Idea
Given a schedule of N days where each day is work ('o') or rest ('x'). Choose K days to work such that after working on day i, you must rest for at least C days (next work day >= i + C + 1). Find all days that MUST be worked on in EVERY valid schedule.

**Key Insight**: Compute the greedy earliest schedule L[1..K] from left to right, and the greedy latest schedule R[1..K] from right to left. Day d is mandatory iff for some task index i, L[i] == R[i] == d.

## 2. Core Observation & Invariant
Any valid schedule must place the i-th work day in the interval [L[i], R[i]]. If L[i] == R[i], the i-th work day has only one possible placement across all valid schedules.

## 3. Step-by-Step Algorithm
1. Greedy forward pass: find earliest day for work 1..K -> L[1..K].
2. Greedy backward pass: find latest day for work K..1 -> R[1..K].
3. For i = 1 to K: if L[i] == R[i], record L[i] as a mandatory day.
4. Print all mandatory days in ascending order.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N + K)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, c;
    if (!(cin >> n >> k >> c)) return 0;

    string s;
    cin >> s;

    vector<int> L(k + 1);
    int cur_day = 0;
    for (int i = 1; i <= k; ++i) {
        while (cur_day < n && s[cur_day] != 'o') cur_day++;
        L[i] = cur_day + 1;
        cur_day += c + 1;
    }

    vector<int> R(k + 1);
    cur_day = n - 1;
    for (int i = k; i >= 1; --i) {
        while (cur_day >= 0 && s[cur_day] != 'o') cur_day--;
        R[i] = cur_day + 1;
        cur_day -= (c + 1);
    }

    for (int i = 1; i <= k; ++i) {
        if (L[i] == R[i]) {
            cout << L[i] << "\n";
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pinpointing unique schedule choices via intersection of earliest and latest greedy bounds.
- **Reusable Pattern**: `Mandatory Element via Left/Right Greedy Bounds: Mandatory iff earliest[i] == latest[i].`
