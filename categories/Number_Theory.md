# 🔢 AtCoder Curriculum: Number Theory

Curated collection of high-value problems in **Number Theory** selected for teaching reusable competitive programming algorithms, structural observations, and mathematical invariants.

- **Total Curated Problems**: 2
- **Taxonomy Tier**: Tag (Domain Level)

---

## 📑 Table of Contents

- [Modular Arithmetic](#modular-arithmetic)
  - [Modular Linear Congruence / Extended Euclidean Algorithm](#modular-linear-congruence--extended-euclidean-algorithm) (1 problems)
- [Prime Numbers](#prime-numbers)
  - [Cubic-Root Prime Factorization (N = p^2 * q)](#cubic-root-prime-factorization-n--p2--q) (1 problems)

---

## Modular Arithmetic

### Modular Linear Congruence / Extended Euclidean Algorithm

#### Throne (`[problem:AtCoder-abc186_e]`)
- **Rating / Difficulty**: 1250
- **Contest**: `abc186` | [AtCoder Link](https://atcoder.jp/contests/abc186/tasks/abc186_e)
- **Detailed Analysis**: [`analysis/AtCoder-abc186_e.md`](../analysis/AtCoder-abc186_e.md)
- **Key Idea**: A piece moves K steps clockwise on a circle of size N, starting at position S. Find minimum steps to reach position 0.
- **Core Observation**: The condition is S + x * K = 0 (mod N), which rearranges to K * x = -S (mod N). This is a linear congruence ax = b (mod m). Solutions exist if and only if gcd(K, N) divides S.
- **Algorithm & Complexity**: Time: O(log(min(K, N))) per testcase, Space: O(1).
- **What This Problem Teaches**: Modular linear congruences, solvability condition via GCD divisibility, and Extended Euclidean Algorithm.
- **Reusable Pattern**: `Extended Euclidean linear congruence solver.`

---

## Prime Numbers

### Cubic-Root Prime Factorization (N = p^2 * q)

#### Happy New Year 2023 (`[problem:AtCoder-abc284_d]`)
- **Rating / Difficulty**: 1050
- **Contest**: `abc284` | [AtCoder Link](https://atcoder.jp/contests/abc284/tasks/abc284_d)
- **Detailed Analysis**: [`analysis/AtCoder-abc284_d.md`](../analysis/AtCoder-abc284_d.md)
- **Key Idea**: Given N = p^2 * q where p and q are prime and N <= 9 * 10^18, find primes p and q.
- **Core Observation**: Because N = p^2 * q, at least one of p or q must be <= N^(1/3) <= 2.15 * 10^6! Testing trial divisors up to N^(1/3) will instantly find one prime factor.
- **Algorithm & Complexity**: Time: O(N^(1/3)) per testcase, Space: O(1).
- **What This Problem Teaches**: Exploiting asymmetric algebraic power structures to bound search space to N^(1/3) rather than sqrt(N).
- **Reusable Pattern**: `N^(1/3) trial division for p^2 * q factorization.`

---
