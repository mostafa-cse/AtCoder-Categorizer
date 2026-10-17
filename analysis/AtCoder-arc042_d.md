# Problem Analysis: AtCoder-arc042_d — あまり

**Problem ID**: `AtCoder-arc042_d`  
**Contest**: `arc042`  
**Rating / Difficulty**: 2247  
**URL**: https://atcoder.jp/contests/arc042/tasks/arc042_d  
**VJudge Tag**: `[problem:AtCoder-arc042_d]`  
**Category File**: [`../categories/number_theory/discrete_log_bsgs_interval_minimum_remainder.md`](../categories/number_theory/discrete_log_bsgs_interval_minimum_remainder.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Discrete Log / Baby Step Giant Step`  

---

## 1. Problem Statement & Key Idea
Find the minimum value of X^i mod P over all integers i in the range [A, B], where P < 2^31 is prime.

## 2. Core Observation & Invariant
If [A, B] spans a multiple of P - 1, the power X^i mod P hits 1 (the global minimum). Otherwise, if B - A <= 2 * 10^7, directly iterate i from A to B computing X^i mod P in O(B - A). If B - A > 2 * 10^7, the minimum value a in [1, P-1] must be tiny by the pigeonhole principle (typically a <= 100). We can iterate candidate remainders a = 1, 2, ... and test if X^i = a (mod P) has a solution with i in [A, B] using Baby-Step Giant-Step.

## 3. Step-by-Step Algorithm
1. 1. If A / (P - 1) != B / (P - 1), output 1.
2. 2. Reduce A, B modulo P - 1.
3. 3. If B - A <= 2 * 10^7, simulate exponentiation iteratively from X^A mod P, tracking the minimum.
4. 4. Otherwise, set sq = ceil(sqrt(P)). Precompute baby steps X^r mod P for r in [0, sq-1] in a sorted array.
5. 5. Test a = 1, 2, ...: compute tar = a * X^(-A) mod P, check giant steps tar * (X^(-sq))^j in the baby step table. If found and j * sq + r <= B - A, output a.

## 4. Complexity Analysis
- **Time Complexity**: `O(min(B - A, sqrt(P) * log(sqrt(P)) + ans * sqrt(P) * log(sqrt(P))))`
- **Space Complexity**: `O(sqrt(P))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

long long mod_pow(long long a, long long n, long long mod) {
    long long r = 1;
    a %= mod;
    while (n > 0) {
        if (n % 2 == 1) r = (long long)((__int128)r * a % mod);
        a = (long long)((__int128)a * a % mod);
        n /= 2;
    }
    return r;
}

long long mod_inv(long long a, long long p) {
    return mod_pow(a, p - 2, p);
}

// Flat hash map / sorted vector for baby steps
struct Entry {
    long long val;
    int idx;
    bool operator<(const Entry& o) const {
        return val < o.val;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long X, P, A, B;
    if (!(cin >> X >> P >> A >> B)) return 0;

    if (A / (P - 1) != B / (P - 1)) {
        cout << 1 << "\n";
        return 0;
    }

    A %= (P - 1);
    B %= (P - 1);
    long long len = B - A;

    long long XA = mod_pow(X, A, P);

    const long long THRESHOLD = 20000000; // 2 * 10^7
    if (len <= THRESHOLD) {
        long long min_val = XA;
        long long cur = XA;
        for (long long i = 0; i < len; ++i) {
            cur = (long long)((__int128)cur * X % P);
            if (cur < min_val) {
                min_val = cur;
                if (min_val == 1) break;
            }
        }
        cout << min_val << "\n";
    } else {
        long long sq = 1;
        while (sq * sq <= P) sq++;

        vector<Entry> table(sq);
        long long cur = 1;
        for (int r = 0; r < sq; ++r) {
            table[r] = {cur, r};
            cur = (long long)((__int128)cur * X % P);
        }
        sort(table.begin(), table.end());

        long long inv_X = mod_inv(X, P);
        long long inv_X_sq = mod_pow(inv_X, sq, P);
        long long inv_XA = mod_inv(XA, P);

        auto lookup = [&](long long val) -> int {
            auto it = lower_bound(table.begin(), table.end(), Entry{val, 0});
            if (it != table.end() && it->val == val) {
                return it->idx;
            }
            return -1;
        };

        for (long long a = 1; a < P; ++a) {
            long long tar = (long long)((__int128)a * inv_XA % P);
            for (int j = 0; j < sq; ++j) {
                int r = lookup(tar);
                if (r != -1 && (long long)j * sq + r <= len) {
                    cout << a << "\n";
                    return 0;
                }
                tar = (long long)((__int128)tar * inv_X_sq % P);
            }
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
