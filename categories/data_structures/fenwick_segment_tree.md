# 📖 Fenwick Tree & Segment Tree Range Queries

- **Tag / Domain**: `Data Structures (DS)`
- **Subtopic**: `Segment Tree / Fenwick Tree`
- **Total Curated Problems**: 2

---

## 💡 Topic Overview
Maintaining dynamic arrays subject to point updates and range queries in O(log N) time over monoids like XOR and maximum.

---

## 🏆 Curated High-Value Problems

### 1. Range Xor Query (`[problem:AtCoder-abc185_f]`)

- **Role**: *Point Update Range XOR with Fenwick Tree*
- **Rating**: `1150` | **Contest**: [`abc185`](https://atcoder.jp/contests/abc185/tasks/abc185_f)
- **Full Analysis**: [AtCoder-abc185_f Analysis](../../analysis/AtCoder-abc185_f.md)

#### Problem Statement & Task
Support point XOR update A[X] ^= Y and range XOR query A[L] ^ ... ^ A[R].

#### Core Invariant & Observation
Range XOR [L, R] = prefix_xor(R) ^ prefix_xor(L - 1).

#### Algorithmic Formulation
1. Build Fenwick tree with XOR combine operation.
2. Update query: fenwick.update(X, Y).
3. Range query: output fenwick.query(R) ^ fenwick.query(L - 1).

**Complexity**: `Time: O(Q log N), Space: O(N).`  
**Editorial Alignment**: Fenwick tree XOR adaptation.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Applying Fenwick tree to any invertible commutative monoid (such as XOR).
- **Reusable Pattern**: `Fenwick Tree point-update range-query.`

---

### 2. Flowers (`[problem:AtCoder-dp_q]`)

- **Role**: *Fenwick Tree Accelerated LIS*
- **Rating**: `1600` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_q)
- **Full Analysis**: [AtCoder-dp_q Analysis](../../analysis/AtCoder-dp_q.md)

#### Problem Statement & Task
Find strictly increasing subsequence of heights maximizing beauty.

#### Core Invariant & Observation
Transforming quadratic inner-loop search into dynamic range queries via data structures.

#### Algorithmic Formulation
1. Maintain Fenwick tree supporting point-update and prefix-max queries.
2. For each flower i: best = fenwick.query(h_i - 1); fenwick.update(h_i, best + a_i).
3. Return fenwick.query(N).

**Complexity**: `Time: O(N log N), Space: O(N).`  
**Editorial Alignment**: Fenwick tree / Segment tree accelerated LIS.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Transforming quadratic inner-loop search into dynamic range queries via data structures.
- **Reusable Pattern**: `BIT/Segment Tree accelerated DP.`

---

[Back to Data Structures (DS) Index](README.md) | [Back to Master Categories](../../README.md)
