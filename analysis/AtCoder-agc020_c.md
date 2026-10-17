# Problem Analysis: AtCoder-agc020_c — C. Median Sum

**Problem ID**: `AtCoder-agc020_c`  
**Contest**: `agc020`  
**Rating / Difficulty**: 2259  
**URL**: https://atcoder.jp/contests/agc020/tasks/agc020_c  
**VJudge Tag**: `[problem:AtCoder-agc020_c]`  
**Category File**: [`../categories/dp/subset_sum_complement_symmetry_bitset_median.md`](../categories/dp/subset_sum_complement_symmetry_bitset_median.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Subset Sum Optimizations`  

---

## 1. Problem Statement & Key Idea
Given $N$ integers $A_1, \dots, A_N$, consider the $2^N - 1$ sums of non-empty subsequences. Find the median of this sorted list.

## 2. Core Observation & Invariant
Complementary subset symmetry: each subset $X$ has complement $\bar{X}$ with $\text{sum}(X) + \text{sum}(\bar{X}) = \sum A$. This pairs up the $2^N$ subsets into complementary pairs summing to $T = \sum A$. The upper half of the subset sums consists of the larger element of each pair, all $\ge \lceil T / 2 \rceil$. The median of all non-empty subsets is therefore the smallest achievable subset sum $\ge \lceil T / 2 \rceil$, solved via `std::bitset`.

## 3. Step-by-Step Algorithm
1. Initialize `bitset<4000005> bs` with `bs[0] = 1`.
2. For each element $a \in A$, update `bs |= (bs << a)`.
3. Find the smallest index $s \ge \lceil (\sum A) / 2 \rceil$ such that `bs[s] == 1`.
4. Output $s$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \cdot \sum A / 64)`
- **Space Complexity**: `O(\sum A / 8)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <bitset>
#include <numeric>

using namespace std;

const int MAX_SUM = 4000005;
bitset<MAX_SUM> bs;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    int total_sum = 0;
    bs[0] = 1;

    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a;
        total_sum += a;
        bs |= (bs << a);
    }

    int half = (total_sum + 1) / 2;
    for (int s = half; s <= total_sum; ++s) {
        if (bs[s]) {
            cout << s << "\n";
            break;
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
