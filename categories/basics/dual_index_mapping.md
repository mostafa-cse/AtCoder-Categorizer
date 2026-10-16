# 📖 Dual Index Mapping (Position <-> Value)

- **Tag / Domain**: `Basics`
- **Subtopic**: `Implementation / Simulation`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Maintaining bidirectional bijections between permutation values and their array indices to perform dynamic position lookups and swaps in O(1) time.

---

## 🏆 Curated High-Value Problems

### 1. Adjacent Swaps (`[problem:AtCoder-abc250_c]`)

- **Role**: *Bidirectional Permutation Bijection*
- **Rating**: `800` | **Contest**: [`abc250`](https://atcoder.jp/contests/abc250/tasks/abc250_c)
- **Full Analysis**: [AtCoder-abc250_c Analysis](../../analysis/AtCoder-abc250_c.md)

#### Problem Statement & Task
Perform Q swaps where each query swaps ball with number x and its adjacent neighbor.

#### Core Invariant & Observation
Locating ball x in an array naively takes O(N). Dual arrays allow O(1) lookup and O(1) swap update.

#### Algorithmic Formulation
1. Maintain pos[x] and val[p].
2. For query x: p = pos[x]. Determine target p2 = (p < N ? p + 1 : p - 1). Let y = val[p2].
3. Swap: val[p]=y, val[p2]=x. Update pos: pos[x]=p2, pos[y]=p.

**Complexity**: `Time: O(Q), Space: O(N).`  
**Editorial Alignment**: Dual array bijection maintenance.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: O(1) bidirectional lookup mapping and maintaining invertible permutations under swap operations.
- **Reusable Pattern**: `Dual index mapping (Position <-> Value).`

---

[Back to Basics Index](README.md) | [Back to Master Categories](../../README.md)
