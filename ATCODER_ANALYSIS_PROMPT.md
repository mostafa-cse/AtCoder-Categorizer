# AtCoder Deep Problem Analysis & Curriculum Master Prompt

```markdown
<USER_REQUEST>
# AtCoder Deep Analysis → Topic Taxonomy → Quality VJudge Curriculum

You are working inside my Competitive Programming project: `AtCoder Categorizer` in Antigravity IDE.

The project contains a complete SQLite database (`data/atcoder_problems.db`) and catalog files containing all 9,782 AtCoder problems across all contests (ABC, ARC, AGC, Educational/EDPC, Typical90, etc.) with difficulty ratings from -10000 to 4300+.

Your task is to build a **world-class, high-quality, learning-oriented Competitive Programming curriculum and VJudge workbook**, processed rating-by-rating or track-by-track.

The final goal is **NOT** to blindly add every problem.
The goal is to identify the **absolute best problems that teach reusable competitive-programming techniques, algorithms, mathematical tools, structural observations, and problem-solving patterns**, while completely rejecting elementary logic building and eliminating redundant duplicate problems.

---

# 1. CORE WORKING PRINCIPLES

### Principle 1: Independent Thinking Before Editorial
For every problem, you must independently analyze and formulate a solution FIRST before reading any editorial.
Do NOT:
- Read tags first and guess the solution from tags.
- Read the editorial before attempting the problem yourself.
- Blindly copy editorial text.

### Principle 2: Anti-Waste-of-Time & Zero Duplicate Solutions Rule
- **One Core Archetype Per Topic**: For any given technique (e.g., Subtree Tree DP, Bitmask DP, Range XOR Fenwick Tree, Convex Hull Trick, 2-Pass Tree Diameter), select only the **single most important / best representative problem** (or a very small set of distinct difficulty-ladder problems).
- **Reject Duplicate Solutions**: If multiple problems share the same core trick or boilerplate solution, DO NOT add them all. Solving multiple problems with the exact same solution idea is a waste of time. Mark redundant problems as **REJECTED (DUPLICATE)** in the log and reference the primary chosen problem.
- **Reject Elementary Logic Building**: Problems focused solely on basic syntax, reading comprehension, 2D array simulation, brute-force enumeration ($N \le 100$), or routine case-work without transferable algorithmic depth MUST be **REJECTED (BASIC LOGIC BUILDING)**.

---

# 2. STANDARDIZED 3-TIER TAXONOMY

Every selected problem must be strictly classified under our standardized 3-Tier Taxonomy:

1. **Tag (Domain Level)**: One of the 11 major algorithmic domains:
   - `Dynamic Programming (DP)`
   - `Graph Theory`
   - `Data Structures (DS)`
   - `Math`
   - `Number Theory`
   - `Combinatorics`
   - `Strings`
   - `Game Theory`
   - `Geometry`
   - `Basics`
   - `Miscellaneous`

2. **Subtopic (Conceptual Framework)**:
   - Examples in DP: `Intro to DP`, `Classic DP`, `Bit Related DP`, `Dp on Different Structures`, `DP Optimizations`, `Digit DP`, `Convex Hull Trick (CHT)`.
   - Examples in Graph: `Trees`, `Connected Components`, `Shortest Paths`, `Directed Graphs`, `Network Flow`.
   - Examples in DS: `Disjoint Set Union (DSU)`, `Segment Tree / Fenwick Tree`, `Queue & Priority Queue`.

3. **Topic / Skill (Specific Algorithmic Pattern)**:
   - Examples: `DP on Trees and DAGs`, `Bitmask DP`, `O(3^N) Submask Enumeration`, `Knapsack Dual State`, `Interval DP / Minimax`, `Prefix Sum Optimized DP`, `Convex Hull Trick (CHT)`, `Tree Diameter via 2-BFS`, `Online Grid DSU`, `Binary Search on Answer / Greedy Feasibility`, `Extended Euclidean Linear Congruence`.

---

# 3. MANDATORY STEP-BY-STEP PROBLEM PIPELINE

For EVERY single problem evaluated, you MUST follow this strict 7-step sequence:

```
[1. Read Problem] ➔ [2. Analyze Structure] ➔ [3. Solve Independently] 
        ➔ [4. Read & Compare Editorial] ➔ [5. Classify Tag & Topics] 
        ➔ [6. Quality & Deduping Filter] ➔ [7. Write Analysis & Code]
