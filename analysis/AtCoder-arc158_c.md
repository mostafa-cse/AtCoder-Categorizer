# Problem Analysis: AtCoder-arc158_c — All Pair Digit Sums

**Problem ID**: `AtCoder-arc158_c`  
**Contest**: `arc158`  
**Rating / Difficulty**: 1875  
**URL**: https://atcoder.jp/contests/arc158/tasks/arc158_c  
**VJudge Tag**: `[problem:AtCoder-arc158_c]`  
**Category File**: [`../categories/number_theory/all_pair_digit_sums_carry_reduction.md`](../categories/number_theory/all_pair_digit_sums_carry_reduction.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Digit Sum Invariants`  
- **Topic (Skill)**: `Carry Reduction Identity for All-Pair Digit Sums`  

---

## 1. Problem Statement & Key Idea
Given an array A of N positive integers (A_i <= 10^{15}). Let f(x) be the sum of digits of x. Find sum_{i=1}^N sum_{j=1}^N f(A_i + A_j).

**Key Insight**: The key mathematical identity is: f(A + B) = f(A) + f(B) - 9 * (number of carries when adding A and B). Summing over all N^2 pairs, the base sum is 2N * sum f(A_i). Carries at digit 10^k occur iff (A_i mod 10^k) + (A_j mod 10^k) >= 10^k.

## 2. Core Observation & Invariant
For each k in 1..15, extract r_i = A_i % 10^k, sort r, and count pairs with r_i + r_j >= 10^k using two pointers in O(N).

## 3. Step-by-Step Algorithm
1. Compute base_sum = 2 * N * sum f(A_i).
2. total_carries = 0.
3. pow10 = 10.
4. For k = 1 to 15:
5.   Extract r_i = A_i % pow10 for all i.
6.   Sort r.
7.   Count pairs (i, j) with r_i + r_j >= pow10 using two pointers.
8.   total_carries += count.
9.   pow10 *= 10.
10. Print base_sum - 9 * total_carries.

## 4. Complexity Analysis
- **Time Complexity**: `O(15 * N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long digit_sum(long long n) {
    long long s = 0;
    while (n > 0) {
        s += n % 10;
        n /= 10;
    }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long total_digit_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_digit_sum += digit_sum(a[i]);
    }

    long long base_ans = 2LL * n * total_digit_sum;
    long long total_carries = 0;

    long long pow10 = 10;
    for (int k = 1; k <= 15; ++k) {
        vector<long long> r(n);
        for (int i = 0; i < n; ++i) {
            r[i] = a[i] % pow10;
        }
        sort(r.begin(), r.end());

        int ptr = n - 1;
        long long carry_count = 0;
        for (int i = 0; i < n; ++i) {
            while (ptr >= 0 && r[i] + r[ptr] >= pow10) {
                ptr--;
            }
            carry_count += (n - 1 - ptr);
        }

        total_carries += carry_count;
        if (k < 15) pow10 *= 10;
    }

    cout << base_ans - 9LL * total_carries << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Digit sum arithmetic reduction through modular carry counting.
- **Reusable Pattern**: `Carry Formula for Digit Sums: f(A + B) = f(A) + f(B) - 9 * carries.`
