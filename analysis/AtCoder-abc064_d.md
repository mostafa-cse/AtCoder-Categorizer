# Problem Analysis: AtCoder-abc064_d — Insertion

**Problem ID**: `AtCoder-abc064_d`  
**Contest**: `abc064`  
**Rating / Difficulty**: 969  
**URL**: https://atcoder.jp/contests/abc064/tasks/abc064_d  
**VJudge Tag**: `[problem:AtCoder-abc064_d]`  
**Category File**: [`../categories/data_structures/prefix_balance_bracket_completion.md`](../categories/data_structures/prefix_balance_bracket_completion.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Stacks & Parentheses`  
- **Topic (Skill)**: `Prefix Balance Minimization for Valid Bracket Completion`  

---

## 1. Problem Statement & Key Idea
Given a bracket string S of length N containing '(' and ')'. Find the shortest valid bracket sequence that contains S as a contiguous substring and is lexicographically smallest.

**Key Idea**: A bracket sequence is valid if and only if prefix balance (count of '(' minus count of ')') is never negative, and final balance is 0.

## 2. Core Observation & Invariant
Track running balance: +1 for '(', -1 for ')'. Let min_bal be the minimum balance reached across all prefixes. If min_bal < 0, we must prepend -min_bal '(' characters at the beginning. After prepending, if the final balance is rem > 0, we must append rem ')' characters at the end. Since '(' < ')', prepending '(' and appending ')' also guarantees lexicographical minimality.

## 3. Step-by-Step Algorithm
1. Scan S, maintaining bal = 0 and min_bal = 0.
2. For each char: if '(' bal++, else bal--; min_bal = min(min_bal, bal).
3. Prepend abs(min_bal) '(' to S.
4. Compute new final balance = bal + abs(min_bal).
5. Append new final balance ')' to S.
6. Output the completed string.

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

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    int bal = 0;
    int min_bal = 0;

    for (char c : s) {
        if (c == '(') bal++;
        else bal--;
        min_bal = min(min_bal, bal);
    }

    int need_open = (min_bal < 0 ? -min_bal : 0);
    int final_bal = bal + need_open;
    int need_close = final_bal;

    string res = string(need_open, '(') + s + string(need_close, ')');
    cout << res << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Prefix balance analysis for optimal parenthesization repair.
- **Reusable Pattern**: `Bracket completion: prepend -min(0, min_prefix_balance) '(', append remaining balance ')'.`
