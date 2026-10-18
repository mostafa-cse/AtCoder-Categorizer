# Problem Analysis: AtCoder-agc063_c — C. Add Mod Operations

**Problem ID**: `AtCoder-agc063_c`  
**Contest**: `agc063`  
**Rating / Difficulty**: 2500  
**URL**: https://atcoder.jp/contests/agc063/tasks/agc063_c  
**VJudge Tag**: `[problem:AtCoder-agc063_c]`  
**Category File**: [`../categories/number_theory/add_mod_operations_crt_cycle.md`](../categories/number_theory/add_mod_operations_crt_cycle.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Chinese Remainder Theorem (CRT)`  

---

## 1. Problem Statement & Key Idea
Transform sequence $A$ to $B$ using at most $N$ operations of the form $A_i \leftarrow (A_i + x) \pmod y$ with $x \ge 0, y \ge 1$.

## 2. Core Observation & Invariant
Check consistency: if $A_i = A_j$ with $B_i \ne B_j$, output `No`. Otherwise, reduce to $N'$ distinct sorted pairs $(A_i, B_i)$. An operation with $y = x + \max(A)$ acts as a circular shift, dropping $\max(A)$ and inserting an interval of length $x + \min(A)$. Using a large modulus $K > \max(A) + \max(B)$ and target residue classes $B'_i = B_i + K \cdot r_i$, $N' - 1$ operations configure differences between adjacent elements, and a final operation $(B'_1, K)$ aligns all values simultaneously in $N' \le N$ operations.

## 3. Step-by-Step Algorithm
1. 1. Check for conflicting mappings $A_i \to B_i$.
2. 2. Remove duplicates to $N'$ sorted distinct pairs.
3. 3. If $N' = 1$, output 0 operations if $A_0 == B_0$, else 1 operation $((B_0 - A_0) \bmod 10^{18}, 10^{18})$.
4. 4. Set $K = \max(\max A, \max B) + 10^9 + 7$.
5. 5. Set $B'_0 = B_0 + K \cdot N'$, $B'_i = B_i + K \cdot i$ for $i \ge 1$.
6. 6. Perform $N'-1$ operations with $x_i$ and $y_i = x_i + \max(A)$.
7. 7. Perform the final operation $(B'_1, K)$.
8. 8. Output `Yes`, operation count, and operations.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> A(n), B(n);
    for (int i = 0; i < n; ++i) cin >> A[i];
    for (int i = 0; i < n; ++i) cin >> B[i];

    map<long long, long long> val_map;
    for (int i = 0; i < n; ++i) {
        if (val_map.count(A[i]) && val_map[A[i]] != B[i]) {
            cout << "No\n";
            return 0;
        }
        val_map[A[i]] = B[i];
    }

    vector<pair<long long, long long>> pairs;
    for (auto &kv : val_map) {
        pairs.push_back({kv.first, kv.second});
    }
    sort(pairs.begin(), pairs.end());
    int n_prime = pairs.size();

    if (n_prime == 1) {
        if (pairs[0].first == pairs[0].second) {
            cout << "Yes\n0\n";
            return 0;
        }
        long long y = 1000000000000000000LL;
        long long x = (pairs[0].second - pairs[0].first) % y;
        if (x < 0) x += y;
        cout << "Yes\n1\n" << x << " " << y << "\n";
        return 0;
    }

    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        max_val = max({max_val, A[i], B[i]});
    }
    long long K = max_val + 1000000007LL;

    vector<long long> B_prime(n_prime);
    B_prime[0] = pairs[0].second + K * n_prime;
    for (int i = 1; i < n_prime; ++i) {
        B_prime[i] = pairs[i].second + K * i;
    }

    vector<long long> x_val(n_prime);
    for (int i = 2; i < n_prime; ++i) {
        x_val[n_prime + 1 - i] = B_prime[i] - B_prime[i - 1];
    }
    x_val[1] = B_prime[0] - B_prime[n_prime - 1];

    vector<pair<long long, long long>> ops;
    vector<long long> cur_A(n_prime);
    for (int i = 0; i < n_prime; ++i) cur_A[i] = pairs[i].first;

    for (int step = 1; step < n_prime; ++step) {
        long long x = (step == 1 ? x_val[1] - cur_A[0] : x_val[step]);
        long long mx = 0;
        for (long long v : cur_A) mx = max(mx, v);
        long long y = x + mx;
        ops.push_back({x, y});
        for (int i = 0; i < n_prime; ++i) {
            cur_A[i] = (cur_A[i] + x) % y;
        }
    }

    ops.push_back({B_prime[1], K});

    cout << "Yes\n" << ops.size() << "\n";
    for (auto &op : ops) {
        cout << op.first << " " << op.second << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
