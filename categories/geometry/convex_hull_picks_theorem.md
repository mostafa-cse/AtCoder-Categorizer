# 📖 Convex Hull + Pick's Theorem + Shoelace Formula for Lattice Points

- **Tag / Domain**: `Geometry`
- **Subtopic**: `Convex Hull & Pick's Theorem`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Convex Hull + Pick's Theorem + Shoelace Formula for Lattice Points**.

---

## 🏆 Curated High-Value Problems

### Piles in AtCoder Farm (`[problem:AtCoder-typical90_ao]`)

- **Role**: *Convex Hull + Pick's Theorem + Shoelace Formula for Lattice Points*
- **Rating**: `2600` (★7) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ao)
- **Full Analysis**: [AtCoder-typical90_ao Analysis](../../analysis/AtCoder-typical90_ao.md)

#### Problem Statement & Task
Given N points in 2D plane, find the number of integer lattice points contained inside or on the boundary of their convex hull.

#### Core Invariant & Observation
Total lattice points = I + B = Area + B/2 + 1. Area is computed using Shoelace formula (2 * Area = cross products). Boundary points B on segment (P1, P2) is gcd(|x1 - x2|, |y1 - y2|).

#### Algorithmic Formulation
1. Compute convex hull using Monotone Chain algorithm.
2. Compute 2 * Area using Shoelace formula.
3. Compute boundary points B = sum gcd(|dx|, |dy|) for all hull edges.
4. Output (2 * Area + B) / 2 + 1 - N (or total lattice points - N if asking for new points).

**Complexity**: `Time: O(N log N), Space: O(N).`  
**Editorial Alignment**: Convex hull with Shoelace formula and Pick's Theorem.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Pick's Theorem, Monotone Chain convex hull, and counting integer lattice points in polygons.
- **Reusable Pattern**: `Convex Hull + Pick's Theorem + Shoelace Formula.`

---

[Back to Master Categories](../../README.md)
