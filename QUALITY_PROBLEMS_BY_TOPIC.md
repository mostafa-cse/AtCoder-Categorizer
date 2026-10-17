# AtCoder Quality Problems by Topic

A structured, topic-wise curriculum catalog of high-value AtCoder problems classified under the official Competitive Programming Curriculum.

### 3-Tier Taxonomy Structure:
1. **Tag** (Major Algorithmic Domain)
2. **Subtopic** (Conceptual Category)
3. **Topic / Skill** (Specific Algorithmic Technique)

---

# Basics

## Bitwise Independence

### Bitwise Independence & Bit-by-Bit Brute Force Verification

- [problem:AtCoder-typical90_ch] **Snuke's Favorite Arrays** (Rating: 1750, ★5) — *N items (N <= 12). Q conditions: A_{x} | A_{y} | A_{z} = w. Count arrays satisfying all conditions modulo 9982...*


## Complement Counting & Run-Length

### Complement Counting via Run-Length Encoding

- [problem:AtCoder-typical90_cf] **There are two types of characters** (Rating: 800, ★3) — *String S of length N with 'o' and 'x'. Count pairs (l, r) with 1 <= l < r <= N such that substring S[l..r] con...*


## Greedy & Invariants

### Corner-First Unique Determinism / 2x2 Subgrid Elimination

- [problem:AtCoder-typical90_ca] **Two by Two** (Rating: 850, ★3) — *H x W matrices A and B. In one operation, add +-1 to any 2x2 subgrid. Can A be transformed to B, and what is t...*


## Backtracking & Recursion

### Grid Simple Cycle Search via DFS Backtracking (Small N <= 16)

- [problem:AtCoder-typical90_bt] **Loop Railway Plan** (Rating: 1350, ★4) — *H x W grid with empty cells '.' and walls '#' (H, W <= 16, H*W <= 16). Find a simple cycle of length >= 3 trav...*


## Bitmask Enumeration & Pruning

### Subgrid Dimension Reduction / Row Bitmask with Column Frequency Counting

- [problem:AtCoder-typical90_bk] **Monochromatic Subgrid** (Rating: 1250, ★4) — *H x W grid (H <= 8, W <= 10^4). Select a subset of rows and columns such that all cells in the subgrid have th...*


## Ternary Search & Optimization

### Discrete Golden-Section / Fibonacci Search on Unimodal Functions

