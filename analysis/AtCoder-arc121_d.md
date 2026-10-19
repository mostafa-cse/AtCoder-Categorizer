# Problem Analysis: AtCoder-arc121_d — D - 1 or 2

**Problem ID**: `AtCoder-arc121_d`  
**Contest**: `arc121`  
**Rating / Difficulty**: 2784  
**URL**: https://atcoder.jp/contests/arc121/tasks/arc121_d  
**VJudge Tag**: `[problem:AtCoder-arc121_d]`  
**Category File**: [`../categories/basics/candy_tastiness_extreme_pairing_two_pointers.md`](../categories/basics/candy_tastiness_extreme_pairing_two_pointers.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Two Pointers`  

---

## 1. Problem Statement & Key Idea
You have N candies with tastiness values A_1, ..., A_N. In each step, you can eat either 1 candy or 2 candies. Minimize max(step_sum) - min(step_sum) across all steps.

## 2. Core Observation & Invariant
Eating 1 candy of value x is equivalent to pairing x with a phantom candy of value 0. If we add Z phantom zeros such that N + Z = 2M is even, every step is a pair of candies. To minimize max(pair_sum) - min(pair_sum) in an array of 2M numbers, the optimal pairing is always the extreme pairing: sort the array and pair the i-th smallest with the i-th largest using two pointers. Since N <= 5000, we can iterate over the number of zeros Z in 0..N such that N + Z is even, pair via two pointers, and find the minimum span.

## 3. Step-by-Step Algorithm
1. 1. Sort the given candy values A.
2. 2. Iterate the number of zeros Z from 0 to N such that (N + Z) is even.
3. 3. Create an array B combining A and Z zeros in sorted order.
4. 4. For M = len(B) / 2, compute pair sums B[i] + B[2M - 1 - i] for all i in 0..M-1.
5. 5. Find max_sum - min_sum for this Z.
6. 6. Output the minimum difference found across all valid Z.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    vector<long long> neg, pos_zero;
    for (long long x : A) {
        if (x < 0) neg.push_back(x);
        else pos_zero.push_back(x);
    }

    int sz_neg = neg.size();
    int sz_pos = pos_zero.size();

    long long ans = -1;

    for (int K = (N + 1) / 2; K <= N; ++K) {
        int num_zeros = 2 * K - N;

        auto get_elem = [&](int idx) -> long long {
            if (idx < sz_neg) return neg[idx];
            idx -= sz_neg;
            if (idx < num_zeros) return 0;
            idx -= num_zeros;
            return pos_zero[idx];
        };

        long long mx = -3e18;
        long long mn = 3e18;

        for (int i = 0; i < K; ++i) {
            long long s = get_elem(i) + get_elem(2 * K - 1 - i);
            if (s > mx) mx = s;
            if (s < mn) mn = s;
        }

        long long diff = mx - mn;
        if (ans == -1 || diff < ans) {
            ans = diff;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
