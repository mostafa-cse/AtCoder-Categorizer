# Binary Search

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Binary Search`

## Description
This topic focuses on binary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If exam $i$ is chosen to receive partial hours $r$, the remaining $q$ exams receiving full score $X$ should greedily be the ones with the largest maximum gain $b_j l_j + (X - b_j) u_j$. Sorting exams by maximum gain and maintaining prefix sums allows an $O(1)$ check for any candidate exam $i$, resulting in an $O(N)$ feasibility check per binary search iteration.
- Common Reductions: Find the minimum total study hours $H$ across $N$ exams so Takahashi's score equals or exceeds Aoki's. Aoki scores $b_i$ on exam $i$. For Takahashi, scoring $s_i \le b_i$ yields $s_i l_i$, while $s_i > b_i$ yields $b_i l_i + (s_i - b_i) u_i$. The score gain function is convex piecewise linear. In an optimal solution, at most one test receives partial study hours $r \in [0, X)$, and $q$ tests receive full $X$ hours. Monotonicity allows binary searching on the total hours $H = qX + r$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc034_c`](../../analysis/AtCoder-agc034_c.md) | C. Tests | 2497 | Find the minimum total study hours $H$ across $N$ exams so Takahashi's score equals or exceeds Aoki's. Aoki scores $b_i$... |
