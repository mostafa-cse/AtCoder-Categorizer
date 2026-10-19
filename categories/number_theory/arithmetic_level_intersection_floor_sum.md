# Floor Sum and Mod Sum of Arithmetic Progression

**Taxonomy Path**: `Number Theory` > `Floor Sum` > `Floor Sum and Mod Sum of Arithmetic Progression`

## Description
This topic focuses on floor sum and mod sum of arithmetic progression techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let f(x) = A_X + x/B_X and g(x) = A_Y + x/B_Y with floor functions F(x), G(x). F(x) == G(x) can only hold when f(x) - g(x) is in [-1, 1). In [-1, 0), F(x) in {G(x)-1, G(x)}, so the equality indicator is 1 - G(x) + F(x). In [0, 1), F(x) in {G(x), G(x)+1}, so the indicator is 1 - F(x) + G(x). The range bounds are solved linearly, and prefix sums of floor(A + x/B) over arithmetic progressions evaluate in O(1) time using block division.
- Common Reductions: Two programmers with starting levels A_X, A_Y gain 1 level every B_X, B_Y menus. Count n in 1..N such that A_X + floor(n / B_X) == A_Y + floor(n / B_Y) across T test cases.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc123_e`](../../analysis/AtCoder-arc123_e.md) | E - Training | 2828 | Two programmers with starting levels A_X, A_Y gain 1 level every B_X, B_Y menus. Count n in 1..N such that A_X + floor(n... |
