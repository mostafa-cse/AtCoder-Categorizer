# Problem Analysis: AtCoder-arc136_d — Without Carry

**Problem ID**: `AtCoder-arc136_d`  
**Contest**: `arc136`  
**Rating / Difficulty**: 1908  
**URL**: https://atcoder.jp/contests/arc136/tasks/arc136_d  
**VJudge Tag**: `[problem:AtCoder-arc136_d]`  
**Category File**: [`../categories/dp/base10_fast_zeta_transform_carry_free.md`](../categories/dp/base10_fast_zeta_transform_carry_free.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `SOS DP / Fast Zeta Transform`  
- **Topic (Skill)**: `Base-10 Multi-Dimensional Fast Zeta Transform / SOS DP for Carry-Free Pairs`  

---

## 1. Problem Statement & Key Idea
Given N integers A_1, ..., A_N (A_i < 10^6). Find the number of pairs (i, j) with i < j such that A_i + A_j does not produce any carry in base 10.

A_i + A_j has no carry iff for all 6 digits d, digit_d(A_i) + digit_d(A_j) <= 9, or digit_d(A_j) <= 9 - digit_d(A_i). Let comp(A_i) be the number with digits 9 - digit_d(A_i). We need the count of A_j whose digits are sub-digits of comp(A_i). This is a 6-dimensional submask sum query over base 10, solved in 6 * 10^6 operations via Fast Zeta Transform (SOS DP in base 10).

## 2. Core Observation & Invariant
Base-10 SOS DP computes multidimensional prefix sums over Cartesian product of 6 dimensions [0..9].

## 3. Step-by-Step Algorithm
1. Store frequency of each A_i in dp array of size 10^6.
2. For each dimension d in 0..5 (place value 10^d): for i = 0 to 999999: if digit < 9, dp[i + 10^d] += dp[i].
3. For each A_i, query dp[comp(A_i)]. Subtract 1 if A_i + A_i has no carry.
4. Divide the sum by 2 and print.

## 4. Complexity Analysis
- **Time Complexity**: `O(6 * 10^6 + N)`
- **Space Complexity**: `O(10^6)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1000000;
int dp[MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        dp[arr[i]]++;
    }

    // Fast Zeta Transform (SOS DP) in base 10 across 6 digits
    int p10 = 1;
    for (int d = 0; d < 6; ++d) {
        for (int i = 0; i < MAX; ++i) {
            if ((i / p10) % 10 < 9) {
                dp[i + p10] += dp[i];
            }
        }
        p10 *= 10;
    }

    auto get_comp = [](int x) {
        int comp = 0;
        int p = 1;
        for (int d = 0; d < 6; ++d) {
            int digit = (x / p) % 10;
            comp += (9 - digit) * p;
            p *= 10;
        }
        return comp;
    };

    long long total_pairs = 0;
    for (int i = 0; i < n; ++i) {
        int comp = get_comp(arr[i]);
        int count = dp[comp];
        bool self_ok = true;
        int temp = arr[i];
        while (temp > 0) {
            if ((temp % 10) * 2 >= 10) {
                self_ok = false;
                break;
            }
            temp /= 10;
        }
        if (self_ok) {
            count--;
        }
        total_pairs += count;
    }

    cout << total_pairs / 2 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Multi-dimensional Fast Zeta Transform / SOS DP generalized to base 10.
- **Reusable Pattern**: `Base-10 SOS DP: Iterate digit positions d, add dp[i] to dp[i + 10^d] for digit < 9.`
