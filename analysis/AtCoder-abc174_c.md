# Problem Analysis: AtCoder-abc174_c — Repsept

**Problem ID**: `AtCoder-abc174_c`  
**Contest**: `abc174`  
**Rating / Difficulty**: 902  
**URL**: https://atcoder.jp/contests/abc174/tasks/abc174_c  
**VJudge Tag**: `[problem:AtCoder-abc174_c]`  
**Category File**: [`../categories/math/pigeonhole_cycle_linear_congruence.md`](../categories/math/pigeonhole_cycle_linear_congruence.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Pigeonhole Cycle Detection on Linear Congruence Sequence`  

---

## 1. Problem Statement & Key Idea
Given K <= 10^6. Does the sequence 7, 77, 777, ... contain any term divisible by K? If so, find the index of the first such term, else output -1.

**Key Idea**: Let a_1 = 7 % K and a_i = (10 * a_{i-1} + 7) % K. We are looking for the smallest i such that a_i == 0.

## 2. Core Observation & Invariant
Because there are only K possible remainders modulo K, by the Pigeonhole Principle, if 0 does not appear in the first K iterations, a remainder must repeat, entering a deterministic periodic cycle that will never reach 0.

## 3. Step-by-Step Algorithm
1. Initialize rem = 0.
2. For step i from 1 to K: rem = (rem * 10 + 7) % K. If rem == 0, return i.
3. If loop completes without rem == 0, output -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(K)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long k;
    if (!(cin >> k)) return 0;

    long long rem = 0;
    for (int i = 1; i <= k; ++i) {
        rem = (rem * 10 + 7) % k;
        if (rem == 0) {
            cout << i << "\n";
            return 0;
        }
    }

    cout << -1 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Cycle detection on linear congruences using Pigeonhole bound.
- **Reusable Pattern**: `Bounded remainder simulation: test at most K steps modulo K.`
