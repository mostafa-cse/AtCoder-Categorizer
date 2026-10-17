# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Sorting items A_1 <= A_2 <= ... <= A_k <= C, customers with budget in [A_i, A_{i+1}-1] are grouped into buckets. DP state dp[j] counts ways to assign budgets to j customers with budget >= A_i satisfying all suffix conditions up to item k. Transitioning from i+1 down to i with multinomial weights (diff)^t / t! solves each k in O(k * N^2) time, totaling O(N^4).
- Common Reductions: N customers with random budgets in 1..C greedily purchase the most expensive available item they can afford. By Hall's condition, at least k items are sold iff for each i in 1..k, at least k - i + 1 customers have budget >= A_i. Compute tail probabilities P(>= k) via suffix DP and multinomial transitions, then recover exact probabilities P(k) = P(>= k) - P(>= k + 1).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc217_c`](../../analysis/AtCoder-arc217_c.md) | C. Greedy Customers 2 | 2173 | N customers with random budgets in 1..C greedily purchase the most expensive available item they can afford. By Hall's c... |
