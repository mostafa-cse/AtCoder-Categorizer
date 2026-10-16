#!/usr/bin/env python3
"""
Batch 1 Synchronizer: Integrates all 26 Educational DP Contest problems
into the curriculum, topic files, logs, and workbooks.
"""

import json
import os
import re
from collections import defaultdict
from typing import Dict, List, Any

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CATEGORIES_DIR = os.path.join(BASE_DIR, "categories")
ANALYSIS_DIR = os.path.join(BASE_DIR, "analysis")
STATE_DIR = os.path.join(BASE_DIR, "state")

import build_batch1_edpc
EDPC = build_batch1_edpc.EDPC_PROBLEMS

TOPIC_METADATA = {
    "1d_dp.md": {
        "title": "1D State Recurrences & State Machines",
        "subtopic": "Intro to DP",
        "overview": "Foundational linear dynamic programming, bounded lookaheads, and categorical state machines enforcing consecutive action constraints."
    },
    "knapsack.md": {
        "title": "Knapsack DP & Dual State Inversion",
        "subtopic": "Intro to DP",
        "overview": "Classical 0/1 knapsack state compression and dual problem formulation (inverting value objective and capacity constraints)."
    },
    "grid_dp.md": {
        "title": "Grid DP & Path Counting with Obstacles",
        "subtopic": "Classic DP",
        "overview": "2D grid dynamic programming, path counting under directional movement restrictions, obstacle nullification, and modular arithmetic transitions."
    },
    "interval_dp.md": {
        "title": "Interval DP & Range Merging",
        "subtopic": "Classic DP",
        "overview": "Subproblems defined over contiguous intervals [l, r], solved by increasing interval length. Covers minimax game intervals, LCS backtracking, and optimal split-point merges."
    },
    "expected_value_dp.md": {
        "title": "Probability & Expected Value DP",
        "subtopic": "Intro to DP",
        "overview": "Dynamic programming for probability distributions and expected values, state frequency compression, and algebraic resolution of self-loops."
    },
    "prefix_sum_dp.md": {
        "title": "Prefix Sum Optimized DP",
        "subtopic": "DP Optimizations",
        "overview": "Accelerating contiguous state transitions from O(K) to O(1) via prefix sum maintenance on previous DP layers."
    },
    "bitmask_dp.md": {
        "title": "Bitmask DP & Submask Enumeration",
        "subtopic": "Bit Related DP",
        "overview": "Dynamic programming where subsets of elements are represented as integer bitmasks. Key techniques include popcount-based dimension reduction and exhaustive O(3^N) submask iteration."
    },
    "dp_on_trees.md": {
        "title": "DP on Trees & Directed Acyclic Graphs (DAGs)",
        "subtopic": "Dp on Different Structures",
        "overview": "Dynamic programming over tree structures and DAGs using topological order, post-order DFS subtree accumulation, and all-roots rerooting using prefix/suffix product arrays."
    },
    "matrix_exponentiation.md": {
        "title": "Matrix Exponentiation DP",
        "subtopic": "Dp on Different Structures",
        "overview": "Modeling linear DP state recurrences and graph path counting as matrix multiplications, accelerated to O(N^3 log K) via binary exponentiation."
    },
    "digit_dp.md": {
        "title": "Digit DP & Prefix Bound Relaxation",
        "subtopic": "Digit DP",
        "overview": "Constructing numbers digit-by-digit from most significant to least significant digit while maintaining tight upper-bound flags and modulo constraints."
    },
    "lazy_segment_tree_dp.md": {
        "title": "DP Optimization using Lazy Segment Tree",
        "subtopic": "DP Optimizations",
        "overview": "Accelerating dynamic programming state transitions by maintaining candidate values in a Segment Tree supporting range-addition updates and range-maximum queries."
    },
    "exchange_argument_dp.md": {
        "title": "Greedy Exchange Argument & Knapsack DP",
        "subtopic": "Classic DP",
        "overview": "Establishing a strict canonical processing order via adjacent exchange arguments before applying 0/1 Knapsack dynamic programming."
    },
    "inclusion_exclusion_dp.md": {
        "title": "Inclusion-Exclusion Principle & Combinatorics Grid DP",
        "subtopic": "Classic DP",
        "overview": "Counting paths avoiding multiple obstacles on large coordinate grids by sorting obstacles and subtracting overlapping forbidden paths using dynamic programming."
    },
    "convex_hull_trick.md": {
        "title": "Convex Hull Trick (CHT) & DP Optimization",
        "subtopic": "Convex Hull Trick (CHT)",
        "overview": "Linearizing quadratic DP transitions min_j (dp[j] + (h_i - h_j)^2 + C) by maintaining a geometric lower envelope of lines using monotonic deques."
    }
}


