# Problem Analysis: AtCoder-arc117_c — Tricolor Pyramid

**Problem ID**: `AtCoder-arc117_c`  
**Contest**: `arc117`  
**Rating / Difficulty**: 1768  
**URL**: https://atcoder.jp/contests/arc117/tasks/arc117_c  
**VJudge Tag**: `[problem:AtCoder-arc117_c]`  
**Category File**: [`../categories/math/cellular_automaton_lucas_theorem_mod3.md`](../categories/math/cellular_automaton_lucas_theorem_mod3.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Lucas Theorem`  
- **Topic (Skill)**: `Cellular Automaton Modulo 3 Linearity via Pascal & Lucas' Theorem`  

---

## 1. Problem Statement & Key Idea
A bottom row of N blocks has colors 'B', 'W', 'R' (encoded as 0, 1, 2 mod 3). Adjacent blocks of identical colors yield that color; different colors yield the third color. Determine the color at the apex (top) of the pyramid.

**Key Insight**: The transition function for colors x and y in Z_3 is f(x, y) = -(x + y) mod 3. Propagating this linear relation up N - 1 levels gives the apex color: (-1)^{N - 1} * sum_{i=0}^{N - 1} C(N - 1, i) * c_i mod 3.

## 2. Core Observation & Invariant
C(N - 1, i) mod 3 can be computed in O(log_3 N) using Lucas' Theorem, or by maintaining 3-adic valuations of factorials.

## 3. Step-by-Step Algorithm
1. Map 'B' -> 0, 'W' -> 1, 'R' -> 2.
2. Write a function nCr_mod3(n, r) using Lucas' Theorem:
3.   while n > 0 or r > 0:
4.     ni = n % 3, ri = r % 3;
5.     if ri > ni: return 0;
6.     res = res * comb(ni, ri) % 3;
7.     n /= 3, r /= 3;
8. Compute apex = (-1)^{N - 1} * sum_{i=0}^{N - 1} nCr_mod3(N - 1, i) * color[i] mod 3.
9. Map apex mod 3 back to character and print.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log_3 N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int comb_small(int n, int r) {
    if (r < 0 || r > n) return 0;
    if (r == 0 || r == n) return 1;
    return n; // n=2, r=1 -> 2
}

int lucas(int n, int r) {
    int res = 1;
    while (n > 0 || r > 0) {
        int ni = n % 3;
        int ri = r % 3;
        if (ri > ni) return 0;
        res = (res * comb_small(ni, ri)) % 3;
        n /= 3;
        r /= 3;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    string s;
    cin >> s;

    auto char_to_val = [](char c) -> int {
        if (c == 'B') return 0;
        if (c == 'W') return 1;
        return 2; // 'R'
    };

    auto val_to_char = [](int v) -> char {
        if (v == 0) return 'B';
        if (v == 1) return 'W';
        return 'R';
    };

    long long sum_val = 0;
    for (int i = 0; i < n; ++i) {
        int coeff = lucas(n - 1, i);
        sum_val += coeff * char_to_val(s[i]);
    }

    sum_val %= 3;

    if ((n - 1) % 2 == 1) {
        sum_val = (3 - sum_val) % 3;
    }

    cout << val_to_char(sum_val) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Recognizing linear modular recurrence in 2D cellular automata and computing binomial coefficients via Lucas' Theorem.
- **Reusable Pattern**: `Pyramid Modulo Linearity: Apex = (-1)^{N-1} sum C(N-1, i) * A[i] mod P using Lucas' Theorem.`
