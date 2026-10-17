# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The set of blocks between i and j inclusive has size |j - i| + 1. The first block among them to be removed is uniformly distributed over the |j - i| + 1 candidates. Block j contributes to the cost of removing i iff i is chosen first among these blocks, with probability 1 / (|j - i| + 1). Summing over all i for a fixed j gives H_j + H_{N - j + 1} - 1. Multiplying by N! gives the exact answer.
- Common Reductions: Compute the total cost of removing N blocks in all N! random orders. By Linearity of Expectation, block j is connected to block i at the moment i is removed iff block i is removed before all blocks strictly between i and j. The probability is 1 / (|j - i| + 1). Summing over all pairs yields a closed-form expression using Harmonic numbers H_m = sum_{k=1}^m 1/k.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc028_b`](../../analysis/AtCoder-agc028_b.md) | B. Removing Blocks | 2172 | Compute the total cost of removing N blocks in all N! random orders. By Linearity of Expectation, block j is connected t... |
