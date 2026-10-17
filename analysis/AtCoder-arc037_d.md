# Problem Analysis: AtCoder-arc037_d — D. Chaotic Polygons

**Problem ID**: `AtCoder-arc037_d`  
**Contest**: `arc037`  
**Rating / Difficulty**: 2258  
**URL**: https://atcoder.jp/contests/arc037/tasks/arc037_d  
**VJudge Tag**: `[problem:AtCoder-arc037_d]`  
**Category File**: [`../categories/dp/sierpinski_gasket_fractal_path_cycle_dp.md`](../categories/dp/sierpinski_gasket_fractal_path_cycle_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Count the number of simple polygons (cycles) formed by the line segments of a Level $L$ Sierpinski gasket modulo $10^9+7$.

## 2. Core Observation & Invariant
A Level $k$ Sierpinski gasket consists of 3 Level $(k-1)$ sub-gaskets meeting at 3 contact vertices. Any simple cycle is either entirely inside one of the 3 sub-gaskets, or visits all 3 sub-gaskets by traversing a path between the contact vertices in each sub-gasket.
Maintaining $a_k$ (paths between two corners not touching the third corner), $b_k$ (paths touching the third corner), and $c_k$ (cycles) yields exact closed-form recurrences: $c_k = 3 c_{k-1} + (a_{k-1} + b_{k-1})^3$, $b_k = b_{k-1} (a_{k-1}^2 + 2 a_{k-1} b_{k-1})$, $a_k = (a_{k-1} + b_{k-1})^2 + a_{k-1} (a_{k-1}^2 + 2 a_{k-1} b_{k-1})$.

## 3. Step-by-Step Algorithm
1. Initialize $a = 1, b = 1, c = 1$ for Level 0.
2. Loop $k$ from 1 to $L$, updating $a, b, c$ using modular arithmetic.
3. Output $c$.

## 4. Complexity Analysis
- **Time Complexity**: `O(L)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int L;
    if (!(cin >> L)) return 0;

    long long a = 1;
    long long b = 1;
    long long c = 1;

    for (int k = 1; k <= L; ++k) {
        long long apb = (a + b) % MOD;
        long long apb2 = (apb * apb) % MOD;
        long long apb3 = (apb2 * apb) % MOD;

        long long c_next = (3 * c + apb3) % MOD;
        long long shared = (a * a + 2 * a % MOD * b) % MOD;
        long long a_next = (apb2 + a * shared) % MOD;
        long long b_next = (b * shared) % MOD;

        a = a_next;
        b = b_next;
        c = c_next;
    }

    cout << c << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
