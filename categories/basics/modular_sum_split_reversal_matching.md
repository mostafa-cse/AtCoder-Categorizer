# Binary Search

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Binary Search`

## Description
This topic focuses on binary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When A and B are sorted ascending, any optimal permutation pairs a prefix of size k without wrapping (A[i] + B[k-1-i] < M) and a suffix of size N-k with wrapping (A[k+j] + B[N-1-j] >= M). To minimize maximum sums, both parts are paired in reverse order. Furthermore, the condition A[k+j] + B[N-1-j] >= M is monotonically non-decreasing in k, leaving only k = k2 (the minimal valid k) and k = N as candidate optimal split points.
- Common Reductions: Sort A and B. Optimal matching splits elements into a non-wrapping prefix and a wrapping suffix, each paired in anti-monotonic order. Monotonicity reduces candidates to k = k2 (found via binary search) and k = N in O(N log N) total time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc201_d`](../../analysis/AtCoder-arc201_d.md) | D. Match, Mod, Minimize | 2389 | Sort A and B. Optimal matching splits elements into a non-wrapping prefix and a wrapping suffix, each paired in anti-mon... |
