# Problem Analysis: AtCoder-dp_j — Sushi

**Problem ID**: `AtCoder-dp_j`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1650  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_j  
**VJudge Tag**: `[problem:AtCoder-dp_j]`  
**Category File**: [`../categories/dp/expected_value_dp.md`](../categories/dp/expected_value_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Expected Value DP with Multi-Frequency States`  

---

## 1. Problem Statement & Key Idea
N plates have 1, 2, or 3 sushi. Repeatedly choose a random plate and eat one sushi if present. Find expected operations to empty all plates.

**Core Idea**: Plate identity is irrelevant; state is the count of plates with 1, 2, and 3 sushi (c1, c2, c3). Picking an empty plate loops back to the same state (self-loop).

## 2. Core Observation & Invariant
Self-loop equation E = 1 + sum(P_i E_i) + P_empty E solves algebraically: E = (N + c1*E1 + c2*E2 + c3*E3) / (c1 + c2 + c3).

## 3. Step-by-Step Algorithm
1. Memoized 3D DP array: memo[c1][c2][c3].
2. Compute recursively using the resolved self-loop formula.
3. Base: memo[0][0][0] = 0.0.

## 4. Complexity Analysis
Time: O(N^3), Space: O(N^3).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

double memo[305][305][305];
bool vis[305][305][305];
int n;

double solve(int c1, int c2, int c3) {
    if (c1 == 0 && c2 == 0 && c3 == 0) return 0.0;
    if (vis[c1][c2][c3]) return memo[c1][c2][c3];

    double sum = n;
    if (c1 > 0) sum += c1 * solve(c1 - 1, c2, c3);
    if (c2 > 0) sum += c2 * solve(c1 + 1, c2 - 1, c3);
    if (c3 > 0) sum += c3 * solve(c1, c2 + 1, c3 - 1);

    vis[c1][c2][c3] = true;
    return memo[c1][c2][c3] = sum / (c1 + c2 + c3);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    int c1 = 0, c2 = 0, c3 = 0;
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        if (a == 1) c1++;
        else if (a == 2) c2++;
        else if (a == 3) c3++;
    }

    cout << fixed << setprecision(12) << solve(c1, c2, c3) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Expected value recurrence with algebraic self-loop resolution.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Multi-frequency state compression and algebraic self-loop elimination in expected value DP.
- **Reusable Pattern**: `Self-loop elimination: E = (1 + \sum P_i E_i) / (1 - P_{self}).`

---
Back to [Expected Value DP with Multi-Frequency States](../categories/dp/expected_value_dp.md) | [Categories Directory](../categories/README.md)