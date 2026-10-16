# 🌲 AtCoder Curriculum: Data Structures (DS)

Curated collection of high-value problems in **Data Structures (DS)** selected for teaching reusable competitive programming algorithms, structural observations, and mathematical invariants.

- **Total Curated Problems**: 3
- **Taxonomy Tier**: Tag (Domain Level)

---

## 📑 Table of Contents

- [Disjoint Set Union (DSU)](#disjoint-set-union-dsu)
  - [Grid Connectivity / Dynamic DSU](#grid-connectivity--dynamic-dsu) (1 problems)
- [Queue & Priority Queue](#queue--priority-queue)
  - [Hybrid Two-Stage Buffer (Queue + Min-Heap)](#hybrid-two-stage-buffer-queue--min-heap) (1 problems)
- [Segment Tree / Fenwick Tree](#segment-tree--fenwick-tree)
  - [Point Update Range XOR Query](#point-update-range-xor-query) (1 problems)

---

## Disjoint Set Union (DSU)

### Grid Connectivity / Dynamic DSU

#### Red Painting (`[problem:AtCoder-typical90_l]`)
- **Rating / Difficulty**: 1250
- **Contest**: `typical90` | [AtCoder Link](https://atcoder.jp/contests/typical90/tasks/typical90_l)
- **Detailed Analysis**: [`analysis/AtCoder-typical90_l.md`](../analysis/AtCoder-typical90_l.md)
- **Key Idea**: Dynamically color grid cells red and answer reachability queries between red cells.
- **Core Observation**: Linearize 2D coordinates (r, c) to 1D index r * W + c. When a cell becomes red, unite it with any adjacent red neighbors. Querying connectivity is checking if both cells are red and share the same DSU root.
- **Algorithm & Complexity**: Time: O(Q * alpha(H * W)), Space: O(H * W).
- **What This Problem Teaches**: 2D-to-1D coordinate flattening and online component maintenance without BFS/DFS reruns.
- **Reusable Pattern**: `Grid coordinate linearization + online DSU.`

---

## Queue & Priority Queue

### Hybrid Two-Stage Buffer (Queue + Min-Heap)

#### Sorting Queries (`[problem:AtCoder-abc217_e]`)
- **Rating / Difficulty**: 1200
- **Contest**: `abc217` | [AtCoder Link](https://atcoder.jp/contests/abc217/tasks/abc217_e)
- **Detailed Analysis**: [`analysis/AtCoder-abc217_e.md`](../analysis/AtCoder-abc217_e.md)
- **Key Idea**: Support three operations: append x to back, print and pop first element, and sort the entire array in ascending order.
- **Core Observation**: Sorting the whole array repeatedly takes O(N log N) per query! However, once an element is sorted, it stays sorted and always precedes newly appended elements. Split storage into two structures: a min-priority-queue (sorted elements) and a FIFO queue (newly appended unsorted elements).
- **Algorithm & Complexity**: Time: O(Q log Q) total (each element enters and leaves min-heap at most once), Space: O(Q).
- **What This Problem Teaches**: Amortized complexity and separating sorted vs unsorted segments using complementary data structures.
- **Reusable Pattern**: `Hybrid Queue + Min-Heap amortized sorting.`

---

## Segment Tree / Fenwick Tree

### Point Update Range XOR Query

#### Range Xor Query (`[problem:AtCoder-abc185_f]`)
- **Rating / Difficulty**: 1150
- **Contest**: `abc185` | [AtCoder Link](https://atcoder.jp/contests/abc185/tasks/abc185_f)
- **Detailed Analysis**: [`analysis/AtCoder-abc185_f.md`](../analysis/AtCoder-abc185_f.md)
- **Key Idea**: Maintain an array subject to two operations: A[X] = A[X] ^ Y, and query range XOR sum A[L] ^ ... ^ A[R].
- **Core Observation**: XOR is associative, commutative, and self-inverting. A Fenwick tree (Binary Indexed Tree) or Segment Tree natively handles point updates and range queries in O(log N).
- **Algorithm & Complexity**: Time: O(Q log N), Space: O(N).
- **What This Problem Teaches**: Applying Fenwick tree to any invertible commutative monoid (such as XOR).
- **Reusable Pattern**: `Fenwick Tree point-update range-query.`

---
