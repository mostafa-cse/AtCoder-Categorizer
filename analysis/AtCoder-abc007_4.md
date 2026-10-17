# Problem Analysis: AtCoder-abc007_4 — 禁止された数字

**Problem ID**: `AtCoder-abc007_4`  
**Contest**: `abc007`  
**Rating / Difficulty**: 1718  
**URL**: https://atcoder.jp/contests/abc007/tasks/abc007_4  
**VJudge Tag**: `[problem:AtCoder-abc007_4]`  
**Category File**: [`../categories/dp/digit_dp_banned_digits_base8.md`](../categories/dp/digit_dp_banned_digits_base8.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP: Base-8 Conversion / Banned Digits Counting`  

---

## 1. Problem Statement & Key Idea
Count the number of integers in [A, B] that contain the digit 4 or 9. (A, B <= 10^18).

**Key Insight**: Count the complement: numbers in [1, X] containing NEITHER 4 nor 9. Digits {0, 1, 2, 3, 5, 6, 7, 8} are allowed (8 valid digits). This is equivalent to standard Digit DP or base-8 conversion.

## 2. Core Observation & Invariant
Answer for [A, B] is (B - A + 1) - (count_valid(B) - count_valid(A - 1)).

## 3. Step-by-Step Algorithm
1. Write a function count_valid(X) using Digit DP:
2.   dp[idx][is_less] stores count of prefixes.
3.   For each digit d in {0..9}: if d == 4 or d == 9, skip.
4.   Transition to next digit updating is_less flag.
5. Ans = (B - A + 1) - (count_valid(B) - count_valid(A - 1)).

## 4. Complexity Analysis
- **Time Complexity**: `O(log10(B))`
- **Space Complexity**: `O(log10(B))`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

long long memo[20][2];
string S;

long long dp(int idx, bool is_less) {
    if (idx == (int)S.size()) return 1;
    if (memo[idx][is_less] != -1) return memo[idx][is_less];

    long long res = 0;
    int limit = is_less ? 9 : (S[idx] - '0');

    for (int d = 0; d <= limit; ++d) {
        if (d == 4 || d == 9) continue;
        res += dp(idx + 1, is_less || (d < limit));
    }

    return memo[idx][is_less] = res;
}

long long count_valid(long long n) {
    if (n < 0) return 0;
    S = to_string(n);
    memset(memo, -1, sizeof(memo));
    return dp(0, false);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    long long valid_b = count_valid(b);
    long long valid_a = count_valid(a - 1);

    long long total_numbers = b - a + 1;
    long long valid_numbers = valid_b - valid_a;

    cout << total_numbers - valid_numbers << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Digit DP counting with forbidden digits mapped to valid base transitions.
- **Reusable Pattern**: `Complementary Digit DP: Count forbidden by subtracting allowed base alphabet count.`
