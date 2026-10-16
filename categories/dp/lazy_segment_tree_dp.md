# 📖 DP Optimization using Lazy Segment Tree

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `DP Optimizations`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Accelerating dynamic programming state transitions by maintaining candidate values in a Segment Tree supporting range-addition updates and range-maximum queries.

---

## 🏆 Curated High-Value Problems

### 1. Intervals (`[problem:AtCoder-dp_w]`)

- **Role**: *Lazy Segment Tree Range-Add Point-Query DP*
- **Rating**: `2350` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_w)
- **Full Analysis**: [AtCoder-dp_w Analysis](../../analysis/AtCoder-dp_w.md)

#### Problem Statement & Task
Construct a binary string s of length N. You are given M intervals [l_i, r_i] with score a_i. An interval gives score a_i if at least one '1' falls in [l_i, r_i]. Maximize total score.

#### Core Invariant & Observation
If the previous '1' is at position j in [l, i], the interval is satisfied. Adding a to range [l, i] updates all valid previous positions in O(log N). dp[i] = max_{0 <= j < i} dp[j].

#### Algorithmic Formulation
1. Group intervals by their right endpoint r.
2. Maintain Lazy Segment Tree of size N+1.
3. For i from 1 to N: for each interval [l, i] with score a: segtree.range_add(l, i, a). dp[i] = segtree.query_max(0, i-1). segtree.update_point(i, dp[i]).
4. Return segtree.query_max(0, N).

**Complexity**: `Time: O((N + M) log N), Space: O(N).`  
**Editorial Alignment**: Range-add point-query Lazy Segment Tree dynamic programming.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Using Lazy Segment Tree to dynamically update previous state transitions across ranges of active intervals.
- **Reusable Pattern**: `Lazy Segment Tree accelerated range-event DP.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
