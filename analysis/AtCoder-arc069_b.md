# Problem Analysis: AtCoder-arc069_b — Menagerie

**Problem ID**: `AtCoder-arc069_b`  
**Contest**: `abc055`  
**Rating / Difficulty**: 1344  
**URL**: https://atcoder.jp/contests/abc055/tasks/arc069_b  
**VJudge Tag**: `[problem:AtCoder-arc069_b]`  
**Category File**: [`../categories/basics/circular_truth_consistency_4case.md`](../categories/basics/circular_truth_consistency_4case.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Circular Invariants`  
- **Topic (Skill)**: `Circular Truth-Telling Consistency 4-Case Brute Force`  

---

## 1. Problem Statement & Key Idea
N animals in a circle: Sheep 'S' (always tell truth), Wolves 'W' (always lie). Animal i says animal i-1 and i+1 are of the same type ('o') or different ('x'). Find a valid assignment or output -1.

**Key Idea**: Once the identities of animal 0 and animal 1 are fixed, every subsequent animal's identity is uniquely forced!

## 2. Core Observation & Invariant
There are only 2 x 2 = 4 choices for (animal 0, animal 1): (S, S), (S, W), (W, S), (W, W). For each choice, deduce animal 2, 3, ..., N-1 sequentially. Finally, verify that animal N-1 and animal 0's statements are consistent with the circular wrap-around to animal 0 and animal 1.

## 3. Step-by-Step Algorithm
1. Iterate over 4 cases for (type[0], type[1]).
2. For i from 1 to N - 2: deduce type[i + 1] from type[i], type[i - 1], and S[i].
3. Check if type[N - 1]'s statement matches (type[N - 2], type[0]).
4. Check if type[0]'s statement matches (type[N - 1], type[1]).
5. If both checks hold: print string and terminate.
6. If all 4 cases fail, print -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    char roles[2] = {'S', 'W'};

    for (char c0 : roles) {
        for (char c1 : roles) {
            string ans(n, ' ');
            ans[0] = c0;
            ans[1] = c1;

            for (int i = 1; i < n - 1; ++i) {
                bool is_same = (s[i] == 'o');
                if (ans[i] == 'W') is_same = !is_same;

                if (is_same) {
                    ans[i + 1] = ans[i - 1];
                } else {
                    ans[i + 1] = (ans[i - 1] == 'S' ? 'W' : 'S');
                }
            }

            // Check wrap-around consistency for n - 1
            bool same_last = (s[n - 1] == 'o');
            if (ans[n - 1] == 'W') same_last = !same_last;
            bool check_last = (same_last ? (ans[n - 2] == ans[0]) : (ans[n - 2] != ans[0]));

            // Check wrap-around consistency for 0
            bool same_zero = (s[0] == 'o');
            if (ans[0] == 'W') same_zero = !same_zero;
            bool check_zero = (same_zero ? (ans[n - 1] == ans[1]) : (ans[n - 1] != ans[1]));

            if (check_last && check_zero) {
                cout << ans << "\n";
                return 0;
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Circular boundary consistency verification via fixing initial seed elements.
- **Reusable Pattern**: `Circular constraint deduction: fix first 2 elements (4 cases) -> propagate -> verify wrap-around.`
