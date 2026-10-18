# Problem Analysis: AtCoder-abc476_g — G - Increasing Popcount

**Problem ID**: `AtCoder-abc476_g`  
**Contest**: `abc476`  
**Rating / Difficulty**: 2477  
**URL**: https://atcoder.jp/contests/abc476/tasks/abc476_g  
**VJudge Tag**: `[problem:AtCoder-abc476_g]`  
**Category File**: [`../categories/graph_theory/increasing_popcount_poset_dilworth.md`](../categories/graph_theory/increasing_popcount_poset_dilworth.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Partially Ordered Set (POSET)`  
- **Topic (Skill)**: `POSET ft Dilworth's and Mirsky's Theorem`  

---

## 1. Problem Statement & Key Idea
Find the minimum maximum label of a sequence on $[L, R]$ where identical values must have strictly increasing popcounts.

## 2. Core Observation & Invariant
Construct a poset DAG on vertices $i \in [L, R]$ with directed edges $i \to j$ when $i < j$ and $\operatorname{popcount}(i) < \operatorname{popcount}(j)$. By Dilworth's Theorem, the minimum path cover equals the size of the maximum antichain, which corresponds to choosing elements in $[L, R]$ with non-increasing popcounts. Decomposing $[L, R+1)$ into $O(\log R)$ canonical dyadic intervals $[l, l + 2^c)$ allows DP over popcounts using Sperner's theorem / binomial coefficients in $O(\log^2 R)$ time.

## 3. Step-by-Step Algorithm
1. 1. Precompute Pascal's triangle for binomial coefficients up to $62$.
2. 2. Decompose $[L, R+1)$ into canonical dyadic intervals $[l, l + 2^c)$ where $2^c = \min(2^{\lfloor \log_2(r-l) \rfloor}, l \& -l)$.
3. 3. In each interval with prefix popcount $p$, update DP array $d[p + i] += \binom{c}{i}$ for $i \in [0, c]$.
4. 4. Maintain prefix maximums $d[i] = \max(d[i], d[i+1])$ from 60 down to 0.
5. 5. Print $d[0]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(T \log^2 R)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int bit_length(unsigned long long x) {
    if (x == 0) return 0;
    return 64 - __builtin_clzll(x);
}

int bit_count(unsigned long long x) {
    return __builtin_popcountll(x);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<vector<unsigned long long>> C(62, vector<unsigned long long>(62, 0));
    for (int i = 0; i < 62; ++i) {
        C[i][0] = C[i][i] = 1;
        for (int j = 1; j < i; ++j) {
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }

    int T;
    if (!(cin >> T)) return 0;

    while (T--) {
        unsigned long long l, r;
        cin >> l >> r;
        r++;
        vector<unsigned long long> d(62, 0);

        while (l < r) {
            unsigned long long diff = r - l;
            int bl = bit_length(diff) - 1;
            unsigned long long p1 = 1ULL << bl;
            unsigned long long lsb = l & (~l + 1);
            unsigned long long x = min(p1, lsb);

            int c = bit_length(x) - 1;
            int p = bit_count(l);
            for (int i = 0; i <= c; ++i) {
                d[p + i] += C[c][i];
            }
            for (int i = 60; i >= 0; --i) {
                if (d[i + 1] > d[i]) d[i] = d[i + 1];
            }
            l += x;
        }

        cout << d[0] << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
