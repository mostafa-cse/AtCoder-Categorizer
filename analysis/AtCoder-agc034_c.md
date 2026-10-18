# Problem Analysis: AtCoder-agc034_c — C. Tests

**Problem ID**: `AtCoder-agc034_c`  
**Contest**: `agc034`  
**Rating / Difficulty**: 2497  
**URL**: https://atcoder.jp/contests/agc034/tasks/agc034_c  
**VJudge Tag**: `[problem:AtCoder-agc034_c]`  
**Category File**: [`../categories/basics/tests_greedy_exam_hours_binary_search.md`](../categories/basics/tests_greedy_exam_hours_binary_search.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Binary Search`  

---

## 1. Problem Statement & Key Idea
Find the minimum total study hours $H$ across $N$ exams so Takahashi's score equals or exceeds Aoki's. Aoki scores $b_i$ on exam $i$. For Takahashi, scoring $s_i \le b_i$ yields $s_i l_i$, while $s_i > b_i$ yields $b_i l_i + (s_i - b_i) u_i$. The score gain function is convex piecewise linear. In an optimal solution, at most one test receives partial study hours $r \in [0, X)$, and $q$ tests receive full $X$ hours. Monotonicity allows binary searching on the total hours $H = qX + r$.

## 2. Core Observation & Invariant
If exam $i$ is chosen to receive partial hours $r$, the remaining $q$ exams receiving full score $X$ should greedily be the ones with the largest maximum gain $b_j l_j + (X - b_j) u_j$. Sorting exams by maximum gain and maintaining prefix sums allows an $O(1)$ check for any candidate exam $i$, resulting in an $O(N)$ feasibility check per binary search iteration.

## 3. Step-by-Step Algorithm
1. 1. Calculate target total score $T = \sum b_i l_i$.
2. 2. For each exam, compute full gain $\Delta_i(X) = b_i l_i + (X - b_i) u_i$.
3. 3. Sort exams by $\Delta_i(X)$ descending and compute prefix sums.
4. 4. Binary search on $H \in [0, NX]$:
5.    a. Decompose $H = qX + r$.
6.    b. If $q \ge N$, return true.
7.    c. For each exam $i$, compute gain from $r$ hours and add the top $q$ full gains excluding $i$.
8.    d. If any choice yields total gain $\ge T$, return true.
9. 5. Output the minimal feasible $H$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log(NX))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Exam {
    long long b, l, u;
    long long gain_X;
    int id;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long X;
    if (!(cin >> n >> X)) return 0;

    vector<Exam> exams(n);
    long long target = 0;
    for (int i = 0; i < n; ++i) {
        cin >> exams[i].b >> exams[i].l >> exams[i].u;
        exams[i].gain_X = exams[i].b * exams[i].l + (X - exams[i].b) * exams[i].u;
        exams[i].id = i;
        target += exams[i].b * exams[i].l;
    }

    sort(exams.begin(), exams.end(), [](const Exam& a, const Exam& b) {
        return a.gain_X > b.gain_X;
    });

    vector<long long> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + exams[i].gain_X;
    }

    auto check = [&](long long H) -> bool {
        long long q = H / X;
        long long r = H % X;
        if (q >= n) return true;

        for (int i = 0; i < n; ++i) {
            long long gain_r = 0;
            if (r <= exams[i].b) {
                gain_r = r * exams[i].l;
            } else {
                gain_r = exams[i].b * exams[i].l + (r - exams[i].b) * exams[i].u;
            }

            long long cur = 0;
            if (i < q) {
                cur = (pref[q + 1] - exams[i].gain_X) + gain_r;
            } else {
                cur = pref[q] + gain_r;
            }

            if (cur >= target) return true;
        }
        return false;
    };

    long long low = 0, high = (long long)n * X, ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
