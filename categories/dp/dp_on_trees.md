# 📖 DP on Trees & Directed Acyclic Graphs (DAGs)

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Dp on Different Structures`
- **Total Curated Problems**: 3

---

## 💡 Topic Overview
Dynamic programming over tree structures and DAGs using topological order, post-order DFS subtree accumulation, and all-roots rerooting using prefix/suffix product arrays.

---

## 🏆 Curated High-Value Problems

### 1. Longest Path (`[problem:AtCoder-dp_g]`)

- **Role**: *DP on Trees and DAGs*
- **Rating**: `1350` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_g)
- **Full Analysis**: [AtCoder-dp_g Analysis](../../analysis/AtCoder-dp_g.md)

#### Problem Statement & Task
Find the length of the longest directed path in a Directed Acyclic Graph (DAG) with N vertices and M edges.

#### Core Invariant & Observation
Acyclic structure guarantees no circular dependencies. Memoized DFS evaluates each vertex and edge exactly once.

#### Algorithmic Formulation
1. Memoized DFS: memo[u] = -1.
2. DFS(u): if memo[u] != -1 return memo[u]. ans = 0. For each neighbor v: ans = max(ans, 1 + DFS(v)). memo[u] = ans.
3. Return max_{u} DFS(u).

**Complexity**: `Time: O(V + E), Space: O(V + E).`  
**Editorial Alignment**: Topological sort DP on DAG.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Topological ordering as the fundamental validity condition for DAG DP.
- **Reusable Pattern**: `Memoized DFS transition over DAG edges.`

---

### 2. Independent Set (`[problem:AtCoder-dp_p]`)

- **Role**: *DP on Trees and DAGs*
- **Rating**: `1500` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_p)
- **Full Analysis**: [AtCoder-dp_p Analysis](../../analysis/AtCoder-dp_p.md)

#### Problem Statement & Task
Count ways to paint vertices of a tree black or white such that no two adjacent vertices are both black.

#### Core Invariant & Observation
If node u is Black, all children must be White. If u is White, each child can be independently either Black or White.

#### Algorithmic Formulation
1. Post-order DFS(u, parent).
2. dp[u][Black] = prod_{v in children} dp[v][White].
3. dp[u][White] = prod_{v in children} (dp[v][Black] + dp[v][White]).
4. Return (dp[root][Black] + dp[root][White]) mod MOD.

**Complexity**: `Time: O(N), Space: O(N).`  
**Editorial Alignment**: Tree independent set combinatorial DP.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Subtree DP, state-color branching, and product-rule combination over tree children.
- **Reusable Pattern**: `Two-state subtree product DP on trees.`

---

### 3. Subtree (`[problem:AtCoder-dp_v]`)

- **Role**: *Tree DP with Subtree Rerooting without Division*
- **Rating**: `2100` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_v)
- **Full Analysis**: [AtCoder-dp_v Analysis](../../analysis/AtCoder-dp_v.md)

#### Problem Statement & Task
For every vertex v in a tree, compute the number of black-connected components containing v modulo M (M may not be prime).

#### Core Invariant & Observation
For each node, children values can be preprocessed into prefix and suffix cumulative products. Excluded child contribution is calculated by multiplying prefix[:i-1] * suffix[i+1:].

#### Algorithmic Formulation
1. DFS1: down[u] = prod_{v in children} (down[v] + 1) mod M.
2. DFS2: compute parent contribution up[u] using prefix and suffix products of sibling values.
3. Ans[u] = down[u] * (up[u] + 1) mod M.

**Complexity**: `Time: O(N), Space: O(N).`  
**Editorial Alignment**: All-roots tree DP rerooting with non-invertible operators.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Tree rerooting technique without modular division via prefix/suffix product arrays.
- **Reusable Pattern**: `Division-free prefix/suffix rerooting on trees.`

---


### We Need Both a and b (`[problem:AtCoder-typical90_bu]`)

- **Role**: *Tree Component Partition DP with 3 Characteristic States*
- **Rating**: `1800` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bu)
- **Full Analysis**: [AtCoder-typical90_bu Analysis](../../analysis/AtCoder-typical90_bu.md)

#### Problem Statement & Task
Tree with N vertices, each vertex labeled 'a' or 'b'. Delete a subset of edges to partition the tree into components such that EVERY component contains BOTH 'a' and 'b'. Count valid edge deletions modulo 10^9+7.

#### Core Invariant & Observation
For each child v of u, we can either CUT edge (u, v) (requiring child component to be valid: dp[v][2]), or KEEP edge (u, v) (merging child component into u's component). Use product rule to combine child states.

#### Algorithmic Formulation
1. Post-order DFS tree DP.
2. For leaf: set dp[leaf][label] = 1, others 0.
3. For node u with children v: combine product of (cut + keep) transitions.
4. Output dp[root][2].

**Complexity**: `Time: O(N), Space: O(N).`  
**Editorial Alignment**: Tree component partition dynamic programming with 3 component states.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Connected component subtree DP, edge cut/keep branch combination, and modular state invariants.
- **Reusable Pattern**: `Tree Component Partition DP.`

---

[Back to Dynamic Programming (DP) Index](README.md) |
