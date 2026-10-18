# Problem Analysis: AtCoder-arc114_e — E. Paper Cutting 2

**Problem ID**: `AtCoder-arc114_e`  
**Contest**: `arc114`  
**Rating / Difficulty**: 2514  
**URL**: https://atcoder.jp/contests/arc114/tasks/arc114_e  
**VJudge Tag**: `[problem:AtCoder-arc114_e]`  
**Category File**: [`../categories/math/paper_cutting_2_linearity_of_expectation.md`](../categories/math/paper_cutting_2_linearity_of_expectation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
A rectangular grid $H \times W$ contains two marked black squares at $(r_1, c_1)$ and $(r_2, c_2)$. Cut lines are chosen uniformly at random without replacement from the remaining lines. After each cut, the piece not containing both black squares is discarded. The process halts when a cut separates the two black squares. By linearity of expectation, the expected number of cuts is $1 + \sum_{L} \mathbb{P}(L \text{ is cut before termination})$.

## 2. Core Observation & Invariant
The process terminates immediately when any of the $S = (r_2 - r_1) + (c_2 - c_1)$ separating cut lines between the two black squares is chosen. A cut line $L$ outside the bounding box at distance $d$ from the box is executed if and only if it is chosen before all $d - 1$ intervening lines and all $S$ terminating lines. Thus, among these $(d - 1) + 1 + S = d + S$ lines, $L$ must be chosen first, which occurs with probability $\frac{1}{d + S}$.

## 3. Step-by-Step Algorithm
1. 1. Calculate bounding box: $r_{min} = \min(r_1, r_2), r_{max} = \max(r_1, r_2), c_{min} = \min(c_1, c_2), c_{max} = \max(c_1, c_2)$.
2. 2. Calculate number of separating lines $S = (r_{max} - r_{min}) + (c_{max} - c_{min})$.
3. 3. Initialize expected cuts $E = 1$.
4. 4. For lines above: $d = 1 \dots r_{min} - 1$, add $\frac{1}{d + S}$ to $E$.
5. 5. For lines below: $d = 1 \dots H - r_{max}$, add $\frac{1}{d + S}$ to $E$.
6. 6. For lines left: $d = 1 \dots c_{min} - 1$, add $\frac{1}{d + S}$ to $E$.
7. 7. For lines right: $d = 1 \dots W - c_{max}$, add $\frac{1}{d + S}$ to $E$.
8. 8. Compute modular inverses $\pmod{998244353}$ and output total expectation.

## 4. Complexity Analysis
- **Time Complexity**: `O(H + W)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long H, W;
    long long h1, w1, h2, w2;
    if (!(cin >> H >> W >> h1 >> w1 >> h2 >> w2)) return 0;

    long long r1 = min(h1, h2);
    long long r2 = max(h1, h2);
    long long c1 = min(w1, w2);
    long long c2 = max(w1, w2);

    long long S = (r2 - r1) + (c2 - c1);

    long long max_d = max({r1, H - r2 + 1, c1, W - c2 + 1});
    long long limit = max_d + S + 5;
    vector<long long> inv(limit + 1, 1);
    for (int i = 2; i <= limit; ++i) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    }

    long long ans = 1; // The final separating cut

    // Top: i from 1 to r1 - 1
    for (long long i = 1; i < r1; ++i) {
        long long d = r1 - i;
        ans = (ans + inv[d + S]) % MOD;
    }

    // Bottom: i from r2 to H - 1
    for (long long i = r2; i < H; ++i) {
        long long d = i - r2 + 1;
        ans = (ans + inv[d + S]) % MOD;
    }

    // Left: j from 1 to c1 - 1
    for (long long j = 1; j < c1; ++j) {
        long long d = c1 - j;
        ans = (ans + inv[d + S]) % MOD;
    }

    // Right: j from c2 to W - 1
    for (long long j = c2; j < W; ++j) {
        long long d = j - c2 + 1;
        ans = (ans + inv[d + S]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
