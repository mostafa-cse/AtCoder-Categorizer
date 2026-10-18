# Problem Analysis: AtCoder-arc066_b — D. Xor Sum

**Problem ID**: `AtCoder-arc066_b`  
**Contest**: `abc050`  
**Rating / Difficulty**: 2606  
**URL**: https://atcoder.jp/contests/abc050/tasks/arc066_b  
**VJudge Tag**: `[problem:AtCoder-arc066_b]`  
**Category File**: [`../categories/dynamic_programming_dp/xor_sum_base2_digit_dp.md`](../categories/dynamic_programming_dp/xor_sum_base2_digit_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP`  

---

## 1. Problem Statement & Key Idea
Count pairs (u, v) with 0 <= u, v <= N such that there exist non-negative integers a, b with a xor b = u and a + b = v, modulo 10^9+7.

## 2. Core Observation & Invariant
Since a + b = (a xor b) + 2(a and b) and (a xor b) and (a and b) = 0, every valid pair (u, v) corresponds bijectively to a choice of base-2 digits c_i in {0, 1, 2} such that sum c_i 2^i <= N.

## 3. Step-by-Step Algorithm
1. Memoized recursion f(n):
2. Base cases: f(0) = 1, f(1) = 2.
3. If n = 2k: f(2k) = f(k) + 2 f(k - 1).
4. If n = 2k + 1: f(2k + 1) = 2 f(k) + f(k - 1).
5. Compute f(N) in O(log N) states.

## 4. Complexity Analysis
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(log N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <map>

using namespace std;

static const int MOD = 1000000007;

map<long long, long long> memo;

long long f(long long n) {
    if (n < 0) return 0;
    if (n == 0) return 1;
    if (n == 1) return 2;
    auto it = memo.find(n);
    if (it != memo.end()) return it->second;

    long long k = n / 2;
    long long res = 0;
    if (n % 2 == 0) {
        res = (f(k) + 2 * f(k - 1)) % MOD;
    } else {
        res = (2 * f(k) + f(k - 1)) % MOD;
    }

    memo[n] = res;
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N;
    if (cin >> N) {
        cout << f(N) << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