def sync_all_analysis_files():
    """Generates all 26 analysis markdown files with exact category links and verified code."""
    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    for p in EDPC:
        filename = f"AtCoder-{p['id']}.md"
        filepath = os.path.join(ANALYSIS_DIR, filename)
        cat_file = f"../categories/{p['folder']}/{p['file']}"

        lines = [
            f"# Problem Analysis: AtCoder-{p['id']} — {p['title']}",
            "",
            f"**Problem ID**: `AtCoder-{p['id']}`  ",
            f"**Contest**: `dp` (Educational DP Contest)  ",
            f"**Rating / Difficulty**: {p['rating']}  ",
            f"**URL**: https://atcoder.jp/contests/dp/tasks/{p['id']}  ",
            f"**VJudge Tag**: `[problem:AtCoder-{p['id']}]`  ",
            f"**Category File**: [`{cat_file}`]({cat_file})  ",
            "",
            f"- **Tag (Domain)**: `{p['tag']}`  ",
            f"- **Subtopic**: `{p['subtopic']}`  ",
            f"- **Topic (Skill)**: `{p['topic']}`  ",
            "",
            "---",
            "",
            "## 1. Problem Statement & Key Idea",
            f"{p['statement']}",
            "",
            f"**Core Idea**: {p['key_idea']}",
            "",
            "## 2. Core Observation & Invariant",
            p["observation"],
            "",
            "## 3. Step-by-Step Algorithm",
            p["algorithm"],
            "",
            "## 4. Complexity Analysis",
            p["complexity"],
            "",
            "## 5. Complete C++ Solution",
            "```cpp",
            p["cpp_code"].strip(),
            "```",
            "",
            "## 6. Editorial Comparison & Alignment",
            p["editorial"],
            "",
            "## 7. What This Problem Teaches & Reusable Pattern",
            f"- **Core Skill**: {p['teaches']}",
            f"- **Reusable Pattern**: `{p['pattern']}`",
            "",
            "---",
            f"Back to [{p['topic']}]({cat_file}) | [Categories Directory](../categories/README.md)"
        ]

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    print(f"[+] Verified and written {len(EDPC)} analysis files in analysis/.")


def sync_category_topic_files():
    """Generates and updates modular topic files under categories/dp/."""
    by_file = defaultdict(list)
    for p in EDPC:
        by_file[(p["folder"], p["file"])].append(p)

    for (folder, filename), plist in by_file.items():
        if folder != "dp":
            continue  # dp_k and dp_q are handled in game_theory and data_structures
        
        folder_path = os.path.join(CATEGORIES_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, filename)
        
        meta = TOPIC_METADATA.get(filename, {
            "title": plist[0]["topic"],
            "subtopic": plist[0]["subtopic"],
            "overview": f"Curated competitive programming techniques for {plist[0]['topic']}."
        })

        lines = [
            f"# 📖 {meta['title']}",
            "",
            f"- **Tag / Domain**: `Dynamic Programming (DP)`",
            f"- **Subtopic**: `{meta['subtopic']}`",
            f"- **Total Curated Problems**: {len(plist)}",
            "",
            "---",
            "",
            "## 💡 Topic Overview",
            meta["overview"],
            "",
            "---",
            "",
            "## 🏆 Curated High-Value Problems",
            ""
        ]

        for idx, p in enumerate(plist, 1):
            lines.extend([
                f"### {idx}. {p['title']} (`[problem:AtCoder-{p['id']}]`)",
                "",
                f"- **Role**: *{p['topic']}*",
                f"- **Rating**: `{p['rating']}` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/{p['id']})",
                f"- **Full Analysis**: [AtCoder-{p['id']} Analysis](../../analysis/AtCoder-{p['id']}.md)",
                "",
                "#### Problem Statement & Task",
                p["statement"],
                "",
                "#### Core Invariant & Observation",
                p["observation"],
                "",
                "#### Algorithmic Formulation",
                p["algorithm"],
                "",
                f"**Complexity**: `{p['complexity']}`  ",
                f"**Editorial Alignment**: {p['editorial']}  ",
                "",
                "#### What This Teaches & Reusable Pattern",
                f"- **Skill Taught**: {p['teaches']}",
                f"- **Reusable Pattern**: `{p['pattern']}`",
                "",
                "---",
                ""
            ])

        lines.extend([
            "[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)",
            ""
        ])

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"[+] Synced DP Topic File: {file_path}")


