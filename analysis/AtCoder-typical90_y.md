# Problem Analysis: AtCoder-typical90_y — Digit Product Equation

**Problem ID**: `AtCoder-typical90_y`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 025)  
**Rating / Difficulty**: 2400 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_y  
**VJudge Tag**: `[problem:AtCoder-typical90_y]`  
**Category File**: [`../categories/math/search_space_invariants.md`](../categories/math/search_space_invariants.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Search Space Invariants & Bounds`  
- **Topic (Skill)**: `Digit Product Value Compression & Inverse Search`  

---

## 1. Problem Statement & Key Idea
Find the number of positive integers m <= N (N <= 10^11) satisfying m - f(m) = B, where f(m) is the product of decimal digits of m.

**Core Idea**: The equation rearranges to m = B + f(m). Instead of iterating 10^11 values of m, iterate the possible values of digit products f(m)!

## 2. Core Observation & Invariant
For numbers up to 11 digits, f(m) is a product of digits from 2 to 9. The number of distinct digit products for 11 digits is at most 44,460! Test each product P: let m = B + P, then check if m <= N and f(m) == P.

## 3. Step-by-Step Algorithm
1. Generate all multisets of up to 11 digits from {0, 1, 2, ..., 9} and collect unique product values P.
2. Also include P = 0.
3. For each unique product P:
   - m = B + P
   - if m <= N and digit_product(m) == P: count++.
4. Output count.

## 4. Complexity Analysis
Time: O(DistinctProducts * 11) ≈ 4.5 * 10^4 * 11 ops (< 0.05s), Space: O(DistinctProducts).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

long long digit_product(long long m) {
    long long prod = 1;
    while (m > 0) {
        prod *= (m % 10);
        m /= 10;
    }
    return prod;
}

void generate_products(int digit, int count_left, long long cur_prod, set<long long>& products) {
    products.insert(cur_prod);
    if (digit > 9 || count_left == 0) return;

    // Option 1: do not use this digit further
    generate_products(digit + 1, count_left, cur_prod, products);

    // Option 2: use this digit
    generate_products(digit, count_left - 1, cur_prod * digit, products);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, b;
    if (!(cin >> n >> b)) return 0;

    set<long long> products;
    products.insert(0); // For numbers containing digit 0
    generate_products(2, 11, 1, products);

    long long ans = 0;
    for (long long p : products) {
        long long m = b + p;
        if (m >= 1 && m <= n && digit_product(m) == p) {
            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Inverting the search space from m to the compact set of digit products f(m).

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Inverting equations to search over compact image spaces (reducing 10^11 to 4.5 * 10^4 states).
- **Reusable Pattern**: `Search Space Inversion / Image Enumeration.`

---
Back to [Digit Product Value Compression & Inverse Search](../categories/math/search_space_invariants.md) | [Categories Directory](../categories/README.md)