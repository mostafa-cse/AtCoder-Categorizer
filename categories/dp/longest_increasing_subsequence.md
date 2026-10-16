# 📖 Longest Bitonic Subsequence via Dual LIS

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Classic DP`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Longest Bitonic Subsequence via Dual LIS**.

---

## 🏆 Curated High-Value Problems

### Chimera (`[problem:AtCoder-typical90_bh]`)

- **Role**: *Longest Bitonic Subsequence via Dual LIS*
- **Rating**: `1600` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bh)
- **Full Analysis**: [AtCoder-typical90_bh Analysis](../../analysis/AtCoder-typical90_bh.md)

#### Problem Statement & Task
Given array A of length N (N <= 3 * 10^5), find the maximum length of a bitonic subsequence (strictly increases up to peak, then strictly decreases).

#### Core Invariant & Observation
Compute standard O(N log N) patience sorting LIS from left to right (inc[i]), and reverse LIS from right to left (dec[i]). Maximize inc[i] + dec[i] - 1 over all i.

#### Algorithmic Formulation
1. Compute inc[i] = length of LIS ending at i using binary search.
2. Reverse A, compute dec[i] = length of LDS starting at i.
3. Return max_{i} (inc[i] + dec[i] - 1).

**Complexity**: `Time: O(N log N), Space: O(N).`  
**Editorial Alignment**: Dual Longest Increasing Subsequence with binary search patience sorting.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Bidirectional LIS decomposition, patience sorting with std::lower_bound, and bitonic subsequence optimization.
- **Reusable Pattern**: `Dual LIS Bitonic Peak Subsequence.`

---

[Back to Master Categories](../../README.md)
