# Problem Analysis: AtCoder-typical90_l — Red Painting

**Problem ID**: `AtCoder-typical90_l`  
**Contest**: `typical90`  
**Rating**: 1250  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_l  
**VJudge Tag**: `[problem:AtCoder-typical90_l]`  
**Category File**: [`../categories/Data_Structures.md`](../categories/Data_Structures.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Grid Connectivity / Dynamic DSU`  

---

## 1. Problem Statement & Key Idea
Dynamically color grid cells red and answer reachability queries between red cells.

## 2. Core Observation & Invariant
Linearize 2D coordinates (r, c) to 1D index r * W + c. When a cell becomes red, unite it with any adjacent red neighbors. Querying connectivity is checking if both cells are red and share the same DSU root.

## 3. Step-by-Step Algorithm
1. Map (r, c) -> r * W + c. Initialize DSU and boolean is_red grid.
2. On color query: set is_red[r][c] = True; for each neighbor (nr, nc) that is red: dsu.unite(idx(r,c), idx(nr,nc)).
3. On reachability query: if is_red[a] and is_red[b] and dsu.same(idx_a, idx_b) -> 'Yes', else 'No'.

## 4. Complexity Analysis
Time: O(Q * alpha(H * W)), Space: O(H * W).

## 5. Editorial Comparison & Alignment
Online dynamic connectivity on 2D grid via DSU.

## 6. What This Problem Teaches
2D-to-1D coordinate flattening and online component maintenance without BFS/DFS reruns.

## 7. Reusable Competitive Programming Pattern
`Grid coordinate linearization + online DSU.`

---
Back to [Category: Data Structures (DS)](../categories/Data_Structures.md) | [Categories Index](../categories/README.md)