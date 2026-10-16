# 📖 Digit Product Value Compression & Inverse Search

- **Tag / Domain**: `Math`
- **Subtopic**: `Search Space Invariants & Bounds`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Digit Product Value Compression & Inverse Search**.

---

## 🏆 Curated High-Value Problems

### Digit Product Equation (`[problem:AtCoder-typical90_y]`)

- **Role**: *Digit Product Value Compression & Inverse Search*
- **Rating**: `2400` (★7) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_y)
- **Full Analysis**: [AtCoder-typical90_y Analysis](../../analysis/AtCoder-typical90_y.md)

#### Problem Statement & Task
Find the number of positive integers m <= N (N <= 10^11) satisfying m - f(m) = B, where f(m) is the product of decimal digits of m.

#### Core Invariant & Observation
For numbers up to 11 digits, f(m) is a product of digits from 2 to 9. The number of distinct digit products for 11 digits is at most 44,460! Test each product P: let m = B + P, then check if m <= N and f(m) == P.

#### Algorithmic Formulation
1. Generate all multisets of up to 11 digits from {0, 1, 2, ..., 9} and collect unique product values P.
2. Also include P = 0.
3. For each unique product P:
   - m = B + P
   - if m <= N and digit_product(m) == P: count++.
4. Output count.

**Complexity**: `Time: O(DistinctProducts * 11) ≈ 4.5 * 10^4 * 11 ops (< 0.05s), Space: O(DistinctProducts).`  
**Editorial Alignment**: Inverting the search space from m to the compact set of digit products f(m).  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Inverting equations to search over compact image spaces (reducing 10^11 to 4.5 * 10^4 states).
- **Reusable Pattern**: `Search Space Inversion / Image Enumeration.`

---

[Back to Master Categories](../../README.md)
