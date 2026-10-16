# Problem Analysis: AtCoder-typical90_ad — K Factors

**Problem ID**: `AtCoder-typical90_ad`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 030)  
**Rating / Difficulty**: 1400 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ad  
**VJudge Tag**: `[problem:AtCoder-typical90_ad]`  
**Category File**: [`../categories/number_theory/modified_sieve.md`](../categories/number_theory/modified_sieve.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Prime Numbers & Sieve`  
- **Topic (Skill)**: `Modified Sieve of Eratosthenes / Prime Factor Multiplicity`  

---

## 1. Problem Statement & Key Idea
Count integers in the range [2, N] (N <= 10^7) that have at least K distinct prime factors.

**Core Idea**: Generalize the Sieve of Eratosthenes: instead of marking compositeness, count prime factors.

## 2. Core Observation & Invariant
Maintain count array factor_count[x]. Whenever an unvisited number i is encountered (factor_count[i] == 0, meaning i is prime), increment factor_count[m] for all multiples m = i, 2i, 3i, ... in O(N log log N) total time.

## 3. Step-by-Step Algorithm
1. vector<int> cnt(N + 1, 0).
2. For i from 2 to N: if cnt[i] == 0: for j from i to N step i: cnt[j]++.
3. Count integers x in 2..N with cnt[x] >= K.

## 4. Complexity Analysis
Time: O(N log log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> cnt(n + 1, 0);
    for (int i = 2; i <= n; ++i) {
        if (cnt[i] == 0) { // i is prime
            for (int j = i; j <= n; j += i) {
                cnt[j]++;
            }
        }
    }

    int ans = 0;
    for (int i = 2; i <= n; ++i) {
        if (cnt[i] >= k) ans++;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Sieve of Eratosthenes harmonic prime factor accumulation.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Adapting prime sieves to accumulate arithmetic functions across multiples in O(N log log N).
- **Reusable Pattern**: `Modified Sieve of Eratosthenes for Arithmetic Functions.`

---
Back to [Modified Sieve of Eratosthenes / Prime Factor Multiplicity](../categories/number_theory/modified_sieve.md) | [Categories Directory](../categories/README.md)