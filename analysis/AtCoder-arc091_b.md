# Problem Analysis: AtCoder-arc091_b — Remainder Reminder

**Problem ID**: `AtCoder-arc091_b`  
**Contest**: `abc090`  
**Rating / Difficulty**: 1129  
**URL**: https://atcoder.jp/contests/abc090/tasks/arc091_b  
**VJudge Tag**: `[problem:AtCoder-arc091_b]`  
**Category File**: [`../categories/math/periodic_remainder_block_counting.md`](../categories/math/periodic_remainder_block_counting.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Periodic Arithmetic`  
- **Topic (Skill)**: `Periodic Remainder Block Counting`  

---

## 1. Problem Statement & Key Idea
Count pairs (a, b) of integers with 1 <= a, b <= N such that a % b >= K.

**Key Idea**: Iterate over b from K + 1 to N. For a fixed b, the sequence a % b is periodic with period b: values cycle through 0, 1, ..., b - 1.

## 2. Core Observation & Invariant
In each complete period of length b, the remainders >= K are K, K+1, ..., b-1 (exactly b - K values). There are floor(N / b) full periods. The remaining incomplete block has length N % b, contributing max(0LL, (N % b) - K + 1) valid values. If K == 0, subtract 1 for a = 0 (since a starts at 1).

## 3. Step-by-Step Algorithm
1. If K == 0, output N * N.
2. Initialize total = 0.
3. For b from K + 1 to N:
4.   full_blocks = N / b; rem = N % b.
5.   total += full_blocks * (b - K) + max(0LL, rem - K + 1).
6. Print total.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    if (k == 0) {
        cout << n * n << "\n";
        return 0;
    }

    long long ans = 0;
    for (long long b = k + 1; b <= n; ++b) {
        long long full = n / b;
        long long rem = n % b;
        ans += full * (b - k);
        ans += max(0LL, rem - k + 1);
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting remainder intervals across full and partial arithmetic periods.
- **Reusable Pattern**: `Periodic remainder count: (N / b) * (b - K) + max(0, N % b - K + 1).`
