# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each baking period must be an integer number of seconds >= 2 (c_i = 1 is strictly suboptimal as it costs A seconds to multiply rate by 1). Thus 2^m <= prod c_i approx N <= 10^{12}, implying m <= 40 stages. For fixed m, the integers c_i partition into (m-j) copies of r and j copies of r+1, easily found by binary search.
- Common Reductions: Baking cookies where eating x cookies takes A seconds and multiplies the baking rate to x cookies/sec. If eating is performed k times, the baking durations c_1, ..., c_{k+1} must satisfy prod c_i >= N, minimizing (k * A + sum c_i). By AM-GM inequality, optimal integers c_i are as close as possible (each r or r+1 where r = floor(N^{1/m})), and m <= 40.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-codefestival_2016_final_e`](../../analysis/AtCoder-codefestival_2016_final_e.md) | Cookies | 2700 | Baking cookies where eating x cookies takes A seconds and multiplies the baking rate to x cookies/sec. If eating is perf... |
