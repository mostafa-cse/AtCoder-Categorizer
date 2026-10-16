# Problem Analysis: AtCoder-abc121_d — XOR World

**Problem ID**: `AtCoder-abc121_d`  
**Contest**: `abc121`  
**Rating / Difficulty**: 1164  
**URL**: https://atcoder.jp/contests/abc121/tasks/abc121_d  
**VJudge Tag**: `[problem:AtCoder-abc121_d]`  
**Category File**: [`../categories/math/period_4_prefix_xor_invariant.md`](../categories/math/period_4_prefix_xor_invariant.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Bitwise Invariants`  
- **Topic (Skill)**: `Period-4 Prefix XOR Invariant`  

---

## 1. Problem Statement & Key Idea
Compute the XOR sum of all integers between A and B inclusive: A XOR (A + 1) ... XOR B (A, B <= 10^12).

**Key Idea**: The range XOR is F(B) XOR F(A - 1), where F(n) = 0 XOR 1 XOR ... XOR n.

## 2. Core Observation & Invariant
Every 4 consecutive integers starting at an even multiple of 4 (4k, 4k+1, 4k+2, 4k+3) XOR to 0: (4k XOR (4k+1)) = 1, and ((4k+2) XOR (4k+3)) = 1, and 1 XOR 1 = 0! Therefore F(n) depends only on n % 4: n % 4 == 0 -> n; n % 4 == 1 -> 1; n % 4 == 2 -> n + 1; n % 4 == 3 -> 0.

## 3. Step-by-Step Algorithm
1. Define F(n): if n < 0 return 0; if n % 4 == 0 return n; if n % 4 == 1 return 1; if n % 4 == 2 return n + 1; else return 0.
2. Output F(B) ^ F(A - 1).

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>

using namespace std;

long long f(long long n) {
    if (n < 0) return 0;
    long long rem = n % 4;
    if (rem == 0) return n;
    if (rem == 1) return 1;
    if (rem == 2) return n + 1;
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    cout << (f(b) ^ f(a - 1)) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Period-4 cancellation pattern for cumulative bitwise XOR.
- **Reusable Pattern**: `Cumulative XOR F(n): {n, 1, n+1, 0}[n % 4].`
