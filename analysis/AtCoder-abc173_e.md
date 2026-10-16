# Problem Analysis: AtCoder-abc173_e — Multiplication 4

**Problem ID**: `AtCoder-abc173_e`  
**Contest**: `abc173`  
**Rating / Difficulty**: 1607  
**URL**: https://atcoder.jp/contests/abc173/tasks/abc173_e  
**VJudge Tag**: `[problem:AtCoder-abc173_e]`  
**Category File**: [`../categories/basics/greedy_max_product_signed_k.md`](../categories/basics/greedy_max_product_signed_k.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy Algorithms`  
- **Topic (Skill)**: `Greedy Maximum Product of K Integers with Signed Extremum`  

---

## 1. Problem Statement & Key Idea
Given an array A of N integers. Select exactly K numbers such that their product is maximized. Output the maximum product modulo 10^9 + 7.

**Key Insight**: Handle sign casework carefully: if all elements must yield a negative product (e.g. all numbers negative and K is odd), pick the K numbers with the SMALLEST absolute values. Otherwise, greedily pair up two positives vs two negatives by larger product.

## 2. Core Observation & Invariant
Separate A into positive numbers pos and negative numbers neg. If product can be non-negative: if K is odd, take the largest positive first, reducing to even K. Then compare pos[i]*pos[i+1] vs neg[j]*neg[j+1] and pick the larger pair.

## 3. Step-by-Step Algorithm
1. Sort positive numbers descending, negative numbers ascending.
2. Check if max product must be negative: if (all non-positive and K is odd) or (N == K and count(neg) is odd):
3.   Sort all elements by absolute value ascending.
4.   Product of first K elements modulo MOD (handling negative modulo).
5. Otherwise, product is >= 0:
6.   If K is odd: take largest positive, K--.
7.   While K >= 2:
8.     Compare product of next 2 positives vs next 2 negatives.
9.     Pick the pair with larger product.
10.     K -= 2.
11. Print final product modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    vector<long long> pos, neg;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (a[i] >= 0) pos.push_back(a[i]);
        else neg.push_back(a[i]);
    }

    sort(pos.rbegin(), pos.rend());
    sort(neg.begin(), neg.end()); // Most negative first

    bool must_be_negative = false;
    if (pos.empty() && k % 2 == 1) must_be_negative = true;
    if (n == k && neg.size() % 2 == 1) must_be_negative = true;

    if (must_be_negative) {
        // Pick k elements with smallest absolute values
        sort(a.begin(), a.end(), [](long long x, long long y) {
            return abs(x) < abs(y);
        });
        long long prod = 1;
        for (int i = 0; i < k; ++i) {
            prod = (prod * ((a[i] % MOD + MOD) % MOD)) % MOD;
        }
        cout << prod << "\n";
        return 0;
    }

    long long prod = 1;
    size_t pi = 0, ni = 0;

    if (k % 2 == 1) {
        prod = (prod * pos[pi++]) % MOD;
        k--;
    }

    while (k > 0) {
        long long p_pair = (pi + 1 < pos.size() ? pos[pi] * pos[pi + 1] : -1);
        long long n_pair = (ni + 1 < neg.size() ? neg[ni] * neg[ni + 1] : -1);

        if (p_pair >= n_pair) {
            prod = (prod * (pos[pi] % MOD)) % MOD;
            prod = (prod * (pos[pi + 1] % MOD)) % MOD;
            pi += 2;
        } else {
            prod = (prod * ((neg[ni] % MOD + MOD) % MOD)) % MOD;
            prod = (prod * ((neg[ni + 1] % MOD + MOD) % MOD)) % MOD;
            ni += 2;
        }
        k -= 2;
    }

    cout << prod << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Signed integer product maximization with two-pointer paired greedy selection.
- **Reusable Pattern**: `Max Product of K Signed: test if negative unavoidable; else take odd positive + greedily pair negatives.`
