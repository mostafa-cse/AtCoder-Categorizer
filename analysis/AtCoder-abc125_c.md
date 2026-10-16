# Problem Analysis: AtCoder-abc125_c — GCD on Blackboard

**Problem ID**: `AtCoder-abc125_c`  
**Contest**: `abc125`  
**Rating / Difficulty**: 1197  
**URL**: https://atcoder.jp/contests/abc125/tasks/abc125_c  
**VJudge Tag**: `[problem:AtCoder-abc125_c]`  
**Category File**: [`../categories/data_structures/prefix_suffix_gcd_exclusion.md`](../categories/data_structures/prefix_suffix_gcd_exclusion.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Prefix & Suffix Arrays`  
- **Topic (Skill)**: `Prefix and Suffix GCD Arrays (Exclusion Technique)`  

---

## 1. Problem Statement & Key Idea
Given N integers A_1..A_N. Replace at most one integer with any integer you choose. Maximize the greatest common divisor of all elements in the array.

**Key Idea**: If we replace element A_i, we should set it to gcd_{j != i} A_j, which makes the new overall GCD equal to gcd(A_1, ..., A_{i-1}, A_{i+1}, ..., A_N).

## 2. Core Observation & Invariant
Precompute prefix GCD array pref[i] = gcd(pref[i-1], A[i]) and suffix GCD array suff[i] = gcd(suff[i+1], A[i]). Then the GCD of all elements except A_i is gcd(pref[i-1], suff[i+1]) in O(log(MAX)). Maximize over all 1 <= i <= N.

## 3. Step-by-Step Algorithm
1. Compute prefix GCDs: pref[i] = gcd(pref[i - 1], A[i]) for i in 1..N.
2. Compute suffix GCDs: suff[i] = gcd(suff[i + 1], A[i]) for i in N..1.
3. Initialize max_gcd = 0.
4. For i from 1 to N: max_gcd = max(max_gcd, gcd(pref[i - 1], suff[i + 1])).
5. Output max_gcd.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(MAX))`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long gcd_ll(long long a, long long b) {
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
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 2, 0);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<long long> pref(n + 2, 0);
    vector<long long> suff(n + 2, 0);

    for (int i = 1; i <= n; ++i) {
        pref[i] = gcd_ll(pref[i - 1], a[i]);
    }
    for (int i = n; i >= 1; --i) {
        suff[i] = gcd_ll(suff[i + 1], a[i]);
    }

    long long max_gcd = 0;
    for (int i = 1; i <= n; ++i) {
        long long g = gcd_ll(pref[i - 1], suff[i + 1]);
        max_gcd = max(max_gcd, g);
    }

    cout << max_gcd << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Prefix and suffix decomposition for single-element exclusion range queries.
- **Reusable Pattern**: `Exclusion query: gcd(pref[i - 1], suff[i + 1]).`
