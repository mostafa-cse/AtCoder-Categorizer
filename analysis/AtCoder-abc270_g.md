# Problem Analysis: AtCoder-abc270_g — Sequence in mod P

**Problem ID**: `AtCoder-abc270_g`  
**Contest**: `abc270`  
**Rating / Difficulty**: 2220  
**URL**: https://atcoder.jp/contests/abc270/tasks/abc270_g  
**VJudge Tag**: `[problem:AtCoder-abc270_g]`  
**Category File**: [`../categories/number_theory/sequence_in_mod_p_affine_recurrence_bsgs.md`](../categories/number_theory/sequence_in_mod_p_affine_recurrence_bsgs.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Discrete Log / Baby Step Giant Step`  

---

## 1. Problem Statement & Key Idea
Find the smallest index i >= 0 such that X_i = G for recurrence X_0 = S, X_i = (A X_{i-1} + B) mod P for prime P <= 10^9.

## 2. Core Observation & Invariant
Unfolding the affine recurrence yields X_i = A^i S + B (A^i - 1) / (A - 1) mod P. Multiplying by (A - 1) yields A^i ((A - 1)S + B) = (A - 1)G + B mod P, which reduces to a standard discrete logarithm A^i = Y mod P solvable via Baby-Step Giant-Step (BSGS) in O(sqrt(P)) time.

## 3. Step-by-Step Algorithm
1. 1. Handle boundary cases: S == G (return 0), A == 0 (check B % P == G), A == 1 (solve linear congruence i * B = G - S mod P).
2. 2. For A >= 2, let L = (A - 1)S + B and R = (A - 1)G + B mod P.
3. 3. If L == 0: return 1 if R == 0 else -1. If R == 0: return -1.
4. 4. Set Y = R * L^{-1} mod P. Solve A^i = Y mod P with BSGS (m = ceil(sqrt(P))).
5. 5. Baby steps: store (A^r, r) for r in [0, m-1] in sorted vector.
6. 6. Giant steps: for q in [0, m], check if Y * (A^{-m})^q exists in baby table to find minimal i = q*m + r.

## 4. Complexity Analysis
- **Time Complexity**: `O(sqrt(P) log(P)) per testcase`
- **Space Complexity**: `O(sqrt(P))`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

long long power(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n, long long mod) {
    return power(n, mod - 2, mod);
}

void solve() {
    long long p, a, b, s, g;
    cin >> p >> a >> b >> s >> g;

    if (s == g) {
        cout << 0 << "\n";
        return;
    }
    if (a == 0) {
        if (b % p == g) cout << 1 << "\n";
        else cout << -1 << "\n";
        return;
    }
    if (a == 1) {
        if (b % p == 0) {
            cout << -1 << "\n";
            return;
        }
        long long diff = (g - s) % p;
        if (diff < 0) diff += p;
        long long ans = (diff * modInverse(b, p)) % p;
        cout << ans << "\n";
        return;
    }

    long long L = ((a - 1) % p * (s % p) + b) % p;
    long long R = ((a - 1) % p * (g % p) + b) % p;
    if (L == 0) {
        if (R == 0) cout << 1 << "\n";
        else cout << -1 << "\n";
        return;
    }
    if (R == 0) {
        cout << -1 << "\n";
        return;
    }

    long long Y = (R * modInverse(L, p)) % p;

    // BSGS for a^i == Y (mod p)
    long long m = sqrt(p) + 1;
    vector<pair<int, int>> baby;
    baby.reserve(m);
    long long cur = 1;
    for (int r = 0; r < m; r++) {
        baby.push_back({(int)cur, r});
        cur = (cur * a) % p;
    }
    sort(baby.begin(), baby.end());
    // remove duplicates keeping smallest r
    vector<pair<int, int>> uniq;
    uniq.reserve(m);
    for (auto& pr : baby) {
        if (uniq.empty() || uniq.back().first != pr.first) {
            uniq.push_back(pr);
        }
    }

    long long a_m = power(a, m, p);
    long long inv_a_m = modInverse(a_m, p);

    long long cur_target = Y;
    for (int q = 0; q <= m; q++) {
        // search cur_target in uniq
        auto it = lower_bound(uniq.begin(), uniq.end(), make_pair((int)cur_target, -1));
        if (it != uniq.end() && it->first == cur_target) {
            long long ans = (long long)q * m + it->second;
            cout << ans << "\n";
            return;
        }
        cur_target = (cur_target * inv_a_m) % p;
    }

    cout << -1 << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
