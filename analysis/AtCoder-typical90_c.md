# Problem Analysis: AtCoder-typical90_c — Longest Circular Road

**Problem ID**: `AtCoder-typical90_c`  
**Contest**: `typical90`  
**Rating**: 1100  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_c  
**VJudge Tag**: `[problem:AtCoder-typical90_c]`  
**Category File**: [`../categories/Graph_Theory.md`](../categories/Graph_Theory.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Tree Diameter / Double BFS-DFS`  

---

## 1. Problem Statement & Key Idea
Add one edge between any two vertices in a tree to form the longest possible cycle.

## 2. Core Observation & Invariant
Adding edge (u, v) creates a cycle of length dist(u, v) + 1. The maximum distance in a tree is by definition the diameter of the tree.

## 3. Step-by-Step Algorithm
1. Run BFS from arbitrary node 1 to find farthest node u.
2. Run BFS from u to find farthest node v. dist(u, v) is the tree diameter.
3. Output dist(u, v) + 1.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Editorial Comparison & Alignment
Two-pass BFS tree diameter proof.

## 6. What This Problem Teaches
Tree diameter characterization and the canonical 2-BFS algorithm.

## 7. Reusable Competitive Programming Pattern
`2-pass BFS tree diameter.`

---
Back to [Category: Graph Theory](../categories/Graph_Theory.md) | [Categories Index](../categories/README.md)