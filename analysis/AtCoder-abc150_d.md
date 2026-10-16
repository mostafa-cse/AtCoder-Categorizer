# Problem Analysis: AtCoder-abc150_d — Semi Common Multiple

**Problem ID**: `AtCoder-abc150_d`  
**Contest**: `abc150`  
**Rating / Difficulty**: 1534  
**URL**: https://atcoder.jp/contests/abc150/tasks/abc150_d  
**VJudge Tag**: `[problem:AtCoder-abc150_d]`  
**Category File**: [`../categories/number_theory/two_adic_lcm_odd_multiples.md`](../categories/number_theory/two_adic_lcm_odd_multiples.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `LCM & Divisibility`  
- **Topic (Skill)**: `2-adic Valuation & Odd Multiple LCM Condition`  

---

## 1. Problem Statement & Key Idea
Given an array A of even positive integers. Find the number of integers X in 1..M such that for every i, X = A_i * (p + 0.5) for some non-negative integer p.

**Key Insight**: X = (A_i / 2) * (2p + 1). Thus, X must be an ODD multiple of each a'_i = A_i / 2. This requires all a'_i to have the exact same 2-adic valuation (power of 2).

## 2. Core Observation & Invariant
If any two a'_i differ in their highest power of 2 dividing them, no such X can exist (output 0). Otherwise, X must be an odd multiple of L = LCM(a'_1, ..., a'_N). The count of odd multiples <= M is ((M / L) + 1) / 2.

## 3. Step-by-Step Algorithm
1. Divide each element of A by 2 to get a'_i.
2. Check that all a'_i have identical __builtin_ctzll(a'_i). If not, print 0.
3. Compute L = LCM(a'_1, ..., a'_N). If at any point L > M, print 0.
4. Print ((M / L) + 1) / 2.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max A))`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    int common_ctz = -1;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] /= 2;
        int c = __builtin_ctzll(a[i]);
        if (common_ctz == -1) common_ctz = c;
        else if (common_ctz != c) {
            cout << 0 << "\n";
            return 0;
        }
    }

    long long L = 1;
    for (int i = 0; i < n; ++i) {
        long long g = gcd(L, a[i]);
        __int128 next_L = (__int128)L * (a[i] / g);
        if (next_L > m) {
            cout << 0 << "\n";
            return 0;
        }
        L = next_L;
    }

    cout << (m / L + 1) / 2 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 2-adic valuation consistency check and odd-multiple LCM counting.
- **Reusable Pattern**: `Odd Multiple of Elements: check equal 2-adic valuations, compute LCM, count odd multiples ((M/L)+1)/2.`
