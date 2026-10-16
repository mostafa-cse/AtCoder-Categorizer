# 📖 Amortized Hybrid Buffers (Queue + Priority Queue)

- **Tag / Domain**: `Data Structures (DS)`
- **Subtopic**: `Queue & Priority Queue`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Splitting collections into sorted and unsorted segments to achieve optimal amortized complexity across dynamic sorting and popping operations.

---

## 🏆 Curated High-Value Problems

### 1. Sorting Queries (`[problem:AtCoder-abc217_e]`)

- **Role**: *Two-Stage Buffer (Queue + Min-Heap)*
- **Rating**: `1200` | **Contest**: [`abc217`](https://atcoder.jp/contests/abc217/tasks/abc217_e)
- **Full Analysis**: [AtCoder-abc217_e Analysis](../../analysis/AtCoder-abc217_e.md)

#### Problem Statement & Task
Support: append x, print and pop first element, and sort the entire array.

#### Core Invariant & Observation
Sorted elements always precede newly appended unsorted elements. On sort query, transfer all FIFO queue elements into min-heap. Each element enters min-heap at most once!

#### Algorithmic Formulation
1. On append x: push to FIFO queue.
2. On sort: move all elements from FIFO queue to min-heap.
3. On pop: if min-heap is non-empty, pop min-heap; else pop FIFO queue.

**Complexity**: `Time: O(Q log Q) amortized, Space: O(Q).`  
**Editorial Alignment**: Two-buffer amortized queue + priority queue split.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Amortized complexity and separating sorted vs unsorted segments using complementary data structures.
- **Reusable Pattern**: `Hybrid Queue + Min-Heap amortized sorting.`

---

[Back to Data Structures (DS) Index](README.md) | [Back to Master Categories](../../README.md)
