# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Inserting identical adjacent bits 00 or 11 preserves the adjacent XOR parity structure of the string. By analyzing the run-length parity of adjacent XOR differences, the reachability condition reduces to a constructive matching between run-lengths of S and T.
- Common Reductions: Given two binary strings S and T, determine if S can be transformed into T by repeatedly inserting two adjacent identical bits (00 or 11), and construct the minimum operations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc223_e`](../../analysis/AtCoder-arc223_e.md) | E. Yin-Yang Two Bits Insertion | 2572 | Given two binary strings S and T, determine if S can be transformed into T by repeatedly inserting two adjacent identica... |
