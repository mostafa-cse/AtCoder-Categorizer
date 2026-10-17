# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Coordinate compressing all initial scores and query score updates yields at most N + Q distinct values. A segment tree over the sorted values maintains card count and score sum. Query x checks if total count >= x, then walks from root to leaf, recursively descending into the right child if it has sufficient cards, or taking all right child cards and descending into the left child.
- Common Reductions: Maintain N card types with score a_i and quota b_i under point score updates, quota updates, and queries asking for the maximum score achievable by selecting x cards total. Greedily taking cards with the highest scores is optimal, implemented via segment tree walking.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc287_g`](../../analysis/AtCoder-abc287_g.md) | G. Balance Update Query | 2180 | Maintain N card types with score a_i and quota b_i under point score updates, quota updates, and queries asking for the ... |
