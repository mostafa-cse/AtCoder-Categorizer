# 2 SAT

**Taxonomy Path**: `Graph Theory` > `Satisfiability` > `2 SAT`

## Description
This topic focuses on 2 sat techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A statement by villager A about B being C is valid iff (H_A ^ D_A) = (H_B ^ C) <=> H_A ^ H_B = D_A ^ C. Because D_A only affects statements made by A, all outgoing targets B_j of A must satisfy H_{B_1} ^ H_{B_j} = C(A -> B_1) ^ C(A -> B_j). Once a consistent 2-coloring on H is found, D_A = H_A ^ H_{B_1} ^ C(A -> B_1) always satisfies all constraints.
- Common Reductions: Determine confusion statuses D_i for N villagers under M statements. A statement A -> (B, C) holds iff H_A ^ H_B = D_A ^ C; since D_A only affects statements made by A, all outgoing targets of A must satisfy H_{B_1} ^ H_{B_j} = C_1 ^ C_j. Finding a 2-coloring of this component system and setting D_A = H_A ^ H_B ^ C solves the problem in O(N + M) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc188_c`](../../analysis/AtCoder-arc188_c.md) | C. Honest or Liar or Confused | 2377 | Determine confusion statuses D_i for N villagers under M statements. A statement A -> (B, C) holds iff H_A ^ H_B = D_A ^... |
