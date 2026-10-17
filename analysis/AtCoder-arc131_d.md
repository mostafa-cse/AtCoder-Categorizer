# Problem Analysis: AtCoder-arc131_d — D. AtArcher

**Problem ID**: `AtCoder-arc131_d`  
**Contest**: `arc131`  
**Rating / Difficulty**: 2271  
**URL**: https://atcoder.jp/contests/arc131/tasks/arc131_d  
**VJudge Tag**: `[problem:AtCoder-arc131_d]`  
**Category File**: [`../categories/basics/difference_array_concentric_score_bands.md`](../categories/basics/difference_array_concentric_score_bands.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `More Techniques`  
- **Topic (Skill)**: `Difference Array`  

---

## 1. Problem Statement & Key Idea
Shoot $N$ arrows into concentric scoring bands $[-r_i, r_i]$ with scores $s_i$ centered at 0. Any two arrows must be separated by distance $\ge D$ ($D \le 10^6$). Find the maximum total score obtainable.

## 2. Core Observation & Invariant
Arrows should be placed at exact intervals of $D$ to remain as close to 0 as possible: $x_j(k) = A + k + j D$ for $j = 0, \dots, N-1$, where $A = -\lfloor \frac{ND}{2} \rfloor$ and shift $k \in [0, D-1]$.
As the shift $k$ increases from $k$ to $k+1$, all arrows shift right by $+1$. An arrow's score only changes when it crosses a concentric ring boundary $\pm r_i$. For each boundary point $B$, at most one arrow $j = \lfloor \frac{B - A - rem}{D} \rfloor$ crosses $B$ at $k = (B - A) \bmod D$. Using a difference array of size $D$, we add score changes for all $2M$ boundaries in $O(M)$ time, and find the maximum total score in $O(M + D)$ time via prefix sums.

## 3. Step-by-Step Algorithm
1. Set $A = -\lfloor \frac{ND}{2} \rfloor$.
2. Initialize difference array `diff` of size $D+1$.
3. For negative boundaries $B = -r_i$, compute $\Delta = s_{i-1} - s_i$ (score increases moving right into ring); find $rem = (B - A) \bmod D$ and check if $j = (B - A - rem) / D \in [0, N-1]$; add $\Delta$ to `diff[rem]`.
4. For positive boundaries $B = r_i + 1$, compute $\Delta = s_i - s_{i-1}$ (score decreases moving right out of ring); find $rem$ and $j$; add $\Delta$ to `diff[rem]`.
5. Compute base score at $k = 0$ for arrows within $[-r_M, r_M]$.
6. Iterate $k = 1 \dots D-1$, accumulating `cur_score += diff[k]` and tracking the maximum score.

## 4. Complexity Analysis
- **Time Complexity**: `O(M + D)`
- **Space Complexity**: `O(D)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, m, d;
    if (!(cin >> n >> m >> d)) return 0;

    vector<long long> r(m + 1);
    for (int i = 0; i <= m; ++i) cin >> r[i];

    vector<long long> s(m);
    for (int i = 0; i < m; ++i) cin >> s[i];

    long long A = -(n * d) / 2;

    auto score_of = [&](long long x) -> long long {
        long long ax = llabs(x);
        if (ax <= r[1]) return s[0];
        if (ax > r[m]) return 0;
        int idx = lower_bound(r.begin(), r.end(), ax) - r.begin();
        return s[idx - 1];
    };

    vector<long long> diff(d + 1, 0);

    auto add_boundary = [&](long long B, long long delta) {
        long long rem = (B - A) % d;
        if (rem < 0) rem += d;
        long long j = (B - A - rem) / d;
        if (j >= 0 && j < n) {
            diff[rem] += delta;
        }
    };

    // Negative side: moving right from -r[i]-1 to -r[i] increases score
    for (int i = 1; i <= m; ++i) {
        long long prev_s = (i < m ? s[i] : 0);
        long long cur_s = s[i - 1];
        long long delta = cur_s - prev_s;
        add_boundary(-r[i], delta);
    }

    // Positive side: moving right from r[i] to r[i]+1 decreases score
    for (int i = 1; i <= m; ++i) {
        long long prev_s = s[i - 1];
        long long cur_s = (i < m ? s[i] : 0);
        long long delta = cur_s - prev_s;
        add_boundary(r[i] + 1, delta);
    }

    // Initial score at k = 0
    long long cur_score = 0;
    // Only arrows within [-r_M, r_M] have non-zero score
    // Arrow j is at A + j * D
    // -r_M <= A + j * D <= r_M
    long long min_j = max(0LL, (long long)ceil((-r[m] - A) / (double)d));
    long long max_j = min(n - 1, (long long)floor((r[m] - A) / (double)d));

    for (long long j = max(0LL, min_j - 2); j <= min(n - 1, max_j + 2); ++j) {
        long long pos = A + j * d;
        cur_score += score_of(pos);
    }

    long long best = cur_score;
    for (int k = 1; k < d; ++k) {
        cur_score += diff[k];
        if (cur_score > best) best = cur_score;
    }

    cout << best << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
