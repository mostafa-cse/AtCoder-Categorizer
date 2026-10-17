# Problem Analysis: AtCoder-arc094_b — Worst Case

**Problem ID**: `AtCoder-arc094_b`  
**Contest**: `abc093`  
**Rating / Difficulty**: 1869  
**URL**: https://atcoder.jp/contests/abc093/tasks/arc094_b  
**VJudge Tag**: `[problem:AtCoder-arc094_b]`  
**Category File**: [`../categories/basics/am_gm_hyperbolic_product_pairing.md`](../categories/basics/am_gm_hyperbolic_product_pairing.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `AM-GM / Hyperbolic Bounding`  
- **Topic (Skill)**: `AM-GM Hyperbolic Pairing for Strict Product Inequalities`  

---

## 1. Problem Statement & Key Idea
Takahashi scored A in round 1 and B in round 2 (total product A * B). Find the maximum number of contestants whose product x_i * y_i is strictly less than A * B, given that all scores are distinct positive integers not using A in round 1 or B in round 2.

**Key Insight**: Let P = A * B. To maximize elements with x * y < P, pair scores around the square root C = floor(sqrt(P - 1)). By AM-GM, product x * y peaks when x approx y approx sqrt(P).

## 2. Core Observation & Invariant
If A == B: answer is 2A - 2. If A != B: let C = floor(sqrt(P - 1)). If C * (C + 1) < P, answer is 2 * C - 1; otherwise answer is 2 * C - 2.

## 3. Step-by-Step Algorithm
1. For each query (A, B):
2.   if A == B: print 2 * A - 2, continue.
3.   P = A * B.
4.   C = sqrt(P - 1).
5.   while ((C + 1) * (C + 1) <= P - 1) C++;
6.   while (C * C > P - 1) C--;
7.   if (C * (C + 1) < P) ans = 2 * C - 1;
8.   else ans = 2 * C - 2;
9.   print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(1) per query`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <cmath>

using namespace std;

void solve() {
    long long a, b;
    cin >> a >> b;

    if (a == b) {
        cout << 2 * a - 2 << "\n";
        return;
    }

    long long P = a * b;
    long long c = sqrt(P - 1);
    while ((c + 1) * (c + 1) <= P - 1) c++;
    while (c * c > P - 1) c--;

    if (c * (c + 1) < P) {
        cout << 2 * c - 1 << "\n";
    } else {
        cout << 2 * c - 2 << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (cin >> q) {
        while (q--) solve();
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Hyperbolic product bound maximization under distinctness and omitted value constraints.
- **Reusable Pattern**: `Strict Product Bound: Compare C*(C+1) with P-1 where C = floor(sqrt(P-1)).`
