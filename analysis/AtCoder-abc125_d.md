# Problem Analysis: AtCoder-abc125_d — Flipping Signs

**Problem ID**: `AtCoder-abc125_d`  
**Contest**: `abc125`  
**Rating / Difficulty**: 833  
**URL**: https://atcoder.jp/contests/abc125/tasks/abc125_d  
**VJudge Tag**: `[problem:AtCoder-abc125_d]`  
**Category File**: [`../categories/math/sign_flip_parity_invariant.md`](../categories/math/sign_flip_parity_invariant.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Invariants & Parity`  
- **Topic (Skill)**: `Sign Flip Parity Invariant`  

---

## 1. Problem Statement & Key Idea
Given an array A of N integers. You can choose adjacent elements A[i] and A[i+1] and multiply both by -1 any number of times. Maximize the sum of elements of A.

**Key Idea**: Multiplying two adjacent elements by -1 preserves the parity of the count of negative numbers: count changes by +2, 0, or -2.

## 2. Core Observation & Invariant
Moreover, because negative signs can be moved along adjacent pairs to any two arbitrary positions, we can flip any pair of elements (i, j). If the total number of negative numbers is even, ALL elements can be made non-negative (sum = sum |A_i|). If odd, exactly one element must remain negative; to maximize the sum, we choose the element with minimum absolute value (sum = sum |A_i| - 2 * min |A_i|).

## 3. Step-by-Step Algorithm
1. Compute total_abs = sum |A_i|, min_abs = min |A_i|, and count negative elements.
2. If negative count is even, output total_abs.
3. If negative count is odd, output total_abs - 2 * min_abs.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long sum_abs = 0;
    long long min_abs = 2e9 + 7;
    int neg_count = 0;

    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        if (a < 0) neg_count++;
        long long abs_val = abs(a);
        sum_abs += abs_val;
        min_abs = min(min_abs, abs_val);
    }

    if (neg_count % 2 == 0) {
        cout << sum_abs << "\n";
    } else {
        cout << sum_abs - 2 * min_abs << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Parity invariant and sign propagation on linear chains.
- **Reusable Pattern**: `Even negative count -> sum |A_i|; Odd negative count -> sum |A_i| - 2 * min |A_i|.`
