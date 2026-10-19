# Problem Analysis: AtCoder-arc123_e — E - Training

**Problem ID**: `AtCoder-arc123_e`  
**Contest**: `arc123`  
**Rating / Difficulty**: 2828  
**URL**: https://atcoder.jp/contests/arc123/tasks/arc123_e  
**VJudge Tag**: `[problem:AtCoder-arc123_e]`  
**Category File**: [`../categories/number_theory/arithmetic_level_intersection_floor_sum.md`](../categories/number_theory/arithmetic_level_intersection_floor_sum.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Floor Sum`  
- **Topic (Skill)**: `Floor Sum and Mod Sum of Arithmetic Progression`  

---

## 1. Problem Statement & Key Idea
Two programmers with starting levels A_X, A_Y gain 1 level every B_X, B_Y menus. Count n in 1..N such that A_X + floor(n / B_X) == A_Y + floor(n / B_Y) across T test cases.

## 2. Core Observation & Invariant
Let f(x) = A_X + x/B_X and g(x) = A_Y + x/B_Y with floor functions F(x), G(x). F(x) == G(x) can only hold when f(x) - g(x) is in [-1, 1). In [-1, 0), F(x) in {G(x)-1, G(x)}, so the equality indicator is 1 - G(x) + F(x). In [0, 1), F(x) in {G(x), G(x)+1}, so the indicator is 1 - F(x) + G(x). The range bounds are solved linearly, and prefix sums of floor(A + x/B) over arithmetic progressions evaluate in O(1) time using block division.

## 3. Step-by-Step Algorithm
1. 1. If B_X == B_Y, return N if A_X == A_Y else 0.
2. 2. WLOG assume B_X < B_Y (swapping X and Y if needed), making slope (B_Y - B_X) / (B_X B_Y) strictly positive.
3. 3. Compute boundary thresholds x_m1, x_0, x_p1 for f(x) - g(x) in [-1, 0) and [0, 1) using ceil division.
4. 4. For [x_m1, x_0) intersected with [1, N+1), add (R - L) - sum(G) + sum(F).
5. 5. For [x_0, x_p1) intersected with [1, N+1), add (R - L) - sum(F) + sum(G).
6. 6. Evaluate prefix floor sums sum_{x=0}^{n-1} floor(A + x/B) = n A + B * q*(q-1)/2 + r*q in O(1).

## 4. Complexity Analysis
- **Time Complexity**: `O(1) per test case, O(T) total`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

typedef __int128_t int128;

long long floor_sum_AP(long long n, long long a, long long b) {
    if (n <= 0) return 0;
    long long q = n / b;
    long long r = n % b;
    int128 sum_div = (int128)b * q * (q - 1) / 2 + (int128)r * q;
    return (long long)((int128)n * a + sum_div);
}

long long range_sum_F(long long L, long long R, long long a, long long b) {
    if (L >= R) return 0;
    return floor_sum_AP(R, a, b) - floor_sum_AP(L, a, b);
}

long long ceil_div(int128 num, int128 den) {
    // den > 0
    if (num >= 0) {
        return (long long)((num + den - 1) / den);
    } else {
        return (long long)(num / den);
    }
}

void solve() {
    long long n, ax, bx, ay, by;
    if (!(cin >> n >> ax >> bx >> ay >> by)) return;

    if (bx == by) {
        if (ax == ay) cout << n << "\n";
        else cout << 0 << "\n";
        return;
    }

    if (bx > by) {
        swap(ax, ay);
        swap(bx, by);
    }

    int128 den = by - bx;
    int128 prod = (int128)bx * by;
    int128 D = ax - ay;

    long long x_m1 = ceil_div((-1 - D) * prod, den);
    long long x_0  = ceil_div((0 - D) * prod, den);
    long long x_p1 = ceil_div((1 - D) * prod, den);

    long long ans = 0;

    // Interval 1: [x_m1, x_0)
    long long L1 = max(1LL, x_m1);
    long long R1 = min(n + 1, x_0);
    if (L1 < R1) {
        long long cnt = R1 - L1;
        long long sum_F = range_sum_F(L1, R1, ax, bx);
        long long sum_G = range_sum_F(L1, R1, ay, by);
        ans += cnt - sum_G + sum_F;
    }

    // Interval 2: [x_0, x_p1)
    long long L2 = max(1LL, x_0);
    long long R2 = min(n + 1, x_p1);
    if (L2 < R2) {
        long long cnt = R2 - L2;
        long long sum_F = range_sum_F(L2, R2, ax, bx);
        long long sum_G = range_sum_F(L2, R2, ay, by);
        ans += cnt - sum_F + sum_G;
    }

    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
