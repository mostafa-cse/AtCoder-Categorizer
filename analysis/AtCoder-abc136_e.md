# Problem Analysis: AtCoder-abc136_e — Max GCD

**Problem ID**: `AtCoder-abc136_e`  
**Contest**: `abc136`  
**Rating / Difficulty**: 1670  
**URL**: https://atcoder.jp/contests/abc136/tasks/abc136_e  
**VJudge Tag**: `[problem:AtCoder-abc136_e]`  
**Category File**: [`../categories/number_theory/sum_invariant_array_gcd_divisors.md`](../categories/number_theory/sum_invariant_array_gcd_divisors.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Divisors`  
- **Topic (Skill)**: `Sum-Invariant Divisor Analysis on Array GCD`  

---

## 1. Problem Statement & Key Idea
An array A of N positive integers. In one operation, choose two elements, increment one and decrement the other. Perform at most K operations to maximize the greatest common divisor of all elements.

**Key Insight**: Each operation increments one element and decrements another, so the sum S = sum_{i=1}^N A_i is strictly invariant! Thus, the final GCD must divide S.

## 2. Core Observation & Invariant
Find all divisors d of S. For a divisor d to be achievable in <= K operations: compute remainders r_i = A_i % d. Sort r_i. To make all elements multiples of d with zero net change, we decrease the first p elements by r_i and increase the remaining N - p elements by d - r_i. The operations needed is sum_{i=0}^{p-1} r_i where sum_{i=0}^{p-1} r_i == sum_{i=p}^{N-1} (d - r_i).

## 3. Step-by-Step Algorithm
1. Compute total sum S = sum A_i.
2. Find all divisors d of S and sort descending.
3. For each divisor d:
4.   Compute r_i = A_i % d and sort ascending.
5.   Let sum_rem = sum r_i. Number of elements to reduce is p = N - (sum_rem / d).
6.   Ops needed = sum_{i=0}^{p-1} r_i.
7.   If ops <= K, return d (first and largest valid d).
8. Print 1.

## 4. Complexity Analysis
- **Time Complexity**: `O(d(S) * N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_sum += a[i];
    }

    vector<long long> divisors;
    for (long long d = 1; d * d <= total_sum; ++d) {
        if (total_sum % d == 0) {
            divisors.push_back(d);
            if (d * d != total_sum) {
                divisors.push_back(total_sum / d);
            }
        }
    }
    sort(divisors.rbegin(), divisors.rend());

    for (long long d : divisors) {
        vector<long long> r(n);
        long long sum_rem = 0;
        for (int i = 0; i < n; ++i) {
            r[i] = a[i] % d;
            sum_rem += r[i];
        }
        sort(r.begin(), r.end());

        int p = n - (sum_rem / d);
        long long ops = 0;
        for (int i = 0; i < p; ++i) {
            ops += r[i];
        }

        if (ops <= k) {
            cout << d << "\n";
            return 0;
        }
    }

    cout << 1 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Invariant sum divisor checking and greedy remainder balance pairing.
- **Reusable Pattern**: `Array Operation Invariant GCD: GCD divides sum(A); check remainders r_i sorted against K.`