```

### Step 1 — Read the Problem Carefully
- Ingest full problem statement, input/output formats, time limit, memory limit, and constraints ($N, M, K, W$, array bounds).
- Carefully examine sample test cases and explanations to understand subtleties and edge conditions.
- Record Problem ID (e.g. `dp_v`), Title, Contest ID, Rating/Difficulty, and URL.

### Step 2 — Analyze the Entire Problem Fully
- Identify hidden properties: monotonicity, optimal substructure, overlapping subproblems, symmetry, invariants, or graph transformations.
- Identify the algorithmic bottleneck: Why does a naive solution ($O(N^2), O(2^N)$) fail? What constraint tells us the required complexity ($N \le 20 \implies O(2^N)$ bitmask, $N \le 10^5 \implies O(N \log N)$ or $O(N)$)?

### Step 3 — Solve the Problem Independently
- Formulate the mathematical state, recurrence relation, or graph transformation.
- Define transitions, base cases, and boundary handling.
- Calculate exact Time Complexity and Space Complexity.
- Write a clean, optimal C++ implementation with fast I/O and zero undefined behavior.

### Step 4 — Read the Official / Community Editorial
- Read the official AtCoder editorial (and Japanese/English community write-ups).
- Compare your independent solution with the editorial:
  - Did the editorial use the same recurrence or invariant?
  - Does the editorial offer a cleaner state compression or an alternative perspective?
  - Note any special edge-case handling or alternative data structures.

### Step 5 — Identify Tag, Subtopic, and Specific Topic
- Map the problem to its canonical Tag (Domain), Subtopic, and Topic (Skill).
- If a problem combines multiple techniques (e.g. DP accelerated by Segment Tree), declare:
  - **Primary Tag & Topic**: The core paradigm (e.g. `Dynamic Programming (DP)` $\to$ `DP Optimization using Data Structures`).
  - **Secondary Tag & Topic**: The supporting tool (e.g. `Data Structures (DS)` $\to$ `Fenwick Tree`).

### Step 6 — Quality & Anti-Redundancy Filter
Evaluate the problem under the strict filter:
- **SELECTED**:
  - Teaches a distinct, reusable algorithmic technique or paradigm.
  - Represents the best/cleanest archetype of its specific skill.
  - Not redundant with any previously selected problem for that topic.
- **REJECTED (DUPLICATE)**:
  - The problem tests the exact same technique and transition as an existing selected problem with no new conceptual insight. (Document the reference problem it duplicates).
- **REJECTED (BASIC LOGIC BUILDING)**:
  - The problem requires only trivial array manipulation, string indexing, or statement-following simulation without generalizable CP algorithms.

### Step 7 — Structured Output & Documentation
If **SELECTED**:
1. Create a detailed individual markdown file: `analysis/AtCoder-<id>.md` (containing full statement summary, invariants, step-by-step algorithm, full verified C++ solution, complexity, and editorial comparison).
2. Append the problem to its specific topic file under `categories/<tag_folder>/<topic_file>.md`.
3. Add a log entry to `SELECTION_LOG.md`.
4. Add the VJudge entry `[problem:AtCoder-<id>]` to `QUALITY_PROBLEMS_BY_TOPIC.md`.

If **REJECTED**:
1. Add an entry to `SELECTION_LOG.md` detailing the exact reason for rejection (basic logic-building vs duplicate of an existing problem).

---

# 4. REQUIRED OUTPUT SCHEMAS

### Schema 1: Individual Analysis File (`analysis/AtCoder-<id>.md`)
```markdown
# Problem Analysis: AtCoder-<id> — <Title>

**Problem ID**: `AtCoder-<id>`  
**Contest**: `<contest_id>`  
**Rating / Difficulty**: <rating>  
**URL**: https://atcoder.jp/contests/<contest_id>/tasks/<id>  
**VJudge Tag**: `[problem:AtCoder-<id>]`  
**Category File**: [`../categories/<tag_folder>/<topic_file>.md`](../categories/<tag_folder>/<topic_file>.md)  

- **Tag (Domain)**: `<Tag Name>`  
- **Subtopic**: `<Subtopic Name>`  
- **Topic (Skill)**: `<Topic / Specific Skill>`  

---

## 1. Problem Statement & Key Idea
<Clear, concise summary of what the problem asks and the core mechanism>

## 2. Core Observation & Invariant
<The critical mathematical/structural insight that unlocks the solution>

## 3. Step-by-Step Algorithm
1. <Step 1>
2. <Step 2>
3. <Step 3>

## 4. Complexity Analysis
- **Time Complexity**: `O(...)`
- **Space Complexity**: `O(...)`

## 5. Complete C++ Solution
```cpp
// Production-quality, clean, well-commented C++ implementation
```

## 6. Editorial Comparison & Alignment
<Comparison between independent solution and official editorial>

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: <What generalizable concept is learned>
- **Reusable Pattern**: `<Canonical CP Code/Thinking Template>`
```

### Schema 2: Selection Log Entry (`SELECTION_LOG.md`)
```markdown
| [problem:AtCoder-<id>] | <Title> | <Rating> | **SELECTED** | <Tag> → <Topic> | Selected: Teaches <concept> (<reusable pattern>) |
| [problem:AtCoder-<id>] | <Title> | <Rating> | **REJECTED** | <Tag> → <Topic> | Rejected: Duplicate of AtCoder-<ref_id>; tests identical transition. |
| [problem:AtCoder-<id>] | <Title> | <Rating> | **REJECTED** | Basics → Implementation | Rejected: Elementary logic building / simulation without reusable algorithm. |
```

---

# 5. EXECUTION STRATEGY & PROGRESSION

1. **Batch Progression**:
   - Process problems in structured batches:
     - Batch 1: Educational DP Contest (`dp_a` through `dp_z`) — The foundational DP curriculum.
     - Batch 2: Typical90 (`typical90_001` through `typical90_090`) — Essential competitive programming patterns.
     - Batch 3: ABC Tasks D, E, F by rating band (800 → 1199, 1200 → 1599, 1600 → 1999, 2000+).
2. **Resumable Workflow**:
   - Maintain a JSON checkpoint (`state/progress.json`) tracking evaluated problem IDs.
   - Never re-evaluate already processed problems.
3. **Completion Gate**:
   - After completing each batch, summarize:
     - Problems evaluated
     - Problems selected vs rejected (with duplicate count)
     - Topics covered
     - Awaiting approval to proceed to the next batch.
</USER_REQUEST>
```
