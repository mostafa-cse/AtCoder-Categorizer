# Problem Analysis: AtCoder-typical90_m — Passing

**Problem ID**: `AtCoder-typical90_m`  
**Contest**: `typical90`  
**Rating**: 1350  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_m  
**VJudge Tag**: `[problem:AtCoder-typical90_m]`  
**Category File**: [`../categories/Graph_Theory.md`](../categories/Graph_Theory.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Two-Way Dijkstra / Intermediate Node Shortest Paths`  

---

## 1. Problem Statement & Key Idea
For every vertex k from 1 to N, find the shortest path from vertex 1 to vertex N passing through k.

## 2. Core Observation & Invariant
Shortest path from 1 to N through k is dist(1, k) + dist(k, N). Since edges are bidirectional, dist(k, N) = dist(N, k). Running Dijkstra only twice (from 1 and from N) resolves all queries in O(1).

## 3. Step-by-Step Algorithm
1. Run Dijkstra from node 1 -> dist1 array.
2. Run Dijkstra from node N -> distN array.
3. For each k in 1..N: output dist1[k] + distN[k].

## 4. Complexity Analysis
Time: O(M log N), Space: O(N + M).

## 5. Editorial Comparison & Alignment
Two-source bidirectional Dijkstra.

## 6. What This Problem Teaches
Decomposing multi-point shortest path queries into two independent single-source runs.

## 7. Reusable Competitive Programming Pattern
`Dual Dijkstra intermediate point distance query.`

---
Back to [Category: Graph Theory](../categories/Graph_Theory.md) | [Categories Index](../categories/README.md)