# Problem Analysis: AtCoder-arc228_c — C - Partially Sort

**Problem ID**: `AtCoder-arc228_c`  
**Contest**: `arc228`  
**Rating / Difficulty**: 2971  
**URL**: https://atcoder.jp/contests/arc228/tasks/arc228_c  
**VJudge Tag**: `[problem:AtCoder-arc228_c]`  
**Category File**: [`../categories/combinatorics/subsequence_partial_sort_inversion_contribution.md`](../categories/combinatorics/subsequence_partial_sort_inversion_contribution.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
Given a permutation P of length N, for each of the 2^N subsequences, sort the elements in the subsequence in place while leaving other elements in their original positions. Find the sum of inversion numbers of all 2^N resulting permutations, modulo 998244353.

## 2. Core Observation & Invariant
Decompose inversions by contribution technique: Type 1 inversions between two chosen or two unchosen elements contribute 2^{N-2} I(P). Type 2 inversions between an unchosen element P_i and the sorted chosen elements equal B + D - 2 min(b, d), where B is smaller elements and D is larger elements in P. Summing over all subsets reduces to evaluating sum binom(B, b) binom(D, d) min(b, d) = B sum_{k=0}^{D-1} binom(B+D-1, k) + D sum_{k=0}^{B-2} binom(B+D-1, k), evaluated in O(N sqrt(N)) via Mo's algorithm or linear shift.

## 3. Step-by-Step Algorithm
1. 1. Compute initial permutation inversions I(P) via Fenwick tree.
2. 2. For each P_i, determine counts of smaller and larger elements B_i = P_i - 1 and D_i = N - P_i.
3. 3. Set up queries for prefix binomial sums sum_{k=0}^M binom(N-1, k).
4. 4. Evaluate prefix binomial sums using Mo's algorithm or two-pointer shifts.
5. 5. Accumulate contributions for Type 1 and Type 2 inversions.
6. 6. Output the total inversions modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N sqrt(N))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const int MOD = 998244353;
const long long INV2 = (MOD + 1) / 2;

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

const int MAXF = 300005;
long long fact[MAXF], inv[MAXF], pow2[MAXF];

void precompute() {
    fact[0] = 1;
    inv[0] = 1;
    pow2[0] = 1;
    for (int i = 1; i < MAXF; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
    inv[MAXF - 1] = modInverse(fact[MAXF - 1]);
    for (int i = MAXF - 2; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
}

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

struct MoQuery {
    int m, k, id;
    int block;
    bool operator<(const MoQuery& other) const {
        if (block != other.block) return block < other.block;
        return (block & 1) ? k < other.k : k > other.k;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
    }

    // Compute B[i] and D[i]
    vector<int> B(n, 0), D(n, 0);
    Fenwick ft1(n);
    long long total_I = 0;
    for (int i = 0; i < n; ++i) {
        B[i] = i - ft1.query(p[i]);
        total_I += B[i];
        ft1.add(p[i], 1);
    }

    Fenwick ft2(n);
    for (int i = n - 1; i >= 0; --i) {
        D[i] = ft2.query(p[i]);
        ft2.add(p[i], 1);
    }

    // Type 1 inversions
    long long ans1 = 0;
    if (n >= 2) {
        ans1 = (pow2[n - 2] * (total_I % MOD)) % MOD;
    }

    // Queries for F(M, K) = sum_{k=0}^K binom(M, k)
    vector<MoQuery> queries;
    vector<int> q1_id(n, -1), q2_id(n, -1);
    int B_SIZE = max(1, (int)(n / sqrt(max(1, 2 * n))));

    for (int i = 0; i < n; ++i) {
        if (B[i] > 0 && D[i] > 0) {
            int M = B[i] + D[i] - 1;
            // query 1: (M, D[i] - 1)
            int k1 = D[i] - 1;
            if (k1 >= 0) {
                q1_id[i] = (int)queries.size();
                queries.push_back({M, min(k1, M), q1_id[i], M / B_SIZE});
            }
            // query 2: (M, B[i] - 2)
            int k2 = B[i] - 2;
            if (k2 >= 0) {
                q2_id[i] = (int)queries.size();
                queries.push_back({M, min(k2, M), q2_id[i], M / B_SIZE});
            }
        }
    }

    sort(queries.begin(), queries.end());

    vector<long long> query_ans(queries.size(), 0);

    // Mo's algorithm state
    int cur_m = 0, cur_k = 0;
    long long cur_val = 1; // F(0, 0) = binom(0, 0) = 1

    for (const auto& qry : queries) {
        int target_m = qry.m;
        int target_k = qry.k;

        while (cur_m < target_m) {
            cur_val = (2 * cur_val - nCr(cur_m, cur_k) + MOD) % MOD;
            cur_m++;
        }
        while (cur_m > target_m) {
            cur_m--;
            cur_val = (cur_val + nCr(cur_m, cur_k)) % MOD * INV2 % MOD;
        }
        while (cur_k < target_k) {
            cur_k++;
            cur_val = (cur_val + nCr(cur_m, cur_k)) % MOD;
        }
        while (cur_k > target_k) {
            cur_val = (cur_val - nCr(cur_m, cur_k) + MOD) % MOD;
            cur_k--;
        }

        query_ans[qry.id] = cur_val;
    }

    // Compute Type 2 inversions
    long long ans2 = 0;
    for (int i = 0; i < n; ++i) {
        int Bi = B[i], Di = D[i];
        long long pow_rem = pow2[(n - 1) - (Bi + Di)];

        long long sum_b_d = 0;
        long long sum_min = 0;

        if (Bi + Di > 0) {
            sum_b_d = (Bi + Di) * pow2[Bi + Di - 1] % MOD;

            if (Bi > 0 && Di > 0) {
                long long term1 = 0;
                if (q1_id[i] != -1) {
                    term1 = Bi * query_ans[q1_id[i]] % MOD;
                }
                long long term2 = 0;
                if (q2_id[i] != -1) {
                    term2 = Di * query_ans[q2_id[i]] % MOD;
                }
                sum_min = (term1 + term2) % MOD;
            }
        }

        long long type2_i = (sum_b_d - 2 * sum_min % MOD + MOD) % MOD;
        type2_i = (type2_i * pow_rem) % MOD;
        ans2 = (ans2 + type2_i) % MOD;
    }

    long long total_ans = (ans1 + ans2) % MOD;
    cout << total_ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
