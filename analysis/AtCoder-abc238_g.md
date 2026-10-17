# Problem Analysis: AtCoder-abc238_g — G. Cubic?

**Problem ID**: `AtCoder-abc238_g`  
**Contest**: `abc238`  
**Rating / Difficulty**: 2254  
**URL**: https://atcoder.jp/contests/abc238/tasks/abc238_g  
**VJudge Tag**: `[problem:AtCoder-abc238_g]`  
**Category File**: [`../categories/miscellaneous/parallel_trit_zobrist_hashing_range_cubes.md`](../categories/miscellaneous/parallel_trit_zobrist_hashing_range_cubes.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Randomized`  
- **Topic (Skill)**: `Randomized Algorithms`  

---

## 1. Problem Statement & Key Idea
Given array $A$ of $N$ integers ($A_i \le 10^6$), answer $Q$ queries: is $\prod_{i=L}^R A_i$ a cubic number (perfect cube)?

## 2. Core Observation & Invariant
A range product is a cube if and only if the sum of exponents of each prime factor is a multiple of 3. We can map each prime $p$ to a random trit vector in $(\mathbb{Z}_3)^{128}$ represented by two 64-bit masks $(h, l)$. Because addition in $\mathbb{Z}_3$ satisfies $3v = 0$, the prefix sum vector at $R$ equals the prefix sum vector at $L-1$ if and only if all prime exponents in $[L, R]$ are $0 \pmod 3$. Parallel bitwise trit addition enables $O(1)$ query time and $O(N \log \max A)$ precomputation.

## 3. Step-by-Step Algorithm
1. Sieve smallest prime factors up to $10^6$ and assign random 128-trit vectors to all primes.
2. Compute prefix trit vectors $pref[i]$ by factoring each $A_i$ and performing parallel bitwise trit addition in $\mathbb{Z}_3$.
3. For each query $(L, R)$, output "Yes" if $pref[R] == pref[L-1]$, and "No" otherwise.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log(\max A) + Q)`
- **Space Complexity**: `O(N + \max A)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <random>

using namespace std;

struct TritVec {
    uint64_t h1, l1;
    uint64_t h2, l2;

    bool operator==(const TritVec& other) const {
        return h1 == other.h1 && l1 == other.l1 && h2 == other.h2 && l2 == other.l2;
    }
};

inline TritVec add_trit_vec(const TritVec& a, const TritVec& b) {
    uint64_t za1 = ~(a.h1 | a.l1);
    uint64_t zb1 = ~(b.h1 | b.l1);
    uint64_t nl1 = (a.l1 & zb1) | (b.l1 & za1) | (a.h1 & b.h1);
    uint64_t nh1 = (a.h1 & zb1) | (b.h1 & za1) | (a.l1 & b.l1);

    uint64_t za2 = ~(a.h2 | a.l2);
    uint64_t zb2 = ~(b.h2 | b.l2);
    uint64_t nl2 = (a.l2 & zb2) | (b.l2 & za2) | (a.h2 & b.h2);
    uint64_t nh2 = (a.h2 & zb2) | (b.h2 & za2) | (a.l2 & b.l2);

    return {nh1, nl1, nh2, nl2};
}

const int MAXA = 1000000;
int spf[MAXA + 1];
TritVec prime_hash[MAXA + 1];

void sieve() {
    for (int i = 2; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }

    mt19937_64 rng(1337);
    for (int i = 2; i <= MAXA; ++i) {
        if (spf[i] == i) {
            // Assign random trit vector: each trit is uniformly in {0, 1, 2}
            // For word 1:
            uint64_t r1_a = rng();
            uint64_t r1_b = rng();
            // To ensure never h=1 and l=1:
            // if both 1, turn into (0, 0)
            uint64_t both1 = r1_a & r1_b;
            uint64_t l1 = r1_a ^ both1;
            uint64_t h1 = r1_b ^ both1;

            uint64_t r2_a = rng();
            uint64_t r2_b = rng();
            uint64_t both2 = r2_a & r2_b;
            uint64_t l2 = r2_a ^ both2;
            uint64_t h2 = r2_b ^ both2;

            prime_hash[i] = {h1, l1, h2, l2};
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    sieve();

    int N, Q;
    if (!(cin >> N >> Q)) return 0;

    vector<TritVec> pref(N + 1, {0, 0, 0, 0});

    for (int i = 1; i <= N; ++i) {
        int a;
        cin >> a;
        TritVec cur = pref[i - 1];
        while (a > 1) {
            int p = spf[a];
            cur = add_trit_vec(cur, prime_hash[p]);
            a /= p;
        }
        pref[i] = cur;
    }

    for (int q = 0; q < Q; ++q) {
        int L, R;
        cin >> L >> R;
        if (pref[R] == pref[L - 1]) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
