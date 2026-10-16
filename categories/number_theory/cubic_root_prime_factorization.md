# 📖 Cubic-Root Prime Factorization (N = p^2 * q)

- **Tag / Domain**: `Number Theory`
- **Subtopic**: `Prime Numbers`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Exploiting asymmetric algebraic power distributions in prime factorizations to bound search boundaries to O(N^(1/3)).

---

## 🏆 Curated High-Value Problems

### 1. Happy New Year 2023 (`[problem:AtCoder-abc284_d]`)

- **Role**: *O(N^(1/3)) Asymmetric Prime Search*
- **Rating**: `1050` | **Contest**: [`abc284`](https://atcoder.jp/contests/abc284/tasks/abc284_d)
- **Full Analysis**: [AtCoder-abc284_d Analysis](../../analysis/AtCoder-abc284_d.md)

#### Problem Statement & Task
Given N = p^2 * q where p and q are prime and N <= 9 * 10^18, find primes p and q.

#### Core Invariant & Observation
Testing trial divisors up to N^(1/3) is guaranteed to find either p or q in a few million operations.

#### Algorithmic Formulation
1. Loop d from 2 up to 3 * 10^6:
   If N % d == 0: if N % (d * d) == 0 -> p = d, q = N / (d * d); else p = isqrt(N / d), q = d; break.
2. Output p and q.

**Complexity**: `Time: O(N^(1/3)), Space: O(1).`  
**Editorial Alignment**: Cubic root trial division for asymmetric prime powers.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Exploiting asymmetric algebraic power structures to bound search space to N^(1/3) rather than sqrt(N).
- **Reusable Pattern**: `N^(1/3) trial division for p^2 * q factorization.`

---

[Back to Number Theory Index](README.md) | [Back to Master Categories](../../README.md)
