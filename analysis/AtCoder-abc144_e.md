# Problem Analysis: AtCoder-abc144_e — Gluttony

**Problem ID**: `AtCoder-abc144_e`  
**Contest**: `abc144`  
**Rating / Difficulty**: 1449  
**URL**: https://atcoder.jp/contests/abc144/tasks/abc144_e  
**VJudge Tag**: `[problem:AtCoder-abc144_e]`  
**Category File**: [`../categories/basics/binary_search_product_allocation.md`](../categories/basics/binary_search_product_allocation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search on Answer`  
- **Topic (Skill)**: `Monotonic Binary Search on Multiplicative Work Allocation`  

---

## 1. Problem Statement & Key Idea
N team members have eating consumption rates A_i and must eat dishes with food amount F_i. Total time is max_i (A'_i * F'_i) after matching members to dishes and reducing rates A_i by at most K total operations. Minimize the maximum completion time.

**Key Insight**: Rearrangement inequality dictates pairing smallest A_i with largest F_i. Then binary search on the minimum achievable maximum product X.

## 2. Core Observation & Invariant
For a fixed target time X, member i paired with food F_i can have maximum rate floor(X / F_i). The required training operations are max(0LL, A_i - floor(X / F_i)). The check condition is monotonic in X.

## 3. Step-by-Step Algorithm
1. Sort A in ascending order and F in descending order.
2. Binary search on answer X in range [0, 10^12]:
3.   Define check(X):
4.     ops = 0.
5.     For i = 0..N-1: ops += max(0LL, A[i] - X / F[i]).
6.     Return ops <= K.
7. If check(mid) is true, high = mid, else low = mid + 1.
8. Output low.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max(A * F)))`
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

    vector<long long> a(n), f(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> f[i];

    sort(a.begin(), a.end());
    sort(f.rbegin(), f.rend());

    long long low = 0, high = 1e12;
    long long ans = high;

    auto check = [&](long long x) -> bool {
        long long ops = 0;
        for (int i = 0; i < n; ++i) {
            long long target_a = x / f[i];
            if (a[i] > target_a) {
                ops += (a[i] - target_a);
                if (ops > k) return false;
            }
        }
        return ops <= k;
    };

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Rearrangement matching combined with monotonic binary search on target minimax product.
- **Reusable Pattern**: `Minimax Product Allocation: sort ascending/descending + binary search on answer with floor division.`
