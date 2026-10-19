# Problem Analysis: AtCoder-arc082_c — E - ConvexScore

**Problem ID**: `AtCoder-arc082_c`  
**Contest**: `arc082`  
**Rating / Difficulty**: 2729  
**URL**: https://atcoder.jp/contests/arc082/tasks/arc082_c  
**VJudge Tag**: `[problem:AtCoder-arc082_c]`  
**Category File**: [`../categories/geometry/convex_score_points_subsets.md`](../categories/geometry/convex_score_points_subsets.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Convex Hull(2D)`  

---

## 1. Problem Statement & Key Idea
Given N points in the 2D plane (N <= 200). For each subset S that forms a convex polygon with positive area, its score is 2^{n - |S|}, where n is the number of points in the convex hull of S. Find the sum of scores over all convex polygons modulo 998244353.

## 2. Core Observation & Invariant
Notice that 2^{n - |S|} is the number of subsets of points from the interior/boundary of the convex hull of S (excluding S itself). Every subset P of points whose convex hull has positive area has a unique set of extreme vertices S = ext(conv(P)), and P can be any of the 2^{n - |S|} subsets containing S. Therefore, the sum of 2^{n - |S|} over all convex polygons S is EXACTLY the number of non-collinear subsets P of size >= 3! Using complementary counting, the answer is 2^N - 1 - N - binom(N, 2) - sum_{collinear lines L, |L| >= 3} (2^{|L|} - 1 - |L| - binom(|L|, 2)).

## 3. Step-by-Step Algorithm
1. 1. If N < 3, return 0.
2. 2. Compute initial answer: 2^N - 1 - N - N*(N-1)/2 modulo 998244353.
3. 3. Enumerate all pairs of points (i, j) to construct canonical integer line equations a*x + b*y + c = 0.
4. 4. For each distinct line with k >= 3 collinear points, subtract 2^k - 1 - k - k*(k-1)/2 modulo 998244353.
5. 5. Output the result modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <tuple>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

long long power_mod(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long gcd_ll(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<pair<long long, long long>> pts(N);
    for (int i = 0; i < N; ++i) {
        cin >> pts[i].first >> pts[i].second;
    }

    if (N < 3) {
        cout << 0 << "\n";
        return 0;
    }

    long long ans = power_mod(2, N) - 1 - N - (1LL * N * (N - 1) / 2);
    ans = (ans % MOD + MOD) % MOD;

    // Find all distinct lines containing at least 2 points
    set<tuple<long long, long long, long long>> lines;

    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            long long dx = pts[j].first - pts[i].first;
            long long dy = pts[j].second - pts[i].second;

            long long g = gcd_ll(abs(dx), abs(dy));
            dx /= g;
            dy /= g;

            if (dx < 0 || (dx == 0 && dy < 0)) {
                dx = -dx;
                dy = -dy;
            }

            long long a = dy;
            long long b = -dx;
            long long c = -(a * pts[i].first + b * pts[i].second);

            lines.insert({a, b, c});
        }
    }

    for (const auto& line : lines) {
        long long a, b, c;
        tie(a, b, c) = line;
        int k = 0;
        for (int i = 0; i < N; ++i) {
            if (a * pts[i].first + b * pts[i].second + c == 0) {
                k++;
            }
        }
        if (k >= 3) {
            long long sub = power_mod(2, k) - 1 - k - (1LL * k * (k - 1) / 2);
            sub = (sub % MOD + MOD) % MOD;
            ans = (ans - sub + MOD) % MOD;
        }
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
