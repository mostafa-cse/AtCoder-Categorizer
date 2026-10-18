# Problem Analysis: AtCoder-abc128_f — F. Frog Jump

**Problem ID**: `AtCoder-abc128_f`  
**Contest**: `abc128`  
**Rating / Difficulty**: 2464  
**URL**: https://atcoder.jp/contests/abc128/tasks/abc128_f  
**VJudge Tag**: `[problem:AtCoder-abc128_f]`  
**Category File**: [`../categories/basics/frog_jump_harmonic_number_pairs.md`](../categories/basics/frog_jump_harmonic_number_pairs.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Very Basic Math`  
- **Topic (Skill)**: `Harmonic Number`  

---

## 1. Problem Statement & Key Idea
Maximize score by jumping $+A, -B, +A, -B, \dots$ to reach $N - 1$. Let $C = A - B > 0$. The sequence of visited lotuses consists of pairs $(kC, N - 1 - kC)$ for $k = 1, 2, \dots$. A lotus is visited twice if and only if $(N - 1) \bmod C == 0$ and $2kC \ge N - 1$. Iterating over all step sizes $C$ and valid $k$ evaluates all feasible paths in $O(N \log N)$ time using the harmonic series.

## 2. Core Observation & Invariant
Because the game ends on a $+A$ jump landing at $N - 1$, $A = N - 1 - kC$. The intermediate forward coordinates are $kC$ and reverse coordinates are $N - 1 - kC$. As long as no coordinates collide or overlap with 0, all lotuses are distinct. Collisions only occur when $C$ divides $N - 1$ and $2kC \ge N - 1$.

## 3. Step-by-Step Algorithm
1. 1. Initialize max score `ans = 0`.
2. 2. Iterate over step difference $C$ from $1$ to $N - 2$.
3. 3. Maintain a running sum `cur = 0` for fixed $C$.
4. 4. Iterate $k = 1, 2, \dots$ while $(k + 1)C < N - 1$.
5. 5. If $(N - 1) \bmod C == 0$ and $2kC \ge N - 1$, break immediately (collision).
6. 6. Add $s[kC] + s[N - 1 - kC]$ to `cur` and update `ans = max(ans, cur)`.
7. 7. Output `ans`.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> s(n);
    for (int i = 0; i < n; ++i) cin >> s[i];

    long long ans = 0;
    for (long long C = 1; C < n; ++C) {
        long long cur = 0;
        for (long long k = 1; k < n; ++k) {
            if ((k + 1) * C >= n - 1) break;
            if ((n - 1) % C == 0 && 2 * k * C >= n - 1) break;
            cur += s[k * C] + s[n - 1 - k * C];
            if (cur > ans) ans = cur;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
