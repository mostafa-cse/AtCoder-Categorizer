# Problem Analysis: AtCoder-arc133_d — Range XOR

**Problem ID**: `AtCoder-arc133_d`  
**Contest**: `arc133`  
**Rating / Difficulty**: 2658  
**URL**: https://atcoder.jp/contests/arc133/tasks/arc133_d  
**VJudge Tag**: `[problem:AtCoder-arc133_d]`  
**Category File**: [`../categories/dynamic_programming_dp/range_xor_prefix_digit_dp.md`](../categories/dynamic_programming_dp/range_xor_prefix_digit_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP`  

---

## 1. Problem Statement & Key Idea
Counting pairs (l, r) with prefix XOR sum f(r) ^ f(l-1) = V reduces via the period-4 property of prefix XORs to 16 arithmetic cases, 4 of which are solved using 2D bitwise Digit DP.

## 2. Core Observation & Invariant
The prefix XOR function f(n) depends only on n mod 4: n (if 0), 1 (if 1), n+1 (if 2), and 0 (if 3). For pairs (x, y) = (l-1, r), cases where both variables depend on n reduce to counting pairs (u, v) with u ^ v = K and u < v within 2D rectangular bounds [u_1, u_2] x [v_1, v_2]. Digit DP on bit positions with state (bit, tight_u, tight_v, cmp) evaluates these in O(log(max R)) time.

## 3. Step-by-Step Algorithm
1. 1. Express the condition as f(x) ^ f(y) = V for L-1 <= x < y <= R.
2. 2. Classify into 16 cases based on (x mod 4, y mod 4).
3. 3. Solve the 12 constant/linear cases using O(1) arithmetic progression counting.
4. 4. Solve the 4 variable cases using 2D Digit DP over bit representations up to 60 bits.
5. 5. Sum results modulo 998244353 and print.

## 4. Complexity Analysis
- **Time Complexity**: `O(log R)`
- **Space Complexity**: `O(log R)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

static const long long MOD = 998244353;

long long count_le(long long n, int r) {
    if (n < 0) return 0;
    long long cnt = (n + 1) / 4;
    long long rem = (n + 1) % 4;
    if (rem > r) cnt++;
    return cnt;
}

long long count_range(long long lo, long long hi, int r) {
    if (lo > hi) return 0;
    return count_le(hi, r) - count_le(lo - 1, r);
}

long long count_pairs_order(long long A1, long long A2, long long B1, long long B2, bool strict_lt) {
    if (A1 > A2 || B1 > B2) return 0;
    long long offset = strict_lt ? 1 : 0;
    long long ans = 0;

    long long b_mid_lo = max(B1, A1 + offset);
    long long b_mid_hi = min(B2, A2 + offset - 1);
    if (b_mid_lo <= b_mid_hi) {
        long long C = offset + A1 - 1;
        long long n = (b_mid_hi - b_mid_lo + 1) % MOD;
        long long sum_b = ((b_mid_lo + b_mid_hi) % MOD) * n % MOD * 499122177LL % MOD; // / 2 mod MOD
        long long sub = (C % MOD) * n % MOD;
        ans = (ans + sum_b - sub + MOD) % MOD;
    }

    long long b_hi_lo = max(B1, A2 + offset);
    if (b_hi_lo <= B2) {
        long long count_b = (B2 - b_hi_lo + 1) % MOD;
        long long count_a = (A2 - A1 + 1) % MOD;
        ans = (ans + count_b * count_a) % MOD;
    }

    return ans;
}

long long memo[62][2][2][2];

long long dp_calc(int bit, int tight_u, int tight_v, int cmp, long long U, long long V, long long K) {
    if (bit < 0) {
        return cmp == 1 ? 1 : 0;
    }
    if (memo[bit][tight_u][tight_v][cmp] != -1) {
        return memo[bit][tight_u][tight_v][cmp];
    }

    int limit_u = tight_u ? ((U >> bit) & 1) : 1;
    int limit_v = tight_v ? ((V >> bit) & 1) : 1;
    int k_bit = (K >> bit) & 1;

    long long ans = 0;
    for (int ub = 0; ub <= limit_u; ++ub) {
        int vb = ub ^ k_bit;
        if (vb > limit_v) continue;

        int new_cmp = cmp;
        if (cmp == 0) {
            if (ub < vb) new_cmp = 1;
            else if (ub > vb) continue;
        }

        int new_tu = tight_u && (ub == limit_u);
        int new_tv = tight_v && (vb == limit_v);

        ans = (ans + dp_calc(bit - 1, new_tu, new_tv, new_cmp, U, V, K)) % MOD;
    }

    return memo[bit][tight_u][tight_v][cmp] = ans;
}

long long count_xor_lt(long long U, long long V, long long K) {
    if (U < 0 || V < 0) return 0;
    memset(memo, -1, sizeof(memo));
    return dp_calc(60, 1, 1, 0, U, V, K);
}

long long count_xor_le(long long U, long long V, long long K) {
    long long res = count_xor_lt(U, V, K);
    if (K == 0 && min(U, V) >= 0) {
        res = (res + (min(U, V) + 1) % MOD) % MOD;
    }
    return res;
}

long long query_2d(long long u1, long long u2, long long v1, long long v2, long long K, bool strict_lt) {
    if (u1 > u2 || v1 > v2) return 0;
    auto fn = strict_lt ? count_xor_lt : count_xor_le;
    long long res = fn(u2, v2, K) - fn(u1 - 1, v2, K) - fn(u2, v1 - 1, K) + fn(u1 - 1, v1 - 1, K);
    res %= MOD;
    if (res < 0) res += MOD;
    return res;
}

long long div_floor(long long a, long long b) {
    long long res = a / b;
    long long rem = a % b;
    if (rem != 0 && ((a < 0) ^ (b < 0))) {
        res--;
    }
    return res;
}

long long div_ceil(long long a, long long b) {
    long long res = a / b;
    long long rem = a % b;
    if (rem != 0 && !((a < 0) ^ (b < 0))) {
        res++;
    }
    return res;
}

pair<long long, long long> get_range(long long lo, long long hi, int r) {
    long long a1 = div_ceil(lo - r, 4);
    long long a2 = div_floor(hi - r, 4);
    return {a1, a2};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long L, R, V;
    if (!(cin >> L >> R >> V)) return 0;

    long long lo = L - 1;
    long long hi = R;
    long long ans = 0;

    // Case 1: (3, 3)
    if (V == 0) {
        long long c = count_range(lo, hi, 3) % MOD;
        ans = (ans + c * (c - 1 + MOD) % MOD * 499122177LL) % MOD;
    }

    // Case 2: (1, 1)
    if (V == 0) {
        long long c = count_range(lo, hi, 1) % MOD;
        ans = (ans + c * (c - 1 + MOD) % MOD * 499122177LL) % MOD;
    }

    // Case 3: (1, 3)
    if (V == 1) {
        auto [a1, a2] = get_range(lo, hi, 1);
        auto [b1, b2] = get_range(lo, hi, 3);
        ans = (ans + count_pairs_order(a1, a2, b1, b2, false)) % MOD;
    }

    // Case 4: (3, 1)
    if (V == 1) {
        auto [a1, a2] = get_range(lo, hi, 3);
        auto [b1, b2] = get_range(lo, hi, 1);
        ans = (ans + count_pairs_order(a1, a2, b1, b2, true)) % MOD;
    }

    // Case 5: (0, 3) -> x = V
    if (V % 4 == 0 && lo <= V && V <= hi) {
        ans = (ans + count_range(V + 1, hi, 3)) % MOD;
    }

    // Case 6: (3, 0) -> y = V
    if (V % 4 == 0 && lo <= V && V <= hi) {
        ans = (ans + count_range(lo, V - 1, 3)) % MOD;
    }

    // Case 7: (2, 3) -> x = V - 1
    if (V >= 1 && (V - 1) % 4 == 2 && lo <= V - 1 && V - 1 <= hi) {
        ans = (ans + count_range(V, hi, 3)) % MOD;
    }

    // Case 8: (3, 2) -> y = V - 1
    if (V >= 1 && (V - 1) % 4 == 2 && lo <= V - 1 && V - 1 <= hi) {
        ans = (ans + count_range(lo, V - 2, 3)) % MOD;
    }

    // Case 9: (0, 1) -> x = V ^ 1
    long long x9 = V ^ 1;
    if (x9 % 4 == 0 && lo <= x9 && x9 <= hi) {
        ans = (ans + count_range(x9 + 1, hi, 1)) % MOD;
    }

    // Case 10: (1, 0) -> y = V ^ 1
    long long y10 = V ^ 1;
    if (y10 % 4 == 0 && lo <= y10 && y10 <= hi) {
        ans = (ans + count_range(lo, y10 - 1, 1)) % MOD;
    }

    // Case 11: (2, 1) -> x = (V ^ 1) - 1
    long long x11 = (V ^ 1) - 1;
    if (x11 >= 0 && x11 % 4 == 2 && lo <= x11 && x11 <= hi) {
        ans = (ans + count_range(x11 + 1, hi, 1)) % MOD;
    }

    // Case 12: (1, 2) -> y = (V ^ 1) - 1
    long long y12 = (V ^ 1) - 1;
    if (y12 >= 0 && y12 % 4 == 2 && lo <= y12 && y12 <= hi) {
        ans = (ans + count_range(lo, y12 - 1, 1)) % MOD;
    }

    // Case 13: (0, 0)
    if (V % 4 == 0) {
        long long K = V / 4;
        auto [a1, a2] = get_range(lo, hi, 0);
        auto [b1, b2] = get_range(lo, hi, 0);
        ans = (ans + query_2d(a1, a2, b1, b2, K, true)) % MOD;
    }

    // Case 14: (0, 2)
    if (V % 4 == 3) {
        long long K = V / 4;
        auto [a1, a2] = get_range(lo, hi, 0);
        auto [b1, b2] = get_range(lo, hi, 2);
        ans = (ans + query_2d(a1, a2, b1, b2, K, false)) % MOD;
    }

    // Case 15: (2, 0)
    if (V % 4 == 3) {
        long long K = V / 4;
        auto [a1, a2] = get_range(lo, hi, 2);
        auto [b1, b2] = get_range(lo, hi, 0);
        ans = (ans + query_2d(a1, a2, b1, b2, K, true)) % MOD;
    }

    // Case 16: (2, 2)
    if (V % 4 == 0) {
        long long K = V / 4;
        auto [a1, a2] = get_range(lo, hi, 2);
        auto [b1, b2] = get_range(lo, hi, 2);
        ans = (ans + query_2d(a1, a2, b1, b2, K, true)) % MOD;
    }

    cout << (ans % MOD + MOD) % MOD << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
