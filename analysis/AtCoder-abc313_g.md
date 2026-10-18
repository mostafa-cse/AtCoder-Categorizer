# Problem Analysis: AtCoder-abc313_g — G - Redistribution of Piles

**Problem ID**: `AtCoder-abc313_g`  
**Contest**: `abc313`  
**Rating / Difficulty**: 2454  
**URL**: https://atcoder.jp/contests/abc313/tasks/abc313_g  
**VJudge Tag**: `[problem:AtCoder-abc313_g]`  
**Category File**: [`../categories/number_theory/redistribution_of_piles_floor_sum.md`](../categories/number_theory/redistribution_of_piles_floor_sum.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Floor Sum`  
- **Topic (Skill)**: `Floor Sum and Mod Sum of Arithmetic Progression`  

---

## 1. Problem Statement & Key Idea
Find the number of reachable multisets of pile sizes after repeatedly choosing $i$ non-empty piles and decrementing them while adding $i$ to a chosen pile.

## 2. Core Observation & Invariant
Sorting the initial array $A$ non-decreasingly, every reachable state corresponds to choosing the number of operations of each type. Equivalently, the number of distinct terminal configurations reduces to summing the number of lattice points bounded by piecewise linear constraints, which evaluates to floor sums of arithmetic progressions $\sum \lfloor (a x + b) / c \rfloor$ across adjacent intervals.

## 3. Step-by-Step Algorithm
1. 1. Sort the input array $A_1 \le A_2 \le \dots \le A_N$.
2. 2. Compute prefix sums and prefix minimum differences.
3. 3. Formulate the boundary of valid operation counts $(x, y)$ as piecewise linear constraints.
4. 4. Decompose the sum of valid points over each linear segment $[L_i, R_i]$ into standard AtCoder `floor_sum` calls in $O(N \log M)$ time.
5. 5. Output the total reachable states modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N + N \log(\max A))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

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

    long long y_max = (a * n + b) / m, x_max = (y_max * m - b);
    if (y_max == 0) return ans;
    ans += (n - (x_max + a - 1) / a) * y_max;
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a);
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    sort(A.begin(), A.end());

    long long s = A[0] * N;
    long long ans = (A[0] + 1) % MOD;

    for (int i = 1; i < N; ++i) {
        long long L = A[i - 1];
        long long R = A[i];
        long long a = N - i;
        long long b = s - L * (N - i);
        long long m = N;

        long long cur = 0;
        cur += floor_sum(R + 1, m, a, b);
        cur -= floor_sum(L + 1, m, a, b);
        cur += (R - L);

        ans = (ans + cur % MOD) % MOD;
        s += (R - L) * (N - i);
    }

    cout << (ans % MOD + MOD) % MOD << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
