# Problem Analysis: AtCoder-abc475_g — G. Has Many Divisors

**Problem ID**: `AtCoder-abc475_g`  
**Contest**: `abc475`  
**Rating / Difficulty**: 2360  
**URL**: https://atcoder.jp/contests/abc475/tasks/abc475_g  
**VJudge Tag**: `[problem:AtCoder-abc475_g]`  
**Category File**: [`../categories/number_theory/highly_composite_avoiding_multiple.md`](../categories/number_theory/highly_composite_avoiding_multiple.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Multiplicative Functions`  
- **Topic (Skill)**: `Number of Divisors / Sum of Divisors / Sigma Function`  

---

## 1. Problem Statement & Key Idea
Find an integer $x \le N$ not divisible by $D$ with the maximum number of divisors. Enforcing $v_p(x) < v_p(D)$ for at least one prime factor $p \mid D$ restricts the search to non-increasing exponent sequences with at most one exception, explored via branch-and-bound DFS.

## 2. Core Observation & Invariant
A positive integer $x \le N$ is not a multiple of $D$ iff there exists at least one prime factor $p \mid D$ such that $v_p(x) < v_p(D)$. Any integer maximizing the divisor count $d(x)$ has non-increasing prime factor exponents $v_2(x) \ge v_3(x) \ge v_5(x) \ge \dots$, except possibly for the single restricted prime factor $p$.

## 3. Step-by-Step Algorithm
1. Factorize $D$. If $D$ has a prime factor $p > 53$, any standard highly composite number formed from the first 16 primes naturally satisfies $v_p(x) = 0 < v_p(D)$.
2. If all prime factors of $D$ are $\le 53$, iterate over each prime factor $p \mid D$, bounding $v_p(x) \le v_p(D) - 1$.
3. Search over non-increasing exponent sequences for primes $q \ne p$ using branch-and-bound DFS pruned at $x \le N$, exploring $\le 281,944$ candidate states.

## 4. Complexity Analysis
- **Time Complexity**: `O(T \cdot \text{HCN_States})`
- **Space Complexity**: `O(\text{primes})`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const vector<long long> PRIMES = {
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53
};

long long best_divs;
unsigned __int128 best_x;
long long N_LIMIT;

void dfs(int p_idx, int restricted_idx, int max_restr_exp, int prev_exp, unsigned __int128 cur_x, long long cur_divs) {
    if (cur_divs > best_divs || (cur_divs == best_divs && cur_x < best_x)) {
        best_divs = cur_divs;
        best_x = cur_x;
    }
    if (p_idx >= (int)PRIMES.size()) return;

    long long p = PRIMES[p_idx];
    int max_e = prev_exp;
    if (p_idx == restricted_idx) {
        max_e = min(max_e, max_restr_exp);
    }

    unsigned __int128 p_pow = 1;
    for (int e = 1; e <= max_e; e++) {
        p_pow *= p;
        if (cur_x > N_LIMIT / p_pow) break;
        int next_prev_exp = (p_idx == restricted_idx ? prev_exp : e);
        dfs(p_idx + 1, restricted_idx, max_restr_exp, next_prev_exp, cur_x * p_pow, cur_divs * (e + 1));
    }
    if (p_idx == restricted_idx) {
        dfs(p_idx + 1, restricted_idx, max_restr_exp, prev_exp, cur_x, cur_divs);
    }
}

void solve() {
    long long n, d;
    if (!(cin >> n >> d)) return;
    N_LIMIT = n;

    vector<pair<long long, int>> d_factors;
    long long temp = d;
    for (long long p : PRIMES) {
        if (temp % p == 0) {
            int cnt = 0;
            while (temp % p == 0) {
                cnt++;
                temp /= p;
            }
            d_factors.push_back({p, cnt});
        }
    }
    best_divs = -1;
    best_x = (unsigned __int128)-1;

    if (temp > 1) {
        dfs(0, -1, 100, 60, 1, 1);
    } else {
        for (auto& pf : d_factors) {
            long long p = pf.first;
            int req_max = pf.second - 1;
            int p_idx = 0;
            while (PRIMES[p_idx] != p) p_idx++;
            dfs(0, p_idx, req_max, 60, 1, 1);
        }
    }

    cout << (long long)best_x << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
