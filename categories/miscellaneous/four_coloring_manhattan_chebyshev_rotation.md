# Manhattan <> Chebyshev

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Manhattan <> Chebyshev`

## Description
This topic focuses on manhattan <> chebyshev techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any two points sharing the same color must have $U_1 \equiv U_2 \pmod 2$ and $V_1 \equiv V_2 \pmod 2$, meaning $|u_1 - u_2|$ and $|v_1 - v_2|$ are never equal to $d$ (they are either $< d$ or $> d$).
- Common Reductions: Color an $H \times W$ grid ($H, W \le 500$) with 4 colors such that no two squares at Manhattan distance $d$ have the same color. Rotating coordinates by 45 degrees transforms Manhattan distance $|i_1 - i_2| + |j_1 - j_2| = d$ into Chebyshev distance $\max(|u_1 - u_2|, |v_1 - v_2|) = d$, where $u = i + j$ and $v = i - j$. Tiling the $(u, v)$ plane into $d \times d$ squares colored periodically with a $2 \times 2$ pattern of 4 colors completely avoids distance $d$ within identical colors.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-code_festival_2017_quala_d`](../../analysis/AtCoder-code_festival_2017_quala_d.md) | D. Four Coloring | 2445 | Color an $H \times W$ grid ($H, W \le 500$) with 4 colors such that no two squares at Manhattan distance $d$ have the sa... |