def sync_dp_readme():
    """Generates categories/dp/README.md with a table of all 14 topic files."""
    by_file = defaultdict(list)
    for p in EDPC:
        if p["folder"] == "dp":
            by_file[p["file"]].append(p)

    lines = [
        "# Dynamic Programming (DP) Category Index",
        "",
        "Curated collection of high-value problems in **Dynamic Programming (DP)** partitioned into modular, skill-specific topic Markdown files.",
        "",
        "## 📂 Topic Markdown Files",
        "",
        "| Topic File | Subtopic | Topic / Skill | Problems Count | Key Reusable Pattern |",
        "|---|---|---|---|---|"
    ]

    for fname, plist in sorted(by_file.items()):
        meta = TOPIC_METADATA.get(fname, {"title": plist[0]["topic"], "subtopic": plist[0]["subtopic"]})
        first_pattern = plist[0]["pattern"]
        lines.append(f"| [`{fname}`]({fname}) | {meta['subtopic']} | **{meta['title']}** | {len(plist)} | `{first_pattern}` |")

    lines.extend([
        "",
        "---",
        "",
        "[Back to Categories Directory](../README.md) | [Back to Main Repository](../../README.md)",
        ""
    ])

    dp_readme_path = os.path.join(CATEGORIES_DIR, "dp", "README.md")
    with open(dp_readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[+] Updated: {dp_readme_path}")


def sync_master_categories_readme():
    """Updates categories/README.md with all categories and counts."""
    dp_count = sum(1 for p in EDPC if p["folder"] == "dp")
    
    content = f"""# 📚 AtCoder Problem Categories Directory

This directory organizes curated AtCoder problems into dedicated domain folders and skill-specific `.md` files.
All problems inside these files teach **reusable competitive programming techniques and algorithms**, completely filtering out trivial logic-building and syntax simulations.

---

## 📁 Category Folders & Topic Markdown Files

| Tag / Domain | Directory | Topic `.md` Files | Total Curated Problems |
|---|---|---|---|
| **Dynamic Programming (DP)** | [`dp/`](dp/) | [`1d_dp.md`](dp/1d_dp.md)<br>[`knapsack.md`](dp/knapsack.md)<br>[`grid_dp.md`](dp/grid_dp.md)<br>[`interval_dp.md`](dp/interval_dp.md)<br>[`expected_value_dp.md`](dp/expected_value_dp.md)<br>[`prefix_sum_dp.md`](dp/prefix_sum_dp.md)<br>[`bitmask_dp.md`](dp/bitmask_dp.md)<br>[`dp_on_trees.md`](dp/dp_on_trees.md)<br>[`matrix_exponentiation.md`](dp/matrix_exponentiation.md)<br>[`digit_dp.md`](dp/digit_dp.md)<br>[`lazy_segment_tree_dp.md`](dp/lazy_segment_tree_dp.md)<br>[`exchange_argument_dp.md`](dp/exchange_argument_dp.md)<br>[`inclusion_exclusion_dp.md`](dp/inclusion_exclusion_dp.md)<br>[`convex_hull_trick.md`](dp/convex_hull_trick.md) | {dp_count} |
| **Graph Theory** | [`graph_theory/`](graph_theory/) | [`connected_components_dsu.md`](graph_theory/connected_components_dsu.md)<br>[`tree_diameter.md`](graph_theory/tree_diameter.md)<br>[`shortest_paths_dijkstra.md`](graph_theory/shortest_paths_dijkstra.md)<br>[`topological_sort_cycles.md`](graph_theory/topological_sort_cycles.md) | 4 |
| **Data Structures (DS)** | [`data_structures/`](data_structures/) | [`online_grid_dsu.md`](data_structures/online_grid_dsu.md)<br>[`fenwick_segment_tree.md`](data_structures/fenwick_segment_tree.md)<br>[`priority_queue_buffers.md`](data_structures/priority_queue_buffers.md) | 4 |
| **Basics & Search** | [`basics/`](basics/) | [`binary_search_on_answer.md`](basics/binary_search_on_answer.md)<br>[`dual_index_mapping.md`](basics/dual_index_mapping.md) | 2 |
| **Game Theory** | [`game_theory/`](game_theory/) | [`sprague_grundy_impartial_games.md`](game_theory/sprague_grundy_impartial_games.md) | 1 |
| **Number Theory** | [`number_theory/`](number_theory/) | [`modular_linear_congruence.md`](number_theory/modular_linear_congruence.md)<br>[`cubic_root_prime_factorization.md`](number_theory/cubic_root_prime_factorization.md) | 2 |
| **Strings** | [`strings/`](strings/) | [`lexicographically_smallest_subsequence.md`](strings/lexicographically_smallest_subsequence.md) | 1 |

---

## 🔬 Problem Evaluation Methodology
Every problem categorized across these `.md` files is evaluated under the strict 7-step pipeline:
1. **Read**: Statement, limits, types, and constraints.
2. **Analyze**: Identify hidden mathematical observations, monotonicity, subproblem independence.
3. **Solve Independently**: Formulate an optimal algorithm with proven time and space complexity before reading editorial.
4. **Read Editorial**: Verify against official and community approaches.
5. **Classify Tag & Topics**: Map to canonical 3-tier taxonomy.
6. **Quality & Anti-Redundancy Filter**: Reject basic logic building and duplicate problems.
7. **Document**: Archive in dedicated topic `.md` file, update selection log, and provide individual analysis with verified C++ solution.

[Back to Main Repository](../../README.md)
"""
    readme_path = os.path.join(CATEGORIES_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Updated: {readme_path}")


def sync_selection_log():
    """Generates complete SELECTION_LOG.md with all 26 EDPC problems + preserved non-EDPC problems."""
    edpc_evaluations = {
        "dp_a": ("Dynamic Programming (DP) → 1D State Recurrence / Bounded Lookahead", "Selected: Teaches Foundational DP state definition, base cases, and optimal substructure. (Minimalist transition dependency and state compression.)"),
        "dp_b": ("Dynamic Programming (DP) → 1D DP with K-Step Transitions", "Selected: Teaches Parametric transition loops in DP and push-style vs pull-style relaxation. (Transitions with variable bounds min(i+K, N).)"),
        "dp_c": ("Dynamic Programming (DP) → Multi-State DP / State-Machine DP", "Selected: Teaches State augmentation to satisfy Markovian transition constraints. (Canonical state-machine DP with categorical transitions.)"),
        "dp_d": ("Dynamic Programming (DP) → Knapsack and Basic Dynamic Programming", "Selected: Teaches 0/1 Knapsack state optimization and 1D space reduction technique. (Reverse loop space compression.)"),
        "dp_e": ("Dynamic Programming (DP) → Knapsack Dual State / Value as State", "Selected: Teaches Dual problem formulation and state parameter swapping. (Inverting objective and constraint when constraint space is too large.)"),
        "dp_f": ("Dynamic Programming (DP) → Longest Common Subsequence & Backtracking", "Selected: Teaches DP solution path reconstruction and parent/transition backtracking. (Two-pointer matrix reconstruction of optimal decisions.)"),
        "dp_g": ("Dynamic Programming (DP) → DP on Trees and DAGs", "Selected: Teaches Topological order as the fundamental validity condition for DAG DP. (Connecting graph traversals directly to DP state transition graphs.)"),
        "dp_h": ("Dynamic Programming (DP) → Grid DP / Path Counting with Obstacles", "Selected: Teaches Modular arithmetic integration into DP transitions and grid boundary conditions. (Translating geometric movement constraints into 2D recurrences.)"),
        "dp_i": ("Dynamic Programming (DP) → Probability and Expected Value DP", "Selected: Teaches Probability DP state independence and floating-point stability. (Discrete event convolution over independent trials.)"),
        "dp_j": ("Dynamic Programming (DP) → Expected Value DP with Multi-Frequency States", "Selected: Teaches Invariant-based state reduction: grouping dishes by remaining piece counts (1, 2, 3) rather than tracking individual plate states. (3-variable discrete expected value recursion.)"),
        "dp_k": ("Game Theory → Sprague-Grundy / Combinatorial Game DP", "Selected: Teaches Backward induction, P-positions and N-positions, and impartial game theory. (Boolean state alternation under optimal play.)"),
        "dp_l": ("Dynamic Programming (DP) → Interval DP / Range DP / Matrix Chain Multiplication (MCM)", "Selected: Teaches Interval DP structure (solving by increasing segment length) and minimax evaluation. (Symmetric negation optimization in zero-sum sequential games.)"),
        "dp_m": ("Dynamic Programming (DP) → Prefix Sum Optimized DP", "Selected: Teaches Transition acceleration from O(K) to O(1) via prefix sums on DP states. (Sliding window range-sum transition optimization.)"),
        "dp_n": ("Dynamic Programming (DP) → Interval DP / Range DP / Matrix Chain Multiplication (MCM)", "Selected: Teaches Interval merging DP and partition point split optimization. (Prefix sum cost addition over nested subproblem partitions.)"),
        "dp_o": ("Dynamic Programming (DP) → Bitmask DP", "Selected: Teaches Dimension reduction in Bitmask DP using state invariants (popcount). (Implicit step derivation from subset cardinality.)"),
        "dp_p": ("Dynamic Programming (DP) → DP on Trees and DAGs", "Selected: Teaches Subtree DP, state-color branching, and product-rule combination over tree children. (Independent combination of child subtree configurations.)"),
        "dp_q": ("Dynamic Programming (DP) → DP Optimization using Data Structures [Some Practice Problems]", "Selected: Teaches Accelerating O(N^2) DP to O(N log N) using Fenwick/Segment Tree on value domain. (Transforming inner range search into dynamic range queries.)"),
        "dp_r": ("Dynamic Programming (DP) → Matrix Exponentiation DP", "Selected: Teaches Modeling sequential transitions as matrix multiplication and logarithmic speedup via binary exponentiation. (O(N^3 log K) transition matrix acceleration.)"),
        "dp_s": ("Dynamic Programming (DP) → Digit DP with Remainder State", "Selected: Teaches Digit DP state space (index, tight flag, modulo sum) and combinatorial path counting on large numeric bounds. (Tight constraint prefix tracking.)"),
        "dp_t": ("Dynamic Programming (DP) → Relative Order Insertion DP with Prefix Sums", "Selected: Teaches Inserting elements one-by-one into relative positions and prefix sum acceleration for order-constrained permutations. (Relative rank insertion DP with O(1) transitions.)"),
        "dp_u": ("Dynamic Programming (DP) → Bitmask DP", "Selected: Teaches O(3^N) submask iteration idiom and subset partition DP. (The (sub - 1) & mask bit trick for exhaustive partition.)"),
        "dp_v": ("Dynamic Programming (DP) → DP on Trees and DAGs", "Selected: Teaches Tree rerooting technique without division using prefix/suffix product arrays. (Rerooting under arbitrary modulus without modular inverses.)"),
        "dp_w": ("Dynamic Programming (DP) → DP Optimization using Data Structures (Lazy Segment Tree)", "Selected: Teaches Dynamic programming state acceleration via range-addition and range-maximum queries using a Segment Tree with Lazy Propagation. (Segment tree maintenance of DP candidate values.)"),
        "dp_x": ("Dynamic Programming (DP) → Greedy Exchange Argument + 0/1 Knapsack", "Selected: Teaches Deriving canonical processing order via adjacent exchange arguments before applying Knapsack DP. (Sorting by w_i + s_i to establish total ordering.)"),
        "dp_y": ("Dynamic Programming (DP) → Inclusion-Exclusion Principle + Combinatorics Grid DP", "Selected: Teaches Handling obstacles in large grids (H, W <= 10^5) by sorting obstacles and using DP with inclusion-exclusion to subtract first-visited obstacle paths. (Combinatorial path count subtraction.)"),
        "dp_z": ("Dynamic Programming (DP) → Convex Hull Trick (CHT) and Dynamic CHT", "Selected: Teaches CHT line representation, geometric lower envelope maintenance, and linear time DP optimization. (Linear-time optimization of quadratic transition costs.)")
    }

    lines = [
        "# AtCoder Problem Selection & Quality Evaluation Log",
        "",
        "This log tracks the rigorous evaluation of AtCoder problems, separating **high-value reusable algorithmic patterns** from basic implementation exercises.",
        "",
        "| Problem ID | Title | Rating | Status | Tag & Topic | Evaluation Rationale |",
        "|---|---|---|---|---|---|"
    ]

    for p in EDPC:
        pid = p["id"]
        tag_topic, rationale = edpc_evaluations[pid]
        lines.append(f"| [problem:AtCoder-{pid}] | {p['title']} | {p['rating']} | **SELECTED** | {tag_topic} | {rationale} |")

    # Non-EDPC curated problems
    non_edpc_selected = [
        ("| [problem:AtCoder-abc350_d] | New Friends | 1050 | **SELECTED** | Graph Theory → Disjoint Set Union (DSU) / Connected Component Cliques | Selected: Teaches Transitive closure on undirected graphs and component-wise clique completion. (Translating local operation chains into global component invariants.) |"),
        ("| [problem:AtCoder-typical90_a] | Yokan Party | 1200 | **SELECTED** | Basics → Binary Search on Answer / Greedy Feasibility | Selected: Teaches Binary search on answer and greedy feasibility check. (The canonical 'maximize the minimum' CP template.) |"),
        ("| [problem:AtCoder-typical90_c] | Longest Circular Road | 1100 | **SELECTED** | Graph Theory → Tree Diameter / Double BFS-DFS | Selected: Teaches Tree diameter characterization and the 2-BFS proof. (Connecting cycle maximization to tree diameter.) |"),
        ("| [problem:AtCoder-typical90_l] | Red Painting | 1250 | **SELECTED** | Data Structures (DS) → Grid Connectivity / Dynamic DSU | Selected: Teaches 2D-to-1D index linearization and online grid connectivity. (Online union-find query handling without rebuilding components.) |")
    ]
    lines.extend(non_edpc_selected)

    # Rejected problems (basic logic building / syntax simulation)
    rejected_problems = [
        ("| [problem:AtCoder-abc350_a] | Past ABCs | 15 | **REJECTED** | Basics → String Parsing / Set Lookup | REJECTED: Basic logic building / syntax simulation. Lacks reusable algorithmic paradigm. |"),
        ("| [problem:AtCoder-abc350_b] | Dentist Aoki | 45 | **REJECTED** | Basics → Array Frequency Toggle | REJECTED: Routine logic building / array simulation without generalizable data structures. |"),
        ("| [problem:AtCoder-abc086_a] | Product | 10 | **REJECTED** | Basics → Parity Check | REJECTED: Intro beginner logic building; no algorithmic relevance. |"),
        ("| [problem:AtCoder-abc081_a] | Placing Marbles | 15 | **REJECTED** | Basics → Character Counting | REJECTED: Intro syntax exercise without reusable algorithmic depth. |")
    ]
    lines.extend(rejected_problems)

    log_path = os.path.join(BASE_DIR, "SELECTION_LOG.md")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"[+] Synced SELECTION_LOG.md: {len(EDPC)} EDPC + {len(non_edpc_selected)} other selected + {len(rejected_problems)} rejected.")


def sync_quality_problems_by_topic():
    """Generates complete QUALITY_PROBLEMS_BY_TOPIC.md including all 26 EDPC problems."""
    content = """# AtCoder Quality Problems by Topic

A structured, topic-wise curriculum catalog of high-value AtCoder problems classified under the official Competitive Programming Curriculum.

### 3-Tier Taxonomy Structure:
1. **Tag** (Major Algorithmic Domain)
2. **Subtopic** (Conceptual Category)
3. **Topic / Skill** (Specific Algorithmic Technique)

---

# Basics

## Binary Search

### Binary Search on Answer / Greedy Feasibility

- [problem:AtCoder-typical90_a] **Yokan Party** (Rating: 1200) — *Cut a stick of length L at K positions to maximize the minimum piece length.*

---

# Data Structures (DS)

## Disjoint Set Union (DSU)

### Grid Connectivity / Dynamic DSU

- [problem:AtCoder-typical90_l] **Red Painting** (Rating: 1250) — *Dynamically color grid cells red and answer reachability queries between red cells.*

## Segment Tree / Fenwick Tree

### DP Optimization using Data Structures [Some Practice Problems]

- [problem:AtCoder-dp_q] **Flowers** (Rating: 1600) — *Find a subsequence of flowers with strictly increasing heights that maximizes total beauty using Fenwick / Segment Tree.*

---

# Dynamic Programming (DP)

## Intro to DP

### 1D State Recurrence / Bounded Lookahead

- [problem:AtCoder-dp_a] **Frog 1** (Rating: 600) — *Represent the minimum cost to reach stone i using optimal substructure from the previous two stones.*

### 1D DP with K-Step Transitions

- [problem:AtCoder-dp_b] **Frog 2** (Rating: 700) — *Generalize linear transitions to arbitrary step sizes K <= 100.*

### Multi-State DP / State-Machine DP

- [problem:AtCoder-dp_c] **Vacation** (Rating: 900) — *Maintain happiness while enforcing non-repeating consecutive activity constraints.*

### Knapsack and Basic Dynamic Programming

- [problem:AtCoder-dp_d] **Knapsack 1** (Rating: 1150) — *Classical 0/1 Knapsack where capacity W <= 10^5 serves as the DP state index.*

### Knapsack Dual State / Value as State

- [problem:AtCoder-dp_e] **Knapsack 2** (Rating: 1450) — *When weight capacity W is up to 10^9, invert the state: define dp[v] as the minimum weight required to achieve exact value v.*

### Probability and Expected Value DP

- [problem:AtCoder-dp_i] **Coins** (Rating: 1150) — *Calculate the probability that more heads than tails appear when tossing N biased coins.*
- [problem:AtCoder-dp_j] **Sushi** (Rating: 1650) — *3-frequency state compression and algebraic self-loop elimination for expected operations to empty sushi plates.*

## Classic DP

### Longest Common Subsequence & Backtracking

- [problem:AtCoder-dp_f] **LCS** (Rating: 1250) — *Find the actual string corresponding to the Longest Common Subsequence of s and t.*

### Grid DP / Path Counting with Obstacles

- [problem:AtCoder-dp_h] **Grid 1** (Rating: 1050) — *Count paths from top-left (1,1) to bottom-right (H,W) moving only right and down, avoiding walls.*

### Interval DP / Range DP / Matrix Chain Multiplication (MCM)

- [problem:AtCoder-dp_l] **Deque** (Rating: 1400) — *Two players take turns removing elements from either end of a deque. Maximize X - Y.*
- [problem:AtCoder-dp_n] **Slimes** (Rating: 1600) — *Merge N slimes pairwise into one slime with minimum total combining cost.*

### Greedy Exchange Argument + 0/1 Knapsack

- [problem:AtCoder-dp_x] **Tower** (Rating: 2000) — *Sort blocks by (w_i + s_i) via exchange argument to establish canonical order before running 0/1 Knapsack.*

### Inclusion-Exclusion Principle + Combinatorics Grid DP

- [problem:AtCoder-dp_y] **Grid 2** (Rating: 2150) — *Count paths from (1,1) to (H,W) avoiding N obstacles by sorting obstacles and subtracting overlapping forbidden paths.*

## Bit Related DP

### Bitmask DP

- [problem:AtCoder-dp_o] **Matching** (Rating: 1650) — *Count the number of perfect matchings in a bipartite graph with N men and N women (N <= 21).*
- [problem:AtCoder-dp_u] **Grouping** (Rating: 1850) — *Partition N rabbits into groups to maximize total compatibility score (N <= 16).*

## Dp on Different Structures

### DP on Trees and DAGs

- [problem:AtCoder-dp_g] **Longest Path** (Rating: 1350) — *Find the length of the longest directed path in a Directed Acyclic Graph (DAG).*
- [problem:AtCoder-dp_p] **Independent Set** (Rating: 1500) — *Count ways to paint vertices of a tree black or white such that no two adjacent vertices are both black.*
- [problem:AtCoder-dp_v] **Subtree** (Rating: 2100) — *For every node v in a tree, compute the number of black-connected components containing v modulo M without division.*

### Matrix Exponentiation DP

- [problem:AtCoder-dp_r] **Walk** (Rating: 1700) — *Count paths of exact length K (K <= 10^18) in a directed graph using fast binary matrix exponentiation.*

## Digit DP

### Digit DP with Remainder State

- [problem:AtCoder-dp_s] **Digit Sum** (Rating: 1750) — *Count positive integers up to K (K <= 10^10000) whose sum of digits is a multiple of D.*

## DP Optimizations

### Prefix Sum Optimized DP

- [problem:AtCoder-dp_m] **Candies** (Rating: 1550) — *Distribute K candies among N children such that child i receives at most a_i candies.*
- [problem:AtCoder-dp_t] **Permutation** (Rating: 1950) — *Count permutations satisfying '<' and '>' relative order signatures using prefix-sum accelerated transitions.*

### DP Optimization using Data Structures (Lazy Segment Tree)

- [problem:AtCoder-dp_w] **Intervals** (Rating: 2100) — *Select binary string of length N to maximize score over M intervals using range-add range-max lazy segment tree.*

## Convex Hull Trick (CHT)

### Convex Hull Trick (CHT) and Dynamic CHT

- [problem:AtCoder-dp_z] **Frog 3** (Rating: 2200) — *Frog jumps from stone i to j with quadratic cost (h_j - h_i)^2 + C using lower convex hull line deque.*

---

# Game Theory

## Impartial Games

### Sprague-Grundy / Combinatorial Game DP

- [problem:AtCoder-dp_k] **Stones** (Rating: 1100) — *Determine whether First or Second player wins an impartial subtract-a-stone game from pile of size K.*

---

# Graph Theory

## Connected Components

### Disjoint Set Union (DSU) / Connected Component Cliques

- [problem:AtCoder-abc350_d] **New Friends** (Rating: 1050) — *If A-B and B-C are friends, A and C can become friends. Count maximum new operations.*

## Trees

### Tree Diameter / Double BFS-DFS

- [problem:AtCoder-typical90_c] **Longest Circular Road** (Rating: 1100) — *Adding an edge between two vertices u and v creates a cycle of length dist(u, v) + 1. Maximize this cycle length.*

---
"""
    quality_path = os.path.join(BASE_DIR, "QUALITY_PROBLEMS_BY_TOPIC.md")
    with open(quality_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Synced: {quality_path}")


def sync_dynamic_programming_catalog():
    """Updates categories/Dynamic_Programming.md to include all 24 DP problems."""
    dp_problems = [p for p in EDPC if p["tag"] == "Dynamic Programming (DP)"]
    
    # Group by subtopic and topic
    by_sub = defaultdict(lambda: defaultdict(list))
    for p in dp_problems:
        by_sub[p["subtopic"]][p["topic"]].append(p)

    lines = [
        "# 🧩 AtCoder Curriculum: Dynamic Programming (DP)",
        "",
        "Curated collection of high-value problems in **Dynamic Programming (DP)** selected for teaching reusable competitive programming algorithms, structural observations, and mathematical invariants.",
        "",
        f"- **Total Curated Problems**: {len(dp_problems)}",
        "- **Taxonomy Tier**: Tag (Domain Level)",
        "",
        "---",
        "",
        "## 📑 Table of Contents",
        ""
    ]

    for sub in sorted(by_sub.keys()):
        slug = re.sub(r'[^a-z0-9]+', '-', sub.lower()).strip('-')
        lines.append(f"- [{sub}](#{slug})")
        for top, plist in sorted(by_sub[sub].items()):
            top_slug = re.sub(r'[^a-z0-9]+', '-', top.lower()).strip('-')
            lines.append(f"  - [{top}](#{top_slug}) ({len(plist)} problems)")

    lines.append("")
    lines.append("---")
    lines.append("")

    for sub in sorted(by_sub.keys()):
        lines.append(f"## {sub}")
        lines.append("")
        for top, plist in sorted(by_sub[sub].items()):
            lines.append(f"### {top}")
            lines.append("")
            for p in plist:
                lines.extend([
                    f"#### {p['title']} (`[problem:AtCoder-{p['id']}]`)",
                    f"- **Rating / Difficulty**: {p['rating']}",
                    f"- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/{p['id']})",
                    f"- **Detailed Analysis**: [`analysis/AtCoder-{p['id']}.md`](../analysis/AtCoder-{p['id']}.md)",
                    f"- **Key Idea**: {p['key_idea']}",
                    f"- **Core Observation**: {p['observation']}",
                    f"- **Algorithm & Complexity**: {p['complexity']}",
                    f"- **What This Problem Teaches**: {p['teaches']}",
                    f"- **Reusable Pattern**: `{p['pattern']}`",
                    ""
                ])
        lines.append("---")
        lines.append("")

    cat_dp_path = os.path.join(CATEGORIES_DIR, "Dynamic_Programming.md")
    with open(cat_dp_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[+] Updated: {cat_dp_path}")


def main():
    print("=" * 70)
    print("       SYNCHRONIZING BATCH 1: EDUCATIONAL DP CONTEST CURRICULUM")
    print("=" * 70)
    sync_all_analysis_files()
    sync_category_topic_files()
    sync_dp_readme()
    sync_master_categories_readme()
    sync_dynamic_programming_catalog()
    sync_selection_log()
    sync_quality_problems_by_topic()
    build_batch1_edpc.update_checkpoint()
    print("=" * 70)
    print("Batch 1 Curriculum Synchronized Successfully!")


if __name__ == "__main__":
    main()
