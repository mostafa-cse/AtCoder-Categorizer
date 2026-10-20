# The XOR Trick

**Taxonomy Path**: `Basics` > `Bit Manipulation` > `The XOR Trick`

## Description
This topic focuses on the xor trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Cumulative XOR sums p_i represent the potentials driving ball movement. Merging balls eliminates local peaks. The balls stabilize if and only if no prefix XOR sum satisfies Z XOR p_i < Z. The XOR trick establishes that Z XOR p_i < Z iff the most significant bit (MSB) of p_i is 1 in Z. Thus, Z must have 0 at every bit position that appears as the MSB of any p_i, while all other bit positions can be freely 0 or 1.
- Common Reductions: Balls with weights w_1, ..., w_{2^N-1} on a line move toward the larger adjacent prefix XOR sum, merging upon collision. Determine how many boundary weights Z <= 2^N-1 ensure all balls come to rest within finite time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc152_e`](../../analysis/AtCoder-arc152_e.md) | E - Xor Annihilation | 2990 | Balls with weights w_1, ..., w_{2^N-1} on a line move toward the larger adjacent prefix XOR sum, merging upon collision.... |
