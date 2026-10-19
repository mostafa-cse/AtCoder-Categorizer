# Problem Analysis: AtCoder-abc283_h — Popcount Sum

**Problem ID**: `AtCoder-abc283_h`  
**Contest**: `abc283`  
**Rating / Difficulty**: 2682  
**URL**: https://atcoder.jp/contests/abc283/tasks/abc283_h  
**VJudge Tag**: `[problem:AtCoder-abc283_h]`  
**Category File**: [`../categories/number_theory/popcount_sum_digit_floor_sum.md`](../categories/number_theory/popcount_sum_digit_floor_sum.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Floor Sum`  
- **Topic (Skill)**: `Floor Sum and Mod Sum of Arithmetic Progression`  

---

## 1. Problem Statement & Key Idea
Compute sum_{k=1}^R popcount(A * k + B) efficiently for A, B, R <= 10^9. Because popcount(X) = sum_{b=0}^{60} ((X >> b) & 1), we can decompose the sum bit-by-bit: the b-th bit of X is 1 iff floor((X + 2^b) / 2^{b+1}) - floor(X / 2^{b+1}) = 1. Summing over k reduces each bit to standard AtCoder floor_sum, solvable in O(log(A + 2^b)) per bit.

## 2. Core Observation & Invariant
Substituting X = A * k + B, the sum over k=1..R becomes sum_{k=1}^R floor((A*k + B + 2^b) / 2^{b+1}) - sum_{k=1}^R floor((A*k + B) / 2^{b+1}). Each sum is an evaluation of ACL floor_sum. With 30 bits, each query runs in O(30 log(mod)) time.

## 3. Step-by-Step Algorithm
1. 1. For each query (N, M, A, B):
2. 2. Loop over bit positions b = 0..30.
3. 3. Compute S_1 = floor_sum(R + 1, 2^{b+1}, A, B + 2^b) and S_2 = floor_sum(R + 1, 2^{b+1}, A, B).
4. 4. Adjust for k=0.
5. 5. Add S_1 - S_2 to total popcount sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(30 log(mod))`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

long long floor_sum(long long n, long long m, long long a, long long b) {
    long long ans = 0;
    if (a >= m) {
        ans += (n - 1) * n / 2 * (a / m);
        a %= m;
    }
    if (b >= m) {
        ans += n * (b / m);
        b %= m;
    }

    long long y_max = (a * n + b) / m;
    long long x_max = (y_max * m - b);
    if (y_max == 0) return ans;

    ans += (n - (x_max + a - 1) / a) * y_max;
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a);
    return ans;
}

long long count_sum(long long limit, long long M, long long R) {
    if (limit < 0) return 0;
    long long total = 0;
    for (int b = 0; b < 30; ++b) {
        long long s1 = floor_sum(limit + 1, 1LL << b, M, R);
        long long s2 = floor_sum(limit + 1, 1LL << (b + 1), M, R);
        total += s1 - 2 * s2;
    }
    return total;
}

void solve() {
    long long N, M, R;
    cin >> N >> M >> R;

    long long k_min = (R == 0) ? 1 : 0;
    long long k_max = (N - R) / M;
    if (k_min > k_max) {
        cout << 0 << "\n";
        return;
    }

    long long ans = count_sum(k_max, M, R) - count_sum(k_min - 1, M, R);
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (!(cin >> T)) return 0;

    while (T--) {
        solve();
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
