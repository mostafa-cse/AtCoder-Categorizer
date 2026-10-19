# Problem Analysis: AtCoder-tokiomarine2020_e — E - O(rand)

**Problem ID**: `AtCoder-tokiomarine2020_e`  
**Contest**: `tokiomarine2020`  
**Rating / Difficulty**: 2757  
**URL**: https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_e  
**VJudge Tag**: `[problem:AtCoder-tokiomarine2020_e]`  
**Category File**: [`../categories/combinatorics/o_rand_inclusion_exclusion_bitwise.md`](../categories/combinatorics/o_rand_inclusion_exclusion_bitwise.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Given N pairwise distinct integers A_1, ..., A_N, find the number of subsets of size 1 <= r <= K such that their bitwise AND is S and bitwise OR is T.

## 2. Core Observation & Invariant
First, filter elements to those satisfying (A_i & S) == S and (A_i | T) == T. The remaining varying bits are B = {b : S_b == 0 and T_b == 1}, with |B| <= 18. For each bit b in B, a violation occurs if all chosen elements have bit b = 0 or all chosen elements have bit b = 1. By the Principle of Inclusion-Exclusion, for any subset of bits U in B, all chosen elements violating all bits in U must have the exact same bit pattern on U (i.e. belong to the same equivalence class of x & U). The number of valid subsets is sum_{U in 2^B} (-1)^{|U|} sum_{groups g} sum_{r=1}^{min(K, |g|)} binom(|g|, r). For M <= N <= 50 and 2^18 masks, this runs in O(2^L * M log M) time.

## 3. Step-by-Step Algorithm
1. 1. If (S & ~T) != 0, return 0.
2. 2. Filter A to only valid elements satisfying (x & S) == S and (x | T) == T.
3. 3. Identify the L <= 18 bits where T has 1 and S has 0, compressing elements to L bits.
4. 4. Precompute combinations binom(n, r) and ways_for_g[g] = sum_{r=1}^{min(K, g)} binom(g, r).
5. 5. Iterate over all masks U in 0..2^L-1, project the M elements onto U, sort, and add (-1)^{popcount(U)} * sum ways_for_g[g].
6. 6. Output the accumulated sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^L * M log M) with L <= 18, M <= 50`
- **Space Complexity**: `O(M + 2^L)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long C[55][55];
long long ways_for_g[55];

void init_comb(int K) {
    for (int i = 0; i <= 50; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }
    for (int g = 1; g <= 50; ++g) {
        ways_for_g[g] = 0;
        for (int r = 1; r <= min(K, g); ++r) {
            ways_for_g[g] += C[g][r];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    long long S, T;
    if (!(cin >> n >> k >> S >> T)) return 0;

    init_comb(k);

    vector<long long> A(n);
    for (int i = 0; i < n; ++i) cin >> A[i];

    if ((S & ~T) != 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> valid;
    for (int i = 0; i < n; ++i) {
        if ((A[i] & S) == S && (A[i] | T) == T) {
            valid.push_back(A[i]);
        }
    }

    long long diff = T ^ S;
    vector<int> bits;
    for (int b = 0; b < 18; ++b) {
        if ((diff >> b) & 1) {
            bits.push_back(b);
        }
    }

    int L = (int)bits.size();
    int M = (int)valid.size();
    if (M == 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<int> c(M);
    for (int i = 0; i < M; ++i) {
        int val = 0;
        for (int j = 0; j < L; ++j) {
            if ((valid[i] >> bits[j]) & 1) {
                val |= (1 << j);
            }
        }
        c[i] = val;
    }

    long long ans = 0;
    int vals[55];

    for (int u = 0; u < (1 << L); ++u) {
        for (int i = 0; i < M; ++i) {
            vals[i] = c[i] & u;
        }
        sort(vals, vals + M);

        long long ways = 0;
        int cur_cnt = 1;
        for (int i = 1; i < M; ++i) {
            if (vals[i] == vals[i - 1]) {
                cur_cnt++;
            } else {
                ways += ways_for_g[cur_cnt];
                cur_cnt = 1;
            }
        }
        ways += ways_for_g[cur_cnt];

        int pop = 0;
        int temp = u;
        while (temp) {
            pop += (temp & 1);
            temp >>= 1;
        }

        if (pop % 2 == 1) {
            ans -= ways;
        } else {
            ans += ways;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
