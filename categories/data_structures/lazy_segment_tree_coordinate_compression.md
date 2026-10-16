# 📖 Dynamic Coordinate Compression + Lazy Segment Tree

- **Tag / Domain**: `Data Structures (DS)`
- **Subtopic**: `Segment Tree / Fenwick Tree`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Dynamic Coordinate Compression + Lazy Segment Tree**.

---

## 🏆 Curated High-Value Problems

### Long Bricks (`[problem:AtCoder-typical90_ac]`)

- **Role**: *Dynamic Coordinate Compression + Lazy Segment Tree*
- **Rating**: `1750` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ac)
- **Full Analysis**: [AtCoder-typical90_ac Analysis](../../analysis/AtCoder-typical90_ac.md)

#### Problem Statement & Task
W-wide ground (W <= 10^9). N bricks fall in order. Brick i spans [L_i, R_i], lands on top of existing bricks in that range, and levels that range to max_height + 1. Output landing height of each brick.

#### Core Invariant & Observation
Since W <= 10^9 is large but N <= 10^5, coordinate compress all 2N interval endpoints {L_i, R_i} into an array of size <= 2 * 10^5.

#### Algorithmic Formulation
1. Collect and coordinate-compress all L_i and R_i.
2. Build Lazy Segment Tree supporting Range Max Query and Range Assignment Update.
3. For each brick: query max height h in [compressed(L_i), compressed(R_i)].
4. Update range [compressed(L_i), compressed(R_i)] to h + 1.
5. Output h + 1.

**Complexity**: `Time: O(N log N), Space: O(N).`  
**Editorial Alignment**: Coordinate compression and lazy range update on Segment Tree.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Handling massive coordinate ranges up to 10^9 via compression and maintaining interval heights with lazy segment tree.
- **Reusable Pattern**: `Coordinate Compression + Lazy Segment Tree Range Max.`

---

[Back to Master Categories](../../README.md)
