# Problem Analysis: AtCoder-abc119_d — Lazy Faith

**Problem ID**: `AtCoder-abc119_d`  
**Contest**: `abc119`  
**Rating / Difficulty**: 1346  
**URL**: https://atcoder.jp/contests/abc119/tasks/abc119_d  
**VJudge Tag**: `[problem:AtCoder-abc119_d]`  
**Category File**: [`../categories/basics/dual_binary_search_two_arrays.md`](../categories/basics/dual_binary_search_two_arrays.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search`  
- **Topic (Skill)**: `Dual Binary Search on Two Sorted Arrays (Shrines & Temples)`  

---

## 1. Problem Statement & Key Idea
A line with A shrines at s_1 < ... < s_A and B temples at t_1 < ... < t_B. Q queries: start at x_i, visit at least 1 shrine and 1 temple. Find the minimum distance traveled.

**Key Idea**: For any starting coordinate x, the optimal shrine must be either the nearest shrine to the left (s_L <= x) or nearest shrine to the right (s_R >= x). The same holds for temples (t_L <= x and t_R >= x).

## 2. Core Observation & Invariant
Using std::lower_bound in s and t, we find the 2 closest shrines and 2 closest temples, producing at most 2 x 2 = 4 candidate pairs (S, T). For a pair (S, T), distance from x is: min(abs(x - S), abs(x - T)) + abs(S - T). We test all 4 combinations in O(1)!

## 3. Step-by-Step Algorithm
1. Sort shrine coordinates s and temple coordinates t.
2. Add -INF and +INF sentinels to avoid boundary checks.
3. For each query x:
4.   Find lower_bound in s: gives s_R, and previous element is s_L.
5.   Find lower_bound in t: gives t_R, and previous element is t_L.
6.   Test 4 candidate pairs (S, T): dist = min(abs(x - S), abs(x - T)) + abs(S - T).
7.   Print the minimum distance.

## 4. Complexity Analysis
- **Time Complexity**: `O((A + B + Q) log(A + B))`
- **Space Complexity**: `O(A + B)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, q;
    if (!(cin >> a >> b >> q)) return 0;

    vector<long long> s(a + 2), t(b + 2);
    s[0] = -INF; s[a + 1] = INF;
    t[0] = -INF; t[b + 1] = INF;

    for (int i = 1; i <= a; ++i) cin >> s[i];
    for (int i = 1; i <= b; ++i) cin >> t[i];

    while (q--) {
        long long x;
        cin >> x;

        auto it_s = lower_bound(s.begin(), s.end(), x);
        long long s_r = *it_s;
        long long s_l = *(it_s - 1);

        auto it_t = lower_bound(t.begin(), t.end(), x);
        long long t_r = *it_t;
        long long t_l = *(it_t - 1);

        long long ans = INF;
        for (long long S : {s_l, s_r}) {
            for (long long T : {t_l, t_r}) {
                long long d = min(abs(x - S), abs(x - T)) + abs(S - T);
                ans = min(ans, d);
            }
        }

        cout << ans << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Dual binary search neighbor retrieval and 4-way turn-around path minimization.
- **Reusable Pattern**: `Visit nearest of set A and set B from x: test 4 combinations of left/right neighbors.`
