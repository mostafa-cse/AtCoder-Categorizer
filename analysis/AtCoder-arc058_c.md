# Problem Analysis: AtCoder-arc058_c — E. Iroha and Haiku

**Problem ID**: `AtCoder-arc058_c`  
**Contest**: `arc058`  
**Rating / Difficulty**: 2473  
**URL**: https://atcoder.jp/contests/arc058/tasks/arc058_c  
**VJudge Tag**: `[problem:AtCoder-arc058_c]`  
**Category File**: [`../categories/dynamic_programming/iroha_and_haiku_suffix_bitmask_dp.md`](../categories/dynamic_programming/iroha_and_haiku_suffix_bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Count length-$N$ sequences with elements in $[1, 10]$ containing an $X, Y, Z$-Haiku subsegment. Complement counting: total sequences $10^N$ minus sequences that never form an $X, Y, Z$-Haiku. Maintain a bitmask of reachable suffix sums up to $S = X + Y + Z \le 17$. Appending digit $d$ shifts the bitmask by $d$ and sets bit $d - 1$. Forbid transitions to any mask containing bits $Z - 1, Y + Z - 1, S - 1$ simultaneously.

## 2. Core Observation & Invariant
Because $X + Y + Z \le 17$, the entire state of recent suffix sums fits into a 17-bit integer ($2^{17} = 131,072$). Suffix bitmask transitions are pure bitwise shifts, allowing $O(10 \cdot 2^{X+Y+Z})$ operations per sequence position.

## 3. Step-by-Step Algorithm
1. 1. Define target bitmask with bits $Z - 1, Y + Z - 1, X + Y + Z - 1$ set.
2. 2. Initialize DP table `dp[0] = 1` for step 0.
3. 3. For step 1 to $N$:
4.    a. Clear `nxt` array.
5.    b. For each reachable mask $m$ and each digit $d \in [1, 10]$:
6.       $nm = ((m \ll d) \mid (1 \ll (d - 1))) \& ((1 \ll S) - 1)$.
7.       If $(nm \& target) \ne target$, add $dp[m]$ to $nxt[nm]$.
8.    c. Set `dp = nxt`.
9. 4. Sum all non-haiku sequences and subtract from $10^N \pmod{10^9+7}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \cdot 10 \cdot 2^{X+Y+Z})`
- **Space Complexity**: `O(2^{X+Y+Z})`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

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

int dp[1 << 17];
int nxt[1 << 17];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, X, Y, Z;
    if (!(cin >> N >> X >> Y >> Z)) return 0;

    int S = X + Y + Z;
    int target = (1 << (Z - 1)) | (1 << (Y + Z - 1)) | (1 << (S - 1));
    int mask_limit = 1 << S;

    dp[0] = 1;

    for (int step = 0; step < N; ++step) {
        for (int m = 0; m < mask_limit; ++m) nxt[m] = 0;

        for (int m = 0; m < mask_limit; ++m) {
            if (dp[m] == 0) continue;
            long long ways = dp[m];
            for (int d = 1; d <= 10; ++d) {
                int nm = ((m << d) | (1 << (d - 1))) & (mask_limit - 1);
                if ((nm & target) == target) continue;
                nxt[nm] = (nxt[nm] + ways) % MOD;
            }
        }

        for (int m = 0; m < mask_limit; ++m) dp[m] = nxt[m];
    }

    long long total_valid = 0;
    for (int m = 0; m < mask_limit; ++m) {
        total_valid = (total_valid + dp[m]) % MOD;
    }

    long long total_all = power(10, N);
    long long ans = (total_all - total_valid + MOD) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
