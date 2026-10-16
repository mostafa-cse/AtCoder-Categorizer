# Problem Analysis: AtCoder-abc197_c — ORXOR

**Problem ID**: `AtCoder-abc197_c`  
**Contest**: `abc197`  
**Rating / Difficulty**: 809  
**URL**: https://atcoder.jp/contests/abc197/tasks/abc197_c  
**VJudge Tag**: `[problem:AtCoder-abc197_c]`  
**Category File**: [`../categories/basics/bitmask_partition_splitting.md`](../categories/basics/bitmask_partition_splitting.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitmask Brute Force`  
- **Topic (Skill)**: `Bitmask Partition Enumeration / Contiguous Splitting`  

---

## 1. Problem Statement & Key Idea
Given an array A of N integers (N <= 20). Partition A into non-empty contiguous subarrays. For each subarray, compute the bitwise OR. Compute the bitwise XOR of all resulting subarray ORs. Find the minimum possible XOR sum across all valid partitions.

**Key Idea**: There are N - 1 possible boundaries between adjacent elements. With N <= 20, N - 1 <= 19, meaning there are exactly 2^(N-1) <= 524,288 possible contiguous partitions.

## 2. Core Observation & Invariant
Each partition corresponds 1-to-1 with a bitmask of length N - 1, where the i-th bit indicates whether to split between A[i] and A[i+1]. We can evaluate each partition in O(N).

## 3. Step-by-Step Algorithm
1. Iterate through mask from 0 to (1 << (N - 1)) - 1.
2. Maintain running_or = A[0] and xor_sum = 0.
3. For i from 0 to N - 2: if (mask >> i) & 1, split: xor_sum ^= running_or, running_or = A[i + 1]; else: running_or |= A[i + 1].
4. At end of array, xor_sum ^= running_or.
5. Track the minimum xor_sum over all masks.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 2^(N-1))`
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
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long min_xor = -1;
    int total_masks = 1 << (n - 1);

    for (int mask = 0; mask < total_masks; ++mask) {
        long long current_xor = 0;
        long long current_or = a[0];

        for (int i = 0; i < n - 1; ++i) {
            if ((mask >> i) & 1) {
                current_xor ^= current_or;
                current_or = a[i + 1];
            } else {
                current_or |= a[i + 1];
            }
        }
        current_xor ^= current_or;

        if (min_xor == -1 || current_xor < min_xor) {
            min_xor = current_xor;
        }
    }

    cout << min_xor << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial. Highly optimal for N <= 20.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitmask fencepost enumeration for contiguous array partitioning.
- **Reusable Pattern**: `Fencepost splitting: iterate mask in 0..(1<<(N-1))-1 to decide split points.`
