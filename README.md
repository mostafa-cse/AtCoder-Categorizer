# AtCoder Problem Categorizer & Deep Learning Analysis

This repository maintains the curated competitive programming curriculum for **[AtCoder](https://atcoder.jp/)**, categorizing high-value problems by **Tag (Domain)**, **Subtopic**, and **Topic (Skill)** using a standardized 3-Tier Taxonomy.

---

## 🎯 Core Curriculum Principle

Problems are evaluated under a strict filter:
- **SELECTED**: Problems that teach reusable competitive programming algorithms, mathematical invariants, structural observations, and optimization paradigms (e.g., Tree DP, Bitmask DP, Range DP, DSU, Segment Tree, Binary Search on Answer, Convex Hull Trick).
- **REJECTED**: Problems focused solely on basic logic building, syntax practice, trivial brute-force, or problem-statement rule simulation without transferable algorithmic depth.

---

## 🔬 Step-by-Step Problem Evaluation Protocol

Every problem in this repository undergoes the exhaustive evaluation pipeline:
1. **Read**: Ingest the problem statement, time/memory limits, and input/output constraints.
2. **Analyze**: Identify hidden mathematical observations, monotonicity, subproblem independence, or structural invariants.
3. **Solve**: Formulate an optimal algorithm with proven time and space complexity.
4. **Identify Tag & Topics**: Map the solution onto the standardized 3-Tier Taxonomy:
   - **Tag**: e.g., `Dynamic Programming (DP)`, `Graph Theory`, `Data Structures (DS)`
   - **Subtopic**: e.g., `Bit Related DP`, `Connected Components`, `Convex Hull Trick`
   - **Topic / Skill**: e.g., `Bitmask DP`, `Disjoint Set Union (DSU)`, `DP on Trees and DAGs`
5. **Read Editorial**: Compare independent findings against official and community editorials to capture alternative solutions or edge-case simplifications.
6. **Finalize**: Commit the problem analysis to [`PROBLEM_ANALYSIS.md`](file:///c:/Users/m0stafakamal/Desktop/AtCoder%20Categorizer/PROBLEM_ANALYSIS.md), record selection/rejection in [`SELECTION_LOG.md`](file:///c:/Users/m0stafakamal/Desktop/AtCoder%20Categorizer/SELECTION_LOG.md), and append to [`QUALITY_PROBLEMS_BY_TOPIC.md`](file:///c:/Users/m0stafakamal/Desktop/AtCoder%20Categorizer/QUALITY_PROBLEMS_BY_TOPIC.md).

---

## 📁 Repository Structure

| File / Folder | Description |
|---|---|
| [`categories/`](categories/) | Category-specific `.md` files organized by domain (DP, Graph Theory, DS, etc.). |
| ↳ [`categories/Dynamic_Programming.md`](categories/Dynamic_Programming.md) | 🧩 Dynamic Programming: Bitmask, Tree DP, CHT, Interval DP, Knapsack, Digit DP, etc. |
| ↳ [`categories/Graph_Theory.md`](categories/Graph_Theory.md) | 🕸️ Graph Theory: Trees, Diameter, DSU, Dijkstra, Shortest Paths, Cycles. |
| ↳ [`categories/Data_Structures.md`](categories/Data_Structures.md) | 🌲 Data Structures: Fenwick Tree, Segment Tree, Online DSU Grid Connectivity. |
| ↳ [`categories/Basics.md`](categories/Basics.md) | ⚡ Basics & Search: Binary Search on Answer, Dual Mapping, Invariants. |
| ↳ [`categories/Game_Theory.md`](categories/Game_Theory.md) | ♟️ Game Theory: Sprague-Grundy, Minimax, Backward Induction. |
| ↳ [`categories/Number_Theory.md`](categories/Number_Theory.md) | 🔢 Number Theory: Extended GCD, Modular Congruences, Cubic-Root Factorization. |
| ↳ [`categories/Strings.md`](categories/Strings.md) | 🔤 Strings: Next-Occurrence Array, Lexicographically Smallest Subsequences. |
| [`analysis/`](analysis/) | Individual problem `.md` analyses with complete step-by-step breakdowns. |
| [`QUALITY_PROBLEMS_BY_TOPIC.md`](QUALITY_PROBLEMS_BY_TOPIC.md) | Master VJudge-compatible workbook organized by Tag, Subtopic, and Topic. |
| [`PROBLEM_ANALYSIS.md`](PROBLEM_ANALYSIS.md) | In-depth breakdown covering Key Ideas, Invariants, Algorithms, Complexity, and Editorial comparisons. |
| [`SELECTION_LOG.md`](SELECTION_LOG.md) | Exhaustive evaluation audit log with status (`SELECTED` vs `REJECTED`) and rationales. |
| [`taxonomy_3tier.json`](taxonomy_3tier.json) | Canonical 3-Tier taxonomy mapping all 11 major algorithmic domains and 576 numbered skills. |
| [`categorize_atcoder.py`](categorize_atcoder.py) | Automated curriculum compiler that builds and updates all documentation files. |
| [`data/atcoder_problems.db`](data/atcoder_problems.db) | Full relational SQLite database of 9,782+ AtCoder problems. |

---

## 🚀 Running the Compiler

To regenerate or extend the categorized curriculum:

```powershell
python categorize_atcoder.py
```
