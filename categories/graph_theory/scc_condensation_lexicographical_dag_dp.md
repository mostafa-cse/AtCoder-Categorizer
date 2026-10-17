# Strongly Connected Components (SCC)

**Taxonomy Path**: `Graph Theory` > `Graph Connectivity` > `Strongly Connected Components (SCC)`

## Description
This topic focuses on strongly connected components (scc) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any walk inside an SCC can visit all its vertices and collect any subset of its characters in sorted order. Once leaving an SCC, you can never return to it. Thus, on the condensed DAG, taking c characters from SCC u takes the c smallest characters of u in non-decreasing order, followed by characters from a successor SCC.
- Common Reductions: In a directed graph where each vertex carries a character, visit vertices along a walk to collect exactly k characters such that the resulting string is lexicographically smallest. Contract the graph into an SCC DAG, sort characters within each SCC, and execute string DP on the DAG.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc030_3`](../../analysis/AtCoder-arc030_3.md) | C. 有向グラフ | 2180 | In a directed graph where each vertex carries a character, visit vertices along a walk to collect exactly k characters s... |
