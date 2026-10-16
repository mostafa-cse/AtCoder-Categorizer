# Problem Analysis: AtCoder-abc155_e — Payment

**Problem ID**: `AtCoder-abc155_e`  
**Contest**: `abc155`  
**Rating / Difficulty**: 1569  
**URL**: https://atcoder.jp/contests/abc155/tasks/abc155_e  
**VJudge Tag**: `[problem:AtCoder-abc155_e]`  
**Category File**: [`../categories/dp/digit_dp_carry_banknotes_payment.md`](../categories/dp/digit_dp_carry_banknotes_payment.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP with Carry on Minimum Digits for Payment and Change`  

---

## 1. Problem Statement & Key Idea
You need to pay an amount N (up to 10^6 digits) using banknotes of denominations 10^k. Both payment and change use the minimum total number of banknotes. Find the minimum total banknotes exchanged.

**Key Insight**: Process digits from right to left (least significant to most significant) with a carry state. At each digit d, you can either pay d notes with no carry, or pay 10 notes to round up (costing 10 - d notes in change) and passing a carry of 1 to the next digit.

## 2. Core Observation & Invariant
Let dp[0] be min banknotes with carry = 0, and dp[1] with carry = 1. For digit d + carry_in: Option A (no new carry): pay (d + carry_in), cost += (d + carry_in). Option B (carry = 1): pay extra, change is 10 - (d + carry_in), cost += 10 - (d + carry_in) + 1 note.

## 3. Step-by-Step Algorithm
1. Reverse string N and append '0' for possible final carry.
2. dp0 = 0 (carry 0), dp1 = 1 (carry 1).
3. For each digit char in N, let d = char - '0':
4.   next_dp0 = min(dp0 + d, dp1 + d + 1);
5.   next_dp1 = min(dp0 + (10 - d), dp1 + (10 - (d + 1)));
6.   dp0 = next_dp0, dp1 = next_dp1.
7. Print dp0.

## 4. Complexity Analysis
- **Time Complexity**: `O(|N|)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    reverse(s.begin(), s.end());
    s.push_back('0');

    long long dp0 = 0; // carry = 0
    long long dp1 = 1; // carry = 1

    for (char c : s) {
        int d = c - '0';
        long long next_dp0 = min(dp0 + d, dp1 + d + 1);
        long long next_dp1 = min(dp0 + (10 - d), dp1 + (10 - (d + 1)));
        dp0 = next_dp0;
        dp1 = next_dp1;
    }

    cout << dp0 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Digit DP with carry for optimal greedy rounding in base 10.
- **Reusable Pattern**: `Minimal Currency Exchange DP: 2-state carry transitions dp[carry] from LSB to MSB.`
