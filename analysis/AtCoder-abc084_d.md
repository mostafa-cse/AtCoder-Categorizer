# Problem Analysis: AtCoder-abc084_d — 2017-like Number

**Problem ID**: `AtCoder-abc084_d`  
**Contest**: `abc084`  
**Rating / Difficulty**: 980  
**URL**: https://atcoder.jp/contests/abc084/tasks/abc084_d  
**VJudge Tag**: `[problem:AtCoder-abc084_d]`  
**Category File**: [`../categories/number_theory/sieve_prefix_query_filter.md`](../categories/number_theory/sieve_prefix_query_filter.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Sieve & Prefix Sums`  
- **Topic (Skill)**: `Sieve of Eratosthenes + Prefix Sum Query Filtering`  

---

## 1. Problem Statement & Key Idea
An odd number N is '2017-like' if both N and (N + 1) / 2 are prime. Answer Q queries: count 2017-like numbers in range [l, r] (l, r <= 10^5, Q <= 10^5).

**Key Idea**: Precompute primality up to 10^5 using Sieve of Eratosthenes in O(M log log M), then build a 1D prefix sum array of 2017-like indicators to answer each query in O(1).

## 2. Core Observation & Invariant
A number N is 2017-like if N % 2 == 1, is_prime[N], and is_prime[(N + 1) / 2]. Store a binary array is_2017[N]. Its prefix sum array pref[x] = sum_{i=1}^x is_2017[i] answers queries via pref[r] - pref[l - 1].

## 3. Step-by-Step Algorithm
1. Compute is_prime array up to 100,000 using Sieve of Eratosthenes.
2. For each i from 1 to 100,000: if i % 2 == 1 and is_prime[i] and is_prime[(i + 1) / 2], set is_2017[i] = 1.
3. Compute prefix sums: pref[i] = pref[i - 1] + is_2017[i].
4. For each query (l, r): print pref[r] - pref[l - 1].

## 4. Complexity Analysis
- **Time Complexity**: `O(MAX log log MAX + Q)`
- **Space Complexity**: `O(MAX)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<bool> is_prime(MAX + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= MAX; ++p) {
        if (is_prime[p]) {
            for (int i = p * p; i <= MAX; i += p) {
                is_prime[i] = false;
            }
        }
    }

    vector<int> is_2017(MAX + 1, 0);
    for (int i = 1; i <= MAX; ++i) {
        if (i % 2 == 1 && is_prime[i] && is_prime[(i + 1) / 2]) {
            is_2017[i] = 1;
        }
    }

    vector<int> pref(MAX + 1, 0);
    for (int i = 1; i <= MAX; ++i) {
        pref[i] = pref[i - 1] + is_2017[i];
    }

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << pref[r] - pref[l - 1] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining Sieve precomputation with prefix sum range queries.
- **Reusable Pattern**: `Static property range queries: Sieve -> Indicator Array -> Prefix Sum -> O(1) Query.`
