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
