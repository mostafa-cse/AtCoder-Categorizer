# 📖 Probability & Expected Value DP

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Intro to DP`
- **Total Curated Problems**: 2

---

## 💡 Topic Overview
Dynamic programming for probability distributions and expected values, state frequency compression, and algebraic resolution of self-loops.

---

## 🏆 Curated High-Value Problems

### 1. Coins (`[problem:AtCoder-dp_i]`)

- **Role**: *Probability and Expected Value DP*
- **Rating**: `1150` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_i)
- **Full Analysis**: [AtCoder-dp_i Analysis](../../analysis/AtCoder-dp_i.md)

#### Problem Statement & Task
N independent biased coins have probabilities p_i of turning up heads. Find the probability that more heads than tails appear.

#### Core Invariant & Observation
Let dp[i][j] be probability of exactly j heads after i coin tosses. Outcome partitions probability mass into two events: heads (p_i) or tails (1 - p_i).

#### Algorithmic Formulation
1. dp[0][0] = 1.0; others 0.0.
2. For i in 1..N: for j in 0..i: dp[i][j] = (j > 0 ? dp[i-1][j-1] * p_i : 0) + dp[i-1][j] * (1 - p_i).
3. Sum dp[N][j] for j > N/2.

**Complexity**: `Time: O(N^2), Space: O(N).`  
**Editorial Alignment**: Poisson binomial distribution dynamic programming.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Probability mass conservation and floating-point accumulation in discrete trial DP.
- **Reusable Pattern**: `Probability convolution DP over independent Bernoulli trials.`

---

### 2. Sushi (`[problem:AtCoder-dp_j]`)

- **Role**: *Expected Value DP with Multi-Frequency States*
- **Rating**: `1650` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_j)
- **Full Analysis**: [AtCoder-dp_j Analysis](../../analysis/AtCoder-dp_j.md)

#### Problem Statement & Task
N plates have 1, 2, or 3 sushi. Repeatedly choose a random plate and eat one sushi if present. Find expected operations to empty all plates.

#### Core Invariant & Observation
Self-loop equation E = 1 + sum(P_i E_i) + P_empty E solves algebraically: E = (N + c1*E1 + c2*E2 + c3*E3) / (c1 + c2 + c3).

#### Algorithmic Formulation
1. Memoized 3D DP array: memo[c1][c2][c3].
2. Compute recursively using the resolved self-loop formula.
3. Base: memo[0][0][0] = 0.0.

**Complexity**: `Time: O(N^3), Space: O(N^3).`  
**Editorial Alignment**: Expected value recurrence with algebraic self-loop resolution.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Multi-frequency state compression and algebraic self-loop elimination in expected value DP.
- **Reusable Pattern**: `Self-loop elimination: E = (1 + \sum P_i E_i) / (1 - P_{self}).`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
