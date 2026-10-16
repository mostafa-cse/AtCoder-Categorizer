# Problem Analysis: AtCoder-abc217_e — Sorting Queries

**Problem ID**: `AtCoder-abc217_e`  
**Contest**: `abc217`  
**Rating**: 1200  
**URL**: https://atcoder.jp/contests/abc217/tasks/abc217_e  
**VJudge Tag**: `[problem:AtCoder-abc217_e]`  
**Category File**: [`../categories/Data_Structures.md`](../categories/Data_Structures.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Queue & Priority Queue`  
- **Topic (Skill)**: `Hybrid Two-Stage Buffer (Queue + Min-Heap)`  

---

## 1. Problem Statement & Key Idea
Support three operations: append x to back, print and pop first element, and sort the entire array in ascending order.

## 2. Core Observation & Invariant
Sorting the whole array repeatedly takes O(N log N) per query! However, once an element is sorted, it stays sorted and always precedes newly appended elements. Split storage into two structures: a min-priority-queue (sorted elements) and a FIFO queue (newly appended unsorted elements).

## 3. Step-by-Step Algorithm
1. When appending x: push x to FIFO queue.
2. When sorting: move all elements from FIFO queue to min-heap.
3. When popping: if min-heap is non-empty, pop from min-heap; else pop from FIFO queue.

## 4. Complexity Analysis
Time: O(Q log Q) total (each element enters and leaves min-heap at most once), Space: O(Q).

## 5. Editorial Comparison & Alignment
Two-buffer amortized queue + priority queue split.

## 6. What This Problem Teaches
Amortized complexity and separating sorted vs unsorted segments using complementary data structures.

## 7. Reusable Competitive Programming Pattern
`Hybrid Queue + Min-Heap amortized sorting.`

---
Back to [Category: Data Structures (DS)](../categories/Data_Structures.md) | [Categories Index](../categories/README.md)