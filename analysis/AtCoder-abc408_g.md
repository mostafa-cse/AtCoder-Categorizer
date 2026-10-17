# Problem Analysis: AtCoder-abc408_g — G. A/B < p/q < C/D

**Problem ID**: `AtCoder-abc408_g`  
**Contest**: `abc408`  
**Rating / Difficulty**: 2167  
**URL**: https://atcoder.jp/contests/abc408/tasks/abc408_g  
**VJudge Tag**: `[problem:AtCoder-abc408_g]`  
**Category File**: [`../categories/miscellaneous/stern_brocot_simplest_fraction_euclidean_reduction.md`](../categories/miscellaneous/stern_brocot_simplest_fraction_euclidean_reduction.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Stern-Brocot Tree and Rational Approximation`  

---

## 1. Problem Statement & Key Idea
Given positive integers A, B, C, D with A/B < C/D, find the smallest denominator q such that there exists an integer p with A/B < p/q < C/D. Solved in O(log(min(B, D))) using the Stern-Brocot Euclidean mediant reduction / continued fractions.

## 2. Core Observation & Invariant
If floor(A/B) + 1 < C/D, an integer exists strictly between the fractions, so q = 1. Otherwise, floor(A/B) = k. Subtracting k gives 0 <= (A - kB)/B < p'/q < (C - kD)/D <= 1. Inverting the inequality yields D/(C - kD) < q/p' < B/(A - kB), which recursively asks for the simplest fraction (minimal numerator q) strictly between the inverted bounds.

## 3. Step-by-Step Algorithm
1. Define recursive function find_pq(A, B, C, D) returning (p, q).
2. Let k = A / B. If (k + 1) * D < C, return (k + 1, 1).
3. If A == k * B, return (k * q + 1, q) where q = D / (C - k*D) + 1.
4. Otherwise, recursively compute (q, p') = find_pq(D, C - k*D, B, A - k*B). Return (k * q + p', q).
5. Use __int128 to prevent overflow during intermediate operations.

## 4. Complexity Analysis
- **Time Complexity**: `O(log(min(B, D))) per testcase`
- **Space Complexity**: `O(log(min(B, D)))`

## 5. C++ Source Code
```cpp
#include <iostream>

using namespace std;

pair<__int128, __int128> find_pq(__int128 A, __int128 B, __int128 C, __int128 D) {
    __int128 k = A / B;
    if ((k + 1) * D < C) {
        return {k + 1, 1};
    }
    if (A == k * B) {
        __int128 rem_C = C - k * D;
        __int128 q = D / rem_C + 1;
        return {k * q + 1, q};
    }
    __int128 rem_A = A - k * B;
    __int128 rem_C = C - k * D;
    auto [q, p_prime] = find_pq(D, rem_C, B, rem_A);
    return {k * q + p_prime, q};
}

void solve_case() {
    long long a, b, c, d;
    cin >> a >> b >> c >> d;
    auto [p, q] = find_pq(a, b, c, d);
    cout << (long long)q << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve_case();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
