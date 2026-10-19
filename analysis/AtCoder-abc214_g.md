# Problem Analysis: AtCoder-abc214_g — G. Three Permutations

**Problem ID**: `AtCoder-abc214_g`  
**Contest**: `abc214`  
**Rating / Difficulty**: 2893  
**URL**: https://atcoder.jp/contests/abc214/tasks/abc214_g  
**VJudge Tag**: `[problem:AtCoder-abc214_g]`  
**Category File**: [`../categories/combinatorics/bipartite_cycle_matching_pie.md`](../categories/combinatorics/bipartite_cycle_matching_pie.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Given two permutations p and q of length N, count the number of permutations r such that r_i != p_i and r_i != q_i for all 1 <= i <= N, modulo 998244353.

## 2. Core Observation & Invariant
By Principle of Inclusion-Exclusion, count permutations r violating at least k constraints (r_i = p_i or r_i = q_i). Form a 2-regular bipartite graph between position indices i and value vertices p_i, q_i. Choosing k violations corresponds to choosing a matching of size k in this graph. The graph decomposes into disjoint simple cycles and paths. For a cycle of length 2L, the number of matchings of size k is (2L / (2L - k)) * binom(2L - k, k). Convolving the matching polynomials across all components yields the coefficient sequence c_k. The final answer is sum_{k=0}^N (-1)^k c_k (N - k)!.

## 3. Step-by-Step Algorithm
1. 1. Construct bipartite graph with edges (i, p_i) and (i, q_i).
2. 2. Decompose graph into connected components (cycles and paths).
3. 3. Compute the matching polynomial for each component via closed form / DP.
4. 4. Convolve polynomials across all components using polynomial multiplication / DP.
5. 5. Apply PIE formula: sum_{k=0}^N (-1)^k c_k (N - k)! mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const long long MOD = 1000000007;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = res * base % MOD;
        base = base * base % MOD;
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

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n), q(n);
    vector<vector<int>> val_to_idx(n + 1);

    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        val_to_idx[p[i]].push_back(i);
    }
    for (int i = 0; i < n; ++i) {
        cin >> q[i];
        val_to_idx[q[i]].push_back(i);
    }

    int max_fact = 2 * n + 10;
    vector<long long> fact(max_fact, 1), inv(max_fact, 1);
    for (int i = 1; i < max_fact; ++i) {
        fact[i] = fact[i - 1] * i % MOD;
    }
    inv[max_fact - 1] = modInverse(fact[max_fact - 1]);
    for (int i = max_fact - 2; i >= 0; --i) {
        inv[i] = inv[i + 1] * (i + 1) % MOD;
    }

    auto nCr = [&](int n_val, int r_val) -> long long {
        if (r_val < 0 || r_val > n_val) return 0;
        return fact[n_val] * inv[r_val] % MOD * inv[n_val - r_val] % MOD;
    };

    vector<bool> visited(n, false);
    vector<int> cycle_lengths;

    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            vector<int> comp;
            vector<int> stk = {i};
            visited[i] = true;
            while (!stk.empty()) {
                int u = stk.back();
                stk.pop_back();
                comp.push_back(u);
                for (int val : {p[u], q[u]}) {
                    for (int nxt : val_to_idx[val]) {
                        if (!visited[nxt]) {
                            visited[nxt] = true;
                            stk.push_back(nxt);
                        }
                    }
                }
            }
            cycle_lengths.push_back(comp.size());
        }
    }

    vector<long long> poly = {1};

    for (int L : cycle_lengths) {
        vector<long long> cur;
        if (L == 1) {
            cur = {1, 1};
        } else {
            cur.assign(L + 1, 0);
            cur[0] = 1;
            for (int k = 1; k <= L; ++k) {
                long long term = (2LL * L % MOD) * modInverse(2 * L - k) % MOD;
                term = term * nCr(2 * L - k, k) % MOD;
                cur[k] = term;
            }
        }

        vector<long long> next_poly(poly.size() + cur.size() - 1, 0);
        for (size_t i = 0; i < poly.size(); ++i) {
            for (size_t j = 0; j < cur.size(); ++j) {
                next_poly[i + j] = (next_poly[i + j] + poly[i] * cur[j]) % MOD;
            }
        }
        poly = move(next_poly);
    }

    long long ans = 0;
    for (size_t k = 0; k < poly.size(); ++k) {
        if ((int)k <= n) {
            long long term = poly[k] * fact[n - k] % MOD;
            if (k % 2 == 1) {
                ans = (ans - term + MOD) % MOD;
            } else {
                ans = (ans + term) % MOD;
            }
        }
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
