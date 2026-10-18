# Product Trick

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Product Trick`

## Description
This topic focuses on product trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Product Trick: each child independently chooses one day they received a cookie. This completely decouples days into choosing cnt[i] children per day with weight W_i(c) = 1/c! * binom(N - c, a_i - c). The total answer is N! times the coefficient of x^N in prod_{i=1}^K (sum_c W_i(c) x^c).
- Common Reductions: In K days, give cookies to a_i children among N. Happiness is the product of cookies received prod c_j. Find the expected happiness multiplied by prod binom(N, a_i) modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-dwacon6th_prelims_c`](../../analysis/AtCoder-dwacon6th_prelims_c.md) | C. Cookie Distribution | 2618 | In K days, give cookies to a_i children among N. Happiness is the product of cookies received prod c_j. Find the expecte... |
