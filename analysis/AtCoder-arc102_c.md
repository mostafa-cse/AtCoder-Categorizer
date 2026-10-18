# Problem Analysis: AtCoder-arc102_c — E. Stop. Otherwise...

**Problem ID**: `AtCoder-arc102_c`  
**Contest**: `arc102`  
**Rating / Difficulty**: 2484  
**URL**: https://atcoder.jp/contests/arc102/tasks/arc102_c  
**VJudge Tag**: `[problem:AtCoder-arc102_c]`  
**Category File**: [`../categories/combinatorics/stop_otherwise_pie_generating_functions.md`](../categories/combinatorics/stop_otherwise_pie_generating_functions.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
For each $i \in [2, 2K]$, count multisets of $N$ dice rolls with faces $1 \dots K$ where no two dice sum to $i$. Group the $K$ faces into pairs $\{u, v\}$ summing to $i$, at most one midpoint face $i/2$ (if $i$ is even and $i \le 2K$), and leftover independent faces. In any valid roll, at most one face of each pair can appear. Generating functions or PIE over which pairs are violated counts valid multisets with fixed coefficient extraction in $O(N)$ per query $i$.

## 2. Core Observation & Invariant
Each pair $\{u, v\}$ with $u + v = i$ cannot both have non-zero counts. If $P$ such pairs exist, choosing $c$ pairs to both appear with positive counts contributes $(-1)^c \binom{P}{c}$, and the remaining problem is standard stars-and-bars allocation of $N - 2c$ balls into $K$ distinct bins.

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials and combinations up to $N + K$.
2. 2. For each query target sum $i$ from 2 to $2K$:
3. 3. Count the number of pairs $P$ of distinct faces $u < v$ such that $u + v = i$ and $1 \le u, v \le K$.
4. 4. Check if there is an isolated midpoint face $m = i / 2$.
5. 5. Using PIE over the $P$ forbidden pairs, iterate $c$ from 0 to $P$: each term is $(-1)^c \binom{P}{c} \binom{N - 2c + K - 1}{K - 1}$.
6. 6. Output the sum for each $i$.

## 4. Complexity Analysis
- **Time Complexity**: `O(K \cdot \min(N, K))`
- **Space Complexity**: `O(N + K)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

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

    int K, N;
    if (!(cin >> K >> N)) return 0;

    int max_val = N + K + 10;
    vector<long long> fact(max_val), inv(max_val);
    fact[0] = 1;
    for (int i = 1; i < max_val; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[max_val - 1] = modInverse(fact[max_val - 1]);
    for (int i = max_val - 2; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    for (int i = 2; i <= 2 * K; ++i) {
        int low = max(1, i - K);
        int high = (i - 1) / 2;
        int P = max(0, high - low + 1);
        int has_mid = (i % 2 == 0 && i / 2 <= K) ? 1 : 0;

        int num_pow = P + has_mid;
        int den_pow = K - P - has_mid;

        long long ans = 0;
        int limit = min(N, num_pow);
        for (int j = 0; j <= limit; ++j) {
            int rem = N - j;
            long long coeff = 0;
            if (den_pow == 0) {
                coeff = (rem == 0 ? 1 : 0);
            } else {
                coeff = nCr(rem + den_pow - 1, den_pow - 1);
            }
            long long term = nCr(num_pow, j) * coeff % MOD;
            ans = (ans + term) % MOD;
        }

        cout << ans << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
