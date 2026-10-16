# 📖 Meet-in-the-Middle with Cardinality and Value Constraints

- **Tag / Domain**: `Basics`
- **Subtopic**: `Meet in the Middle`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Meet-in-the-Middle with Cardinality and Value Constraints**.

---

## 🏆 Curated High-Value Problems

### Typical Shop (`[problem:AtCoder-typical90_ay]`)

- **Role**: *Meet-in-the-Middle with Cardinality and Value Constraints*
- **Rating**: `1750` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ay)
- **Full Analysis**: [AtCoder-typical90_ay Analysis](../../analysis/AtCoder-typical90_ay.md)

#### Problem Statement & Task
N items (N <= 40) with price A_i. Choose exactly K items such that total price <= P. Count ways.

#### Core Invariant & Observation
Group subsets of half 1 by item count: list1[c] stores prices. Group subsets of half 2 by count: list2[c]. For each count c, sort list2[K - c] and use std::upper_bound to count prices <= P - price1.

#### Algorithmic Formulation
1. Split A into left (size n1 = N/2) and right (size n2 = N - n1).
2. Enumerate 2^n1 subsets -> group by count of chosen items.
3. Enumerate 2^n2 subsets -> group by count, sort each group.
4. For each count c in 0..K: for price in group1[c]: binary search count in group2[K - c] with price <= P - price.
5. Output total ways.

**Complexity**: `Time: O(2^(N/2) * (N/2) log(2^(N/2))), Space: O(2^(N/2)).`  
**Editorial Alignment**: Meet-in-the-middle splitting 40 items into 20 + 20 with cardinality-indexed binary search.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Meet-in-the-middle technique, subset generation, and cardinality-indexed binary search lookups.
- **Reusable Pattern**: `Meet-in-the-Middle with Cardinality Grouping.`

---

[Back to Master Categories](../../README.md)
