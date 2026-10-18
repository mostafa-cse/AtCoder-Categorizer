# Problem Analysis: AtCoder-abc438_g — G - Sum of Min

**Problem ID**: `AtCoder-abc438_g`  
**Contest**: `abc438`  
**Rating / Difficulty**: 2455  
**URL**: https://atcoder.jp/contests/abc438/tasks/abc438_g  
**VJudge Tag**: `[problem:AtCoder-abc438_g]`  
**Category File**: [`../categories/number_theory/sum_of_min_extended_euclid_fenwick.md`](../categories/number_theory/sum_of_min_extended_euclid_fenwick.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Euclidean Algorithm`  
- **Topic (Skill)**: `Extended Euclid`  

---

## 1. Problem Statement & Key Idea
Compute $\sum_{k=0}^{NM-1} \min(A_{k \bmod N}, B_{k \bmod M})$ efficiently.

## 2. Core Observation & Invariant
By the Chinese Remainder Theorem and Bezout's identity, the pair $(k \bmod N, k \bmod M)$ visits each pair $(i, j)$ where $i \equiv j \pmod{g}$ exactly $g$ times, where $g = \gcd(N, M)$. This decomposes the problem into $g$ independent subproblems of sizes $N/g$ and $M/g$. Within each subproblem, elements of $B$ can be permuted along arithmetic progressions modulo $M/g$, converting the sum of minima into circular range queries evaluated using a Fenwick tree.

## 3. Step-by-Step Algorithm
1. 1. Compute $g = \gcd(N, M)$.
2. 2. Partition indices of $A$ and $B$ into $g$ residue classes modulo $g$.
3. 3. For each residue class $r \in [0, g-1]$:
4.    - Map elements of $B$ to their cycle positions using modular inverse via Extended Euclid.
5.    - Sort queries on $A_i$ and insert elements of $B_j$ into a Fenwick tree.
6.    - Query counts and prefix sums of $B_j \le A_i$ and $B_j > A_i$.
7. 4. Aggregate results across all $g$ residue classes and scale by $g$.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) \log(N + M))`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long d = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

long long modInverse(long long a, long long m) {
    long long x, y;
    extgcd(a, m, x, y);
    return (x % m + m) % m;
}

struct Fenwick {
    int n;
    vector<long long> tree;
    Fenwick(int n) : n(n), tree(n + 2, 0) {}
    void add(int idx, long long val) {
        for (++idx; idx <= n; idx += idx & -idx) tree[idx] += val;
    }
    long long query(int idx) {
        long long sum = 0;
        for (++idx; idx > 0; idx -= idx & -idx) sum += tree[idx];
        return sum;
    }
};

struct Query {
    int x, r_bound, sign, q_idx;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, M, K;
    if (!(cin >> N >> M >> K)) return 0;

    vector<long long> A(N), B(M);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < M; ++i) cin >> B[i];

    long long g = std::gcd(N, M);
    long long total_ans = 0;

    for (int r = 0; r < g; ++r) {
        if (r >= K) continue;
        long long num_terms = (K - 1 - r) / g + 1;

        int N_prime = N / g;
        int M_prime = M / g;

        vector<long long> A_sub(N_prime), B_sub(M_prime);
        for (int i = 0; i < N_prime; ++i) A_sub[i] = A[r + (long long)i * g];
        for (int j = 0; j < M_prime; ++j) B_sub[j] = B[r + (long long)j * g];

        if (M_prime == 1) {
            for (int k = 0; k < N_prime; ++k) {
                if (k < num_terms) {
                    long long C = (num_terms - 1 - k) / N_prime + 1;
                    long long term = (min(A_sub[k], B_sub[0]) % MOD) * (C % MOD) % MOD;
                    total_ans = (total_ans + term) % MOD;
                }
            }
            continue;
        }

        long long N_inv = modInverse(N_prime, M_prime);
        vector<long long> B_perm(M_prime);
        for (int j = 0; j < M_prime; ++j) {
            B_perm[j] = B_sub[((long long)j * N_prime) % M_prime];
        }

        vector<pair<long long, long long>> full_period_queries;
        struct RangeQuery {
            long long x;
            int L, R;
        };
        vector<RangeQuery> range_queries;

        for (int k = 0; k < N_prime; ++k) {
            if (k >= num_terms) continue;
            long long C = (num_terms - 1 - k) / N_prime + 1;
            long long x = A_sub[k];
            long long q = C / M_prime;
            int rem = C % M_prime;
            int start = ((long long)k * N_inv) % M_prime;

            if (q > 0) {
                full_period_queries.push_back({x, q});
            }
            if (rem > 0) {
                if (start + rem <= M_prime) {
                    range_queries.push_back({x, start, start + rem - 1});
                } else {
                    range_queries.push_back({x, start, M_prime - 1});
                    range_queries.push_back({x, 0, (start + rem - 1) % M_prime});
                }
            }
        }

        vector<long long> sorted_B = B_perm;
        sort(sorted_B.begin(), sorted_B.end());
        vector<long long> pref_sorted_B(M_prime + 1, 0);
        for (int i = 0; i < M_prime; ++i) pref_sorted_B[i + 1] = pref_sorted_B[i] + sorted_B[i];

        for (const auto& fp : full_period_queries) {
            long long x = fp.first;
            long long q = fp.second;
            int idx = upper_bound(sorted_B.begin(), sorted_B.end(), x) - sorted_B.begin();
            long long sum_val = pref_sorted_B[idx] + (long long)(M_prime - idx) * x;
            total_ans = (total_ans + (sum_val % MOD) * (q % MOD)) % MOD;
        }

        vector<Query> prefix_queries;
        int num_q = range_queries.size();
        for (int q_idx = 0; q_idx < num_q; ++q_idx) {
            long long x = range_queries[q_idx].x;
            int L = range_queries[q_idx].L;
            int R = range_queries[q_idx].R;
            prefix_queries.push_back({(int)x, R, 1, q_idx});
            if (L > 0) {
                prefix_queries.push_back({(int)x, L - 1, -1, q_idx});
            }
        }

        sort(prefix_queries.begin(), prefix_queries.end(), [](const Query& a, const Query& b) {
            return a.x < b.x;
        });

        vector<pair<long long, int>> b_elements(M_prime);
        for (int j = 0; j < M_prime; ++j) b_elements[j] = {B_perm[j], j};
        sort(b_elements.begin(), b_elements.end());

        Fenwick bit_cnt(M_prime + 1), bit_sum(M_prime + 1);
        vector<long long> query_results(num_q, 0);

        int b_ptr = 0;
        for (const auto& q : prefix_queries) {
            while (b_ptr < M_prime && b_elements[b_ptr].first <= q.x) {
                bit_cnt.add(b_elements[b_ptr].second, 1);
                bit_sum.add(b_elements[b_ptr].second, b_elements[b_ptr].first);
                b_ptr++;
            }
            long long cnt_le = bit_cnt.query(q.r_bound);
            long long sum_le = bit_sum.query(q.r_bound);
            long long cnt_gt = (q.r_bound + 1) - cnt_le;
            long long ans_val = sum_le + cnt_gt * q.x;
            query_results[q.q_idx] += (long long)q.sign * ans_val;
        }

        for (long long res : query_results) {
            total_ans = (total_ans + res % MOD + MOD) % MOD;
        }
    }

    cout << total_ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
