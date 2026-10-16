# 📖 Two Pointers with Frequency Map / K-Distinct Subarray

- **Tag / Domain**: `Data Structures (DS)`
- **Subtopic**: `Two Pointers / Sliding Window`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Two Pointers with Frequency Map / K-Distinct Subarray**.

---

## 🏆 Curated High-Value Problems

### There are few types of elements (`[problem:AtCoder-typical90_ah]`)

- **Role**: *Two Pointers with Frequency Map / K-Distinct Subarray*
- **Rating**: `1250` (★4) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ah)
- **Full Analysis**: [AtCoder-typical90_ah Analysis](../../analysis/AtCoder-typical90_ah.md)

#### Problem Statement & Task
Given an array of length N (N <= 10^5) and integer K, find the maximum length of a contiguous subarray containing at most K distinct elements.

#### Core Invariant & Observation
Maintain a frequency hash map of elements in window [l, r]. Expand r; when map size exceeds K, advance l until map size <= K.

#### Algorithmic Formulation
1. Initialize l = 0, max_len = 0, map<int, int> freq.
2. For r from 0 to N - 1:
   - freq[A[r]]++
   - while freq.size() > K: freq[A[l]]--; if freq[A[l]] == 0 freq.erase(A[l]); l++
   - max_len = max(max_len, r - l + 1)
3. Output max_len.

**Complexity**: `Time: O(N log N), Space: O(N).`  
**Editorial Alignment**: Classic two-pointer sliding window maintaining distinct element count.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Two-pointer sliding window technique, dynamic frequency tracking, and shrinking left bound on constraint violation.
- **Reusable Pattern**: `Two Pointers with Frequency Map.`

---

[Back to Master Categories](../../README.md)
