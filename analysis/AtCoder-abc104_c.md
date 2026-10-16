# Problem Analysis: AtCoder-abc104_c — All Green

**Problem ID**: `AtCoder-abc104_c`  
**Contest**: `abc104`  
**Rating / Difficulty**: 1393  
**URL**: https://atcoder.jp/contests/abc104/tasks/abc104_c  
**VJudge Tag**: `[problem:AtCoder-abc104_c]`  
**Category File**: [`../categories/basics/bitmask_complete_sets_greedy_fill.md`](../categories/basics/bitmask_complete_sets_greedy_fill.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitmask Brute Force`  
- **Topic (Skill)**: `Bitmask Complete Problem Sets with Fractional Greedy Fill`  

---

## 1. Problem Statement & Key Idea
D problem scores: 100i points for solving problem i, plus complete bonus c_i if all p_i problems are solved. Find the minimum total problems solved to achieve score >= G (D <= 10).

**Key Idea**: There are only D <= 10 problem sets. Each set is either completely solved (earning all points + bonus c_i) or partially solved.

## 2. Core Observation & Invariant
Enumerate the 2^D subsets of problem sets that are COMPLETELY solved. If total score from full sets is still < G, greedily solve problems from the highest available unsolved problem set until score >= G. The minimum problems needed across all 2^D masks is optimal.

## 3. Step-by-Step Algorithm
1. Iterate mask from 0 to (1 << D) - 1.
2. Sum score and problem count for all sets i where (mask >> i) & 1.
3. If score < G: scan from highest unsolved set i = D - 1 down to 0: if !((mask >> i) & 1): solve remaining problems needed from set i; if solved < p_i, add to count, score satisfies G, break; else skip.
4. Track minimum problems across all valid masks.
5. Print the minimum.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^D * D)`
- **Space Complexity**: `O(D)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct SetInfo {
    int p;
    long long c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int d;
    long long g;
    if (!(cin >> d >> g)) return 0;

    vector<SetInfo> sets(d);
    for (int i = 0; i < d; ++i) {
        cin >> sets[i].p >> sets[i].c;
    }

    int min_problems = 1e9;

    for (int mask = 0; mask < (1 << d); ++mask) {
        long long current_score = 0;
        int current_count = 0;

        for (int i = 0; i < d; ++i) {
            if ((mask >> i) & 1) {
                current_score += (long long)(i + 1) * 100 * sets[i].p + sets[i].c;
                current_count += sets[i].p;
            }
        }

        if (current_score < g) {
            for (int i = d - 1; i >= 0; --i) {
                if (!((mask >> i) & 1)) {
                    long long pt = (i + 1) * 100;
                    long long needed = (g - current_score + pt - 1) / pt;
                    if (needed < sets[i].p) {
                        current_count += needed;
                        current_score += needed * pt;
                        break;
                    } else {
                        current_count += sets[i].p - 1;
                        current_score += (sets[i].p - 1) * pt;
                    }
                }
            }
        }

        if (current_score >= g) {
            min_problems = min(min_problems, current_count);
        }
    }

    cout << min_problems << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining bitmask complete selection with greedy partial allocation.
- **Reusable Pattern**: `Bitmask complete sets + greedy partial remainder fill.`
