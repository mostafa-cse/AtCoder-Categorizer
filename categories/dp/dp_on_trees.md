# 📖 DP on Trees & DAGs

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Dp on Different Structures`
- **Total Curated Problems**: 3

---

## 💡 Topic Overview
Dynamic programming defined on tree structures and Directed Acyclic Graphs. Tree DP typically proceeds via bottom-up post-order DFS where each node aggregates optimal substructure from its subtrees, or via two-pass all-roots tree rerooting.

---

## 🏆 Curated High-Value Problems

### 1. Independent Set (`[problem:AtCoder-dp_p]`)

- **Role**: *Foundational Subtree Tree DP*
- **Rating**: `1500` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_p)
- **Full Analysis**: [AtCoder-dp_p Analysis](../../analysis/AtCoder-dp_p.md)

#### Problem Statement & Task
Count ways to paint vertices of a tree black or white such that no two adjacent vertices are both black.

#### Core Invariant & Observation
If node u is Black, all children MUST be White. If u is White, each child v can independently be Black or White. Transitions combine via multiplication over children subtrees.

#### Algorithmic Formulation
1. Post-order DFS(u, parent).
2. dp[u][Black] = prod_{v in children} dp[v][White].
3. dp[u][White] = prod_{v in children} (dp[v][Black] + dp[v][White]).
4. Return (dp[root][Black] + dp[root][White]) mod 10^9+7.

**Complexity**: `Time: O(N), Space: O(N).`  
**Editorial Alignment**: Standard 2-state tree independent set counting.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Subtree DP, state-color branching, and product-rule combination over tree children.
- **Reusable Pattern**: `Two-state subtree product DP on trees.`

---

### 2. Subtree (`[problem:AtCoder-dp_v]`)

- **Role**: *Advanced All-Roots Tree Rerooting (Without Division)*
- **Rating**: `2100` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_v)
- **Full Analysis**: [AtCoder-dp_v Analysis](../../analysis/AtCoder-dp_v.md)

#### Problem Statement & Task
For EVERY vertex v in a tree, count the number of black-connected components containing v modulo M (M may not be prime).

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

### 3. Longest Path (`[problem:AtCoder-dp_g]`)

- **Role**: *Topological Order DP on DAGs*
- **Rating**: `1350` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_g)
- **Full Analysis**: [AtCoder-dp_g Analysis](../../analysis/AtCoder-dp_g.md)

#### Problem Statement & Task
Find the length of the longest directed path in a Directed Acyclic Graph (DAG).

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

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
