# Problem Analysis: AtCoder-typical90_cb — Let's Share Bit

**Problem ID**: `AtCoder-typical90_cb`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 080)  
**Rating / Difficulty**: 2200 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_cb  
**VJudge Tag**: `[problem:AtCoder-typical90_cb]`  
**Category File**: [`../categories/combinatorics/inclusion_exclusion.md`](../categories/combinatorics/inclusion_exclusion.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion-Exclusion Principle`  
- **Topic (Skill)**: `Inclusion-Exclusion on Bitwise Constraints`  

---

## 1. Problem Statement & Key Idea
N bitmasks A_1, ..., A_N in [0, 2^D - 1] (N <= 20, D <= 60). Count integers x in [0, 2^D - 1] such that (x & A_i) != 0 for all i.

**Core Idea**: Inclusion-Exclusion on the negated conditions: (x & A_i) == 0.

## 2. Core Observation & Invariant
For subset S of conditions, x & A_i = 0 for all i in S iff x & (OR_{i in S} A_i) == 0. Let M = OR_{i in S} A_i. The bits of x where M has 1 must be 0; remaining D - popcount(M) bits can be chosen freely (2^(D - popcount(M)) choices).

## 3. Step-by-Step Algorithm
1. Loop mask from 0 to 2^N - 1.
2. M = OR of A_i for i where mask has bit i.
3. ways = 1ULL << (D - popcount(M)).
4. If popcount(mask) is odd: ans -= ways; else ans += ways.
5. Output ans.

## 4. Complexity Analysis
Time: O(N * 2^N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d;
    if (!(cin >> n >> d)) return 0;

    vector<unsigned long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    int total_subsets = 1 << n;

    for (int mask = 0; mask < total_subsets; ++mask) {
        unsigned long long combined_or = 0;
        int subset_size = 0;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                subset_size++;
                combined_or |= a[i];
            }
        }

        int fixed_zero_bits = __builtin_popcountll(combined_or);
        int free_bits = d - fixed_zero_bits;
        long long ways = (1LL << free_bits);

        if (subset_size % 2 == 1) {
            ans -= ways;
        } else {
            ans += ways;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Inclusion-Exclusion principle on bitwise OR condition negation.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Inclusion-Exclusion Principle, bitwise independence, and bitmask subset iteration.
- **Reusable Pattern**: `Inclusion-Exclusion on Bitwise Constraints.`

---
Back to [Inclusion-Exclusion on Bitwise Constraints](../categories/combinatorics/inclusion_exclusion.md) | [Categories Directory](../categories/README.md)