# 📖 Modified Sieve of Eratosthenes / Prime Factor Multiplicity

- **Tag / Domain**: `Number Theory`
- **Subtopic**: `Prime Numbers & Sieve`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Modified Sieve of Eratosthenes / Prime Factor Multiplicity**.

---

## 🏆 Curated High-Value Problems

### K Factors (`[problem:AtCoder-typical90_ad]`)

- **Role**: *Modified Sieve of Eratosthenes / Prime Factor Multiplicity*
- **Rating**: `1400` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ad)
- **Full Analysis**: [AtCoder-typical90_ad Analysis](../../analysis/AtCoder-typical90_ad.md)

#### Problem Statement & Task
Count integers in the range [2, N] (N <= 10^7) that have at least K distinct prime factors.

#### Core Invariant & Observation
Maintain count array factor_count[x]. Whenever an unvisited number i is encountered (factor_count[i] == 0, meaning i is prime), increment factor_count[m] for all multiples m = i, 2i, 3i, ... in O(N log log N) total time.

#### Algorithmic Formulation
1. vector<int> cnt(N + 1, 0).
2. For i from 2 to N: if cnt[i] == 0: for j from i to N step i: cnt[j]++.
3. Count integers x in 2..N with cnt[x] >= K.

**Complexity**: `Time: O(N log log N), Space: O(N).`  
**Editorial Alignment**: Sieve of Eratosthenes harmonic prime factor accumulation.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Adapting prime sieves to accumulate arithmetic functions across multiples in O(N log log N).
- **Reusable Pattern**: `Modified Sieve of Eratosthenes for Arithmetic Functions.`

---

[Back to Master Categories](../../README.md)
