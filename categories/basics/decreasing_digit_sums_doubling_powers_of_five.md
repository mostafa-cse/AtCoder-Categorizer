# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Notice 2^i * 5^{50} n = 10^i * 5^{50-i} n. Multiplying by 10^i appends trailing zeros without changing digit sum, so f(2^i x) = f(5^{50-i} n). As i increases, the exponent 50 - i decreases, naturally shrinking the digit sum. Concatenating 5^50..5^99 with 100 zero-padding spaces eliminates carry interference and ensures strictly decreasing digit sums for all 50 steps.
- Common Reductions: Construct an integer x < 10^10000 whose base-10 digit sum strictly decreases under repeated doubling: f(2^{i-1} x) > f(2^i x) for all 1 <= i <= N (N <= 50). Solved via powers of five.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-agc066_b]` | Decreasing Digit Sums | 2162 | Construct an integer x < 10^10000 whose base-10 digit sum strictly decreases under repeated doubling: f(2^{i-1} x) > f(2... |
