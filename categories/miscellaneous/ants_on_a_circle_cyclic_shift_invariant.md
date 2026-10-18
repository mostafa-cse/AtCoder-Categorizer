# Permutations and Permutation Cycles

**Taxonomy Path**: `Miscellaneous` > `Permutations` > `Permutations and Permutation Cycles`

## Description
This topic focuses on permutations and permutation cycles techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When two ants collide, their identity swap is equivalent to maintaining cyclic ordering. Each ant crossing coordinate 0 in the positive direction shifts the cyclic permutation offset by $+1$, while crossing in the negative direction shifts by $-1$. Total net shift modulo $N$ identifies which ant in the sorted array corresponds to ant 1.
- Common Reductions: Determine the final positions of $N$ ants moving on a circle of circumference $L$ after time $T$, reversing directions upon collisions. Colliding ants can be viewed as passing through each other, so the multiset of final coordinates is exactly $\{(X_i \pm T) \bmod L\}$. Because ants cannot jump over each other on a circle, their cyclic order is strictly preserved. Tracking total counterclockwise zero-crossings identifies the exact cyclic permutation shift.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc013_c`](../../analysis/AtCoder-agc013_c.md) | C. Ants on a Circle | 2462 | Determine the final positions of $N$ ants moving on a circle of circumference $L$ after time $T$, reversing directions u... |
