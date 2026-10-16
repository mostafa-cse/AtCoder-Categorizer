# Problem Analysis: AtCoder-abc032_c — Columns

**Problem ID**: `AtCoder-abc032_c`  
**Contest**: `abc032`  
**Rating / Difficulty**: 1244  
**URL**: https://atcoder.jp/contests/abc032/tasks/abc032_c  
**VJudge Tag**: `[problem:AtCoder-abc032_c]`  
**Category File**: [`../categories/basics/monotonic_subarray_product_window.md`](../categories/basics/monotonic_subarray_product_window.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Two Pointers`  
- **Topic (Skill)**: `Monotonic Subarray Product Window`  

---

## 1. Problem Statement & Key Idea
Given an array S of N positive integers. Find the maximum length of a contiguous subarray whose product of elements is at most K.

**Key Idea**: If any element in the array is 0, the product of the entire array is 0 <= K, so the maximum length is N.

## 2. Core Observation & Invariant
Assuming all elements are positive (S_i >= 1), the product is monotonically increasing with the right endpoint. We can maintain a sliding window [L, R] using two pointers: multiply by S[R]; while product > K and L <= R, divide by S[L] and increment L. The window size R - L + 1 gives the maximum valid length ending at R.

## 3. Step-by-Step Algorithm
1. If any element is 0: print N and exit.
2. If K == 0: print 0 and exit.
3. Initialize L = 0, product = 1, max_len = 0.
4. For R from 0 to N - 1: product *= S[R]; while product > K and L <= R: product /= S[L], L++; max_len = max(max_len, R - L + 1).
5. Print max_len.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> s(n);
    bool has_zero = false;
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
        if (s[i] == 0) has_zero = true;
    }

    if (has_zero) {
        cout << n << "\n";
        return 0;
    }
    if (k == 0) {
        cout << 0 << "\n";
        return 0;
    }

    int max_len = 0;
    long long prod = 1;
    int l = 0;

    for (int r = 0; r < n; ++r) {
        prod *= s[r];
        while (l <= r && prod > k) {
            prod /= s[l];
            l++;
        }
        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Two pointers sliding window on strictly multiplicative monotonic chains.
- **Reusable Pattern**: `Sliding window product: prod *= A[R], while (prod > K) prod /= A[L++].`
