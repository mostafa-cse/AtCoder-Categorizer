# Splitting Objects into Light and Heavy / Case Processing

**Taxonomy Path**: `Data Structures (DS)` > `Square Root Decomposition` > `Splitting Objects into Light and Heavy / Case Processing`

## Description
This topic focuses on splitting objects into light and heavy / case processing techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each person has a collection of disjoint inside intervals. The sum of interval counts across all people is $M / 2 \le 10^5$. We partition people into Heavy ($> B$ intervals) and Light ($\le B$ intervals) with threshold $B \approx 700$. There are at most $M / (2B) \approx 140$ Heavy people. For each Heavy person, we precompute their overlap with all other people in $O(M)$ time via a single chronological sweep. For pairs of Light people, two pointers computes the intersection in $O(B)$ time.
- Common Reductions: Given $M$ entry/exit timestamps for $N$ people at an office. Answer $Q$ queries: total duration during which both person $A$ and person $B$ were simultaneously inside the office.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc365_g`](../../analysis/AtCoder-abc365_g.md) | G. AtCoder Office | 2254 | Given $M$ entry/exit timestamps for $N$ people at an office. Answer $Q$ queries: total duration during which both person... |
