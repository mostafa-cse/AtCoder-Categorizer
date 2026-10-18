# Problem Analysis: AtCoder-abc479_g — G. Tuning

**Problem ID**: `AtCoder-abc479_g`  
**Contest**: `abc479`  
**Rating / Difficulty**: 2386  
**URL**: https://atcoder.jp/contests/abc479/tasks/abc479_g  
**VJudge Tag**: `[problem:AtCoder-abc479_g]`  
**Category File**: [`../categories/miscellaneous/collinear_manhattan_weighted_median.md`](../categories/miscellaneous/collinear_manhattan_weighted_median.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Search Techniques`  
- **Topic (Skill)**: `Ternary Search`  

---

## 1. Problem Statement & Key Idea
Given points (A_i, B_i), minimize sum of Manhattan perturbations |c_i| + |d_i| such that all points become collinear through the origin. The Manhattan distance to line Y = s X (|s| <= 1) is |B_i - s A_i|, and to X = t Y (|t| <= 1) is |A_i - t B_i|. Both reduce to weighted median problems on rational slopes, solved with __int128 exact arithmetic in O(N log N) time.

## 2. Core Observation & Invariant
Perturbed points (A_i + c_i, B_i + d_i) lie on a line through the origin. The minimum Manhattan distance from (A_i, B_i) to line Y = s X (|s| <= 1) is |B_i - s A_i|, and to X = t Y (|t| <= 1) is |A_i - t B_i|. Both reduce to finding the weighted median of critical slope ratios in [-1, 1], evaluated exactly using __int128 rational arithmetic.

## 3. Step-by-Step Algorithm
1. Case 1: Line Y = s X with s in [-1, 1]. For points with A_i != 0, critical points are B_i / A_i with weight |A_i|. Sort points in [-1, 1] and find the weighted median s, clamping to [-1, 1]. Evaluate sum |B_i - s A_i|.
2. Case 2: Line X = t Y with t in [-1, 1]. For points with B_i != 0, critical points are A_i / B_i with weight |B_i|. Find weighted median t clamped to [-1, 1] and evaluate sum |A_i - t B_i|.
3. Take the minimum of the two cases and output the exact irreducible fraction p / q.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

typedef __int128_t int128;

int128 gcd128(int128 a, int128 b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

struct Frac {
    int128 num, den;
    Frac(int128 n = 0, int128 d = 1) {
        if (d < 0) { n = -n; d = -d; }
        int128 g = gcd128(n, d);
        num = n / g;
        den = d / g;
    }
    bool operator<(const Frac& o) const {
        return num * o.den < o.num * den;
    }
    bool operator<=(const Frac& o) const {
        return num * o.den <= o.num * den;
    }
    bool operator>(const Frac& o) const {
        return num * o.den > o.num * den;
    }
    Frac operator*(const Frac& o) const {
        return Frac(num * o.num, den * o.den);
    }
    Frac operator+(const Frac& o) const {
        return Frac(num * o.den + o.num * den, den * o.den);
    }
    Frac operator-(const Frac& o) const {
        return Frac(num * o.den - o.num * den, den * o.den);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> A(n), B(n);
    for (int i = 0; i < n; ++i) cin >> A[i];
    for (int i = 0; i < n; ++i) cin >> B[i];

    // Case 1: slope s in [-1, 1], cost is sum |B_i - s * A_i|
    struct Pt1 {
        Frac s;
        int128 w;
        bool operator<(const Pt1& o) const {
            return s < o.s;
        }
    };
    vector<Pt1> pts1;
    int128 const1 = 0;
    int128 total_w1 = 0;
    for (int i = 0; i < n; ++i) {
        if (A[i] == 0) {
            const1 += abs(B[i]);
        } else {
            Frac si(B[i], A[i]);
            int128 w = abs(A[i]);
            pts1.push_back({si, w});
            total_w1 += w;
        }
    }
    sort(pts1.begin(), pts1.end());
    Frac best_s(0, 1);
    int128 cur_w1 = 0;
    for (auto& pt : pts1) {
        cur_w1 += pt.w;
        if (cur_w1 * 2 >= total_w1) {
            best_s = pt.s;
            break;
        }
    }
    if (best_s < Frac(-1, 1)) best_s = Frac(-1, 1);
    if (best_s > Frac(1, 1)) best_s = Frac(1, 1);

    Frac val1(const1, 1);
    for (int i = 0; i < n; ++i) {
        if (A[i] != 0) {
            Frac diff = Frac(B[i], 1) - best_s * Frac(A[i], 1);
            if (diff.num < 0) diff.num = -diff.num;
            val1 = val1 + diff;
        }
    }

    // Case 2: slope t in [-1, 1], cost is sum |A_i - t * B_i|
    vector<Pt1> pts2;
    int128 const2 = 0;
    int128 total_w2 = 0;
    for (int i = 0; i < n; ++i) {
        if (B[i] == 0) {
            const2 += abs(A[i]);
        } else {
            Frac ti(A[i], B[i]);
            int128 w = abs(B[i]);
            pts2.push_back({ti, w});
            total_w2 += w;
        }
    }
    sort(pts2.begin(), pts2.end());
    Frac best_t(0, 1);
    int128 cur_w2 = 0;
    for (auto& pt : pts2) {
        cur_w2 += pt.w;
        if (cur_w2 * 2 >= total_w2) {
            best_t = pt.s;
            break;
        }
    }
    if (best_t < Frac(-1, 1)) best_t = Frac(-1, 1);
    if (best_t > Frac(1, 1)) best_t = Frac(1, 1);

    Frac val2(const2, 1);
    for (int i = 0; i < n; ++i) {
        if (B[i] != 0) {
            Frac diff = Frac(A[i], 1) - best_t * Frac(B[i], 1);
            if (diff.num < 0) diff.num = -diff.num;
            val2 = val2 + diff;
        }
    }

    Frac ans = (val1 < val2 ? val1 : val2);
    // Print numerator and denominator
    auto print128 = [](int128 x) {
        if (x == 0) {
            cout << 0;
            return;
        }
        string s;
        while (x > 0) {
            s.push_back((char)('0' + (x % 10)));
            x /= 10;
        }
        reverse(s.begin(), s.end());
        cout << s;
    };
    print128(ans.num);
    cout << " ";
    print128(ans.den);
    cout << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
