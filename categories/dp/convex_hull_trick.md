# 📖 Convex Hull Trick (CHT) & DP Optimization

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Convex Hull Trick (CHT)`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Optimizing transitions of the form dp[i] = min_{j < i} (dp[j] + cost(j, i)) where cost can be linearized into lines y = m*x + b.

---

## 🏆 Curated High-Value Problems

### 1. Frog 3 (`[problem:AtCoder-dp_z]`)

- **Role**: *Monotonic Convex Hull Trick (CHT)*
- **Rating**: `2200` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_z)
- **Full Analysis**: [AtCoder-dp_z Analysis](../../analysis/AtCoder-dp_z.md)

#### Problem Statement & Task
Frog jumps from stone i to j with quadratic cost (h_j - h_i)^2 + C where heights are strictly increasing.

#### Core Invariant & Observation
Since heights h_i are strictly increasing, slopes are strictly decreasing and query points are strictly increasing. A deque maintains the lower convex hull in O(1) amortized time per query.

#### Algorithmic Formulation
1. Deque stores lines.
2. For stone j: pop front while line[0].eval(h_j) >= line[1].eval(h_j).
3. dp[j] = deque.front().eval(h_j) + h_j^2 + C.
4. Add new line (slope = -2*h_j, intercept = h_j^2 + dp[j]) to back, popping non-convex lines.

**Complexity**: `Time: O(N), Space: O(N).`  
**Editorial Alignment**: Canonical Convex Hull Trick with monotonic slopes and queries.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Geometric line lower envelope maintenance, convex hull deque operations, and linearizing quadratic DP costs.
- **Reusable Pattern**: `Monotonic Convex Hull Trick (CHT).`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
