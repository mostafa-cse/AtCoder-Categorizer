# Problem Analysis: AtCoder-abc119_c — Synthetic Kadomatsu

**Problem ID**: `AtCoder-abc119_c`  
**Contest**: `abc119`  
**Rating / Difficulty**: 1346  
**URL**: https://atcoder.jp/contests/abc119/tasks/abc119_c  
**VJudge Tag**: `[problem:AtCoder-abc119_c]`  
**Category File**: [`../categories/basics/quaternary_choice_backtracking.md`](../categories/basics/quaternary_choice_backtracking.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Backtracking`  
- **Topic (Skill)**: `4-State Quaternary Choice Backtracking (4^N)`  

---

## 1. Problem Statement & Key Idea
N bamboos of lengths l_1..l_N. You want to craft three bamboos of lengths A, B, C. Magic 1 (10 MP): combine two bamboos into one. Magic 2 (1 MP): lengthen or shorten by 1. Find the minimum MP needed (N <= 8).

**Key Idea**: Each of the N bamboos can be assigned to one of 4 roles: (0) not used; (1) used to form A; (2) used to form B; (3) used to form C.

## 2. Core Observation & Invariant
Because N <= 8, there are 4^N <= 4^8 = 65,536 possible assignments. For any assignment where at least one bamboo is assigned to A, B, and C: if k bamboos are assigned to A with total length L_A, combining them costs 10 * (k - 1) MP, and adjusting to length A costs |L_A - A| MP. We test all 4^N assignments.

## 3. Step-by-Step Algorithm
1. Write DFS(idx, sumA, sumB, sumC, cntA, cntB, cntC):
2. If idx == N: if cntA > 0 && cntB > 0 && cntC > 0: return 10*(cntA+cntB+cntC-3) + |sumA - A| + |sumB - B| + |sumC - C|; else return INF.
3. Recurse 4 branches: (1) not used; (2) add l[idx] to A; (3) add l[idx] to B; (4) add l[idx] to C.
4. Return minimum across all 4 branches.
5. Start DFS(0, 0, 0, 0, 0, 0, 0).

## 4. Complexity Analysis
- **Time Complexity**: `O(4^N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int INF = 1e9;
int n, A, B, C;
vector<int> l;

int dfs(int idx, int sumA, int sumB, int sumC, int cntA, int cntB, int cntC) {
    if (idx == n) {
        if (cntA == 0 || cntB == 0 || cntC == 0) return INF;
        int mp = 10 * (cntA + cntB + cntC - 3);
        mp += abs(sumA - A) + abs(sumB - B) + abs(sumC - C);
        return mp;
    }

    int res = dfs(idx + 1, sumA, sumB, sumC, cntA, cntB, cntC);
    res = min(res, dfs(idx + 1, sumA + l[idx], sumB, sumC, cntA + 1, cntB, cntC));
    res = min(res, dfs(idx + 1, sumA, sumB + l[idx], sumC, cntA, cntB + 1, cntC));
    res = min(res, dfs(idx + 1, sumA, sumB, sumC + l[idx], cntA, cntB, cntC + 1));

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> A >> B >> C)) return 0;

    l.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> l[i];
    }

    cout << dfs(0, 0, 0, 0, 0, 0, 0) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Complete search over small multi-target subset partitioning via quaternary recursion.
- **Reusable Pattern**: `Multi-group assignment: 4-branch DFS assigning element i to {None, Group 1, Group 2, Group 3}.`
