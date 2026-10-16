# Problem Analysis: AtCoder-abc148_e — Double Factorial

**Problem ID**: `AtCoder-abc148_e`  
**Contest**: `abc148`  
**Rating / Difficulty**: 818  
**URL**: https://atcoder.jp/contests/abc148/tasks/abc148_e  
**VJudge Tag**: `[problem:AtCoder-abc148_e]`  
**Category File**: [`../categories/math/legendre_double_factorial.md`](../categories/math/legendre_double_factorial.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Number Theory`  
- **Topic (Skill)**: `Legendre's Formula on Double Factorial / p-adic Valuation`  

---

## 1. Problem Statement & Key Idea
Given N <= 10^18. Calculate the number of trailing zeros in the decimal representation of N!! = N * (N - 2) * (N - 4) ...

**Key Idea**: Trailing zeros are formed by factors of 10 = 2 * 5. If N is odd, N!! contains only odd factors, so v_2(N!!) = 0 and trailing zeros = 0. If N is even, trailing zeros = v_5(N!!).

## 2. Core Observation & Invariant
For even N, N!! = 2^(N/2) * (N/2)!. The factors of 5 come from even multiples of 5, which are multiples of 10: 10, 20, 30... Dividing N by 2 maps each number 2k to k, giving exact Legendre formula v_5((N/2)!) = sum_{k >= 1} floor((N/2) / 5^k) = sum_{k >= 1} floor(N / (2 * 5^k)).

## 3. Step-by-Step Algorithm
1. If N % 2 == 1, output 0.
2. Initialize ans = 0, current_divisor = 10.
3. While N >= current_divisor: ans += N / current_divisor, current_divisor *= 5.
4. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(log_5 N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    if (n % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    long long ans = 0;
    long long div = 10;
    while (n >= div) {
        ans += n / div;
        if (n / 5 < div) break; // prevent overflow
        div *= 5;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial approach exactly.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting p-adic valuations in non-standard factorial sequences.
- **Reusable Pattern**: `Trailing zeros in even double factorials: v_5(N!!) = v_5((N/2)!).`
