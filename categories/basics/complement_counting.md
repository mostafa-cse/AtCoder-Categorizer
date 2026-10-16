# 📖 Complement Counting via Run-Length Encoding

- **Tag / Domain**: `Basics`
- **Subtopic**: `Complement Counting & Run-Length`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Complement Counting via Run-Length Encoding**.

---

## 🏆 Curated High-Value Problems

### There are two types of characters (`[problem:AtCoder-typical90_cf]`)

- **Role**: *Complement Counting via Run-Length Encoding*
- **Rating**: `800` (★3) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_cf)
- **Full Analysis**: [AtCoder-typical90_cf Analysis](../../analysis/AtCoder-typical90_cf.md)

#### Problem Statement & Task
String S of length N with 'o' and 'x'. Count pairs (l, r) with 1 <= l < r <= N such that substring S[l..r] contains both 'o' and 'x'.

#### Core Invariant & Observation
Substrings of identical characters are subsegments within contiguous runs. Using Run-Length Encoding, a run of length L contributes L*(L - 1)/2 invalid pairs. Subtract from total pairs in O(N).

#### Algorithmic Formulation
1. Run-length encode string into block lengths L_1, L_2, ...
2. invalid = sum L_i * (L_i - 1) / 2.
3. Output N*(N - 1)/2 - invalid.

**Complexity**: `Time: O(N), Space: O(1).`  
**Editorial Alignment**: Complement counting subtracting contiguous monochromatic runs.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Complement Counting principle and Run-Length Encoding decomposition.
- **Reusable Pattern**: `Complement Counting with Run-Length Encoding.`

---

[Back to Master Categories](../../README.md)
