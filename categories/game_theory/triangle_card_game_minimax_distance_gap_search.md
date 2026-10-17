# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For an opening card $a \in A$, Bob can win if and only if either playing $B_{\min}$ prevents any triangle ($|a - B_{\min}| < c < a + B_{\min}$ has count 0 in $A \setminus \{a\}$), or there exists $b \in B$ whose distance to $A \setminus \{a\}$ is at least $a$. Alice wins if she has any opening move where Bob cannot win.
- Common Reductions: Alice chooses a card $A_i$, then Bob chooses $B_j$, then Alice chooses $A_k$ ($k \neq i$). Alice wins if the three lengths form a non-degenerate triangle. Determine if Alice can guarantee a win with optimal play.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc170_d`](../../analysis/AtCoder-arc170_d.md) | D. Triangle Card Game | 2279 | Alice chooses a card $A_i$, then Bob chooses $B_j$, then Alice chooses $A_k$ ($k \neq i$). Alice wins if the three lengt... |
