# Games on Arbitrary Graphs

**Taxonomy Path**: `Game Theory` > `Graph Games` > `Games on Arbitrary Graphs`

## Description
This topic focuses on games on arbitrary graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because moves require strictly decreasing stone counts A_v < A_u, this defines a DAG on moves. If Takahashi moves piece to v where A_v < A_s and v is a losing starting position for the next player in the tree rooted at s, Takahashi can force a win. If Aoki tries to move back to s, Takahashi simply repeats his winning strategy because A_v < A_s guarantees Takahashi never runs out of stones before Aoki does. Thus, s is winning iff there is a neighbor v with A_v < A_s that is losing.
- Common Reductions: A piece starts at node s on a tree with stone counts A_v. A player moves piece from u to neighbor v with A_v < A_u, removing 1 stone from u. The player unable to move loses. Find all winning starting nodes s.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc010_f`](../../analysis/AtCoder-agc010_f.md) | F. Tree Game | 2897 | A piece starts at node s on a tree with stone counts A_v. A player moves piece from u to neighbor v with A_v < A_u, remo... |
