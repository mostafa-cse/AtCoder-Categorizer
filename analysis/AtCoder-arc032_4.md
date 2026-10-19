# Problem Analysis: AtCoder-arc032_4 — D - アットコーダーモンスターズ

**Problem ID**: `AtCoder-arc032_4`  
**Contest**: `arc032`  
**Rating / Difficulty**: 2861  
**URL**: https://atcoder.jp/contests/arc032/tasks/arc032_4  
**VJudge Tag**: `[problem:AtCoder-arc032_4]`  
**Category File**: [`../categories/combinatorics/chebyshev_bounding_square_subsets_inclusion_exclusion.md`](../categories/combinatorics/chebyshev_bounding_square_subsets_inclusion_exclusion.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Given N points in 2D, find the minimum side length L of an axis-aligned bounding square that can cover at least K points, and count the number of subsets of K points whose Chebyshev bounding square has side length exactly L, modulo 10^9+7.

## 2. Core Observation & Invariant
First, the minimum side length L is determined by sorting pairwise coordinate differences or binary searching with a 2D sliding window. Once L is fixed, any valid subset of K points must have Chebyshev bounding square of side length exactly L. For each candidate position of an L x L square, we use inclusion-exclusion across the 4 boundaries (left, right, bottom, top) to count subsets of size K that span both horizontally by L and vertically by L.

## 3. Step-by-Step Algorithm
1. 1. Binary search for the minimum bounding square side length L using 2D prefix sums / sliding window.
2. 2. Discretize coordinates of points and grid squares.
3. 3. For each bounding square [X, X+L] x [Y, Y+L], use 2D range counts to get total points C.
4. 4. Apply 4-boundary inclusion-exclusion: C(C, K) - C(C_strict, K) ... to count subsets whose bounding box matches [X, X+L] x [Y, Y+L] exactly.
5. 5. Sum counts modulo 10^9+7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 log N)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MAXC = 3000;
static const long long MOD = 1000000007;

int grid[MAXC + 2][MAXC + 2];
int pref[MAXC + 2][MAXC + 2];

long long fact[100005], inv[100005];

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
}

// 1-indexed sum in [x1, x2] x [y1, y2]
int query_rect(int x1, int y1, int x2, int y2) {
    x1 = max(1, x1); y1 = max(1, y1);
    x2 = min(MAXC + 1, x2); y2 = min(MAXC + 1, y2);
    if (x1 > x2 || y1 > y2) return 0;
    return pref[x2][y2] - pref[x1 - 1][y2] - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    if (!(cin >> N >> K)) return 0;

    fact[0] = inv[0] = 1;
    for (int i = 1; i <= N; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 1; i--) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;
        grid[x + 1][y + 1]++;
    }

    for (int i = 1; i <= MAXC + 1; i++) {
        for (int j = 1; j <= MAXC + 1; j++) {
            pref[i][j] = grid[i][j] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
        }
    }

    auto check = [&](int m) -> bool {
        for (int x = 1; x <= MAXC + 1; x++) {
            int x2 = min(MAXC + 1, x + m);
            for (int y = 1; y <= MAXC + 1; y++) {
                int y2 = min(MAXC + 1, y + m);
                if (query_rect(x, y, x2, y2) >= K) return true;
            }
        }
        return false;
    };

    int low = 0, high = MAXC, m = MAXC;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (check(mid)) {
            m = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    // Now count combinations
    long long total_ways = 0;

    for (int x = 1; x <= MAXC + 1; x++) {
        int x2 = min(MAXC + 1, x + m);
        for (int y = 1; y <= MAXC + 1; y++) {
            int y2 = min(MAXC + 1, y + m);

            int all_pts = query_rect(x, y, x2, y2);
            if (all_pts < K) continue;

            int left_edge = query_rect(x, y, x, y2);
            int top_edge = query_rect(x, y, x2, y);
            int corner_top_left = grid[x][y];
            int union_pts = left_edge + top_edge - corner_top_left;

            long long ways = (nCr(all_pts, K)
                            - nCr(all_pts - left_edge, K)
                            - nCr(all_pts - top_edge, K)
                            + nCr(all_pts - union_pts, K)) % MOD;
            ways = (ways + 2 * MOD) % MOD;
            total_ways = (total_ways + ways) % MOD;
        }
    }

    cout << m << "\n";
    cout << total_ways << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
