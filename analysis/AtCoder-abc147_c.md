# Problem Analysis: AtCoder-abc147_c — HonestOrUnkind2

**Problem ID**: `AtCoder-abc147_c`  
**Contest**: `abc147`  
**Rating / Difficulty**: 977  
**URL**: https://atcoder.jp/contests/abc147/tasks/abc147_c  
**VJudge Tag**: `[problem:AtCoder-abc147_c]`  
**Category File**: [`../categories/basics/bitmask_truth_consistency.md`](../categories/basics/bitmask_truth_consistency.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitmask Brute Force`  
- **Topic (Skill)**: `Bitmask Truth Assignment Consistency Verification`  

---

## 1. Problem Statement & Key Idea
There are N people (N <= 15). Each person is either honest (always speaks the truth) or unkind (can say anything). Person i makes A_i statements of the form: person x is honest (y=1) or unkind (y=0). Find the maximum number of honest people in any consistent scenario.

**Key Idea**: With N <= 15, there are only 2^N <= 32768 possible truth assignments. For each assignment mask, we verify whether all statements made by honest people are true.

## 2. Core Observation & Invariant
Unkind people have no constraints (their statements can be true or false). But if person i is assumed honest ((mask >> i) & 1 == 1), every single claim they make MUST match the assumed mask: if person i says person x is y, then ((mask >> x) & 1) must equal y.

## 3. Step-by-Step Algorithm
1. Iterate mask from 0 to (1 << N) - 1.
2. Set valid = true.
3. For each person i: if (mask >> i) & 1: for each claim (x, y) made by i: if ((mask >> x) & 1) != y, valid = false, break.
4. If valid is true, update max_honest = max(max_honest, popcount(mask)).
5. Output max_honest.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^N * sum(A_i))`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Statement {
    int x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Statement>> st(n);
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        st[i].resize(a);
        for (int j = 0; j < a; ++j) {
            cin >> st[i][j].x >> st[i][j].y;
            st[i][j].x--; // 0-indexed
        }
    }

    int max_honest = 0;
    int total_masks = 1 << n;

    for (int mask = 0; mask < total_masks; ++mask) {
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                for (const auto& s : st[i]) {
                    int expected = (mask >> s.x) & 1;
                    if (expected != s.y) {
                        ok = false;
                        break;
                    }
                }
            }
            if (!ok) break;
        }

        if (ok) {
            int honest_cnt = __builtin_popcount(mask);
            max_honest = max(max_honest, honest_cnt);
        }
    }

    cout << max_honest << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitmask enumeration for Knight/Knave Boolean satisfiability verification.
- **Reusable Pattern**: `Verify consistency of truth-tellers: honest persons' statements must match assignment mask.`
