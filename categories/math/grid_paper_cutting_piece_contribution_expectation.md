# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By linearity of expectation, the expected number of pieces after t cuts depends on the number of horizontal cuts h and vertical cuts w made among the t cuts. Since each cut is chosen uniformly from all remaining grid lines, (h, w) follows a hypergeometric distribution. The expected product E[h * w] = t(t-1)(H-1)(W-1) / (N(N-1)). This allows the total sum over all steps to be evaluated in O(K)!
- Common Reductions: A paper of size H x W has H-1 horizontal and W-1 vertical cut lines (N = H + W - 2). We choose a permutation of K cut lines uniformly at random and cut along them sequentially. Find the expected total piece perimeter/count times P(N, K) modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-keyence2019_f`](../../analysis/AtCoder-keyence2019_f.md) | F - Paper Cutting | 2967 | A paper of size H x W has H-1 horizontal and W-1 vertical cut lines (N = H + W - 2). We choose a permutation of K cut li... |
