# Tree Isomorphism

**Taxonomy Path**: `Miscellaneous` > `General` > `Tree Isomorphism`

## Description
This topic focuses on tree isomorphism techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Enclosing S as ( + S + ) forms a single rooted tree where each matched pair () is a node and nested pairs are children. Consecutive reversals of child subsegments allow arbitrary reordering of a node's children. If node u has k children with isomorphism counts c_1, ..., c_m, the number of distinct ordered sequences is k! / (c_1! * ... * c_m!). The total count is the product of these multinomial coefficients across all vertices.
- Common Reductions: Given a valid parenthesis sequence S, reversing balanced subsegments bijects to rooted ordered trees where contiguous reversals generate the full symmetric group of sibling subtrees. Distinct reachable strings correspond to all valid permutations of sibling subtrees, counted via tree isomorphism hashing and multinomial coefficients.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc194_d`](../../analysis/AtCoder-arc194_d.md) | D. Reverse Brackets | 2164 | Given a valid parenthesis sequence S, reversing balanced subsegments bijects to rooted ordered trees where contiguous re... |
