# Problem Analysis: AtCoder-dp_y — Grid 2

**Problem ID**: `AtCoder-dp_y`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 2150  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_y  
**VJudge Tag**: `[problem:AtCoder-dp_y]`  
**Category File**: [`../categories/dp/inclusion_exclusion_dp.md`](../categories/dp/inclusion_exclusion_dp.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion-Exclusion`  
- **Topic (Skill)**: `First-Hit Obstacle Inclusion-Exclusion DP`  

---

## 1. Problem Statement & Key Idea
Grid of size H x W with N <= 3000 obstacles. Count paths from (1, 1) to (H, W) avoiding all obstacles. (H, W <= 10^5).

**Core Idea**: Grid is too huge for 2D DP (H, W <= 10^5), but obstacle count N <= 3000 is small. Define dp[i] = paths from (1, 1) to obstacle i whose FIRST encountered obstacle is obstacle i.

## 2. Core Observation & Invariant
dp[i] = binom((r_i - 1) + (c_i - 1), r_i - 1) - sum_{j < i, r_j <= r_i, c_j <= c_i} (dp[j] * binom((r_i - r_j) + (c_i - c_j), r_i - r_j)).

## 3. Step-by-Step Algorithm
1. Add destination (H, W) as (N+1)-th obstacle.
2. Sort obstacles by (r, c).
3. Precompute factorials and inverse factorials up to H + W.
4. For each obstacle i: dp[i] = ways(1,1 to i) - sum_{j < i} (dp[j] * ways(j to i)).
5. Return dp[destination].

## 4. Complexity Analysis
Time: O(N^2 + (H + W)), Space: O(N + H + W).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1e9 + 7;
const int MAX = 200005;

long long fact[MAX], invFact[MAX];

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAX; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAX - 1] = modInverse(fact[MAX - 1]);
    for (int i = MAX - 2; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

long long paths(int r1, int c1, int r2, int c2) {
    int dr = r2 - r1;
    int dc = c2 - c1;
    if (dr < 0 || dc < 0) return 0;
    return nCr(dr + dc, dr);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int h, w, n;
    if (!(cin >> h >> w >> n)) return 0;

    struct Point { int r, c; };
    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].r >> pts[i].c;

    // Add destination
    pts.push_back({h, w});
    sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
        if (a.r != b.r) return a.r < b.r;
        return a.c < b.c;
    });

    int total_pts = pts.size();
    vector<long long> dp(total_pts, 0);

    for (int i = 0; i < total_pts; ++i) {
        dp[i] = paths(1, 1, pts[i].r, pts[i].c);
        for (int j = 0; j < i; ++j) {
            if (pts[j].r <= pts[i].r && pts[j].c <= pts[i].c) {
                long long subtract = (dp[j] * paths(pts[j].r, pts[j].c, pts[i].r, pts[i].c)) % MOD;
                dp[i] = (dp[i] - subtract + MOD) % MOD;
            }
        }
    }

    cout << dp[total_pts - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
First-hit obstacle inclusion-exclusion dynamic programming.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combinatorial grid paths with obstacles using first-encounter inclusion-exclusion.
- **Reusable Pattern**: `First-hit inclusion-exclusion over coordinate points.`

---
Back to [First-Hit Obstacle Inclusion-Exclusion DP](../categories/dp/inclusion_exclusion_dp.md) | [Categories Directory](../categories/README.md)