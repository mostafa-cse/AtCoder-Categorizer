# Problem Analysis: AtCoder-abc350_d — New Friends

**Problem ID**: `AtCoder-abc350_d`  
**Contest**: `abc350`  
**Rating**: 1050  
**URL**: https://atcoder.jp/contests/abc350/tasks/abc350_d  
**VJudge Tag**: `[problem:AtCoder-abc350_d]`  
**Category File**: [`../categories/Graph_Theory.md`](../categories/Graph_Theory.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Connected Components`  
- **Topic (Skill)**: `Disjoint Set Union (DSU) / Connected Component Cliques`  

---

## 1. Problem Statement & Key Idea
If A-B and B-C are friends, A and C can become friends. Calculate maximum new operations.

## 2. Core Observation & Invariant
The operation creates the transitive closure of the graph. Every connected component of size S will eventually become a complete graph (clique) with S*(S-1)/2 edges.

## 3. Step-by-Step Algorithm
1. Build DSU over all N vertices and M edges.
2. For each component root, obtain component vertex count S and existing edge count E.
3. Total new edges = sum_{components} (S * (S - 1) / 2 - E).

## 4. Complexity Analysis
Time: O(N + M * alpha(N)), Space: O(N).

## 5. Editorial Comparison & Alignment
Transitive closure clique completion via DSU.

## 6. What This Problem Teaches
Transitive relations on graphs and component-wise clique maximization.

## 7. Reusable Competitive Programming Pattern
`DSU component aggregation and clique edge counting.`

---
Back to [Category: Graph Theory](../categories/Graph_Theory.md) | [Categories Index](../categories/README.md)