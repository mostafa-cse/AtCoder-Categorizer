# 📖 Greedy Splitting / Automatic Prerequisite Satisfaction by Diminishing Returns

- **Tag / Domain**: `Basics`
- **Subtopic**: `Greedy Algorithms`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Greedy Splitting / Automatic Prerequisite Satisfaction by Diminishing Returns**.

---

## 🏆 Curated High-Value Problems

### I will not drop out (`[problem:AtCoder-typical90_av]`)

- **Role**: *Greedy Splitting / Automatic Prerequisite Satisfaction by Diminishing Returns*
- **Rating**: `800` (★3) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_av)
- **Full Analysis**: [AtCoder-typical90_av Analysis](../../analysis/AtCoder-typical90_av.md)

#### Problem Statement & Task
N problems, time limit K minutes. Problem i awards B_i points for first minute, and additional A_i - B_i points for second minute. Maximize total score.

#### Core Invariant & Observation
Because points are diminishing (B_i >= A_i - B_i), any greedy algorithm that picks the largest available bonus will ALWAYS pick B_i before A_i - B_i! The prerequisite dependency is automatically satisfied.

#### Algorithmic Formulation
1. Create a list of 2N elements: B_i and A_i - B_i for each problem.
2. Sort all 2N elements descending.
3. Sum the top K elements.

**Complexity**: `Time: O(N log N), Space: O(N).`  
**Editorial Alignment**: Splitting dependent tasks into independent rewards using concavity / diminishing returns.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Eliminating dependency constraints in greedy selection when incremental rewards are concave/diminishing.
- **Reusable Pattern**: `Greedy Task Splitting with Diminishing Returns.`

---

[Back to Master Categories](../../README.md)
