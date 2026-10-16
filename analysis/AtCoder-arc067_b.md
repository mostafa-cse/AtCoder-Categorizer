# Problem Analysis: AtCoder-arc067_b — Walk and Teleport

**Problem ID**: `AtCoder-arc067_b`  
**Contest**: `abc052`  
**Rating / Difficulty**: 1060  
**URL**: https://atcoder.jp/contests/abc052/tasks/arc067_b  
**VJudge Tag**: `[problem:AtCoder-arc067_b]`  
**Category File**: [`../categories/basics/adjacent_step_greedy_comparison.md`](../categories/basics/adjacent_step_greedy_comparison.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Adjacent Greedy Transition / Cost Comparison`  

---

## 1. Problem Statement & Key Idea
N towns on a 1D line at coordinates X_1 < X_2 < ... < X_N. You start at X_1 and visit all towns in increasing order. Walking distance d costs d * A fatigue; teleporting to any town costs B fatigue. Find the minimum fatigue to visit all towns.

**Key Idea**: Visiting towns 1..N in increasing order means we transition from X_i to X_{i+1} for each i in 1..N-1.

## 2. Core Observation & Invariant
Each step between adjacent towns i and i+1 is completely independent. For each segment, walking costs (X_{i+1} - X_i) * A, while teleporting costs B. The optimal choice is strictly min((X_{i+1} - X_i) * A, B).

## 3. Step-by-Step Algorithm
1. Initialize total_fatigue = 0.
2. For i from 0 to N - 2: total_fatigue += min((X[i+1] - X[i]) * A, B).
3. Print total_fatigue.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long a, b;
    if (!(cin >> n >> a >> b)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) {
        cin >> x[i];
    }

    long long total = 0;
    for (int i = 0; i < n - 1; ++i) {
        long long walk = (x[i + 1] - x[i]) * a;
        total += min(walk, b);
    }

    cout << total << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Independent local greedy decisions along monotonic 1D paths.
- **Reusable Pattern**: `Adjacent choice: sum min((X[i+1] - X[i]) * cost_per_unit, fixed_cost).`
