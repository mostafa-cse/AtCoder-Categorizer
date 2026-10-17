# Problem Analysis: AtCoder-arc126_c — Maximize GCD

**Problem ID**: `AtCoder-arc126_c`  
**Contest**: `arc126`  
**Rating / Difficulty**: 1824  
**URL**: https://atcoder.jp/contests/arc126/tasks/arc126_c  
**VJudge Tag**: `[problem:AtCoder-arc126_c]`  
**Category File**: [`../categories/number_theory/harmonic_range_sum_max_gcd.md`](../categories/number_theory/harmonic_range_sum_max_gcd.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Harmonic Range Sum`  
- **Topic (Skill)**: `Harmonic Range Sum with Prefix Aggregates for Maximum GCD`  

---

## 1. Problem Statement & Key Idea
Given array A of N integers and K operations. In each operation, increment any element by 1. Find the maximum possible GCD of all elements.

**Key Insight**: If K is sufficient to make all A_i equal to max(A), then remaining operations can be split equally to make GCD = max(A) + floor((K - rem) / N). Otherwise, GCD g <= max(A). For each candidate g in [2, max(A)], evaluate the cost to round every A_i up to the next multiple of g using prefix sums in O(max(A) / g) harmonic sum time.

## 2. Core Observation & Invariant
Sum_{g=2}^{max(A)} max(A)/g = O(max(A) log(max(A))) ~ 3 * 10^5 * 13 ~ 4 * 10^6 operations.

## 3. Step-by-Step Algorithm
1. Let M = max(A).
2. Calculate cost to make all A_i = M. If K >= cost: print M + (K - cost) / N.
3. Precompute count and prefix sum arrays of A up to 2 * M.
4. For g = M down to 1:
5.   cost = 0;
6.   For k = 1 to ceil(M / g):
7.     l = (k - 1) * g + 1, r = k * g;
8.     cnt = count in [l, r], sum = sum in [l, r];
9.     cost += cnt * r - sum;
10.   If cost <= K: print g, break.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M log M)`
- **Space Complexity**: `O(M)`

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

    vector<long long> a(n);
    long long max_val = 0;
    long long sum_a = 0;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
        sum_a += a[i];
    }

    long long cost_to_max = max_val * n - sum_a;
    if (k >= cost_to_max) {
        long long extra = (k - cost_to_max) / n;
        cout << max_val + extra << "\n";
        return 0;
    }

    int limit = 2 * max_val;
    vector<long long> cnt(limit + 1, 0), pref_sum(limit + 1, 0);

    for (int i = 0; i < n; ++i) {
        cnt[a[i]]++;
        pref_sum[a[i]] += a[i];
    }

    for (int i = 1; i <= limit; ++i) {
        cnt[i] += cnt[i - 1];
        pref_sum[i] += pref_sum[i - 1];
    }

    for (long long g = max_val; g >= 1; --g) {
        long long cur_cost = 0;
        for (long long mult = g; mult - g < max_val; mult += g) {
            long long l = mult - g + 1;
            long long r = mult;
            long long c = cnt[r] - cnt[l - 1];
            long long s = pref_sum[r] - pref_sum[l - 1];
            cur_cost += c * mult - s;
        }

        if (cur_cost <= k) {
            cout << g << "\n";
            return 0;
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Evaluating rounding costs to multiples across all divisor candidates in harmonic time.
- **Reusable Pattern**: `Harmonic Divisor Sweep: Evaluate sum k*g - A_i via prefix sum chunks in O(M log M).`
