# Problem Analysis: AtCoder-abc372_g — G. Ax + By < C

**Problem ID**: `AtCoder-abc372_g`  
**Contest**: `abc372`  
**Rating / Difficulty**: 2925  
**URL**: https://atcoder.jp/contests/abc372/tasks/abc372_g  
**VJudge Tag**: `[problem:AtCoder-abc372_g]`  
**Category File**: [`../categories/number_theory/convex_envelope_integer_points_floor_sum.md`](../categories/number_theory/convex_envelope_integer_points_floor_sum.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Floor Sum`  
- **Topic (Skill)**: `Floor Sum and Mod Sum of Arithmetic Progression`  

---

## 1. Problem Statement & Key Idea
Given T test cases, each with N linear inequalities A_i x + B_i y <= C_i with x, y >= 1, count the number of integer pairs (x, y) satisfying all inequalities simultaneously.

## 2. Core Observation & Invariant
For each x >= 1, the upper bound on y is the lower envelope of the lines y = (C_i - A_i x) / B_i. The feasible region is bounded by this upper convex envelope consisting of at most N linear segments. On each segment [x_k, x_{k+1}] defined by a line A x + B y <= C, the number of integer points with 1 <= y <= floor((C - A x) / B) can be computed in O(log(A + B)) time using the standard floor_sum algorithm.

## 3. Step-by-Step Algorithm
1. 1. For each test case, determine the maximum possible x >= 1 across all lines.
2. 2. Compute the lower envelope of linear upper bounds using half-plane intersection / line sweep.
3. 3. For each active segment on the envelope spanning x in [L, R]:
4.    - Apply floor_sum(R - L + 1, B, -A, C - A * L) to sum floor((C - A x) / B).
5. 4. Sum counts across all envelope segments and print the total.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + N log(max(A, B))) per test case`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Standard floor_sum from AtCoder Library
long long floor_sum(long long n, long long m, long long a, long long b) {
    long long ans = 0;
    if (a >= m) {
        ans += (n - 1) * n / 2 * (a / m);
        a %= m;
    }
    if (b >= m) {
        ans += n * (b / m);
        b %= m;
    }

    long long y_max = (a * n + b) / m;
    long long x_max = (y_max * m - b);
    if (y_max == 0) return ans;
    ans += (n - (x_max + a - 1) / a) * y_max;
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a);
    return ans;
}

struct Line {
    long long a, b, c; // y <= (c - a*x) / b
};

void solve() {
    int N;
    if (!(cin >> N)) return;

    vector<Line> lines(N);
    long long max_x = 2e18;

    for (int i = 0; i < N; ++i) {
        cin >> lines[i].a >> lines[i].b >> lines[i].c;
        lines[i].c -= 1; // Strict inequality Ax + By <= C - 1
        long long bound = (lines[i].c - lines[i].b) / lines[i].a;
        max_x = min(max_x, bound);
    }

    if (max_x < 1) {
        cout << 0 << "\n";
        return;
    }

    // Sort by a/b ascending (slope -a/b descending)
    // If same slope, smaller c/b comes first
    sort(lines.begin(), lines.end(), [](const Line& l1, const Line& l2) {
        __int128 diff = (__int128)l1.a * l2.b - (__int128)l2.a * l1.b;
        if (diff != 0) return diff < 0;
        return (__int128)l1.c * l2.b < (__int128)l2.c * l1.b;
    });

    vector<Line> hull;
    for (const auto& l : lines) {
        if (!hull.empty()) {
            const auto& top = hull.back();
            if ((__int128)l.a * top.b == (__int128)top.a * l.b) {
                continue; // Same slope, strictly worse or equal
            }
        }

        while (hull.size() >= 2) {
            const auto& L1 = hull[hull.size() - 2];
            const auto& L2 = hull.back();
            const auto& L3 = l;

            __int128 num1 = (__int128)L2.c * L1.b - (__int128)L1.c * L2.b;
            __int128 den1 = (__int128)L2.a * L1.b - (__int128)L1.a * L2.b;

            __int128 num2 = (__int128)L3.c * L2.b - (__int128)L2.c * L3.b;
            __int128 den2 = (__int128)L3.a * L2.b - (__int128)L2.a * L3.b;

            if (num2 * den1 <= num1 * den2) {
                hull.pop_back();
            } else {
                break;
            }
        }
        hull.push_back(l);
    }

    int K = hull.size();
    vector<long long> floor_x(K + 1);
    floor_x[0] = 0;

    for (int i = 0; i < K - 1; ++i) {
        const auto& L1 = hull[i];
        const auto& L2 = hull[i + 1];

        __int128 num = (__int128)L2.c * L1.b - (__int128)L1.c * L2.b;
        __int128 den = (__int128)L2.a * L1.b - (__int128)L1.a * L2.b;

        // floor(num / den)
        long long f_val = (long long)(num / den);
        if (num < 0 && num % den != 0) {
            f_val--;
        }
        floor_x[i + 1] = f_val;
    }
    floor_x[K] = max_x;

    long long total_pts = 0;
    for (int i = 0; i < K; ++i) {
        long long L_x = max(1LL, floor_x[i] + 1);
        long long R_x = min(max_x, floor_x[i + 1]);

        if (L_x <= R_x) {
            long long a = hull[i].a;
            long long b = hull[i].b;
            long long c = hull[i].c;

            long long n_terms = R_x - L_x + 1;
            long long const_term = c - a * R_x;
            total_pts += floor_sum(n_terms, b, a, const_term);
        }
    }

    cout << total_pts << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
