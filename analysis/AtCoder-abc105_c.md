# Problem Analysis: AtCoder-abc105_c — Base -2 Number

**Problem ID**: `AtCoder-abc105_c`  
**Contest**: `abc105`  
**Rating / Difficulty**: 1204  
**URL**: https://atcoder.jp/contests/abc105/tasks/abc105_c  
**VJudge Tag**: `[problem:AtCoder-abc105_c]`  
**Category File**: [`../categories/math/negative_base_conversion.md`](../categories/math/negative_base_conversion.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Base Conversion`  
- **Topic (Skill)**: `Negative Base Division / Modulo Arithmetic`  

---

## 1. Problem Statement & Key Idea
Given an integer N. Find its base -2 representation, i.e., a binary string S = S_k...S_0 such that N = sum_{i=0}^k S_i * (-2)^i with S_k != 0 (or '0' if N = 0).

**Key Idea**: In base -2, each digit must be either 0 or 1. If N is odd, the least significant bit S_0 must be 1; if even, S_0 = 0.

## 2. Core Observation & Invariant
When we extract rem = N % (-2), C++ standard gives rem in {-1, 0, 1}. If rem is negative (-1), we adjust rem += 2 and quotient N = (N - rem) / (-2). This ensures every remainder digit is strictly in {0, 1}.

## 3. Step-by-Step Algorithm
1. If N == 0, output '0'.
2. While N != 0:
3.   Compute remainder rem = N % (-2).
4.   Compute N = N / (-2).
5.   If rem < 0: rem += 2, N += 1.
6.   Append rem to result string.
7. Reverse result string and output.

## 4. Complexity Analysis
- **Time Complexity**: `O(log_2 |N|)`
- **Space Complexity**: `O(log_2 |N|)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    if (n == 0) {
        cout << "0\n";
        return 0;
    }

    string res = "";
    while (n != 0) {
        long long rem = n % -2;
        n /= -2;
        if (rem < 0) {
            rem += 2;
            n += 1;
        }
        res += to_string(rem);
    }

    reverse(res.begin(), res.end());
    cout << res << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Non-standard radix division with negative base Euclidean remainder normalization.
- **Reusable Pattern**: `Base -B: rem = N % (-B); if (rem < 0) { rem += B; N += 1; }.`
