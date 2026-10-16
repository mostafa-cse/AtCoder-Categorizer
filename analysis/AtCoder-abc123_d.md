# Problem Analysis: AtCoder-abc123_d — Cake 123

**Problem ID**: `AtCoder-abc123_d`  
**Contest**: `abc123`  
**Rating / Difficulty**: 1489  
**URL**: https://atcoder.jp/contests/abc123/tasks/abc123_d  
**VJudge Tag**: `[problem:AtCoder-abc123_d]`  
**Category File**: [`../categories/basics/top_k_sum_three_arrays.md`](../categories/basics/top_k_sum_three_arrays.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Priority Queue`  
- **Topic (Skill)**: `Priority Queue Top-K Sum of Three Arrays (Pruning to K)`  

---

## 1. Problem Statement & Key Idea
Three arrays A (size X), B (size Y), C (size Z) with X, Y, Z <= 1000. Find the K largest sums of the form A_i + B_j + C_k, where K <= 3000.

**Key Insight**: Notice that K <= 3000 is much smaller than X * Y * Z = 10^9. First compute all X * Y sums of A_i + B_j, sort descending, and retain only the top min(K, X * Y) sums. Then pair these top sums with C.

## 2. Core Observation & Invariant
Any sum of A_i + B_j not in the top K cannot possibly belong to the top K sums of A_i + B_j + C_k. Pruning to K elements reduces the candidate pool to K * Z <= 3 * 10^6 sums, easily sorted in O(K * Z log(K * Z)).

## 3. Step-by-Step Algorithm
1. Compute all pairwise sums ab[i * Y + j] = A[i] + B[j].
2. Sort ab in descending order and resize to min((int)ab.size(), K).
3. Compute all sums abc = ab[i] + C[j] for i in 0..|ab|-1, j in 0..Z-1.
4. Sort abc descending.
5. Print the first K elements of abc.

## 4. Complexity Analysis
- **Time Complexity**: `O(X * Y log(X * Y) + K * Z log(K * Z))`
- **Space Complexity**: `O(X * Y + K * Z)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x, y, z, k;
    if (!(cin >> x >> y >> z >> k)) return 0;

    vector<long long> a(x), b(y), c(z);
    for (int i = 0; i < x; ++i) cin >> a[i];
    for (int i = 0; i < y; ++i) cin >> b[i];
    for (int i = 0; i < z; ++i) cin >> c[i];

    vector<long long> ab;
    ab.reserve(x * y);
    for (int i = 0; i < x; ++i) {
        for (int j = 0; j < y; ++j) {
            ab.push_back(a[i] + b[j]);
        }
    }

    sort(ab.rbegin(), ab.rend());
    if ((int)ab.size() > k) ab.resize(k);

    vector<long long> abc;
    abc.reserve(ab.size() * z);
    for (long long sum_ab : ab) {
        for (int i = 0; i < z; ++i) {
            abc.push_back(sum_ab + c[i]);
        }
    }

    sort(abc.rbegin(), abc.rend());
    for (int i = 0; i < k; ++i) {
        cout << abc[i] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pruning multi-array sum spaces to K largest intermediate candidates.
- **Reusable Pattern**: `Top-K Sum of 3 Arrays: sort(A+B), take top K, then sort(top_K + C) and take top K.`
