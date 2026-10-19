# Problem Analysis: AtCoder-hhkb2020_f — Random Max

**Problem ID**: `AtCoder-hhkb2020_f`  
**Contest**: `hhkb2020`  
**Rating / Difficulty**: 2691  
**URL**: https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_f  
**VJudge Tag**: `[problem:AtCoder-hhkb2020_f]`  
**Category File**: [`../categories/math/random_max_continuous_expectation.md`](../categories/math/random_max_continuous_expectation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
For N independent uniform continuous variables x_i ~ U[L_i, R_i], E[max x_i] = T_max - int_{max L_i}^{T_max} F(t) dt where F(t) = prod g_i(t) / prod(R_i - L_i). On [max L_i, T_max], each factor g_i(t) transitions from linear (t - L_i) to constant (R_i - L_i) exactly at t = R_i. By sweeping t across sorted distinct R_i >= max L_i, we maintain the polynomial prod (t - L_i) using synthetic polynomial division in O(N^2) total time.

## 2. Core Observation & Invariant
Since all t >= max L_j >= L_i for all i, no variable ever enters the linear state from 0; variables are initially in state (t - L_i) if R_i > max L_j (or constant if R_i <= max L_j), and at t = R_i they exit to constant (R_i - L_i). Thus, the polynomial P(t) only undergoes divisions by (t - L_i), each taking O(N) via Horner's synthetic division.

## 3. Step-by-Step Algorithm
1. 1. Let c0 = max L_i, cK = max R_i, and V = prod (R_i - L_i) mod MOD.
2. 2. Construct the initial polynomial P(t) = prod_{i: R_i > c0} (t - L_i) by successive O(N) polynomial multiplications.
3. 3. Gather distinct endpoints in [c0, cK] sorted in ascending order.
4. 4. For each interval [t1, t2], integrate P(t) over [t1, t2] term by term, multiplying by the current constant factor.
5. 5. At t2, for every variable with R_i = t2, divide P(t) by (t - L_i) via synthetic division and multiply constant factor by (R_i - L_i).
6. 6. Compute E * (N+1)! * V = (N+1)! * (cK * V - total_integral) mod MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

static const long long MOD = 1000000007;

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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> intervals(n);
    long long c0 = 0;
    long long cK = 0;
    for (int i = 0; i < n; ++i) {
        cin >> intervals[i].first >> intervals[i].second;
        c0 = max(c0, intervals[i].first);
        cK = max(cK, intervals[i].second);
    }

    long long init_const = 1;
    vector<long long> poly = {1}; // poly[d] is coeff of t^d

    map<long long, vector<long long>> events;
    vector<long long> pts_set;
    pts_set.push_back(c0);

    for (int i = 0; i < n; ++i) {
        long long L = intervals[i].first;
        long long R = intervals[i].second;
        if (R <= c0) {
            init_const = (init_const * (R - L)) % MOD;
        } else {
            events[R].push_back(L);
            pts_set.push_back(R);
            vector<long long> new_poly(poly.size() + 1, 0);
            for (size_t d = 0; d < poly.size(); ++d) {
                new_poly[d + 1] = (new_poly[d + 1] + poly[d]) % MOD;
                new_poly[d] = (new_poly[d] - (L % MOD) * poly[d]) % MOD;
                if (new_poly[d] < 0) new_poly[d] += MOD;
            }
            poly = move(new_poly);
        }
    }

    sort(pts_set.begin(), pts_set.end());
    pts_set.erase(unique(pts_set.begin(), pts_set.end()), pts_set.end());

    // Precompute inv
    vector<long long> inv(n + 2, 0);
    for (int i = 1; i <= n + 1; ++i) {
        inv[i] = modInverse(i);
    }

    long long total_integral = 0;
    long long cur_const = init_const;

    for (size_t k = 0; k + 1 < pts_set.size(); ++k) {
        long long t1 = pts_set[k] % MOD;
        long long t2 = pts_set[k + 1] % MOD;

        long long int_poly = 0;
        long long p1 = t1;
        long long p2 = t2;

        for (size_t d = 0; d < poly.size(); ++d) {
            long long term = (p2 - p1 + MOD) % MOD;
            term = (term * inv[d + 1]) % MOD;
            int_poly = (int_poly + poly[d] * term) % MOD;

            p1 = (p1 * t1) % MOD;
            p2 = (p2 * t2) % MOD;
        }

        total_integral = (total_integral + cur_const * int_poly) % MOD;

        long long event_R = pts_set[k + 1];
        auto it = events.find(event_R);
        if (it != events.end()) {
            for (long long L : it->second) {
                int m = (int)poly.size() - 1;
                vector<long long> Q(m, 0);
                Q[m - 1] = poly[m];
                long long L_mod = L % MOD;
                for (int j = m - 1; j > 0; --j) {
                    Q[j - 1] = (poly[j] + L_mod * Q[j]) % MOD;
                }
                poly = move(Q);
                cur_const = (cur_const * ((event_R - L) % MOD)) % MOD;
            }
        }
    }

    long long V = 1;
    for (int i = 0; i < n; ++i) {
        V = (V * ((intervals[i].second - intervals[i].first) % MOD)) % MOD;
    }

    long long ans = ((cK % MOD) * V - total_integral) % MOD;
    if (ans < 0) ans += MOD;

    long long fact = 1;
    for (int i = 1; i <= n + 1; ++i) {
        fact = (fact * i) % MOD;
    }
    ans = (ans * fact) % MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
