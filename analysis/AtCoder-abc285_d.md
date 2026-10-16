# Problem Analysis: AtCoder-abc285_d — Change of User Name

**Problem ID**: `AtCoder-abc285_d`  
**Contest**: `abc285`  
**Rating**: 950  
**URL**: https://atcoder.jp/contests/abc285/tasks/abc285_d  
**VJudge Tag**: `[problem:AtCoder-abc285_d]`  
**Category File**: [`../categories/Graph_Theory.md`](../categories/Graph_Theory.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Directed Graphs`  
- **Topic (Skill)**: `Cycle Detection / Functional Graph Component Analysis`  

---

## 1. Problem Statement & Key Idea
N users want to change their handles from S_i to T_i. Determine if all changes can be performed without handle collisions.

## 2. Core Observation & Invariant
Build directed graph with edge S_i -> T_i. A valid sequence of changes exists if and only if the directed graph contains NO directed cycle.

## 3. Step-by-Step Algorithm
1. Build adjacency list of directed edges S_i -> T_i.
2. Compute in-degrees and perform Kahn's Topological Sort (or 3-color DFS cycle check).
3. If all nodes can be topologically sorted, output 'Yes'; else 'No'.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Editorial Comparison & Alignment
Topological sort cycle check on string handle transitions.

## 6. What This Problem Teaches
Modeling sequential dependencies as directed graph cycles and topological ordering.

## 7. Reusable Competitive Programming Pattern
`Topological sort cycle detection for dependency resolution.`

---
Back to [Category: Graph Theory](../categories/Graph_Theory.md) | [Categories Index](../categories/README.md)