- [problem:AtCoder-typical90_ba] **Discrete Dowsing** (Rating: 2600, ★7) — *Interactive problem: array A of length N (N <= 1500) strictly increases then strictly decreases (strictly unim...*


## Meet in the Middle

### Meet-in-the-Middle with Cardinality and Value Constraints

- [problem:AtCoder-typical90_ay] **Typical Shop** (Rating: 1750, ★5) — *N items (N <= 40) with price A_i. Choose exactly K items such that total price <= P. Count ways....*


## Greedy Algorithms

### Greedy Splitting / Automatic Prerequisite Satisfaction by Diminishing Returns

- [problem:AtCoder-typical90_av] **I will not drop out** (Rating: 800, ★3) — *N problems, time limit K minutes. Problem i awards B_i points for first minute, and additional A_i - B_i point...*


## Array Transformations

### Virtual Circular Array Shift via Modulo Pointer Offset

- [problem:AtCoder-typical90_ar] **Shift and Swapping** (Rating: 800, ★3) — *Array of length N, Q queries: (1) swap A_x and A_y; (2) shift array right circularly A = (A_N, A_1, ..., A_{N-...*


## Permutations & Brute Force

### Permutation Enumeration with Adjacency Graph Pruning

- [problem:AtCoder-typical90_af] **AtCoder Ekiden** (Rating: 850, ★3) — *N runners (N <= 10) run N sections. Runner i takes A_{i, j} time for section j. M pairs of runners (X_k, Y_k) ...*


## Backtracking & Recursion

### Recursive Backtracking & Prefix Balance Invariant

- [problem:AtCoder-typical90_b] **Encyclopedia of Parentheses** (Rating: 800, ★3) — *Print all valid parentheses strings of length N in lexicographical order. N <= 16....*


## Binary Search

### Binary Search on Answer / Greedy Feasibility

- [problem:AtCoder-typical90_a] **Yokan Party** (Rating: 1200) — *Cut a stick of length L at K positions to maximize the minimum piece length.*

---

# Data Structures (DS)

## Square Root Decomposition

### Square Root Decomposition on Graph Vertex Degrees (Heavy-Light)

- [problem:AtCoder-typical90_ce] **Colorful Graph** (Rating: 2300, ★6) — *Graph with N, M <= 2*10^5. Q <= 2*10^5 queries: given (x, y), print color of vertex x, then color x and all it...*


## Prefix Sums & Difference Arrays

### 2D Prefix Sums for Bounded Window Maximization

- [problem:AtCoder-typical90_cc] **Friendly Group** (Rating: 1750, ★5) — *N students with height A_i <= 5000 and weight B_i <= 5000. Find maximum students in a group with max_A - min_A...*


## Disjoint Set Union (DSU) & Fenwick Tree

### Alternating Difference Prefix Sums & Interval DSU Reachability

- [problem:AtCoder-typical90_bp] **Paired Information** (Rating: 1750, ★5) — *Array A of length N. Q queries: (0) told A_x + A_{x+1} = V; (1) given (x, y, v), if A_x = v, determine value o...*


## Prefix Sums & Difference Arrays

### Difference Array Local Perturbation for O(1) Range Update Inconvenience

- [problem:AtCoder-typical90_bl] **Uplift** (Rating: 800, ★3) — *Array A of length N. Total inconvenience is sum_{i=1}^{N-1} |A_{i+1} - A_i|. Q queries: add V to range [L, R]....*


## Bitset Optimization

### Batch Bitset Acceleration on DAG Reachability Queries

- [problem:AtCoder-typical90_bg] **Many Graph Queries** (Rating: 2600, ★7) — *Directed Acyclic Graph (DAG) with N <= 60000 vertices, M <= 100000 edges. Q <= 100000 queries: can A_i reach B...*


## Two Pointers / Sliding Window

### Two Pointers with Frequency Map / K-Distinct Subarray

- [problem:AtCoder-typical90_ah] **There are few types of elements** (Rating: 1250, ★4) — *Given an array of length N (N <= 10^5) and integer K, find the maximum length of a contiguous subarray contain...*


## Segment Tree / Fenwick Tree

### Dynamic Coordinate Compression + Lazy Segment Tree

- [problem:AtCoder-typical90_ac] **Long Bricks** (Rating: 1750, ★5) — *W-wide ground (W <= 10^9). N bricks fall in order. Brick i spans [L_i, R_i], lands on top of existing bricks i...*


## Prefix Sums & Difference Arrays

### 2D Imos Method / 2D Difference Array

- [problem:AtCoder-typical90_ab] **Cluttered Paper** (Rating: 1300, ★4) — *N axis-aligned sheets of paper are placed on a 1000 x 1000 grid. Each rectangle covers [lx, rx) x [ly, ry). Fo...*


## Segment Tree / Fenwick Tree

### Circle Chord Intersection Counting via Fenwick Tree

- [problem:AtCoder-typical90_q] **Crossing Segments** (Rating: 2450, ★7) — *N vertices arranged circularly 1..N. M chords connect pairs (L_i, R_i). Count pairs of chords that intersect s...*


## Disjoint Set Union (DSU)

### Grid Connectivity / Dynamic DSU

- [problem:AtCoder-typical90_l] **Red Painting** (Rating: 1250) — *Dynamically color grid cells red and answer reachability queries between red cells.*

## Segment Tree / Fenwick Tree

### DP Optimization using Data Structures [Some Practice Problems]

- [problem:AtCoder-dp_q] **Flowers** (Rating: 1600) — *Find a subsequence of flowers with strictly increasing heights that maximizes total beauty using Fenwick / Segment Tree.*

---

# Dynamic Programming (DP)

## DP Optimizations

### Two Pointers with Fenwick Tree Inversions + Prefix Sum Accelerated Partition DP

- [problem:AtCoder-typical90_ck] **Partitions and Inversions** (Rating: 2600, ★7) — *Partition array A of length N into contiguous subarrays such that each subarray contains at most K inversions....*


## Dp on Different Structures

### Tree Component Partition DP with 3 Characteristic States

- [problem:AtCoder-typical90_bu] **We Need Both a and b** (Rating: 1800, ★5) — *Tree with N vertices, each vertex labeled 'a' or 'b'. Delete a subset of edges to partition the tree into comp...*


## Classic DP

### Longest Bitonic Subsequence via Dual LIS

- [problem:AtCoder-typical90_bh] **Chimera** (Rating: 1600, ★5) — *Given array A of length N (N <= 3 * 10^5), find the maximum length of a bitonic subsequence (strictly increase...*


## Bit Related DP

### Minimax Subset Partition Bitmask DP with O(3^N) Submask Iteration

- [problem:AtCoder-typical90_as] **Simple Grouping** (Rating: 2150, ★6) — *N points in 2D plane (N <= 15). Partition points into K non-empty groups. Cost of a group is the maximum squar...*


## Intro to DP

### Digit Sum Divisibility Invariant & 9-Step Bounded Lookahead DP

- [problem:AtCoder-typical90_ap] **Multiple of 9** (Rating: 1150, ★4) — *Count the number of positive integers whose digit sum equals K (K <= 10^5) and are multiples of 9. Modulo 10^9...*


## DP Optimizations

### Segment Tree Accelerated Range Knapsack DP

- [problem:AtCoder-typical90_ak] **Don't Leave the Spice** (Rating: 1750, ★5) — *Dishes require exact weight W (W <= 10000). N spices with weight range [L_i, R_i] and value V_i. Find maximum ...*


## Classic DP

### Interval DP / Elimination and Outer Pairing

- [problem:AtCoder-typical90_s] **Pick Two** (Rating: 2100, ★6) — *2N integers are arranged in a row. Repeatedly remove an adjacent pair (x, y) with cost |x - y| until all numbe...*


## Classic DP

### Subsequence Matching DP / Automaton DP

- [problem:AtCoder-typical90_h] **AtCounter** (Rating: 1150, ★4) — *Given string S of length N, count the number of subsequences equal to 'atcoder' modulo 10^9+7....*


## DP on Different Structures

### Doubling DP / Matrix Exponentiation on Modular Digit Transitions

- [problem:AtCoder-typical90_e] **Restricted Digits** (Rating: 2400, ★7) — *Count N-digit positive integers (N <= 10^18) whose digits are chosen from a set of K non-zero digits and are d...*


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

## Grundy Number / Nim

### Sprague-Grundy Theorem on Multi-Pile Impartial Games

- [problem:AtCoder-typical90_ae] **VS AtCoder** (Rating: 2150, ★6) — *N independent piles with white stones W_i <= 50 and blue stones B_i <= 50. Turn moves: (1) change (W, B) to (W...*


## Impartial Games

### Sprague-Grundy / Combinatorial Game DP

- [problem:AtCoder-dp_k] **Stones** (Rating: 1100) — *Determine whether First or Second player wins an impartial subtract-a-stone game from pile of size K.*

---

# Graph Theory

## Shortest Paths & Binary Search

### Monotonicity of Floyd-Warshall Distance & Dual Binary Search

- [problem:AtCoder-typical90_ci] **Chokudai's Demand** (Rating: 1850, ★5) — *Complete graph with N <= 40 vertices. Some edges have unknown weight X. Count number of integer values of X >=...*


## Bipartite Matching & Network Flow

### Bipartite Matching on Geometric Directional Lattice via Dinic / Hopcroft-Karp

- [problem:AtCoder-typical90_by] **Planes on a 2D Plane** (Rating: 2600, ★7) — *N points A_i, N destination points B_j. Each point A_i must move to a unique destination B_j along one of 8 co...*


## Topological Sort

### K Distinct Topological Sorts via Kahn Backtracking

- [problem:AtCoder-typical90_bs] **Fuzzy Priority** (Rating: 2550, ★7) — *Given a DAG with N vertices and M edges, output K distinct topological sort permutations, or output -1 if fewe...*


## Reverse Graph & BFS

### Reverse Topological / Reverse Graph BFS Ordering

- [problem:AtCoder-typical90_bj] **Paint All** (Rating: 2100, ★6) — *N balls initially white. Ball i can be painted black if ball A_i or B_i is already painted black, or unconditi...*


## Functional Graphs

### Cycle Detection & Periodicity on Functional Graphs (Rho Algorithm)

- [problem:AtCoder-typical90_bf] **Original Calculator** (Rating: 1250, ★4) — *A calculator displays integer x (0 <= x < 10^5). Pressing button replaces x with (x + digit_sum(x)) mod 10^5. ...*


## Graph Modeling & Transformations

### Auxiliary Intermediate Node for Clique / Hypergraph Compression in BFS

- [problem:AtCoder-typical90_bb] **Takahashi Number** (Rating: 2150, ★6) — *N authors, M research papers. Paper i is co-authored by K_i authors. Co-authors have collaboration distance 1....*


## Minimum Spanning Tree (MST)

### Difference Array Graph Transformation & Minimum Spanning Tree (Kruskal)

- [problem:AtCoder-typical90_aw] **Flip Digits 2** (Rating: 2150, ★6) — *Binary string of length N. M operations with cost C_i flip bits in [L_i, R_i]. Find minimum cost to make it po...*


## Shortest Paths

### 0-1 BFS with State Direction / Minimum Turn Path

- [problem:AtCoder-typical90_aq] **Maze Challenge with Lack of Sleep** (Rating: 1350, ★4) — *H x W grid with walls. Start at (r_s, c_s), goal at (r_t, c_t). Moving in the same direction costs 0 turns; ch...*


## Network Flow

### Maximum Weight Closure / Project Selection Problem via Min-Cut

- [problem:AtCoder-typical90_an] **Get More Money** (Rating: 2550, ★7) — *N houses with burglary alarms awarding reward A_i. Unlocking house i costs key price W. Opening house i requir...*


## Trees

### Contribution to the Sum / Edge Subtree Size Multiplication

- [problem:AtCoder-typical90_am] **Tree Distance** (Rating: 1500, ★5) — *Given a tree with N vertices, compute the sum of distances between all N*(N - 1)/2 pairs of vertices: sum_{1 <...*


## Trees & LCA

### Euler Tour DFS Order + LCA for Minimal Subtree on Subset of Vertices

- [problem:AtCoder-typical90_ai] **Preserve Connectivity** (Rating: 2450, ★7) — *Given a tree with N vertices, answer Q queries: each query gives K vertices V_1, ..., V_K. Find the minimum nu...*


## Trees

### Bipartite 2-Coloring of Trees & Pigeonhole Independent Set

- [problem:AtCoder-typical90_z] **Independent Set on a Tree** (Rating: 1200, ★4) — *Given a tree with N vertices (N even), find an independent set of size exactly N / 2....*


## Directed Graphs

### Strongly Connected Components (SCC) / Tarjan & Kosaraju

- [problem:AtCoder-typical90_u] **Come Back in One Piece** (Rating: 1750, ★5) — *Given a directed graph with N vertices and M edges, count the number of pairs of vertices (u, v) with u < v su...*


## Shortest Paths

### Dual-Source Dijkstra / Intermediate Node Shortest Path

- [problem:AtCoder-typical90_m] **Passing** (Rating: 1350, ★5) — *Given a weighted undirected graph with N vertices and M edges, for each vertex k from 1 to N, find the length ...*


## Connected Components

### Disjoint Set Union (DSU) / Connected Component Cliques

- [problem:AtCoder-abc350_d] **New Friends** (Rating: 1050) — *If A-B and B-C are friends, A and C can become friends. Count maximum new operations.*

## Trees

### Tree Diameter / Double BFS-DFS

- [problem:AtCoder-typical90_c] **Longest Circular Road** (Rating: 1100) — *Adding an edge between two vertices u and v creates a cycle of length dist(u, v) + 1. Maximize this cycle length.*

---


# Strings

## Greedy on Strings

### Next-Occurrence Array / Lexicographically Smallest Subsequence

- [problem:AtCoder-typical90_f] **Smallest Subsequence** (Rating: 1500, ★5) — *Given string S of length N, find the lexicographically smallest subsequence of length K....*

---


# Geometry

## Convex Hull & Pick's Theorem

### Convex Hull + Pick's Theorem + Shoelace Formula for Lattice Points

- [problem:AtCoder-typical90_ao] **Piles in AtCoder Farm** (Rating: 2600, ★7) — *Given N points in 2D plane, find the number of integer lattice points contained inside or on the boundary of t...*


## Angular Sweep / Polar Angles

### Polar Angle Sort + Binary Search for Opposite Vector

- [problem:AtCoder-typical90_i] **Three Point Angle** (Rating: 2100, ★6) — *Given N points in 2D plane (N <= 2000), choose three distinct points p_j, p_i, p_k to maximize the angle betwe...*

---


# Combinatorics

## Inclusion-Exclusion Principle

### Inclusion-Exclusion on Bitwise Constraints

- [problem:AtCoder-typical90_cb] **Let's Share Bit** (Rating: 2200, ★6) — *N bitmasks A_1, ..., A_N in [0, 2^D - 1] (N <= 20, D <= 60). Count integers x in [0, 2^D - 1] such that (x & A...*


## Stars and Bars & Combinatorial Bounds

### Spacing Constraint Combinatorics + Harmonic Series O(N log N)

- [problem:AtCoder-typical90_o] **Don't be too close** (Rating: 2150, ★6) — *For each k from 1 to N, count non-empty subsets of {1, 2, ..., N} such that any two chosen elements have absol...*

---


# Math

## Pigeonhole Principle

### Pigeonhole Principle Collision Search on Subset Sums

- [problem:AtCoder-typical90_cj] **Similar but Different Ways** (Rating: 2150, ★6) — *N <= 88 cards with values A_i <= 88. Q incompatible pairs. Find TWO distinct valid subsets of cards having ide...*


## Arithmetic Series & Digit Ranges

### Digit-Length Interval Partition & Arithmetic Series Summation

- [problem:AtCoder-typical90_cd] **Counting Numbers** (Rating: 850, ★3) — *For each integer x in [L, R] (L, R <= 10^18), write x down x times. Count total digits written modulo 99824435...*


## Invariants & Monoids

### Binary Positional Weight Invariant on String Rewriting

- [problem:AtCoder-typical90_bv] **ABC String 2** (Rating: 2100, ★6) — *String of length N over {'a', 'b', 'c'}. Operation replaces 'b' with 'aa' and 'c' with 'bb'. Total operations ...*


## Optimization & Medians

### Manhattan Median Principle / Dimension Separation L1 Minimization

- [problem:AtCoder-typical90_br] **Plant Planning** (Rating: 1200, ★4) — *Given N factories at coordinates (X_i, Y_i), choose plant location (x, y) to minimize the sum of Manhattan dis...*


## Probability & Expected Value

### Linearity of Expectation on Inversions

- [problem:AtCoder-typical90_bn] **Various Arrays** (Rating: 1550, ★5) — *N independent random variables A_i chosen uniformly from [L_i, R_i]. Find the expected number of inversions (p...*


## Linear Algebra & Basis

### Gaussian Elimination over GF(2) / XOR Basis for Linear Systems

- [problem:AtCoder-typical90_be] **Flip Flap** (Rating: 2200, ★6) — *N switches, M bulbs. Switch i toggles a subset of bulbs. Target state S specifies desired on/off states for ea...*


## Coordinate Geometry & Metrics

### 45-Degree Coordinate Rotation / Manhattan to Chebyshev Distance Transformation

- [problem:AtCoder-typical90_aj] **Max Manhattan Distance** (Rating: 1600, ★5) — *Given N points (x_i, y_i), answer Q queries: for point q, find max Manhattan distance |x_q - x_j| + |y_q - y_j...*


## Search Space Invariants & Bounds

### Digit Product Value Compression & Inverse Search

- [problem:AtCoder-typical90_y] **Digit Product Equation** (Rating: 2400, ★7) — *Find the number of positive integers m <= N (N <= 10^11) satisfying m - f(m) = B, where f(m) is the product of...*

---


# Number Theory

## Prime Numbers & Sieve

### Modified Sieve of Eratosthenes / Prime Factor Multiplicity

- [problem:AtCoder-typical90_ad] **K Factors** (Rating: 1400, ★5) — *Count integers in the range [2, N] (N <= 10^7) that have at least K distinct prime factors....*

---

### Batch 3 Part 1: ABC Curated Ladder (800 - 970)
- `[problem:AtCoder-abc168_d]` — **.. (Double Dots)** (Rating: 804) | Topic: `Shortest Path Tree / BFS Parent Reconstruction` | Analysis: [`analysis/AtCoder-abc168_d.md`](analysis/AtCoder-abc168_d.md)
- `[problem:AtCoder-abc197_c]` — **ORXOR** (Rating: 809) | Topic: `Bitmask Partition Enumeration / Contiguous Splitting` | Analysis: [`analysis/AtCoder-abc197_c.md`](analysis/AtCoder-abc197_c.md)
- `[problem:AtCoder-abc148_e]` — **Double Factorial** (Rating: 818) | Topic: `Legendre's Formula on Double Factorial / p-adic Valuation` | Analysis: [`analysis/AtCoder-abc148_e.md`](analysis/AtCoder-abc148_e.md)
- `[problem:AtCoder-abc141_d]` — **Powerful Discount Tickets** (Rating: 823) | Topic: `Max-Heap Greedy Reduction` | Analysis: [`analysis/AtCoder-abc141_d.md`](analysis/AtCoder-abc141_d.md)
- `[problem:AtCoder-abc003_3]` — **AtCoder Programming Course** (Rating: 824) | Topic: `Greedy Sorting on Floating Point Recurrence` | Analysis: [`analysis/AtCoder-abc003_3.md`](analysis/AtCoder-abc003_3.md)
- `[problem:AtCoder-abc142_d]` — **Disjoint Set of Common Divisors** (Rating: 827) | Topic: `Coprime Divisor Selection via Prime Factorization of GCD` | Analysis: [`analysis/AtCoder-abc142_d.md`](analysis/AtCoder-abc142_d.md)
- `[problem:AtCoder-abc197_d]` — **Opposite** (Rating: 831) | Topic: `2D Point Rotation around Center via Complex Numbers` | Analysis: [`analysis/AtCoder-abc197_d.md`](analysis/AtCoder-abc197_d.md)
- `[problem:AtCoder-abc204_d]` — **Cooking** (Rating: 832) | Topic: `Dual Partition Subset Sum via Bitset Optimization` | Analysis: [`analysis/AtCoder-abc204_d.md`](analysis/AtCoder-abc204_d.md)
- `[problem:AtCoder-abc125_d]` — **Flipping Signs** (Rating: 833) | Topic: `Sign Flip Parity Invariant` | Analysis: [`analysis/AtCoder-abc125_d.md`](analysis/AtCoder-abc125_d.md)
- `[problem:AtCoder-abc076_c]` — **Dubious Document 2** (Rating: 846) | Topic: `Rightmost Match Lexicographical Minimization` | Analysis: [`analysis/AtCoder-abc076_c.md`](analysis/AtCoder-abc076_c.md)
- `[problem:AtCoder-arc080_b]` — **Grid Coloring** (Rating: 852) | Topic: `Snake / Boustrophedon Connected Fill` | Analysis: [`analysis/AtCoder-arc080_b.md`](analysis/AtCoder-arc080_b.md)
- `[problem:AtCoder-abc027_b]` — **Island Bridges** (Rating: 855) | Topic: `Prefix Imbalance Minimum Cuts` | Analysis: [`analysis/AtCoder-abc027_b.md`](analysis/AtCoder-abc027_b.md)
- `[problem:AtCoder-abc130_d]` — **Enough Array** (Rating: 865) | Topic: `Monotonic Subarray Sum Threshold Counting` | Analysis: [`analysis/AtCoder-abc130_d.md`](analysis/AtCoder-abc130_d.md)
- `[problem:AtCoder-arc095_b]` — **Binomial Coefficients** (Rating: 867) | Topic: `Binomial Coefficient Unimodality Maximization` | Analysis: [`analysis/AtCoder-arc095_b.md`](analysis/AtCoder-arc095_b.md)
- `[problem:AtCoder-abc178_d]` — **Redistribution** (Rating: 875) | Topic: `Prefix Sum Transition Acceleration on Partition DP` | Analysis: [`analysis/AtCoder-abc178_d.md`](analysis/AtCoder-abc178_d.md)
- `[problem:AtCoder-abc160_d]` — **Line++** (Rating: 879) | Topic: `Shortcut Distance Closed Form Enumeration` | Analysis: [`analysis/AtCoder-abc160_d.md`](analysis/AtCoder-abc160_d.md)
- `[problem:AtCoder-abc206_d]` — **KAIBUNsyo** (Rating: 879) | Topic: `Equivalence Relation Component Collapse via DSU` | Analysis: [`analysis/AtCoder-abc206_d.md`](analysis/AtCoder-abc206_d.md)
- `[problem:AtCoder-abc127_d]` — **Integer Cards** (Rating: 887) | Topic: `Two-Array Ascending/Descending Greedy Replacement` | Analysis: [`analysis/AtCoder-abc127_d.md`](analysis/AtCoder-abc127_d.md)
- `[problem:AtCoder-abc174_c]` — **Repsept** (Rating: 902) | Topic: `Pigeonhole Cycle Detection on Linear Congruence Sequence` | Analysis: [`analysis/AtCoder-abc174_c.md`](analysis/AtCoder-abc174_c.md)
- `[problem:AtCoder-abc138_d]` — **Ki** (Rating: 920) | Topic: `Tree Subtree Imos / Prefix Sum DFS Propagation` | Analysis: [`analysis/AtCoder-abc138_d.md`](analysis/AtCoder-abc138_d.md)
- `[problem:AtCoder-abc134_d]` — **Preparing Boxes** (Rating: 926) | Topic: `Reverse Multiples Harmonic Greedy / Back-Substitution` | Analysis: [`analysis/AtCoder-abc134_d.md`](analysis/AtCoder-abc134_d.md)
- `[problem:AtCoder-arc065_a]` — **Daydream** (Rating: 930) | Topic: `Reverse Greedy Suffix Parsing / Ambiguity Inversion` | Analysis: [`analysis/AtCoder-arc065_a.md`](analysis/AtCoder-arc065_a.md)
- `[problem:AtCoder-abc172_c]` — **Tsundoku** (Rating: 930) | Topic: `Dual Monotonic Prefix Sum Optimization` | Analysis: [`analysis/AtCoder-abc172_c.md`](analysis/AtCoder-abc172_c.md)
- `[problem:AtCoder-abc188_d]` — **Snuke Prime** (Rating: 933) | Topic: `Coordinate-Compressed Event Sweep / Imos Method` | Analysis: [`analysis/AtCoder-abc188_d.md`](analysis/AtCoder-abc188_d.md)
- `[problem:AtCoder-abc133_d]` — **Rain Flows into Dams** (Rating: 938) | Topic: `Odd Cycle Telescoping Alternating Sum` | Analysis: [`analysis/AtCoder-abc133_d.md`](analysis/AtCoder-abc133_d.md)
- `[problem:AtCoder-abc110_c]` — **String Transformation** (Rating: 949) | Topic: `Alphabet Bijection / Isomorphism Verification` | Analysis: [`analysis/AtCoder-abc110_c.md`](analysis/AtCoder-abc110_c.md)
- `[problem:AtCoder-abc079_d]` — **Wall** (Rating: 949) | Topic: `Digit Transformation Graph via Floyd-Warshall` | Analysis: [`analysis/AtCoder-abc079_d.md`](analysis/AtCoder-abc079_d.md)
- `[problem:AtCoder-abc085_d]` — **Katana Thrower** (Rating: 954) | Topic: `Threshold-Bounded Greedy Consumption` | Analysis: [`analysis/AtCoder-abc085_d.md`](analysis/AtCoder-abc085_d.md)
- `[problem:AtCoder-abc151_d]` — **Maze Master** (Rating: 959) | Topic: `All-Pairs Grid BFS / Grid Maze Diameter` | Analysis: [`analysis/AtCoder-abc151_d.md`](analysis/AtCoder-abc151_d.md)
- `[problem:AtCoder-abc172_d]` — **Sum of Divisors** (Rating: 963) | Topic: `Divisor Contribution Summation / Order-of-Summation Swap` | Analysis: [`analysis/AtCoder-abc172_d.md`](analysis/AtCoder-abc172_d.md)
- `[problem:AtCoder-abc202_d]` — **aab aba baa** (Rating: 966) | Topic: `Lexicographical K-th Permutation via Combinatorial Branching` | Analysis: [`analysis/AtCoder-abc202_d.md`](analysis/AtCoder-abc202_d.md)
- `[problem:AtCoder-abc051_c]` — **Back and Forth** (Rating: 968) | Topic: `Disjoint Grid Paths Outer Boundary Routing` | Analysis: [`analysis/AtCoder-abc051_c.md`](analysis/AtCoder-abc051_c.md)
- `[problem:AtCoder-abc064_d]` — **Insertion** (Rating: 969) | Topic: `Prefix Balance Minimization for Valid Bracket Completion` | Analysis: [`analysis/AtCoder-abc064_d.md`](analysis/AtCoder-abc064_d.md)

### Batch 3 Part 2: ABC Curated Ladder (970 - 1090)
- `[problem:AtCoder-abc147_c]` — **HonestOrUnkind2** (Rating: 977) | Topic: `Bitmask Truth Assignment Consistency Verification` | Analysis: [`analysis/AtCoder-abc147_c.md`](analysis/AtCoder-abc147_c.md)
- `[problem:AtCoder-abc084_d]` — **2017-like Number** (Rating: 980) | Topic: `Sieve of Eratosthenes + Prefix Sum Query Filtering` | Analysis: [`analysis/AtCoder-abc084_d.md`](analysis/AtCoder-abc084_d.md)
- `[problem:AtCoder-abc161_d]` — **Lunlun Number** (Rating: 991) | Topic: `Digit BFS Queue Generation / Monotonic Transition` | Analysis: [`analysis/AtCoder-abc161_d.md`](analysis/AtCoder-abc161_d.md)
- `[problem:AtCoder-abc088_d]` — **Grid Repainting** (Rating: 999) | Topic: `Grid BFS Shortest Path / Free Cell Maximization` | Analysis: [`analysis/AtCoder-abc088_d.md`](analysis/AtCoder-abc088_d.md)
- `[problem:AtCoder-abc145_d]` — **Knight** (Rating: 1009) | Topic: `2-Vector Linear Combination + Modular Binomial Combinatorics` | Analysis: [`analysis/AtCoder-abc145_d.md`](analysis/AtCoder-abc145_d.md)
- `[problem:AtCoder-abc156_d]` — **Bouquet** (Rating: 1014) | Topic: `Total Subsets minus Forbidden Combinations (Fermat Mod Inv)` | Analysis: [`analysis/AtCoder-abc156_d.md`](analysis/AtCoder-abc156_d.md)
- `[problem:AtCoder-abc153_e]` — **Crested Ibis vs Monster** (Rating: 1015) | Topic: `Unbounded Knapsack / Minimum Cost Target Reachability` | Analysis: [`analysis/AtCoder-abc153_e.md`](analysis/AtCoder-abc153_e.md)
- `[problem:AtCoder-abc112_d]` — **Partition** (Rating: 1025) | Topic: `Maximum GCD of Sum Partition / Divisor Feasibility` | Analysis: [`analysis/AtCoder-abc112_d.md`](analysis/AtCoder-abc112_d.md)
- `[problem:AtCoder-abc170_d]` — **Not Divisible** (Rating: 1033) | Topic: `Sieve Divisor Elimination / Multiples Marking` | Analysis: [`analysis/AtCoder-abc170_d.md`](analysis/AtCoder-abc170_d.md)
- `[problem:AtCoder-abc160_e]` — **Red and Green Apples** (Rating: 1036) | Topic: `Top-(X+Y) Greedy Unification via Candidate Filtering` | Analysis: [`analysis/AtCoder-abc160_e.md`](analysis/AtCoder-abc160_e.md)
- `[problem:AtCoder-abc114_c]` — **755** (Rating: 1045) | Topic: `Digit Recursion / 3-Branch DFS Enumeration` | Analysis: [`analysis/AtCoder-abc114_c.md`](analysis/AtCoder-abc114_c.md)
- `[problem:AtCoder-abc152_d]` — **Handstand 2** (Rating: 1045) | Topic: `First-Last Digit Pair Frequency Matrix Double Counting` | Analysis: [`analysis/AtCoder-abc152_d.md`](analysis/AtCoder-abc152_d.md)
- `[problem:AtCoder-abc185_f]` — **Range Xor Query** (Rating: 1053) | Topic: `Point Update Range XOR Query on Fenwick Tree` | Analysis: [`analysis/AtCoder-abc185_f.md`](analysis/AtCoder-abc185_f.md)
- `[problem:AtCoder-abc178_e]` — **Dist Max** (Rating: 1054) | Topic: `45-degree Coordinate Rotation for Manhattan Maxima` | Analysis: [`analysis/AtCoder-abc178_e.md`](analysis/AtCoder-abc178_e.md)
- `[problem:AtCoder-abc177_e]` — **Coprime** (Rating: 1057) | Topic: `Pairwise Coprime via Smallest Prime Factor (SPF) Sieve` | Analysis: [`analysis/AtCoder-abc177_e.md`](analysis/AtCoder-abc177_e.md)
- `[problem:AtCoder-arc067_b]` — **Walk and Teleport** (Rating: 1060) | Topic: `Adjacent Greedy Transition / Cost Comparison` | Analysis: [`analysis/AtCoder-arc067_b.md`](analysis/AtCoder-arc067_b.md)
- `[problem:AtCoder-abc166_e]` — **This Message Will Self-Destruct in 5s** (Rating: 1062) | Topic: `Algebraic Rearrangement Hash Frequency Match` | Analysis: [`analysis/AtCoder-abc166_e.md`](analysis/AtCoder-abc166_e.md)
- `[problem:AtCoder-abc191_c]` — **Digital Graffiti** (Rating: 1063) | Topic: `Corner Vertices 2x2 Topological Counting on Grids` | Analysis: [`analysis/AtCoder-abc191_c.md`](analysis/AtCoder-abc191_c.md)
- `[problem:AtCoder-abc075_c]` — **Bridge** (Rating: 1067) | Topic: `Cut-Edge / Bridge Detection via DFS / DSU Edge Removal` | Analysis: [`analysis/AtCoder-abc075_c.md`](analysis/AtCoder-abc075_c.md)
- `[problem:AtCoder-abc140_d]` — **Face Produces Unhappiness** (Rating: 1074) | Topic: `Run-Length Inversion / Boundary Reduction Greedy` | Analysis: [`analysis/AtCoder-abc140_d.md`](analysis/AtCoder-abc140_d.md)
- `[problem:AtCoder-abc194_d]` — **Journey** (Rating: 1078) | Topic: `Coupon Collector's Problem / Geometric Distribution Linearity of Expectation` | Analysis: [`analysis/AtCoder-abc194_d.md`](analysis/AtCoder-abc194_d.md)
- `[problem:AtCoder-abc194_e]` — **Mex Min** (Rating: 1088) | Topic: `Sliding Window Frequency Tracking / Minimum Missing Non-Negative` | Analysis: [`analysis/AtCoder-abc194_e.md`](analysis/AtCoder-abc194_e.md)
- `[problem:AtCoder-abc115_d]` — **Christmas** (Rating: 1088) | Topic: `Recursive Burger Fractal Binary Search / Tree Size Division` | Analysis: [`analysis/AtCoder-abc115_d.md`](analysis/AtCoder-abc115_d.md)

### Batch 3 Part 3: ABC Curated Ladder (1090 - 1199)
- `[problem:AtCoder-arc100_a]` — **Linear Approximation** (Rating: 1089) | Topic: `1D L1-Norm / Absolute Deviation Median Minimization` | Analysis: [`analysis/AtCoder-arc100_a.md`](analysis/AtCoder-arc100_a.md)
- `[problem:AtCoder-arc084_a]` — **Snuke Festival** (Rating: 1096) | Topic: `Dual Binary Search on Middle Anchor / Triplet Counting` | Analysis: [`analysis/AtCoder-arc084_a.md`](analysis/AtCoder-arc084_a.md)
- `[problem:AtCoder-abc035_c]` — **Othello** (Rating: 1096) | Topic: `1D Parity Difference Array (Imos Mod 2)` | Analysis: [`analysis/AtCoder-abc035_c.md`](analysis/AtCoder-abc035_c.md)
- `[problem:AtCoder-abc182_e]` — **Akari** (Rating: 1098) | Topic: `4-Way Linear Beam Propagation on Grids` | Analysis: [`analysis/AtCoder-abc182_e.md`](analysis/AtCoder-abc182_e.md)
- `[problem:AtCoder-abc099_c]` — **Strange Bank** (Rating: 1101) | Topic: `Coin Change / Minimum Steps with Dual Exponential Bases` | Analysis: [`analysis/AtCoder-abc099_c.md`](analysis/AtCoder-abc099_c.md)
- `[problem:AtCoder-abc129_d]` — **Lamp** (Rating: 1103) | Topic: `4-Directional Prefix Ray DP Precomputation` | Analysis: [`analysis/AtCoder-abc129_d.md`](analysis/AtCoder-abc129_d.md)
- `[problem:AtCoder-arc097_a]` — **K-th Substring** (Rating: 1108) | Topic: `Bounded-Length Substring Generation for Small K-th Ranking` | Analysis: [`analysis/AtCoder-arc097_a.md`](analysis/AtCoder-arc097_a.md)
- `[problem:AtCoder-arc091_b]` — **Remainder Reminder** (Rating: 1129) | Topic: `Periodic Remainder Block Counting` | Analysis: [`analysis/AtCoder-arc091_b.md`](analysis/AtCoder-arc091_b.md)
- `[problem:AtCoder-abc192_e]` — **Train** (Rating: 1135) | Topic: `Periodic Departure Schedule Dijkstra` | Analysis: [`analysis/AtCoder-abc192_e.md`](analysis/AtCoder-abc192_e.md)
- `[problem:AtCoder-abc165_c]` — **Many Requirements** (Rating: 1136) | Topic: `Monotonic Non-Decreasing Sequence Generation via DFS` | Analysis: [`analysis/AtCoder-abc165_c.md`](analysis/AtCoder-abc165_c.md)
- `[problem:AtCoder-abc124_d]` — **Handstand** (Rating: 1138) | Topic: `Run-Length Compression Sliding Window Expansion` | Analysis: [`analysis/AtCoder-abc124_d.md`](analysis/AtCoder-abc124_d.md)
- `[problem:AtCoder-abc112_c]` — **Pyramid** (Rating: 1147) | Topic: `Center Parameter Brute Force with Positive Reference Anchor` | Analysis: [`analysis/AtCoder-abc112_c.md`](analysis/AtCoder-abc112_c.md)
- `[problem:AtCoder-abc198_e]` — **Unique Color** (Rating: 1161) | Topic: `Tree Path Ancestor Frequency Stack Backtracking` | Analysis: [`analysis/AtCoder-abc198_e.md`](analysis/AtCoder-abc198_e.md)
- `[problem:AtCoder-arc064_a]` — **Boxes and Candies** (Rating: 1164) | Topic: `Adjacent Pair Overlap Forward Greedy Reduction` | Analysis: [`analysis/AtCoder-arc064_a.md`](analysis/AtCoder-arc064_a.md)
- `[problem:AtCoder-abc121_d]` — **XOR World** (Rating: 1164) | Topic: `Period-4 Prefix XOR Invariant` | Analysis: [`analysis/AtCoder-abc121_d.md`](analysis/AtCoder-abc121_d.md)
- `[problem:AtCoder-arc081_b]` — **Coloring Dominoes** (Rating: 1165) | Topic: `Domino Tiling Chromatic Transition DP` | Analysis: [`analysis/AtCoder-arc081_b.md`](analysis/AtCoder-arc081_b.md)
- `[problem:AtCoder-abc132_d]` — **Blue and Red Balls** (Rating: 1167) | Topic: `Alternating Block Partitioning via Stars and Bars` | Analysis: [`analysis/AtCoder-abc132_d.md`](analysis/AtCoder-abc132_d.md)
- `[problem:AtCoder-abc188_e]` — **Peddler** (Rating: 1170) | Topic: `DAG Topological Minimum Ancestor Cost DP` | Analysis: [`analysis/AtCoder-abc188_e.md`](analysis/AtCoder-abc188_e.md)
- `[problem:AtCoder-abc109_d]` — **Make Them Even** (Rating: 1172) | Topic: `Snake Path Parity Propagation` | Analysis: [`analysis/AtCoder-abc109_d.md`](analysis/AtCoder-abc109_d.md)
- `[problem:AtCoder-abc179_e]` — **Sequence Sum** (Rating: 1175) | Topic: `Periodic Orbit Prefix Sum Acceleration` | Analysis: [`analysis/AtCoder-abc179_e.md`](analysis/AtCoder-abc179_e.md)
- `[problem:AtCoder-abc070_d]` — **Transit Tree Path** (Rating: 1182) | Topic: `Fixed Transit Vertex Root-Referenced Tree Distances` | Analysis: [`analysis/AtCoder-abc070_d.md`](analysis/AtCoder-abc070_d.md)
- `[problem:AtCoder-abc208_d]` — **Shortest Path Queries 2** (Rating: 1190) | Topic: `Floyd-Warshall Intermediate Vertex State Accumulation` | Analysis: [`analysis/AtCoder-abc208_d.md`](analysis/AtCoder-abc208_d.md)
- `[problem:AtCoder-abc146_d]` — **Coloring Edges on Tree** (Rating: 1192) | Topic: `Greedy Edge Coloring of Trees via Maximum Degree Bound` | Analysis: [`analysis/AtCoder-abc146_d.md`](analysis/AtCoder-abc146_d.md)
- `[problem:AtCoder-abc181_e]` — **Transformable Teacher** (Rating: 1193) | Topic: `Prefix-Suffix Parity Split with Binary Search Insertion` | Analysis: [`analysis/AtCoder-abc181_e.md`](analysis/AtCoder-abc181_e.md)
- `[problem:AtCoder-abc125_c]` — **GCD on Blackboard** (Rating: 1197) | Topic: `Prefix and Suffix GCD Arrays (Exclusion Technique)` | Analysis: [`analysis/AtCoder-abc125_c.md`](analysis/AtCoder-abc125_c.md)

### Batch 4 Part 1A: ABC Curated Ladder (1204 - 1270)
- `[problem:AtCoder-abc105_c]` — **Base -2 Number** (Rating: 1204) | Topic: `Negative Base Division / Modulo Arithmetic` | Analysis: [`analysis/AtCoder-abc105_c.md`](analysis/AtCoder-abc105_c.md)
- `[problem:AtCoder-abc176_e]` — **Bomber** (Rating: 1204) | Topic: `Max Row/Col Intersection Overlap Filtering` | Analysis: [`analysis/AtCoder-abc176_e.md`](analysis/AtCoder-abc176_e.md)
- `[problem:AtCoder-abc147_d]` — **Xor Sum 4** (Rating: 1205) | Topic: `Bitwise Independent Contribution Summation modulo 10^9+7` | Analysis: [`analysis/AtCoder-abc147_d.md`](analysis/AtCoder-abc147_d.md)
- `[problem:AtCoder-abc157_d]` — **Friend Suggestions** (Rating: 1208) | Topic: `DSU Component Sizing with Mutual Exclusion` | Analysis: [`analysis/AtCoder-abc157_d.md`](analysis/AtCoder-abc157_d.md)
- `[problem:AtCoder-abc200_d]` — **Happy Birthday! 2** (Rating: 1217) | Topic: `Pigeonhole Principle 2^N > 200 Modulo 200 Subset Collision` | Analysis: [`analysis/AtCoder-abc200_d.md`](analysis/AtCoder-abc200_d.md)
- `[problem:AtCoder-abc089_d]` — **Practical Skill Test** (Rating: 1220) | Topic: `Modulo-D Strided Prefix Sums` | Analysis: [`analysis/AtCoder-abc089_d.md`](analysis/AtCoder-abc089_d.md)
- `[problem:AtCoder-arc074_a]` — **Chocolate Bar** (Rating: 1223) | Topic: `3-Way Grid Rectangular Partitioning Casework` | Analysis: [`analysis/AtCoder-arc074_a.md`](analysis/AtCoder-arc074_a.md)
- `[problem:AtCoder-abc198_d]` — **Send More Money** (Rating: 1224) | Topic: `Cryptarithmetic Permutation Search via std::next_permutation` | Analysis: [`analysis/AtCoder-abc198_d.md`](analysis/AtCoder-abc198_d.md)
- `[problem:AtCoder-abc096_d]` — **Five, Five Everywhere** (Rating: 1226) | Topic: `Modulo-5 Arithmetic Residue Selection for Prime Subsets` | Analysis: [`analysis/AtCoder-abc096_d.md`](analysis/AtCoder-abc096_d.md)
- `[problem:AtCoder-abc174_e]` — **Logs** (Rating: 1227) | Topic: `Binary Search on Answer / Greedy Chunk Division` | Analysis: [`analysis/AtCoder-abc174_e.md`](analysis/AtCoder-abc174_e.md)
- `[problem:AtCoder-abc390_e]` — **Vitamin Balance** (Rating: 1227) | Topic: `3-Resource Dual Knapsack DP with Monotonic Search` | Analysis: [`analysis/AtCoder-abc390_e.md`](analysis/AtCoder-abc390_e.md)
- `[problem:AtCoder-abc164_d]` — **Multiple of 2019** (Rating: 1232) | Topic: `Suffix Modulo 2019 Prefix Arithmetic (Coprime Base)` | Analysis: [`analysis/AtCoder-abc164_d.md`](analysis/AtCoder-abc164_d.md)
- `[problem:AtCoder-abc054_c]` — **One-stroke Path** (Rating: 1244) | Topic: `Hamiltonian Path Permutation DFS` | Analysis: [`analysis/AtCoder-abc054_c.md`](analysis/AtCoder-abc054_c.md)
- `[problem:AtCoder-abc032_c]` — **Columns** (Rating: 1244) | Topic: `Monotonic Subarray Product Window` | Analysis: [`analysis/AtCoder-abc032_c.md`](analysis/AtCoder-abc032_c.md)
- `[problem:AtCoder-abc176_d]` — **Wizard in Maze** (Rating: 1248) | Topic: `0-1 BFS on 5x5 Warp Moves` | Analysis: [`analysis/AtCoder-abc176_d.md`](analysis/AtCoder-abc176_d.md)
- `[problem:AtCoder-abc179_d]` — **Leaping Tak** (Rating: 1251) | Topic: `DP with Range Transitions Accelerated by Prefix Sums` | Analysis: [`analysis/AtCoder-abc179_d.md`](analysis/AtCoder-abc179_d.md)
- `[problem:AtCoder-arc083_a]` — **Sugar Water** (Rating: 1255) | Topic: `2-Phase Feasible State Enumeration / Knapsack Density Maximization` | Analysis: [`analysis/AtCoder-arc083_a.md`](analysis/AtCoder-arc083_a.md)
- `[problem:AtCoder-abc180_e]` — **Traveling Salesman among Aerial Cities** (Rating: 1256) | Topic: `TSP Bitmask DP with Asymmetric Metric` | Analysis: [`analysis/AtCoder-abc180_e.md`](analysis/AtCoder-abc180_e.md)
- `[problem:AtCoder-abc138_e]` — **Strings of Impurity** (Rating: 1257) | Topic: `Periodic String Subsequence Matching via Position Binary Search` | Analysis: [`analysis/AtCoder-abc138_e.md`](analysis/AtCoder-abc138_e.md)
- `[problem:AtCoder-arc092_a]` — **2D Plane 2N Points** (Rating: 1268) | Topic: `Bipartite Matching / Greedy Sweepline on 2D Coordinates` | Analysis: [`analysis/AtCoder-arc092_a.md`](analysis/AtCoder-arc092_a.md)

### Batch 4 Part 1B: ABC Curated Ladder (1270 - 1344)
- `[problem:AtCoder-arc097_b]` — **Equals** (Rating: 1270) | Topic: `Permutation Position Cycles via DSU` | Analysis: [`analysis/AtCoder-arc097_b.md`](analysis/AtCoder-arc097_b.md)
- `[problem:AtCoder-abc184_d]` — **increment of coins** (Rating: 1276) | Topic: `3D Expected Value Backward Induction DP` | Analysis: [`analysis/AtCoder-abc184_d.md`](analysis/AtCoder-abc184_d.md)
- `[problem:AtCoder-abc196_d]` — **Hanjo** (Rating: 1277) | Topic: `Grid Domino Tiling Backtracking DFS` | Analysis: [`analysis/AtCoder-abc196_d.md`](analysis/AtCoder-abc196_d.md)
- `[problem:AtCoder-abc103_d]` — **Islands War** (Rating: 1278) | Topic: `Interval Scheduling / Right-Endpoint Greedy Cuts` | Analysis: [`analysis/AtCoder-abc103_d.md`](analysis/AtCoder-abc103_d.md)
- `[problem:AtCoder-abc126_d]` — **Even Relation** (Rating: 1279) | Topic: `Tree 2-Coloring via Edge Weight Parities` | Analysis: [`analysis/AtCoder-abc126_d.md`](analysis/AtCoder-abc126_d.md)
- `[problem:AtCoder-abc183_e]` — **Queen on Grid** (Rating: 1288) | Topic: `2D Grid DP with 3-Way Running Prefix Sums` | Analysis: [`analysis/AtCoder-abc183_e.md`](analysis/AtCoder-abc183_e.md)
- `[problem:AtCoder-abc154_e]` — **Almost Everywhere Zero** (Rating: 1298) | Topic: `Digit DP with Tight Flag and Non-Zero Count State` | Analysis: [`analysis/AtCoder-abc154_e.md`](analysis/AtCoder-abc154_e.md)
- `[problem:AtCoder-abc137_d]` — **Summer Vacation** (Rating: 1313) | Topic: `Reverse Time Greedy with Max-Heap Priority Queue` | Analysis: [`analysis/AtCoder-abc137_d.md`](analysis/AtCoder-abc137_d.md)
- `[problem:AtCoder-abc201_d]` — **Game in Momotetsu World** (Rating: 1317) | Topic: `Minimax Game DP on 2D Grid` | Analysis: [`analysis/AtCoder-abc201_d.md`](analysis/AtCoder-abc201_d.md)
- `[problem:AtCoder-abc106_d]` — **AtCoder Express 2** (Rating: 1319) | Topic: `2D Prefix Sums on Interval Endpoints [L, R]` | Analysis: [`analysis/AtCoder-abc106_d.md`](analysis/AtCoder-abc106_d.md)
- `[problem:AtCoder-abc134_e]` — **Sequence Decomposing** (Rating: 1320) | Topic: `Dilworth's Theorem / Minimum Decreasing Chains via Multiset Greedy` | Analysis: [`analysis/AtCoder-abc134_e.md`](analysis/AtCoder-abc134_e.md)
- `[problem:AtCoder-abc190_f]` — **Shift and Inversions** (Rating: 1321) | Topic: `Cyclic Shift Inversion Update via Fenwick Tree` | Analysis: [`analysis/AtCoder-abc190_f.md`](analysis/AtCoder-abc190_f.md)
- `[problem:AtCoder-abc191_e]` — **Come Back Quickly** (Rating: 1323) | Topic: `Multi-Source Dijkstra Shortest Cycle / Self-Loop Detection` | Analysis: [`analysis/AtCoder-abc191_e.md`](analysis/AtCoder-abc191_e.md)
- `[problem:AtCoder-abc021_c]` — **Shortest Path Count** (Rating: 1324) | Topic: `BFS Shortest Path Counting on DAG` | Analysis: [`analysis/AtCoder-abc021_c.md`](analysis/AtCoder-abc021_c.md)
- `[problem:AtCoder-abc100_d]` — **Patisserie ABC** (Rating: 1331) | Topic: `8-Sign Octant Projection for 3D Extremal Sums` | Analysis: [`analysis/AtCoder-abc100_d.md`](analysis/AtCoder-abc100_d.md)
- `[problem:AtCoder-abc135_d]` — **Digits Parade** (Rating: 1334) | Topic: `Digit DP Modulo 13` | Analysis: [`analysis/AtCoder-abc135_d.md`](analysis/AtCoder-abc135_d.md)
- `[problem:AtCoder-abc114_d]` — **756** (Rating: 1337) | Topic: `Prime Exponent Partitioning for Highly Composite Numbers` | Analysis: [`analysis/AtCoder-abc114_d.md`](analysis/AtCoder-abc114_d.md)
- `[problem:AtCoder-abc126_e]` — **1 or 2** (Rating: 1340) | Topic: `System of Parity Constraints / DSU Component Count` | Analysis: [`analysis/AtCoder-abc126_e.md`](analysis/AtCoder-abc126_e.md)
- `[problem:AtCoder-abc151_e]` — **Max-Min Sums** (Rating: 1344) | Topic: `Combinatorial Contribution of Sorted Elements (Binomial Sums)` | Analysis: [`analysis/AtCoder-abc151_e.md`](analysis/AtCoder-abc151_e.md)
- `[problem:AtCoder-arc069_b]` — **Menagerie** (Rating: 1344) | Topic: `Circular Truth-Telling Consistency 4-Case Brute Force` | Analysis: [`analysis/AtCoder-arc069_b.md`](analysis/AtCoder-arc069_b.md)

### Batch 4 Part 2A: ABC Curated Ladder (1345 - 1406)
- `[problem:AtCoder-abc073_d]` — **joisino's travel** (Rating: 1345) | Topic: `Floyd-Warshall + Permutation Search on Target Subsets` | Analysis: [`analysis/AtCoder-abc073_d.md`](analysis/AtCoder-abc073_d.md)
- `[problem:AtCoder-abc099_d]` — **Good Grid** (Rating: 1345) | Topic: `Grid (i + j) % 3 Coloring with Color Permutations` | Analysis: [`analysis/AtCoder-abc099_d.md`](analysis/AtCoder-abc099_d.md)
- `[problem:AtCoder-abc119_c]` — **Synthetic Kadomatsu** (Rating: 1346) | Topic: `4-State Quaternary Choice Backtracking (4^N)` | Analysis: [`analysis/AtCoder-abc119_c.md`](analysis/AtCoder-abc119_c.md)
- `[problem:AtCoder-arc062_a]` — **AtCoDeer and Election Report** (Rating: 1346) | Topic: `Monotonic Ratio Ceiling Multiplier` | Analysis: [`analysis/AtCoder-arc062_a.md`](analysis/AtCoder-arc062_a.md)
- `[problem:AtCoder-abc119_d]` — **Lazy Faith** (Rating: 1346) | Topic: `Dual Binary Search on Two Sorted Arrays (Shrines & Temples)` | Analysis: [`analysis/AtCoder-abc119_d.md`](analysis/AtCoder-abc119_d.md)
- `[problem:AtCoder-abc152_e]` — **Flatten** (Rating: 1348) | Topic: `LCM of Array Modulo 10^9+7 via Prime Exponent Maxima` | Analysis: [`analysis/AtCoder-abc152_e.md`](analysis/AtCoder-abc152_e.md)
- `[problem:AtCoder-abc169_e]` — **Count Median** (Rating: 1353) | Topic: `Interval Medians Feasible Range [Min Median, Max Median]` | Analysis: [`analysis/AtCoder-abc169_e.md`](analysis/AtCoder-abc169_e.md)
- `[problem:AtCoder-abc128_d]` — **equeue** (Rating: 1354) | Topic: `Double-Ended Queue Brute Force Insertion/Deletion with Priority Queue` | Analysis: [`analysis/AtCoder-abc128_d.md`](analysis/AtCoder-abc128_d.md)
- `[problem:AtCoder-abc120_d]` — **Decayed Bridges** (Rating: 1355) | Topic: `Reverse Offline Edge Addition with DSU Connected Component Pairs` | Analysis: [`analysis/AtCoder-abc120_d.md`](analysis/AtCoder-abc120_d.md)
- `[problem:AtCoder-abc187_e]` — **Through Path** (Rating: 1358) | Topic: `Tree Edge Cut Orienting with Subtree Difference Array DFS` | Analysis: [`analysis/AtCoder-abc187_e.md`](analysis/AtCoder-abc187_e.md)
- `[problem:AtCoder-arc063_b]` — **An Invisible Hand** (Rating: 1376) | Topic: `Stock Buy-Low Sell-High Count of Max Profit Pairs` | Analysis: [`analysis/AtCoder-arc063_b.md`](analysis/AtCoder-arc063_b.md)
- `[problem:AtCoder-abc037_d]` — **Paths** (Rating: 1377) | Topic: `2D Grid Strictly Increasing Paths Memoized DFS / DAG DP` | Analysis: [`analysis/AtCoder-abc037_d.md`](analysis/AtCoder-abc037_d.md)
- `[problem:AtCoder-abc019_4]` — **Takahashi and Tree** (Rating: 1378) | Topic: `Interactive Tree Diameter via 2-Query BFS/DFS` | Analysis: [`analysis/AtCoder-abc019_4.md`](analysis/AtCoder-abc019_4.md)
- `[problem:AtCoder-abc197_e]` — **Traveler** (Rating: 1379) | Topic: `Coordinate Compression Color Segments Left/Right DP` | Analysis: [`analysis/AtCoder-abc197_e.md`](analysis/AtCoder-abc197_e.md)
- `[problem:AtCoder-abc080_d]` — **Recording** (Rating: 1383) | Topic: `Channel Interval Merging with Imos Difference Array` | Analysis: [`analysis/AtCoder-abc080_d.md`](analysis/AtCoder-abc080_d.md)
- `[problem:AtCoder-abc015_4]` — **Takahashi's Pain** (Rating: 1388) | Topic: `2D Bound 0-1 Knapsack DP (Capacity + Item Count Limit)` | Analysis: [`analysis/AtCoder-abc015_4.md`](analysis/AtCoder-abc015_4.md)
- `[problem:AtCoder-abc104_c]` — **All Green** (Rating: 1393) | Topic: `Bitmask Complete Problem Sets with Fractional Greedy Fill` | Analysis: [`analysis/AtCoder-abc104_c.md`](analysis/AtCoder-abc104_c.md)
- `[problem:AtCoder-abc153_f]` — **Silver Fox vs Monster** (Rating: 1393) | Topic: `Coordinate Range Bombs with Queue / Difference Array Greedy` | Analysis: [`analysis/AtCoder-abc153_f.md`](analysis/AtCoder-abc153_f.md)
- `[problem:AtCoder-abc029_d]` — **1** (Rating: 1393) | Topic: `Digit DP Counting Occurrences of Digit '1'` | Analysis: [`analysis/AtCoder-abc029_d.md`](analysis/AtCoder-abc029_d.md)
- `[problem:AtCoder-abc142_e]` — **Get Everything** (Rating: 1397) | Topic: `Exact Set Cover Shortest Path / Bitmask Knapsack DP` | Analysis: [`analysis/AtCoder-abc142_e.md`](analysis/AtCoder-abc142_e.md)
- `[problem:AtCoder-arc098_b]` — **Xor Sum 2** (Rating: 1404) | Topic: `Two Pointers Bitwise Disjoint Subarray Counting (Sum == XOR)` | Analysis: [`analysis/AtCoder-arc098_b.md`](analysis/AtCoder-arc098_b.md)
- `[problem:AtCoder-abc026_d]` — **Takahashi and Equation** (Rating: 1406) | Topic: `Binary Search on Continuous Function f(t) = At + B sin(Ct) = 100` | Analysis: [`analysis/AtCoder-abc026_d.md`](analysis/AtCoder-abc026_d.md)

### Batch 4 Part 2B: ABC Curated Ladder (1409 - 1459)
- `[problem:AtCoder-abc212_e]` — **Safety Journey** (Rating: 1410) | Topic: `Complement Graph DP / Total Sum Subtraction Trick` | Analysis: [`analysis/AtCoder-abc212_e.md`](analysis/AtCoder-abc212_e.md)
- `[problem:AtCoder-abc215_e]` — **Chain Contestant** (Rating: 1413) | Topic: `Bitmask DP with Contiguous Element Tracking` | Analysis: [`analysis/AtCoder-abc215_e.md`](analysis/AtCoder-abc215_e.md)
- `[problem:AtCoder-abc002_4]` — **Faction** (Rating: 1418) | Topic: `Maximum Clique via Bitmask Verification` | Analysis: [`analysis/AtCoder-abc002_4.md`](analysis/AtCoder-abc002_4.md)
- `[problem:AtCoder-abc184_e]` — **Third Avenue** (Rating: 1418) | Topic: `Grid BFS with Teleporter Equivalence Class Clearance` | Analysis: [`analysis/AtCoder-abc184_e.md`](analysis/AtCoder-abc184_e.md)
- `[problem:AtCoder-abc184_f]` — **Programming Contest** (Rating: 1423) | Topic: `Meet-in-the-Middle on Subset Sum N <= 40` | Analysis: [`analysis/AtCoder-abc184_f.md`](analysis/AtCoder-abc184_f.md)
- `[problem:AtCoder-abc117_d]` — **XXOR** (Rating: 1423) | Topic: `Bitwise Digit DP with Upper Bound Constraint` | Analysis: [`analysis/AtCoder-abc117_d.md`](analysis/AtCoder-abc117_d.md)
- `[problem:AtCoder-abc192_d]` — **Base n** (Rating: 1425) | Topic: `Binary Search on Positional Notation Base with Overflow Guard` | Analysis: [`analysis/AtCoder-abc192_d.md`](analysis/AtCoder-abc192_d.md)
- `[problem:AtCoder-arc078_b]` — **Fennec VS. Snuke** (Rating: 1431) | Topic: `Tree Multi-Source BFS Voronoi Territory Partition` | Analysis: [`analysis/AtCoder-arc078_b.md`](analysis/AtCoder-arc078_b.md)
- `[problem:AtCoder-abc131_e]` — **Friendships** (Rating: 1433) | Topic: `Star Graph Baseline with Redundant Edge Reduction` | Analysis: [`analysis/AtCoder-abc131_e.md`](analysis/AtCoder-abc131_e.md)
- `[problem:AtCoder-abc034_c]` — **Grid Paths** (Rating: 1440) | Topic: `Large Grid Path Combinations via Modular Inverse Factorials` | Analysis: [`analysis/AtCoder-abc034_c.md`](analysis/AtCoder-abc034_c.md)
- `[problem:AtCoder-abc167_e]` — **Colorful Blocks** (Rating: 1442) | Topic: `Adjacent Matching Constraints Combinatorics` | Analysis: [`analysis/AtCoder-abc167_e.md`](analysis/AtCoder-abc167_e.md)
- `[problem:AtCoder-abc157_e]` — **Simple String Queries** (Rating: 1443) | Topic: `Alphabet Frequency Fenwick Trees / Ordered Sets` | Analysis: [`analysis/AtCoder-abc157_e.md`](analysis/AtCoder-abc157_e.md)
- `[problem:AtCoder-arc093_b]` — **Grid Components** (Rating: 1445) | Topic: `Split Half Grid with Isolated Dot Sprinkling` | Analysis: [`analysis/AtCoder-arc093_b.md`](analysis/AtCoder-arc093_b.md)
- `[problem:AtCoder-abc005_4]` — **Takoyaki Plate** (Rating: 1447) | Topic: `2D Prefix Sums Subrectangle Optimization with Monotonic Envelope` | Analysis: [`analysis/AtCoder-abc005_4.md`](analysis/AtCoder-abc005_4.md)
- `[problem:AtCoder-abc144_e]` — **Gluttony** (Rating: 1449) | Topic: `Monotonic Binary Search on Multiplicative Work Allocation` | Analysis: [`analysis/AtCoder-abc144_e.md`](analysis/AtCoder-abc144_e.md)
- `[problem:AtCoder-abc159_e]` — **Dividing Chocolate** (Rating: 1450) | Topic: `Bitmask Horizontal Cuts with Greedy Vertical Sweeping` | Analysis: [`analysis/AtCoder-abc159_e.md`](analysis/AtCoder-abc159_e.md)
- `[problem:AtCoder-arc090_b]` — **People on a Line** (Rating: 1452) | Topic: `Potentialized Disjoint Set Union (Weighted DSU)` | Analysis: [`analysis/AtCoder-arc090_b.md`](analysis/AtCoder-arc090_b.md)
- `[problem:AtCoder-abc148_f]` — **Playing Tag on Tree** (Rating: 1457) | Topic: `Tree BFS Distances and Evader Leaf Reachability` | Analysis: [`analysis/AtCoder-abc148_f.md`](analysis/AtCoder-abc148_f.md)
- `[problem:AtCoder-abc105_d]` — **Candy Distribution** (Rating: 1458) | Topic: `Prefix Sum Modulo Frequency Matching` | Analysis: [`analysis/AtCoder-abc105_d.md`](analysis/AtCoder-abc105_d.md)
- `[problem:AtCoder-abc141_e]` — **Who Says a Pun?** (Rating: 1459) | Topic: `Longest Common Non-Overlapping Substring DP` | Analysis: [`analysis/AtCoder-abc141_e.md`](analysis/AtCoder-abc141_e.md)

### Batch 4 Part 3A: ABC Curated Ladder (1460 - 1528)
- `[problem:AtCoder-arc108_c]` — **Keep Graph Connected** (Rating: 1460) | Topic: `Spanning Tree Constructive Node Coloring` | Analysis: [`analysis/AtCoder-arc108_c.md`](analysis/AtCoder-arc108_c.md)
- `[problem:AtCoder-abc186_e]` — **Throne** (Rating: 1461) | Topic: `Linear Congruence Equation via Extended Euclidean Algorithm` | Analysis: [`analysis/AtCoder-abc186_e.md`](analysis/AtCoder-abc186_e.md)
- `[problem:AtCoder-abc251_d]` — **At Most 3** (Rating: 1463) | Topic: `Constructive Base-100 Representation for Additive Basis` | Analysis: [`analysis/AtCoder-abc251_d.md`](analysis/AtCoder-abc251_d.md)
- `[problem:AtCoder-abc349_e]` — **Weighted Tic-Tac-Toe** (Rating: 1464) | Topic: `3x3 Grid Minimax Game DP with Memoization` | Analysis: [`analysis/AtCoder-abc349_e.md`](analysis/AtCoder-abc349_e.md)
- `[problem:AtCoder-abc285_e]` — **Work or Rest** (Rating: 1466) | Topic: `Circular Segment Decomposition DP` | Analysis: [`analysis/AtCoder-abc285_e.md`](analysis/AtCoder-abc285_e.md)
- `[problem:AtCoder-abc185_e]` — **Sequence Matching** (Rating: 1468) | Topic: `Edit Distance / Sequence Alignment DP with Cost Function` | Analysis: [`analysis/AtCoder-abc185_e.md`](analysis/AtCoder-abc185_e.md)
- `[problem:AtCoder-arc116_c]` — **Multiple Sequences** (Rating: 1468) | Topic: `Prime Factorization Combinatorics / Stars and Bars` | Analysis: [`analysis/AtCoder-arc116_c.md`](analysis/AtCoder-arc116_c.md)
- `[problem:AtCoder-abc075_d]` — **Axis-Parallel Rectangle** (Rating: 1470) | Topic: `2D Coordinate Selection O(N^4) Search for K Points` | Analysis: [`analysis/AtCoder-abc075_d.md`](analysis/AtCoder-abc075_d.md)
- `[problem:AtCoder-arc073_b]` — **Simple Knapsack** (Rating: 1477) | Topic: `Knapsack with Small Weight Variance [W, W+3]` | Analysis: [`analysis/AtCoder-arc073_b.md`](analysis/AtCoder-arc073_b.md)
- `[problem:AtCoder-arc120_c]` — **Swaps 2** (Rating: 1478) | Topic: `Invariant Value Coordinate Assignment + Fenwick Inversion Counting` | Analysis: [`analysis/AtCoder-arc120_c.md`](analysis/AtCoder-arc120_c.md)
- `[problem:AtCoder-abc290_e]` — **Make it Palindrome** (Rating: 1485) | Topic: `Two Pointers Contribution to Sum for Non-Matching Pairs` | Analysis: [`analysis/AtCoder-abc290_e.md`](analysis/AtCoder-abc290_e.md)
- `[problem:AtCoder-abc123_d]` — **Cake 123** (Rating: 1489) | Topic: `Priority Queue Top-K Sum of Three Arrays (Pruning to K)` | Analysis: [`analysis/AtCoder-abc123_d.md`](analysis/AtCoder-abc123_d.md)
- `[problem:AtCoder-abc175_d]` — **Moving Piece** (Rating: 1491) | Topic: `Functional Graph Permutation Cycle Decomposition with Round Trips` | Analysis: [`analysis/AtCoder-abc175_d.md`](analysis/AtCoder-abc175_d.md)
- `[problem:AtCoder-abc222_e]` — **Red and Blue Tree** (Rating: 1491) | Topic: `Tree Edge Frequencies via DFS + Subset Sum Knapsack` | Analysis: [`analysis/AtCoder-abc222_e.md`](analysis/AtCoder-abc222_e.md)
- `[problem:AtCoder-abc174_f]` — **Range Set Query** (Rating: 1495) | Topic: `Offline Range Distinct Elements Query using Fenwick Tree` | Analysis: [`analysis/AtCoder-abc174_f.md`](analysis/AtCoder-abc174_f.md)
- `[problem:AtCoder-abc170_e]` — **Smart Infants** (Rating: 1502) | Topic: `Dual Multiset (Multiset of Multiset Maxima) Dynamic Maintenance` | Analysis: [`analysis/AtCoder-abc170_e.md`](analysis/AtCoder-abc170_e.md)
- `[problem:AtCoder-abc022_c]` — **Blue Bird** (Rating: 1505) | Topic: `Shortest Cycle through Source via All-Pairs Shortest Path` | Analysis: [`analysis/AtCoder-abc022_c.md`](analysis/AtCoder-abc022_c.md)
- `[problem:AtCoder-abc133_e]` — **Virus Tree 2** (Rating: 1505) | Topic: `Distance-2 Tree Coloring Combinatorics via DFS` | Analysis: [`analysis/AtCoder-abc133_e.md`](analysis/AtCoder-abc133_e.md)
- `[problem:AtCoder-abc210_d]` — **National Railway** (Rating: 1507) | Topic: `2D Grid DP Coordinate Manhattan Distance Transformation` | Analysis: [`analysis/AtCoder-abc210_d.md`](analysis/AtCoder-abc210_d.md)
- `[problem:AtCoder-arc087_b]` — **FT Robot** (Rating: 1508) | Topic: `Independent X/Y Coordinate Subset Sum Knapsack DP` | Analysis: [`analysis/AtCoder-arc087_b.md`](analysis/AtCoder-arc087_b.md)
- `[problem:AtCoder-abc156_e]` — **Roaming** (Rating: 1514) | Topic: `Stars and Bars Empty Boxes Combinatorics` | Analysis: [`analysis/AtCoder-abc156_e.md`](analysis/AtCoder-abc156_e.md)
- `[problem:AtCoder-abc189_e]` — **Rotate and Flip** (Rating: 1526) | Topic: `2D Affine Transformation Matrix Composition` | Analysis: [`analysis/AtCoder-abc189_e.md`](analysis/AtCoder-abc189_e.md)

### Batch 4 Part 3B: ABC Curated Ladder (1528 - 1599)
- `[problem:AtCoder-abc139_e]` — **League** (Rating: 1528) | Topic: `DAG Longest Path / Topological Sort on Match Dependencies` | Analysis: [`analysis/AtCoder-abc139_e.md`](analysis/AtCoder-abc139_e.md)
- `[problem:AtCoder-abc145_e]` — **All-you-can-eat** (Rating: 1528) | Topic: `Order-Dependent 0-1 Knapsack (Sorting by Time Before DP)` | Analysis: [`analysis/AtCoder-abc145_e.md`](analysis/AtCoder-abc145_e.md)
- `[problem:AtCoder-abc161_f]` — **Division or Subtraction** (Rating: 1528) | Topic: `Number Theory Divisor Analysis on N and N-1` | Analysis: [`analysis/AtCoder-abc161_f.md`](analysis/AtCoder-abc161_f.md)
- `[problem:AtCoder-abc122_d]` — **We Like AGC** (Rating: 1533) | Topic: `Dynamic Programming on Last 3 Characters / Forbidden Pattern Counting` | Analysis: [`analysis/AtCoder-abc122_d.md`](analysis/AtCoder-abc122_d.md)
- `[problem:AtCoder-abc150_d]` — **Semi Common Multiple** (Rating: 1534) | Topic: `2-adic Valuation & Odd Multiple LCM Condition` | Analysis: [`analysis/AtCoder-abc150_d.md`](analysis/AtCoder-abc150_d.md)
- `[problem:AtCoder-abc027_c]` — **Doubling Game** (Rating: 1539) | Topic: `Binary Tree Game Theory Minimax Depth Parity` | Analysis: [`analysis/AtCoder-abc027_c.md`](analysis/AtCoder-abc027_c.md)
- `[problem:AtCoder-arc075_b]` — **Widespread** (Rating: 1544) | Topic: `Binary Search on Answer / Splash Damage Allocation` | Analysis: [`analysis/AtCoder-arc075_b.md`](analysis/AtCoder-arc075_b.md)
- `[problem:AtCoder-arc079_b]` — **Decrease** (Rating: 1545) | Topic: `Reverse Operation Constructive Array Synthesis modulo N` | Analysis: [`analysis/AtCoder-arc079_b.md`](analysis/AtCoder-arc079_b.md)
- `[problem:AtCoder-abc146_f]` — **Sugoroku** (Rating: 1545) | Topic: `Greedy Reverse BFS / Range Minimum for Lexicographical Jumps` | Analysis: [`analysis/AtCoder-abc146_f.md`](analysis/AtCoder-abc146_f.md)
- `[problem:AtCoder-abc129_e]` — **Sum Equals Xor** (Rating: 1547) | Topic: `Digit DP on Bitwise Condition a + b = a ^ b (Disjoint Bits)` | Analysis: [`analysis/AtCoder-abc129_e.md`](analysis/AtCoder-abc129_e.md)
- `[problem:AtCoder-abc034_d]` — **Salt Water** (Rating: 1549) | Topic: `Binary Search on Average / Dinkelbach Fractional Programming` | Analysis: [`analysis/AtCoder-abc034_d.md`](analysis/AtCoder-abc034_d.md)
- `[problem:AtCoder-arc085_b]` — **ABS** (Rating: 1550) | Topic: `Game Theory Minimax 1-Step Lookahead / Card Draw Reduction` | Analysis: [`analysis/AtCoder-arc085_b.md`](analysis/AtCoder-arc085_b.md)
- `[problem:AtCoder-abc018_3]` — **Diamond Count** (Rating: 1553) | Topic: `2D Vertical Consecutive Run Prefix Sums for Diamond Pattern Matching` | Analysis: [`analysis/AtCoder-abc018_3.md`](analysis/AtCoder-abc018_3.md)
- `[problem:AtCoder-abc175_e]` — **Picking Goods** (Rating: 1554) | Topic: `2D Grid DP with Per-Row Item Capacity Constraint (At Most 3 Items)` | Analysis: [`analysis/AtCoder-abc175_e.md`](analysis/AtCoder-abc175_e.md)
- `[problem:AtCoder-arc083_b]` — **Restoring Road Network** (Rating: 1563) | Topic: `Reverse Floyd-Warshall Strict Triangle Inequality Edge Minimality` | Analysis: [`analysis/AtCoder-arc083_b.md`](analysis/AtCoder-arc083_b.md)
- `[problem:AtCoder-abc051_d]` — **Candidates of No Shortest Paths** (Rating: 1566) | Topic: `Floyd-Warshall Edge Shortest Path Criterion` | Analysis: [`analysis/AtCoder-abc051_d.md`](analysis/AtCoder-abc051_d.md)
- `[problem:AtCoder-arc086_b]` — **Non-decreasing** (Rating: 1567) | Topic: `Constructive Prefix/Suffix Cumulative Addition via Global Dominant Extremum` | Analysis: [`analysis/AtCoder-arc086_b.md`](analysis/AtCoder-arc086_b.md)
- `[problem:AtCoder-abc155_e]` — **Payment** (Rating: 1569) | Topic: `Digit DP with Carry on Minimum Digits for Payment and Change` | Analysis: [`analysis/AtCoder-abc155_e.md`](analysis/AtCoder-abc155_e.md)
- `[problem:AtCoder-arc060_a]` — **Tak and Cards** (Rating: 1583) | Topic: `Subset Average Equals A via Shifted Zero-Sum Knapsack DP` | Analysis: [`analysis/AtCoder-arc060_a.md`](analysis/AtCoder-arc060_a.md)
- `[problem:AtCoder-abc030_d]` — **Strange Dictionary** (Rating: 1586) | Topic: `Functional Graph Cycle Detection with Large K (K up to 10^100000)` | Analysis: [`analysis/AtCoder-abc030_d.md`](analysis/AtCoder-abc030_d.md)
- `[problem:AtCoder-abc183_f]` — **Confluence** (Rating: 1586) | Topic: `Disjoint Set Union with Small-to-Large Map Merging` | Analysis: [`analysis/AtCoder-abc183_f.md`](analysis/AtCoder-abc183_f.md)
- `[problem:AtCoder-abc035_d]` — **Treasure Hunt** (Rating: 1591) | Topic: `Forward & Reversed Graph Dijkstra for Time-Constrained Round Trips` | Analysis: [`analysis/AtCoder-abc035_d.md`](analysis/AtCoder-abc035_d.md)
- `[problem:AtCoder-abc113_d]` — **Number of Amidakuji** (Rating: 1597) | Topic: `DP over Amidakuji Horizontal Bars via Non-Adjacent Bitmasks` | Analysis: [`analysis/AtCoder-abc113_d.md`](analysis/AtCoder-abc113_d.md)

### Batch 5 Part 1A: ABC Curated Ladder (1600 - 1650)
- `[problem:AtCoder-abc036_d]` — **Coloring** (Rating: 1602) | Topic: `Tree DP: White or Black Coloring with No Adjacent Black Nodes` | Analysis: [`analysis/AtCoder-abc036_d.md`](analysis/AtCoder-abc036_d.md)
- `[problem:AtCoder-arc043_b]` — **Difficulty** (Rating: 1606) | Topic: `4-Step Increasing Sequence with 2x Ratio via Coordinate Prefix Sums` | Analysis: [`analysis/AtCoder-arc043_b.md`](analysis/AtCoder-arc043_b.md)
- `[problem:AtCoder-abc017_3]` — **High Score** (Rating: 1607) | Topic: `Complementary Segment Imos / Minimum Cost Interval Piercing` | Analysis: [`analysis/AtCoder-abc017_3.md`](analysis/AtCoder-abc017_3.md)
- `[problem:AtCoder-abc173_e]` — **Multiplication 4** (Rating: 1607) | Topic: `Greedy Maximum Product of K Integers with Signed Extremum` | Analysis: [`analysis/AtCoder-abc173_e.md`](analysis/AtCoder-abc173_e.md)
- `[problem:AtCoder-abc195_e]` — **Lucky 7 Battle** (Rating: 1609) | Topic: `Backward Game Theory DP modulo 7 with Controllable State Sets` | Analysis: [`analysis/AtCoder-abc195_e.md`](analysis/AtCoder-abc195_e.md)
- `[problem:AtCoder-arc076_b]` — **Built?** (Rating: 1615) | Topic: `Minimum Spanning Tree on 2D Points via Adjacent Coordinate Edges` | Analysis: [`analysis/AtCoder-arc076_b.md`](analysis/AtCoder-arc076_b.md)
- `[problem:AtCoder-abc210_e]` — **Ring MST** (Rating: 1618) | Topic: `Kruskal MST on Ring via Modular GCD Component Reduction` | Analysis: [`analysis/AtCoder-abc210_e.md`](analysis/AtCoder-abc210_e.md)
- `[problem:AtCoder-abc165_e]` — **Rotation Matching** (Rating: 1620) | Topic: `Constructive Distance Parity Partitioning on Circular Cycle` | Analysis: [`analysis/AtCoder-abc165_e.md`](analysis/AtCoder-abc165_e.md)
- `[problem:AtCoder-abc203_d]` — **Pond** (Rating: 1622) | Topic: `2D Subgrid Median via Binary Search on Answer + 2D Prefix Sums` | Analysis: [`analysis/AtCoder-abc203_d.md`](analysis/AtCoder-abc203_d.md)
- `[problem:AtCoder-abc132_e]` — **Hopscotch Addict** (Rating: 1625) | Topic: `Modulo-3 Expanded Graph Shortest Path BFS` | Analysis: [`analysis/AtCoder-abc132_e.md`](analysis/AtCoder-abc132_e.md)
- `[problem:AtCoder-arc017_3]` — **Minimalist** (Rating: 1625) | Topic: `Meet-in-the-Middle on Subset Sum N <= 32` | Analysis: [`analysis/AtCoder-arc017_3.md`](analysis/AtCoder-arc017_3.md)
- `[problem:AtCoder-abc202_e]` — **Count Descendants** (Rating: 1638) | Topic: `Euler Tour Subtree Range Query + Depth Coordinate Binary Search` | Analysis: [`analysis/AtCoder-abc202_e.md`](analysis/AtCoder-abc202_e.md)
- `[problem:AtCoder-abc025_c]` — **Twins and Tic-Tac-Toe** (Rating: 1640) | Topic: `Minimax Search on 3x3 Game Board with Known Payoff Functions` | Analysis: [`analysis/AtCoder-abc025_c.md`](analysis/AtCoder-abc025_c.md)
- `[problem:AtCoder-arc071_b]` — **###** (Rating: 1641) | Topic: `2D Rectilinear Area Decomposition into 1D Coordinate Gaps` | Analysis: [`analysis/AtCoder-arc071_b.md`](analysis/AtCoder-arc071_b.md)
- `[problem:AtCoder-arc033_3]` — **Data Structure** (Rating: 1641) | Topic: `Binary Lifting on Fenwick Tree for K-th Smallest Element` | Analysis: [`analysis/AtCoder-arc033_3.md`](analysis/AtCoder-arc033_3.md)
- `[problem:AtCoder-abc227_d]` — **Project Planning** (Rating: 1643) | Topic: `Binary Search on Answer with Capped Work Allocations min(A_i, P)` | Analysis: [`analysis/AtCoder-abc227_d.md`](analysis/AtCoder-abc227_d.md)
- `[problem:AtCoder-abc190_e]` — **Magical Ornament** (Rating: 1645) | Topic: `Multi-Source BFS on K Targets + TSP Bitmask DP` | Analysis: [`analysis/AtCoder-abc190_e.md`](analysis/AtCoder-abc190_e.md)
- `[problem:AtCoder-abc321_f]` — **#(subset sum = K) with Add and Erase** (Rating: 1645) | Topic: `Dynamic 0-1 Knapsack with Rollback / Subtraction Undo` | Analysis: [`analysis/AtCoder-abc321_f.md`](analysis/AtCoder-abc321_f.md)
- `[problem:AtCoder-arc088_b]` — **Wide Flip** (Rating: 1646) | Topic: `Central Boundary Invariant on Reversible Interval Flips` | Analysis: [`analysis/AtCoder-arc088_b.md`](analysis/AtCoder-arc088_b.md)
- `[problem:AtCoder-abc196_e]` — **Filters** (Rating: 1650) | Topic: `Composition of Clamping Intervals [L, R] with Linear Shift` | Analysis: [`analysis/AtCoder-abc196_e.md`](analysis/AtCoder-abc196_e.md)
- `[problem:AtCoder-abc282_e]` — **Choose Two and Eat One** (Rating: 1604) | Topic: `Maximum Spanning Tree on Complete Graph with Modular Exponentiation` | Analysis: [`analysis/AtCoder-abc282_e.md`](analysis/AtCoder-abc282_e.md)
- `[problem:AtCoder-abc275_f]` — **Erase Subarrays** (Rating: 1608) | Topic: `2-State DP on Subarray Deletion to Match Target Sum` | Analysis: [`analysis/AtCoder-abc275_f.md`](analysis/AtCoder-abc275_f.md)

### Batch 5 Part 1B: ABC Curated Ladder (1651 - 1699)
- `[problem:AtCoder-abc054_d]` — **Mixing Experiment** (Rating: 1655) | Topic: `2-Ratio Knapsack DP / Ratio Reduction to Target GCD` | Analysis: [`analysis/AtCoder-abc054_d.md`](analysis/AtCoder-abc054_d.md)
- `[problem:AtCoder-arc035_c]` — **Traffic Conditions in AtCoder Kingdom** (Rating: 1655) | Topic: `Online All-Pairs Shortest Path Incremental Edge Addition` | Analysis: [`analysis/AtCoder-arc035_c.md`](analysis/AtCoder-arc035_c.md)
- `[problem:AtCoder-abc040_d]` — **Road Aging Countermeasures** (Rating: 1656) | Topic: `Offline Query Sorting with Disjoint Set Union Sweep-Line` | Analysis: [`analysis/AtCoder-abc040_d.md`](analysis/AtCoder-abc040_d.md)
- `[problem:AtCoder-abc118_d]` — **Match Matching** (Rating: 1657) | Topic: `Unbounded Knapsack for Lexicographically Largest Number` | Analysis: [`analysis/AtCoder-abc118_d.md`](analysis/AtCoder-abc118_d.md)
- `[problem:AtCoder-abc224_e]` — **Integers on Grid** (Rating: 1657) | Topic: `Group-by-Value DP on Grids with Row/Column Maximum Buffering` | Analysis: [`analysis/AtCoder-abc224_e.md`](analysis/AtCoder-abc224_e.md)
- `[problem:AtCoder-abc057_d]` — **Maximum Average Sets** (Rating: 1658) | Topic: `Greedy Top Elements Average + Combinatorics on Boundary Frequency` | Analysis: [`analysis/AtCoder-abc057_d.md`](analysis/AtCoder-abc057_d.md)
- `[problem:AtCoder-abc263_e]` — **Sugoroku 3** (Rating: 1659) | Topic: `Expected Value DP with Self-Loop Formula + Range Sum Acceleration` | Analysis: [`analysis/AtCoder-abc263_e.md`](analysis/AtCoder-abc263_e.md)
- `[problem:AtCoder-abc244_f]` — **Shortest Good Path** (Rating: 1661) | Topic: `Shortest Path on Graph with Bitmask Parities (0-1 BFS)` | Analysis: [`analysis/AtCoder-abc244_f.md`](analysis/AtCoder-abc244_f.md)
- `[problem:AtCoder-abc162_e]` — **Sum of gcd of Tuples** (Rating: 1662) | Topic: `Inclusion-Exclusion Multiple Counting from K down to 1` | Analysis: [`analysis/AtCoder-abc162_e.md`](analysis/AtCoder-abc162_e.md)
- `[problem:AtCoder-abc166_f]` — **Three Variables Game** (Rating: 1668) | Topic: `Greedy Lookahead with Invariant Sum Constrained State` | Analysis: [`analysis/AtCoder-abc166_f.md`](analysis/AtCoder-abc166_f.md)
- `[problem:AtCoder-abc271_f]` — **XOR on Grid Path** (Rating: 1669) | Topic: `Meet-in-the-Middle on 2D Grid Paths` | Analysis: [`analysis/AtCoder-abc271_f.md`](analysis/AtCoder-abc271_f.md)
- `[problem:AtCoder-abc041_d]` — **Footrace** (Rating: 1670) | Topic: `Topological Ordering Count via Bitmask DP` | Analysis: [`analysis/AtCoder-abc041_d.md`](analysis/AtCoder-abc041_d.md)
- `[problem:AtCoder-abc136_e]` — **Max GCD** (Rating: 1670) | Topic: `Sum-Invariant Divisor Analysis on Array GCD` | Analysis: [`analysis/AtCoder-abc136_e.md`](analysis/AtCoder-abc136_e.md)
- `[problem:AtCoder-abc151_f]` — **Enclose All** (Rating: 1671) | Topic: `Minimum Enclosing Circle: Pair and Triple Circumcircle Search` | Analysis: [`analysis/AtCoder-abc151_f.md`](analysis/AtCoder-abc151_f.md)
- `[problem:AtCoder-abc130_e]` — **Common Subsequence** (Rating: 1676) | Topic: `2D DP Counting Common Subsequences with 2D Prefix Sums` | Analysis: [`analysis/AtCoder-abc130_e.md`](analysis/AtCoder-abc130_e.md)
- `[problem:AtCoder-abc246_f]` — **typewriter** (Rating: 1677) | Topic: `Principle of Inclusion-Exclusion (PIE) on Keyboard Key Sets` | Analysis: [`analysis/AtCoder-abc246_f.md`](analysis/AtCoder-abc246_f.md)
- `[problem:AtCoder-arc061_b]` — **Snuke's Coloring** (Rating: 1682) | Topic: `Sparse Grid 3x3 Window Counting via Coordinate Hash Map` | Analysis: [`analysis/AtCoder-arc061_b.md`](analysis/AtCoder-arc061_b.md)
- `[problem:AtCoder-abc031_d]` — **Goroawase** (Rating: 1688) | Topic: `Digit String Length Partition Search` | Analysis: [`analysis/AtCoder-abc031_d.md`](analysis/AtCoder-abc031_d.md)
- `[problem:AtCoder-abc219_e]` — **Moat** (Rating: 1690) | Topic: `Bitmask Grid Shapes with Connectivity (DSU) and Hole-Free (Outer BFS) Checking` | Analysis: [`analysis/AtCoder-abc219_e.md`](analysis/AtCoder-abc219_e.md)
- `[problem:AtCoder-abc260_e]` — **At Least One** (Rating: 1692) | Topic: `Two Pointers / Sliding Window on Multi-Interval Coverage` | Analysis: [`analysis/AtCoder-abc260_e.md`](analysis/AtCoder-abc260_e.md)
- `[problem:AtCoder-abc201_e]` — **Xor Distances** (Rating: 1694) | Topic: `Tree XOR Distances Bit-by-Bit Counting via Root DFS` | Analysis: [`analysis/AtCoder-abc201_e.md`](analysis/AtCoder-abc201_e.md)
- `[problem:AtCoder-arc022_3]` — **Romeo and Juliet** (Rating: 1694) | Topic: `Tree Diameter Endpoints via 2-Pass BFS/DFS` | Analysis: [`analysis/AtCoder-arc022_3.md`](analysis/AtCoder-arc022_3.md)
- `[problem:AtCoder-abc110_d]` — **Factorization** (Rating: 1695) | Topic: `Prime Factorization + Stars and Bars on Exponents` | Analysis: [`analysis/AtCoder-abc110_d.md`](analysis/AtCoder-abc110_d.md)
- `[problem:AtCoder-abc143_e]` — **Travel by Car** (Rating: 1695) | Topic: `Dual Floyd-Warshall (Distance Reachability then Refuel Count)` | Analysis: [`analysis/AtCoder-abc143_e.md`](analysis/AtCoder-abc143_e.md)
- `[problem:AtCoder-abc006_4]` — **Playing Cards Insertion Sort** (Rating: 1696) | Topic: `Minimum Card Insertions = N - LIS(A) via Patience Sorting` | Analysis: [`analysis/AtCoder-abc006_4.md`](analysis/AtCoder-abc006_4.md)
- `[problem:AtCoder-abc247_f]` — **Cards** (Rating: 1697) | Topic: `Functional Graph Permutation Cycle Decomposition + Lucas Numbers` | Analysis: [`analysis/AtCoder-abc247_f.md`](analysis/AtCoder-abc247_f.md)
- `[problem:AtCoder-abc169_f]` — **Knapsack for All Subsets** (Rating: 1698) | Topic: `3-Choice State Dynamic Programming on Subsets of Subsets` | Analysis: [`analysis/AtCoder-abc169_f.md`](analysis/AtCoder-abc169_f.md)

### Batch 5 Part 2A: ABC Curated Ladder (1700 - 1750)
- `[problem:AtCoder-abc294_g]` — **Distance Queries on a Tree** (Rating: 1702) | Topic: `Dynamic Tree Distance via Euler Tour Subtree Add and LCA` | Analysis: [`analysis/AtCoder-abc294_g.md`](analysis/AtCoder-abc294_g.md)
- `[problem:AtCoder-abc021_d]` — **多重ループ** (Rating: 1704) | Topic: `Multiset Combination with Repetition: C(n + k - 1, k)` | Analysis: [`analysis/AtCoder-abc021_d.md`](analysis/AtCoder-abc021_d.md)
- `[problem:AtCoder-arc147_c]` — **Min Diff Sum** (Rating: 1704) | Topic: `Min Sum of Pairwise Differences on Intervals via Median Pairing` | Analysis: [`analysis/AtCoder-arc147_c.md`](analysis/AtCoder-arc147_c.md)
- `[problem:AtCoder-abc204_e]` — **Rush Hour 2** (Rating: 1710) | Topic: `Dijkstra with Convex Time-Dependent Delay / Derivative Optimization` | Analysis: [`analysis/AtCoder-abc204_e.md`](analysis/AtCoder-abc204_e.md)
- `[problem:AtCoder-abc018_4]` — **バレンタインデー** (Rating: 1711) | Topic: `Partial Bitmask Enumeration with Greedy Sorting on Dual Dimension` | Analysis: [`analysis/AtCoder-abc018_4.md`](analysis/AtCoder-abc018_4.md)
- `[problem:AtCoder-abc116_d]` — **Various Sushi** (Rating: 1712) | Topic: `Greedy Exchange Argument with Two Compensating Quantities` | Analysis: [`analysis/AtCoder-abc116_d.md`](analysis/AtCoder-abc116_d.md)
- `[problem:AtCoder-abc147_e]` — **Balanced Path** (Rating: 1713) | Topic: `Grid Path Subset Sum with Bitset Acceleration` | Analysis: [`analysis/AtCoder-abc147_e.md`](analysis/AtCoder-abc147_e.md)
- `[problem:AtCoder-abc179_f]` — **Simplified Reversi** (Rating: 1713) | Topic: `Dual Monotonic Coordinate Chmin Query / 2D Reversi Boundary Tracking` | Analysis: [`analysis/AtCoder-abc179_f.md`](analysis/AtCoder-abc179_f.md)
- `[problem:AtCoder-arc077_b]` — **11** (Rating: 1715) | Topic: `Combinatorics on Single-Duplicate Sequence / Complementary Subsequence Counting` | Analysis: [`analysis/AtCoder-arc077_b.md`](analysis/AtCoder-arc077_b.md)
- `[problem:AtCoder-abc007_4]` — **禁止された数字** (Rating: 1718) | Topic: `Digit DP: Base-8 Conversion / Banned Digits Counting` | Analysis: [`analysis/AtCoder-abc007_4.md`](analysis/AtCoder-abc007_4.md)
- `[problem:AtCoder-arc116_d]` — **I Wanna Win The Game** (Rating: 1718) | Topic: `Bit-by-Bit Carry DP with XOR-Zero Parity Constraint` | Analysis: [`analysis/AtCoder-arc116_d.md`](analysis/AtCoder-arc116_d.md)
- `[problem:AtCoder-arc139_b]` — **Make N** (Rating: 1719) | Topic: `Square Root / LCM Dominance Threshold on 2-Denomination Unbounded Knapsack` | Analysis: [`analysis/AtCoder-arc139_b.md`](analysis/AtCoder-arc139_b.md)
- `[problem:AtCoder-arc103_c]` — **Tr/ee** (Rating: 1722) | Topic: `Tree Construction by Component Size Complementarity (Caterpillar Spine)` | Analysis: [`analysis/AtCoder-arc103_c.md`](analysis/AtCoder-arc103_c.md)
- `[problem:AtCoder-arc056_b]` — **駐車場** (Rating: 1726) | Topic: `Maximum Bottleneck Path via Modified Dijkstra / Min-Vertex Path Capacity` | Analysis: [`analysis/AtCoder-arc056_b.md`](analysis/AtCoder-arc056_b.md)
- `[problem:AtCoder-arc138_c]` — **Rotate and Play Game** (Rating: 1728) | Topic: `Raney's Lemma / Circular Prefix Balance on 2-Player Game` | Analysis: [`analysis/AtCoder-arc138_c.md`](analysis/AtCoder-arc138_c.md)
- `[problem:AtCoder-abc013_4]` — **阿弥陀** (Rating: 1730) | Topic: `Binary Lifting on Permutations / Amidakuji Exponentiation` | Analysis: [`analysis/AtCoder-abc013_4.md`](analysis/AtCoder-abc013_4.md)
- `[problem:AtCoder-arc074_b]` — **3N Numbers** (Rating: 1730) | Topic: `Dual Priority Queue Prefix/Suffix Optimization (3N Elements Partition)` | Analysis: [`analysis/AtCoder-arc074_b.md`](analysis/AtCoder-arc074_b.md)
- `[problem:AtCoder-abc032_d]` — **ナップサック問題** (Rating: 1731) | Topic: `Constraint-Adaptive Knapsack (Meet-in-the-Middle vs Weight DP vs Dual Value DP)` | Analysis: [`analysis/AtCoder-abc032_d.md`](analysis/AtCoder-abc032_d.md)
- `[problem:AtCoder-abc358_g]` — **AtCoder Tour** (Rating: 1737) | Topic: `Grid Graph Bounded Step DP with Infinite Stay Greedy Extension` | Analysis: [`analysis/AtCoder-abc358_g.md`](analysis/AtCoder-abc358_g.md)
- `[problem:AtCoder-abc104_d]` — **We Love ABC** (Rating: 1739) | Topic: `Subsequence Pattern Matching Expectation / DP on Automaton with Wildcards` | Analysis: [`analysis/AtCoder-abc104_d.md`](analysis/AtCoder-abc104_d.md)
- `[problem:AtCoder-arc071_c]` — **TrBBnsformBBtion** (Rating: 1739) | Topic: `Algebraic Invariant / Value Mapping Modulo 3 on String Rewriting` | Analysis: [`analysis/AtCoder-arc071_c.md`](analysis/AtCoder-arc071_c.md)
- `[problem:AtCoder-abc137_e]` — **Coins Respawn** (Rating: 1740) | Topic: `Bellman-Ford Constrained Negative Cycle Reachability (1 -> cycle -> N)` | Analysis: [`analysis/AtCoder-abc137_e.md`](analysis/AtCoder-abc137_e.md)
- `[problem:AtCoder-arc165_c]` — **Social Distance on Graph** (Rating: 1743) | Topic: `Binary Search on Min Same-Color Distance / Bipartite 2-Coloring Feasibility` | Analysis: [`analysis/AtCoder-arc165_c.md`](analysis/AtCoder-arc165_c.md)
- `[problem:AtCoder-arc044_b]` — **最短路問題** (Rating: 1744) | Topic: `Layered Graph Counting by BFS Distance Levels` | Analysis: [`analysis/AtCoder-arc044_b.md`](analysis/AtCoder-arc044_b.md)
- `[problem:AtCoder-abc206_e]` — **Divide Both** (Rating: 1745) | Topic: `Coprime / Divisor Multiple Counting with Extreme Quotient Exclusions` | Analysis: [`analysis/AtCoder-abc206_e.md`](analysis/AtCoder-abc206_e.md)
- `[problem:AtCoder-arc079_c]` — **Decrease (Judge ver.)** (Rating: 1745) | Topic: `Bulk Simulation / Monotonic Invariant on Multi-Decrement Process` | Analysis: [`analysis/AtCoder-arc079_c.md`](analysis/AtCoder-arc079_c.md)
- `[problem:AtCoder-arc042_c]` — **おやつ** (Rating: 1746) | Topic: `Descending Sort Relaxation on Knapsack Boundary (Exempt Heaviest Item)` | Analysis: [`analysis/AtCoder-arc042_c.md`](analysis/AtCoder-arc042_c.md)
- `[problem:AtCoder-arc161_c]` — **Dyed by Majority (Odd Tree)** (Rating: 1746) | Topic: `Greedy Leaf-Upwards Forcing on Tree Majority Constraints` | Analysis: [`analysis/AtCoder-arc161_c.md`](analysis/AtCoder-arc161_c.md)
- `[problem:AtCoder-arc028_3]` — **高橋王国の分割統治** (Rating: 1748) | Topic: `Tree Node Removal Max-Component Decomposition / Centroid Prerequisite` | Analysis: [`analysis/AtCoder-arc028_3.md`](analysis/AtCoder-arc028_3.md)
- `[problem:AtCoder-arc072_b]` — **Alice&Brown** (Rating: 1749) | Topic: `Impartial Game Parity / Modular Difference Invariant (|X - Y| <= 1)` | Analysis: [`analysis/AtCoder-arc072_b.md`](analysis/AtCoder-arc072_b.md)
- `[problem:AtCoder-abc203_e]` — **White Pawn** (Rating: 1750) | Topic: `Coordinate Set Row Sweep-Line with Simultaneous Block/Capture Transitions` | Analysis: [`analysis/AtCoder-abc203_e.md`](analysis/AtCoder-abc203_e.md)
- `[problem:AtCoder-arc111_c]` — **Too Heavy** (Rating: 1750) | Topic: `Permutation Cycle Decomposition with Minimum-Capacity Catalyst Sorting` | Analysis: [`analysis/AtCoder-arc111_c.md`](analysis/AtCoder-arc111_c.md)

### Batch 5 Part 2B: ABC Curated Ladder (1751 - 1799)
- `[problem:AtCoder-abc023_c]` — **収集王** (Rating: 1752) | Topic: `Row/Column Candy Count with Sparse Cell Adjustment` | Analysis: [`analysis/AtCoder-abc023_c.md`](analysis/AtCoder-abc023_c.md)
- `[problem:AtCoder-abc293_g]` — **Triple Index** (Rating: 1753) | Topic: `Mo's Algorithm for Range Triples C(c, 3)` | Analysis: [`analysis/AtCoder-abc293_g.md`](analysis/AtCoder-abc293_g.md)
- `[problem:AtCoder-abc161_e]` — **Yutori** (Rating: 1760) | Topic: `Mandatory Task Identification via Leftmost vs Rightmost Greedy Schedules` | Analysis: [`analysis/AtCoder-abc161_e.md`](analysis/AtCoder-abc161_e.md)
- `[problem:AtCoder-abc146_e]` — **Rem of Sum is Num** (Rating: 1762) | Topic: `Prefix Sum Shift Transformation (S_i - i) mod K with Sliding Window Map` | Analysis: [`analysis/AtCoder-abc146_e.md`](analysis/AtCoder-abc146_e.md)
- `[problem:AtCoder-abc162_f]` — **Select Half** (Rating: 1764) | Topic: `Non-Adjacent Selection via Skip-Budget DP` | Analysis: [`analysis/AtCoder-abc162_f.md`](analysis/AtCoder-abc162_f.md)
- `[problem:AtCoder-abc353_g]` — **Merchant Takahashi** (Rating: 1765) | Topic: `Segment Tree Optimization for 1D Manhattan Distance DP` | Analysis: [`analysis/AtCoder-abc353_g.md`](analysis/AtCoder-abc353_g.md)
- `[problem:AtCoder-arc117_c]` — **Tricolor Pyramid** (Rating: 1768) | Topic: `Cellular Automaton Modulo 3 Linearity via Pascal & Lucas' Theorem` | Analysis: [`analysis/AtCoder-arc117_c.md`](analysis/AtCoder-arc117_c.md)
- `[problem:AtCoder-arc064_c]` — **Cosmic Rays** (Rating: 1769) | Topic: `Continuous Euclidean Distance on Circular Barriers via Dense Dijkstra` | Analysis: [`analysis/AtCoder-arc064_c.md`](analysis/AtCoder-arc064_c.md)
- `[problem:AtCoder-abc126_f]` — **XOR Matching** (Rating: 1770) | Topic: `Constructive XOR Palindromic Sandwich Sequence` | Analysis: [`analysis/AtCoder-abc126_f.md`](analysis/AtCoder-abc126_f.md)
- `[problem:AtCoder-abc154_f]` — **Many Many Paths** (Rating: 1775) | Topic: `Double Hockey-Stick Identity on Grid Path Combinations` | Analysis: [`analysis/AtCoder-abc154_f.md`](analysis/AtCoder-abc154_f.md)
- `[problem:AtCoder-abc010_4]` — **浮気予防** (Rating: 1777) | Topic: `Min-Cut / Max-Flow Model on Network Disconnection` | Analysis: [`analysis/AtCoder-abc010_4.md`](analysis/AtCoder-abc010_4.md)
- `[problem:AtCoder-abc377_g]` — **Edit to Match** (Rating: 1782) | Topic: `Trie-Accelerated Prefix Edit Distance / LCS Minimization` | Analysis: [`analysis/AtCoder-abc377_g.md`](analysis/AtCoder-abc377_g.md)
- `[problem:AtCoder-abc192_f]` — **Potion** (Rating: 1783) | Topic: `Exact Cardinality Modulo Remainder Knapsack DP` | Analysis: [`analysis/AtCoder-abc192_f.md`](analysis/AtCoder-abc192_f.md)
- `[problem:AtCoder-abc339_g]` — **Smaller Sum** (Rating: 1792) | Topic: `Persistent Segment Tree for Online Range Value-Bounded Sum` | Analysis: [`analysis/AtCoder-abc339_g.md`](analysis/AtCoder-abc339_g.md)
- `[problem:AtCoder-abc171_f]` — **Strivore** (Rating: 1795) | Topic: `Canonical Greedy Subsequence Embedding / Distinct Superstring Counting` | Analysis: [`analysis/AtCoder-abc171_f.md`](analysis/AtCoder-abc171_f.md)
- `[problem:AtCoder-arc089_b]` — **Checker** (Rating: 1797) | Topic: `2D Periodic Chessboard Coordinate Reduction and 2D Prefix Sums` | Analysis: [`analysis/AtCoder-arc089_b.md`](analysis/AtCoder-arc089_b.md)

### Batch 5 Part 3A: ABC Curated Ladder (1800 - 1850)
- `[problem:AtCoder-arc100_b]` — **Equal Cut** (Rating: 1801) | Topic: `4-Partition Array Optimization via Monotonic Two-Pointer Sweep` | Analysis: [`analysis/AtCoder-arc100_b.md`](analysis/AtCoder-arc100_b.md)
- `[problem:AtCoder-arc150_c]` — **Path and Subsequence** (Rating: 1802) | Topic: `Worst-Case Subsequence Matching on Graph via 0-1 BFS` | Analysis: [`analysis/AtCoder-arc150_c.md`](analysis/AtCoder-arc150_c.md)
- `[problem:AtCoder-arc157_c]` — **YY Square** (Rating: 1802) | Topic: `Moment-Tracking Grid Path DP (E[X^2] Expansion)` | Analysis: [`analysis/AtCoder-arc157_c.md`](analysis/AtCoder-arc157_c.md)
- `[problem:AtCoder-abc038_d]` — **プレゼント** (Rating: 1804) | Topic: `2D Partially-Ordered LIS via Asymmetric Sorting (w ascending, h descending)` | Analysis: [`analysis/AtCoder-abc038_d.md`](analysis/AtCoder-abc038_d.md)
- `[problem:AtCoder-abc199_d]` — **RGB Coloring 2** (Rating: 1804) | Topic: `DFS Tree Order Backtracking on Small-Graph 3-Coloring with Root Symmetry` | Analysis: [`analysis/AtCoder-abc199_d.md`](analysis/AtCoder-abc199_d.md)
- `[problem:AtCoder-arc143_c]` — **Piles of Pebbles** (Rating: 1805) | Topic: `Periodic Round Invariant Modulo (X + Y) on Multi-Pile Pebble Game` | Analysis: [`analysis/AtCoder-arc143_c.md`](analysis/AtCoder-arc143_c.md)
- `[problem:AtCoder-arc041_c]` — **ウサギ跳び** (Rating: 1808) | Topic: `1D Compression Invariant on Converging Directed Clusters` | Analysis: [`analysis/AtCoder-arc041_c.md`](analysis/AtCoder-arc041_c.md)
- `[problem:AtCoder-arc102_b]` — **All Your Paths are Different Lengths** (Rating: 1810) | Topic: `Base-2 Doubling DAG Construction for Exact Path Interval [0, L - 1]` | Analysis: [`analysis/AtCoder-arc102_b.md`](analysis/AtCoder-arc102_b.md)
- `[problem:AtCoder-arc128_c]` — **Max Dot** (Rating: 1810) | Topic: `Convex Monotonic Variable Assignment via Suffix Average Efficiency` | Analysis: [`analysis/AtCoder-arc128_c.md`](analysis/AtCoder-arc128_c.md)
- `[problem:AtCoder-abc199_e]` — **Permutation** (Rating: 1814) | Topic: `Subset Bitmask DP with Prefix Count Constraints` | Analysis: [`analysis/AtCoder-abc199_e.md`](analysis/AtCoder-abc199_e.md)
- `[problem:AtCoder-arc064_b]` — **An Ordinary Game** (Rating: 1814) | Topic: `Combinatorial Game Parity Determined by Boundary Endpoints` | Analysis: [`analysis/AtCoder-arc064_b.md`](analysis/AtCoder-arc064_b.md)
- `[problem:AtCoder-abc312_g]` — **Avoid Straight Line** (Rating: 1819) | Topic: `Tree Non-Collinear Triplet Counting via Junction Center Decomposition` | Analysis: [`analysis/AtCoder-abc312_g.md`](analysis/AtCoder-abc312_g.md)
- `[problem:AtCoder-abc207_e]` — **Mod i** (Rating: 1820) | Topic: `Partition DP with Modulo Remainder State Bucketing` | Analysis: [`analysis/AtCoder-abc207_e.md`](analysis/AtCoder-abc207_e.md)
- `[problem:AtCoder-abc211_e]` — **Red Polyomino** (Rating: 1823) | Topic: `Grid Connected Polyomino Generation with Canonical Deduplication` | Analysis: [`analysis/AtCoder-abc211_e.md`](analysis/AtCoder-abc211_e.md)
- `[problem:AtCoder-arc037_c]` — **億マス計算** (Rating: 1824) | Topic: `Binary Search on Answer for K-th Matrix Product / Multi-Set Item` | Analysis: [`analysis/AtCoder-arc037_c.md`](analysis/AtCoder-arc037_c.md)
- `[problem:AtCoder-arc126_c]` — **Maximize GCD** (Rating: 1824) | Topic: `Harmonic Range Sum with Prefix Aggregates for Maximum GCD` | Analysis: [`analysis/AtCoder-arc126_c.md`](analysis/AtCoder-arc126_c.md)
- `[problem:AtCoder-abc186_f]` — **Rook on Grid** (Rating: 1833) | Topic: `2D Obstacle Grid Sweep-Line with Fenwick Tree Deduplication` | Analysis: [`analysis/AtCoder-abc186_f.md`](analysis/AtCoder-abc186_f.md)
- `[problem:AtCoder-abc297_g]` — **Constrained Nim 2** (Rating: 1834) | Topic: `Sprague-Grundy Closed Form for Bounded-Move Nim: (X mod (L+R)) / L` | Analysis: [`analysis/AtCoder-abc297_g.md`](analysis/AtCoder-abc297_g.md)
- `[problem:AtCoder-abc008_3]` — **コイン** (Rating: 1836) | Topic: `Linearity of Expectation over Permutations via Divisor Relative Rank` | Analysis: [`analysis/AtCoder-abc008_3.md`](analysis/AtCoder-abc008_3.md)
- `[problem:AtCoder-arc050_b]` — **花束** (Rating: 1838) | Topic: `Binary Search on Answer for Dual-Recipe Resource Allocation` | Analysis: [`analysis/AtCoder-arc050_b.md`](analysis/AtCoder-arc050_b.md)
- `[problem:AtCoder-abc128_e]` — **Roadwork** (Rating: 1840) | Topic: `Time-Space Diagonal Projection (S_i - X_i) Sweep-Line with Active Multiset` | Analysis: [`analysis/AtCoder-abc128_e.md`](analysis/AtCoder-abc128_e.md)
- `[problem:AtCoder-abc368_g]` — **Add and Multiply Queries** (Rating: 1841) | Topic: `Exponential Growth Sparse Set Skipping with Fenwick Range Sum` | Analysis: [`analysis/AtCoder-abc368_g.md`](analysis/AtCoder-abc368_g.md)
- `[problem:AtCoder-abc011_4]` — **大ジャンプ** (Rating: 1843) | Topic: `45-Degree Grid Rotation Decomposing 2D Random Walk into Independent 1D Walks` | Analysis: [`analysis/AtCoder-abc011_4.md`](analysis/AtCoder-abc011_4.md)
- `[problem:AtCoder-abc023_d]` — **射撃王** (Rating: 1843) | Topic: `Binary Search on Answer with Feasibility Deadline Verification` | Analysis: [`analysis/AtCoder-abc023_d.md`](analysis/AtCoder-abc023_d.md)
- `[problem:AtCoder-abc165_f]` — **LIS on Tree** (Rating: 1843) | Topic: `Rollback LIS on Tree via DFS Call-Stack Undo` | Analysis: [`analysis/AtCoder-abc165_f.md`](analysis/AtCoder-abc165_f.md)
- `[problem:AtCoder-abc155_d]` — **Pairs** (Rating: 1845) | Topic: `Binary Search on K-th Pair Product with Sign-Partitioned Two Pointers` | Analysis: [`analysis/AtCoder-abc155_d.md`](analysis/AtCoder-abc155_d.md)

### Batch 5 Part 3B: ABC Curated Ladder (1851 - 1899)
- `[problem:AtCoder-abc150_e]` — **Change a Little Bit** (Rating: 1851) | Topic: `Expected Permutation Rank / Contribution to Sum on Bit-Flip Costs` | Analysis: [`analysis/AtCoder-abc150_e.md`](analysis/AtCoder-abc150_e.md)
- `[problem:AtCoder-abc014_4]` — **閉路** (Rating: 1856) | Topic: `Cycle Length upon Edge Addition via Tree LCA (dist(u, v) + 1)` | Analysis: [`analysis/AtCoder-abc014_4.md`](analysis/AtCoder-abc014_4.md)
- `[problem:AtCoder-abc022_d]` — **Big Bang** (Rating: 1857) | Topic: `Centroid Invariant Distance Ratio for 2D Similarity Transformations` | Analysis: [`analysis/AtCoder-abc022_d.md`](analysis/AtCoder-abc022_d.md)
- `[problem:AtCoder-abc004_4]` — **マーブル** (Rating: 1861) | Topic: `Contiguous Block Placement DP for Colored Particles on 1D Line` | Analysis: [`analysis/AtCoder-abc004_4.md`](analysis/AtCoder-abc004_4.md)
- `[problem:AtCoder-abc188_f]` — **+1-1x2** (Rating: 1865) | Topic: `Backward Parity Branching Recursion with Memoization from Target to Source` | Analysis: [`analysis/AtCoder-abc188_f.md`](analysis/AtCoder-abc188_f.md)
- `[problem:AtCoder-abc158_e]` — **Divisible Substring** (Rating: 1866) | Topic: `Prime Modular Suffix Invariant for Divisible Substring Counting` | Analysis: [`analysis/AtCoder-abc158_e.md`](analysis/AtCoder-abc158_e.md)
- `[problem:AtCoder-arc094_b]` — **Worst Case** (Rating: 1869) | Topic: `AM-GM Hyperbolic Pairing for Strict Product Inequalities` | Analysis: [`analysis/AtCoder-arc094_b.md`](analysis/AtCoder-arc094_b.md)
- `[problem:AtCoder-arc105_d]` — **Let's Play Nim** (Rating: 1871) | Topic: `Phase-Shifted Combinatorial Game with Nim Parity Inversion` | Analysis: [`analysis/AtCoder-arc105_d.md`](analysis/AtCoder-arc105_d.md)
- `[problem:AtCoder-abc140_e]` — **Second Sum** (Rating: 1873) | Topic: `Second Largest Element Contribution via Ordered Set Predecessors/Successors` | Analysis: [`analysis/AtCoder-abc140_e.md`](analysis/AtCoder-abc140_e.md)
- `[problem:AtCoder-arc158_c]` — **All Pair Digit Sums** (Rating: 1875) | Topic: `Carry Reduction Identity for All-Pair Digit Sums` | Analysis: [`analysis/AtCoder-arc158_c.md`](analysis/AtCoder-arc158_c.md)
- `[problem:AtCoder-abc159_f]` — **Knapsack for All Segments** (Rating: 1876) | Topic: `3-Phase Automaton Knapsack DP for All-Subsegment Subset Counting` | Analysis: [`analysis/AtCoder-abc159_f.md`](analysis/AtCoder-abc159_f.md)
- `[problem:AtCoder-abc164_e]` — **Two Currencies** (Rating: 1877) | Topic: `2D State Dijkstra on Resource/Currency Bounds` | Analysis: [`analysis/AtCoder-abc164_e.md`](analysis/AtCoder-abc164_e.md)
- `[problem:AtCoder-abc178_f]` — **Contrast** (Rating: 1877) | Topic: `Pigeonhole Inversion and Cyclic Shift Collision Resolution` | Analysis: [`analysis/AtCoder-abc178_f.md`](analysis/AtCoder-abc178_f.md)
- `[problem:AtCoder-abc172_e]` — **NEQ** (Rating: 1880) | Topic: `Principle of Inclusion-Exclusion on Constrained Sequence Derangements` | Analysis: [`analysis/AtCoder-abc172_e.md`](analysis/AtCoder-abc172_e.md)
- `[problem:AtCoder-abc076_d]` — **AtCoder Express** (Rating: 1884) | Topic: `Velocity Profile Chmin Envelope via Bidirectional Relaxation on Doubled Grid` | Analysis: [`analysis/AtCoder-abc076_d.md`](analysis/AtCoder-abc076_d.md)
- `[problem:AtCoder-arc091_c]` — **LISDL** (Rating: 1889) | Topic: `Erdős–Szekeres Extremal Permutation Construction (LIS = A, LDS = B)` | Analysis: [`analysis/AtCoder-arc091_c.md`](analysis/AtCoder-arc091_c.md)
- `[problem:AtCoder-abc302_g]` — **Sort from 1 to 4** (Rating: 1891) | Topic: `Minimum Swaps to Sort Finite-Alphabet Array via Directed Cycle Decomposition` | Analysis: [`analysis/AtCoder-abc302_g.md`](analysis/AtCoder-abc302_g.md)
- `[problem:AtCoder-abc173_f]` — **Intervals on Tree** (Rating: 1892) | Topic: `Forest Connected Components Identity (C = V - E) via Contribution to Sum` | Analysis: [`analysis/AtCoder-abc173_f.md`](analysis/AtCoder-abc173_f.md)
- `[problem:AtCoder-abc187_f]` — **Close Group** (Rating: 1895) | Topic: `Minimum Clique Partition via O(3^N) Submask Enumeration DP` | Analysis: [`analysis/AtCoder-abc187_f.md`](analysis/AtCoder-abc187_f.md)
- `[problem:AtCoder-abc168_e]` — **∙ (Bullet)** (Rating: 1896) | Topic: `Orthogonal Vector Slope Pairing with Mutually Exclusive Subset Combinatorics` | Analysis: [`analysis/AtCoder-abc168_e.md`](analysis/AtCoder-abc168_e.md)
- `[problem:AtCoder-arc051_c]` — **掛け算** (Rating: 1898) | Topic: `Octave Saturation / Min-Heap Transition to Modular Round-Robin Exponentiation` | Analysis: [`analysis/AtCoder-arc051_c.md`](analysis/AtCoder-arc051_c.md)

### Batch 5 Part 4A: ABC Curated Ladder (1900 - 1950)
- `[problem:AtCoder-arc053_c]` — **魔法使い高橋君** (Rating: 1901) | Topic: `Greedy Exchange Argument on Bipartite Temperature Deltas (a < b ascending, a >= b descending)` | Analysis: [`analysis/AtCoder-arc053_c.md`](analysis/AtCoder-arc053_c.md)
- `[problem:AtCoder-arc004_3]` — **平均値太郎の憂鬱** (Rating: 1904) | Topic: `Average Remainder Bounding and Modular Divisibility on Truncated Arithmetic Progression` | Analysis: [`analysis/AtCoder-arc004_3.md`](analysis/AtCoder-arc004_3.md)
- `[problem:AtCoder-arc014_4]` — **grepマスター** (Rating: 1904) | Topic: `Interval Union under Bounded Expansion via Sorted Gap Prefix Sums` | Analysis: [`analysis/AtCoder-arc014_4.md`](analysis/AtCoder-arc014_4.md)
- `[problem:AtCoder-abc149_e]` — **Handshake** (Rating: 1905) | Topic: `Top-M Pairwise Sums via Threshold Binary Search and Prefix Accumulation` | Analysis: [`analysis/AtCoder-abc149_e.md`](analysis/AtCoder-abc149_e.md)
- `[problem:AtCoder-arc058_b]` — **Iroha and a Grid** (Rating: 1905) | Topic: `Grid Path Combinations with Rectangular Cutout via Bottleneck Diagonal Partition` | Analysis: [`analysis/AtCoder-arc058_b.md`](analysis/AtCoder-arc058_b.md)
- `[problem:AtCoder-arc136_d]` — **Without Carry** (Rating: 1908) | Topic: `Base-10 Multi-Dimensional Fast Zeta Transform / SOS DP for Carry-Free Pairs` | Analysis: [`analysis/AtCoder-arc136_d.md`](analysis/AtCoder-arc136_d.md)
- `[problem:AtCoder-arc112_c]` — **DFS Game** (Rating: 1913) | Topic: `Tree DFS Minimax Game with Subtree Size Parity Inversion and Greedy Child Ordering` | Analysis: [`analysis/AtCoder-arc112_c.md`](analysis/AtCoder-arc112_c.md)
- `[problem:AtCoder-abc009_3]` — **辞書式順序ふたたび** (Rating: 1915) | Topic: `Greedy Lexicographical String Construction with Feasibility Verification under Edit Budget` | Analysis: [`analysis/AtCoder-abc009_3.md`](analysis/AtCoder-abc009_3.md)
- `[problem:AtCoder-abc142_f]` — **Pure** (Rating: 1919) | Topic: `Induced Directed Cycle Extraction via Shortest Cycle BFS Search` | Analysis: [`analysis/AtCoder-abc142_f.md`](analysis/AtCoder-abc142_f.md)
- `[problem:AtCoder-arc026_3]` — **蛍光灯** (Rating: 1930) | Topic: `Interval Cover Minimum Cost DP Accelerated by Range Minimum Segment Tree` | Analysis: [`analysis/AtCoder-arc026_3.md`](analysis/AtCoder-arc026_3.md)
- `[problem:AtCoder-abc131_f]` — **Must Be Rectangular!** (Rating: 1937) | Topic: `Bipartite Component Product Transformation for 2D Grid Point Rectangulation` | Analysis: [`analysis/AtCoder-abc131_f.md`](analysis/AtCoder-abc131_f.md)
- `[problem:AtCoder-abc127_e]` — **Cell Distance** (Rating: 1938) | Topic: `Manhattan Pairwise Distance Contribution over Subsets via Dimension Decoupling` | Analysis: [`analysis/AtCoder-abc127_e.md`](analysis/AtCoder-abc127_e.md)
- `[problem:AtCoder-arc151_c]` — **01 Game** (Rating: 1940) | Topic: `Interval Grundy Decomposition under Alternating Parity Boundary Constraints` | Analysis: [`analysis/AtCoder-arc151_c.md`](analysis/AtCoder-arc151_c.md)
- `[problem:AtCoder-abc258_g]` — **Triangle** (Rating: 1944) | Topic: `Bitset-Accelerated Triangle Counting via Neighbor Set Intersections O(N^3 / 64)` | Analysis: [`analysis/AtCoder-abc258_g.md`](analysis/AtCoder-abc258_g.md)
- `[problem:AtCoder-abc197_f]` — **Construct a Palindrome** (Rating: 1945) | Topic: `Bidirectional Symmetric Pair BFS for Shortest Palindromic Graph Walk` | Analysis: [`analysis/AtCoder-abc197_f.md`](analysis/AtCoder-abc197_f.md)
- `[problem:AtCoder-abc193_e]` — **Oversleeping** (Rating: 1948) | Topic: `Dual Periodic Cycle Synchronization via Chinese Remainder Theorem on Interval Windows` | Analysis: [`analysis/AtCoder-abc193_e.md`](analysis/AtCoder-abc193_e.md)

### Batch 5 Part 4B: ABC Curated Ladder (1951 - 1999)
- `[problem:AtCoder-arc098_c]` — **Range Minimum Queries** (Rating: 1951) | Topic: `Min-Max Spread Optimization via Fixed Lower Bound and Segmented Greedy Extraction` | Analysis: [`analysis/AtCoder-arc098_c.md`](analysis/AtCoder-arc098_c.md)
- `[problem:AtCoder-abc191_d]` — **Circle Lattice Points** (Rating: 1953) | Topic: `Exact Circle Lattice Point Counting via Fixed-Point Integer Scaling and 1D Sweep` | Analysis: [`analysis/AtCoder-abc191_d.md`](analysis/AtCoder-abc191_d.md)
- `[problem:AtCoder-arc025_3]` — **ウサギとカメ** (Rating: 1954) | Topic: `All-Pairs Shortest Path Distance Scaling Inequality Counting via Dijkstra and Binary Search` | Analysis: [`analysis/AtCoder-arc025_3.md`](analysis/AtCoder-arc025_3.md)
- `[problem:AtCoder-abc200_e]` — **Patisserie ABC 2** (Rating: 1955) | Topic: `Lexicographical K-th Triplet Selection under Bounded Sum via Stars and Bars Bounding` | Analysis: [`analysis/AtCoder-abc200_e.md`](analysis/AtCoder-abc200_e.md)
- `[problem:AtCoder-abc017_4]` — **サプリメント** (Rating: 1956) | Topic: `Non-Duplicate Contiguous Partition DP Accelerated by Monotonic Left-Bound Prefix Sums` | Analysis: [`analysis/AtCoder-abc017_4.md`](analysis/AtCoder-abc017_4.md)
- `[problem:AtCoder-arc153_c]` — **± Increasing Sequence** (Rating: 1960) | Topic: `Difference Sequence Linear Equation Construction with Suffix Sum Invariants` | Analysis: [`analysis/AtCoder-arc153_c.md`](analysis/AtCoder-arc153_c.md)
- `[problem:AtCoder-abc167_f]` — **Bracket Sequencing** (Rating: 1961) | Topic: `Bipartite Greedy Balance Sorting for Bracket Sequence Concatenation` | Analysis: [`analysis/AtCoder-abc167_f.md`](analysis/AtCoder-abc167_f.md)
- `[problem:AtCoder-abc216_g]` — **01Sequence** (Rating: 1963) | Topic: `Greedy Rightmost Interval 1-Filling via DSU Predecessor Jumping and Fenwick Tree` | Analysis: [`analysis/AtCoder-abc216_g.md`](analysis/AtCoder-abc216_g.md)
- `[problem:AtCoder-arc105_c]` — **Camels and Bridge** (Rating: 1964) | Topic: `Extremal Permutation Evaluation with Segment Weight Constraints and DAG Distance DP` | Analysis: [`analysis/AtCoder-arc105_c.md`](analysis/AtCoder-arc105_c.md)
- `[problem:AtCoder-abc152_f]` — **Tree and Constraints** (Rating: 1965) | Topic: `Principle of Inclusion-Exclusion on Tree Path Cover Constraints via Bitmask Edge Unions` | Analysis: [`analysis/AtCoder-abc152_f.md`](analysis/AtCoder-abc152_f.md)
- `[problem:AtCoder-abc170_f]` — **Pond Skater** (Rating: 1968) | Topic: `Bounded Ray-Shooting Grid BFS with Early Pruning on Directional Steps` | Analysis: [`analysis/AtCoder-abc170_f.md`](analysis/AtCoder-abc170_f.md)
- `[problem:AtCoder-arc029_3]` — **高橋君と国家** (Rating: 1973) | Topic: `Super-Source Vertex Activation Transformation for Minimum Spanning Tree` | Analysis: [`analysis/AtCoder-arc029_3.md`](analysis/AtCoder-arc029_3.md)
- `[problem:AtCoder-arc075_c]` — **Meaningful Mean** (Rating: 1979) | Topic: `Mean Threshold Normalization to Prefix Monotonic Inversion Counting via Fenwick Tree` | Analysis: [`analysis/AtCoder-arc075_c.md`](analysis/AtCoder-arc075_c.md)
- `[problem:AtCoder-arc108_d]` — **AB** (Rating: 1987) | Topic: `Formal Grammar String Rewriting Casework and Fibonacci Transition Invariants` | Analysis: [`analysis/AtCoder-arc108_d.md`](analysis/AtCoder-arc108_d.md)
- `[problem:AtCoder-arc106_d]` — **Powers** (Rating: 1988) | Topic: `Binomial Expansion Decoupling of Pairwise Sum Powers via Power-Sum Moments` | Analysis: [`analysis/AtCoder-arc106_d.md`](analysis/AtCoder-arc106_d.md)
- `[problem:AtCoder-abc305_g]` — **Banned Substrings** (Rating: 1989) | Topic: `Automaton Transition Matrix Exponentiation for Banned Substring Avoidance O(V^3 log N)` | Analysis: [`analysis/AtCoder-abc305_g.md`](analysis/AtCoder-abc305_g.md)
- `[problem:AtCoder-arc065_b]` — **Connectivity** (Rating: 1996) | Topic: `Dual Graph Joint Connectivity Counting via Component Root Hash Pairing` | Analysis: [`analysis/AtCoder-arc065_b.md`](analysis/AtCoder-arc065_b.md)
- `[problem:AtCoder-arc120_d]` — **Bracket Score 2** (Rating: 1996) | Topic: `Extremal Pairing Upper Bound Attainment via Sign-Alternating Bracket Stack` | Analysis: [`analysis/AtCoder-arc120_d.md`](analysis/AtCoder-arc120_d.md)
- `[problem:AtCoder-arc134_d]` — **Concatenate Subsequences** (Rating: 1998) | Topic: `Lexicographical Minimal Concatenated Subsequence via Two-Phase Greedy Selection` | Analysis: [`analysis/AtCoder-arc134_d.md`](analysis/AtCoder-arc134_d.md)

### Batch 6 Part 1A: ABC / ARC Curated Ladder (2000 - 2018)
- `[problem:AtCoder-abc388_g]` — **Simultaneous Kagamimochi 2** (Rating: 2001) | Topic: `Sparse Table Range Max Query with Binary Search for Monotone Pair Matching` | Analysis: [`analysis/AtCoder-abc388_g.md`](analysis/AtCoder-abc388_g.md)
- `[problem:AtCoder-arc099_b]` — **Snuke Numbers** (Rating: 2001) | Topic: `Snuke Numbers via Base-10 Digit Addition and S(x) Ratio Greedy Search` | Analysis: [`analysis/AtCoder-arc099_b.md`](analysis/AtCoder-arc099_b.md)
- `[problem:AtCoder-abc127_f]` — **Absolute Minima** (Rating: 2003) | Topic: `Online Running Median and Dynamic Absolute Deviation via Two Heaps` | Analysis: [`analysis/AtCoder-abc127_f.md`](analysis/AtCoder-abc127_f.md)
- `[problem:AtCoder-arc039_c]` — **幼稚園児高橋君** (Rating: 2004) | Topic: `2D 4-Way Doubly Linked List Node Deletion and Grid Path Compression` | Analysis: [`analysis/AtCoder-arc039_c.md`](analysis/AtCoder-arc039_c.md)
- `[problem:AtCoder-arc229_e]` — **Taka and Hashi** (Rating: 2004) | Topic: `Multi-Modal Reachability via Dual DSU Equivalence Classes and Label-1 Traversal` | Analysis: [`analysis/AtCoder-arc229_e.md`](analysis/AtCoder-arc229_e.md)
- `[problem:AtCoder-arc169_c]` — **Not So Consecutive** (Rating: 2005) | Topic: `Run-Length Constrained Sequence Counting via Sliding Window Prefix Sums` | Analysis: [`analysis/AtCoder-arc169_c.md`](analysis/AtCoder-arc169_c.md)
- `[problem:AtCoder-arc189_d]` — **Takahashi is Slime** (Rating: 2006) | Topic: `Subarray Monotonic Doubling Expansion via Segment Tree Range Max` | Analysis: [`analysis/AtCoder-arc189_d.md`](analysis/AtCoder-arc189_d.md)
- `[problem:AtCoder-abc308_g]` — **Minimum Xor Pair Query** (Rating: 2008) | Topic: `Dynamic Minimum XOR Pair Maintenance via Adjacent Elements in Sorted Multiset` | Analysis: [`analysis/AtCoder-abc308_g.md`](analysis/AtCoder-abc308_g.md)
- `[problem:AtCoder-arc124_d]` — **Yet Another Sorting Problem** (Rating: 2008) | Topic: `Bipartite Transposition Permutation Sorting via Permutation Cycle Decomposition` | Analysis: [`analysis/AtCoder-arc124_d.md`](analysis/AtCoder-arc124_d.md)
- `[problem:AtCoder-arc173_c]` — **Not Median** (Rating: 2008) | Topic: `Alternating Sign Invariant and Median Parity Breaking Search` | Analysis: [`analysis/AtCoder-arc173_c.md`](analysis/AtCoder-arc173_c.md)
- `[problem:AtCoder-abc181_f]` — **Silver Woods** (Rating: 2009) | Topic: `DSU Geometric Bottleneck Percolation for Maximum Clearance Circle Passage` | Analysis: [`analysis/AtCoder-abc181_f.md`](analysis/AtCoder-abc181_f.md)
- `[problem:AtCoder-arc104_c]` — **Fair Elevator** (Rating: 2009) | Topic: `Non-Overlapping Block Interval Partition DP under Endpoint Matching Constraints` | Analysis: [`analysis/AtCoder-arc104_c.md`](analysis/AtCoder-arc104_c.md)
- `[problem:AtCoder-arc148_d]` — **mod M Game** (Rating: 2009) | Topic: `Modular Pairing Invariants and Symmetric Strategy in Mod-M Sum Games` | Analysis: [`analysis/AtCoder-arc148_d.md`](analysis/AtCoder-arc148_d.md)
- `[problem:AtCoder-arc010_3]` — **積み上げパズル** (Rating: 2011) | Topic: `Bitmask DP with Stream Element Selection and Consecutive State Tracking` | Analysis: [`analysis/AtCoder-arc010_3.md`](analysis/AtCoder-arc010_3.md)
- `[problem:AtCoder-abc375_g]` — **Road Blocked 2** (Rating: 2014) | Topic: `Critical Shortest-Path Edges via Shortest Path DAG and Double-Mod Path Counting` | Analysis: [`analysis/AtCoder-abc375_g.md`](analysis/AtCoder-abc375_g.md)
- `[problem:AtCoder-arc032_3]` — **仕事計画** (Rating: 2014) | Topic: `Lexicographically Smallest Maximum Interval Scheduling via Backward DP` | Analysis: [`analysis/AtCoder-arc032_3.md`](analysis/AtCoder-arc032_3.md)
- `[problem:AtCoder-arc009_3]` — **高橋君、24歳** (Rating: 2015) | Topic: `Large N Derangement Counting via Combinations and Montmort Numbers` | Analysis: [`analysis/AtCoder-arc009_3.md`](analysis/AtCoder-arc009_3.md)
- `[problem:AtCoder-arc070_b]` — **No Need** (Rating: 2015) | Topic: `Monotone Essential Elements via 0-1 Knapsack DP and Binary Search` | Analysis: [`analysis/AtCoder-arc070_b.md`](analysis/AtCoder-arc070_b.md)
- `[problem:AtCoder-abc472_g]` — **Cascading Grid** (Rating: 2018) | Topic: `Maximum Weight Closure via Min-Cut on Grid Directed Reachability` | Analysis: [`analysis/AtCoder-abc472_g.md`](analysis/AtCoder-abc472_g.md)
- `[problem:AtCoder-arc183_c]` — **Not Argmax** (Rating: 2018) | Topic: `Cartesian Tree Root Partition Interval DP under Argmax Constraints` | Analysis: [`analysis/AtCoder-arc183_c.md`](analysis/AtCoder-arc183_c.md)

### Batch 6 Part 1B: ABC / ARC Curated Ladder (2018 - 2050)
- `[problem:AtCoder-arc212_d]` — **Two Rooms** (Rating: 2018) | Topic: `Local Search Potential Ascent for Two-Partition Intimacy Maximization` | Analysis: [`analysis/AtCoder-arc212_d.md`](analysis/AtCoder-arc212_d.md)
- `[problem:AtCoder-abc401_g]` — **Push Simultaneously** (Rating: 2022) | Topic: `Bottleneck Maximum Bipartite Matching via Binary Search on Continuous Distance` | Analysis: [`analysis/AtCoder-abc401_g.md`](analysis/AtCoder-abc401_g.md)
- `[problem:AtCoder-abc208_e]` — **Digit Products** (Rating: 2024) | Topic: `Map-Accelerated Digit DP on Sparse Product States` | Analysis: [`analysis/AtCoder-abc208_e.md`](analysis/AtCoder-abc208_e.md)
- `[problem:AtCoder-abc205_e]` — **White and Black Balls** (Rating: 2025) | Topic: `Reflection Principle for Shifted Diagonal Grid Walks` | Analysis: [`analysis/AtCoder-abc205_e.md`](analysis/AtCoder-abc205_e.md)
- `[problem:AtCoder-arc187_b]` — **Sum of CC** (Rating: 2026) | Topic: `Connected Component Boundary Independence and Linearity of Expectation` | Analysis: [`analysis/AtCoder-arc187_b.md`](analysis/AtCoder-arc187_b.md)
- `[problem:AtCoder-abc403_g]` — **Odd Position Sum Query** (Rating: 2028) | Topic: `Dynamic Segment Tree with Parity-Dependent Index Shift Aggregations` | Analysis: [`analysis/AtCoder-abc403_g.md`](analysis/AtCoder-abc403_g.md)
- `[problem:AtCoder-arc112_d]` — **Skate** (Rating: 2028) | Topic: `Row-Column Bipartite Graph DSU for Grid Sliding Reachability` | Analysis: [`analysis/AtCoder-arc112_d.md`](analysis/AtCoder-arc112_d.md)
- `[problem:AtCoder-arc170_c]` — **Prefix Mex Sequence** (Rating: 2028) | Topic: `Prefix MEX Sequence State Tracking via Cardinality DP` | Analysis: [`analysis/AtCoder-arc170_c.md`](analysis/AtCoder-arc170_c.md)
- `[problem:AtCoder-abc394_g]` — **Dense Buildings** (Rating: 2031) | Topic: `Kruskal Reconstruction Tree Maximum Bottleneck Path Query via Binary Lifting` | Analysis: [`analysis/AtCoder-abc394_g.md`](analysis/AtCoder-abc394_g.md)
- `[problem:AtCoder-abc243_g]` — **Sqrt** (Rating: 2032) | Topic: `Two-Level Square Root DP with Prefix Sum Value Aggregation` | Analysis: [`analysis/AtCoder-abc243_g.md`](analysis/AtCoder-abc243_g.md)
- `[problem:AtCoder-arc029_2]` — **高橋君と禁断の書** (Rating: 2032) | Topic: `Rotated Rectangle Bounding Box Containment via Binary Search on Angle` | Analysis: [`analysis/AtCoder-arc029_2.md`](analysis/AtCoder-arc029_2.md)
- `[problem:AtCoder-abc003_4]` — **AtCoder社の冬** (Rating: 2033) | Topic: `4-Boundary Subgrid Bounding Box Inclusion-Exclusion` | Analysis: [`analysis/AtCoder-abc003_4.md`](analysis/AtCoder-abc003_4.md)
- `[problem:AtCoder-abc139_f]` — **Engines** (Rating: 2034) | Topic: `Polar Angle Sorting and Two-Pointer Sliding Window for Maximum Vector Subset Sum` | Analysis: [`analysis/AtCoder-abc139_f.md`](analysis/AtCoder-abc139_f.md)
- `[problem:AtCoder-abc163_e]` — **Active Infants** (Rating: 2037) | Topic: `Greedy Descending Sort with Deque Extreme-Slot Interval DP` | Analysis: [`analysis/AtCoder-abc163_e.md`](analysis/AtCoder-abc163_e.md)
- `[problem:AtCoder-arc137_c]` — **Distinct Numbers** (Rating: 2043) | Topic: `Strategy-Stealing and Extreme Gap Parity Invariant in Subtraction Game` | Analysis: [`analysis/AtCoder-arc137_c.md`](analysis/AtCoder-arc137_c.md)
- `[problem:AtCoder-abc204_f]` — **Hanjo 2** (Rating: 2044) | Topic: `Profile DP with Matrix Exponentiation for Domino and Monomino Tiling` | Analysis: [`analysis/AtCoder-abc204_f.md`](analysis/AtCoder-abc204_f.md)
- `[problem:AtCoder-abc266_g]` — **Yet Another RGB Sequence** (Rating: 2045) | Topic: `Substring Bounded Sequence Counting via Symbol Fusion and Slot Restriction` | Analysis: [`analysis/AtCoder-abc266_g.md`](analysis/AtCoder-abc266_g.md)
- `[problem:AtCoder-abc217_g]` — **Groups** (Rating: 2047) | Topic: `Modular Congruence-Constrained Set Partitions (Constrained Stirling Numbers)` | Analysis: [`analysis/AtCoder-abc217_g.md`](analysis/AtCoder-abc217_g.md)
- `[problem:AtCoder-abc160_f]` — **Distributing Integers** (Rating: 2048) | Topic: `Tree Rerooting DP on Topological Linear Extensions` | Analysis: [`analysis/AtCoder-abc160_f.md`](analysis/AtCoder-abc160_f.md)
- `[problem:AtCoder-abc024_d]` — **動的計画法** (Rating: 2050) | Topic: `Modular Inverse Parameter Reconstruction from Recurrence Matrix` | Analysis: [`analysis/AtCoder-abc024_d.md`](analysis/AtCoder-abc024_d.md)
