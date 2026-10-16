# Problem Analysis: AtCoder-arc062_a — AtCoDeer and Election Report

**Problem ID**: `AtCoder-arc062_a`  
**Contest**: `abc046`  
**Rating / Difficulty**: 1346  
**URL**: https://atcoder.jp/contests/abc046/tasks/arc062_a  
**VJudge Tag**: `[problem:AtCoder-arc062_a]`  
**Category File**: [`../categories/math/monotonic_ratio_multiplier.md`](../categories/math/monotonic_ratio_multiplier.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Greedy Multipliers`  
- **Topic (Skill)**: `Monotonic Ratio Ceiling Multiplier`  

---

## 1. Problem Statement & Key Idea
Two candidates with vote ratios T_i : A_i reported N times. Current votes never decrease: cur_T >= prev_T and cur_A >= prev_A. At step i, votes must be in ratio T_i : A_i (i.e. cur_T = k * T_i, cur_A = k * A_i for some integer k >= 1). Minimize final total votes cur_T + cur_A.

**Key Idea**: Find the smallest integer multiplier k >= 1 such that k * T_i >= cur_T and k * A_i >= cur_A.

## 2. Core Observation & Invariant
To satisfy both inequalities simultaneously, k must satisfy: k >= ceil(cur_T / T_i) = (cur_T + T_i - 1) / T_i, and k >= ceil(cur_A / A_i) = (cur_A + A_i - 1) / A_i. Setting k = max((cur_T + T_i - 1) / T_i, (cur_A + A_i - 1) / A_i) greedily minimizes votes at each step.

## 3. Step-by-Step Algorithm
1. Initialize cur_T = T[0], cur_A = A[0].
2. For i from 1 to N - 1:
3.   k = max((cur_T + T[i] - 1) / T[i], (cur_A + A[i] - 1) / A[i]).
4.   cur_T = k * T[i]; cur_A = k * A[i].
5. Print cur_T + cur_A.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long cur_t, cur_a;
    cin >> cur_t >> cur_a;

    for (int i = 1; i < n; ++i) {
        long long t, a;
        cin >> t >> a;

        long long kt = (cur_t + t - 1) / t;
        long long ka = (cur_a + a - 1) / a;
        long long k = max(kt, ka);

        cur_t = k * t;
        cur_a = k * a;
    }

    cout << cur_t + cur_a << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy ratio multiplier expansion under componentwise monotonic lower bounds.
- **Reusable Pattern**: `Min multiplier k: k = max(ceil(cur_A / new_A), ceil(cur_B / new_B)).`
