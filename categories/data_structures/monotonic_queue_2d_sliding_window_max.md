# Monotonic Queue 2D

**Taxonomy Path**: `Data Structures (DS)` > `Monotonic Data Structures` > `Monotonic Queue 2D`

## Description
This topic focuses on monotonic queue 2d techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let ah = min(h1, h2) and aw = min(w1, w2). For Takahashi placement at (r, c), Aoki can choose any top-left (r', c') with r <= r' <= r + h1 - ah and c <= c' <= c + w1 - aw. Precomputing all ah x aw sums S[r'][c'] via 2D prefix sums, Aoki choice is the maximum of S in a 2D window of size (h1 - ah + 1) x (w1 - aw + 1). Applying 1D monotonic deque maximum row-by-row followed by 1D monotonic deque column-by-column computes all 2D window maximums in optimal O(HW) time and memory.
- Common Reductions: Takahashi selects an h1 x w1 subgrid on an H x W board to paint black, after which Aoki places an h2 x w2 white stamp entirely inside Takahashi subgrid (effectively size min(h1, h2) x min(w1, w2)) to erase black cells. Takahashi maximizes the remaining sum of black cells. This reduces to computing for every Takahashi placement (r, c) the maximum sub-rectangle sum available to Aoki inside that window via 2D sliding window maximum.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc228_f`](../../analysis/AtCoder-abc228_f.md) | I. Stamp Game | 2179 | Takahashi selects an h1 x w1 subgrid on an H x W board to paint black, after which Aoki places an h2 x w2 white stamp en... |
