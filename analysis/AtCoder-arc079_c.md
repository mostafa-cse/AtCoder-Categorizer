# Problem Analysis: AtCoder-arc079_c — Decrease (Judge ver.)

**Problem ID**: `AtCoder-arc079_c`  
**Contest**: `arc079`  
**Rating / Difficulty**: 1745  
**URL**: https://atcoder.jp/contests/arc079/tasks/arc079_c  
**VJudge Tag**: `[problem:AtCoder-arc079_c]`  
**Category File**: [`../categories/basics/bulk_simulation_decrement_process.md`](../categories/basics/bulk_simulation_decrement_process.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Simulation / Invariant`  
- **Topic (Skill)**: `Bulk Simulation / Monotonic Invariant on Multi-Decrement Process`  

---

## 1. Problem Statement & Key Idea
Given an array A of N numbers (N <= 50). In each operation, choose an element >= N, decrease it by N, and increase all other N - 1 elements by 1. Find the total number of operations until all elements are <= N - 1.

**Key Insight**: Each operation reduces the total sum of elements by 1. When multiple elements are >= N, we can simulate them in batches (bulk decrement) where each element i performs floor(A_i / N) operations simultaneously.

## 2. Core Observation & Invariant
Since N <= 50, performing bulk operations drastically shrinks large values within a few rounds, terminating in under 100 iterations.

## 3. Step-by-Step Algorithm
1. Initialize total_ops = 0.
2. Loop:
3.   Check if all A[i] <= N - 1; if so, break.
4.   For each i, count k_i = A[i] / N.
5.   batch_ops = sum(k_i).
6.   total_ops += batch_ops.
7.   For each i: A[i] = A[i] - k_i * N + (batch_ops - k_i).
8. Print total_ops.

## 4. Complexity Analysis
- **Time Complexity**: `O(rounds * N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long total_ops = 0;

    while (true) {
        bool finished = true;
        for (int i = 0; i < n; ++i) {
            if (a[i] >= n) {
                finished = false;
                break;
            }
        }
        if (finished) break;

        vector<long long> k(n, 0);
        long long batch_ops = 0;
        for (int i = 0; i < n; ++i) {
            k[i] = a[i] / n;
            batch_ops += k[i];
        }

        total_ops += batch_ops;

        for (int i = 0; i < n; ++i) {
            a[i] = a[i] - k[i] * n + (batch_ops - k[i]);
        }
    }

    cout << total_ops << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Simulating multi-element reduction processes via bulk simultaneous quotient steps.
- **Reusable Pattern**: `Bulk Step Simulation: Batch apply k_i = A_i / N across all elements simultaneously.`
