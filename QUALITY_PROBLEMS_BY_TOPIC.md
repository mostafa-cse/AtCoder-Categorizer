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

### Batch 6 Part 2A: ABC / ARC Curated Ladder (2051 - 2073)
- `[problem:AtCoder-abc253_g]` — **Swap Many Times** (Rating: 2051) | Topic: `Block Simulation and Invariant Reversal` | Analysis: [`analysis/AtCoder-abc253_g.md`](analysis/AtCoder-abc253_g.md)
- `[problem:AtCoder-abc369_g]` — **As far as possible** (Rating: 2055) | Topic: `Tree Longest Path Decomposition and Greedy Subtree Weight` | Analysis: [`analysis/AtCoder-abc369_g.md`](analysis/AtCoder-abc369_g.md)
- `[problem:AtCoder-arc114_c]` — **Sequence Scores** (Rating: 2056) | Topic: `Contribution to the Sum and Linearity of Expectation` | Analysis: [`analysis/AtCoder-arc114_c.md`](analysis/AtCoder-arc114_c.md)
- `[problem:AtCoder-arc159_d]` — **LIS 2** (Rating: 2056) | Topic: `Coordinate-Compressed Segment Tree Optimized Interval LIS` | Analysis: [`analysis/AtCoder-arc159_d.md`](analysis/AtCoder-arc159_d.md)
- `[problem:AtCoder-arc176_c]` — **Max Permutation** (Rating: 2056) | Topic: `Permutation Construction with Value Upper Bound Counting` | Analysis: [`analysis/AtCoder-arc176_c.md`](analysis/AtCoder-arc176_c.md)
- `[problem:AtCoder-abc350_g]` — **Mediator** (Rating: 2058) | Topic: `Small-to-Large Tree Rerooting for Online Forest Queries` | Analysis: [`analysis/AtCoder-abc350_g.md`](analysis/AtCoder-abc350_g.md)
- `[problem:AtCoder-abc433_g]` — **Substring Game** (Rating: 2060) | Topic: `Suffix Automaton DAG Impartial Game Evaluation` | Analysis: [`analysis/AtCoder-abc433_g.md`](analysis/AtCoder-abc433_g.md)
- `[problem:AtCoder-arc197_d]` — **Ancestor Relation** (Rating: 2062) | Topic: `Comparability Graph Tree Reconstruction and Component Decomposition` | Analysis: [`analysis/AtCoder-arc197_d.md`](analysis/AtCoder-arc197_d.md)
- `[problem:AtCoder-arc111_d]` — **Orientation** (Rating: 2064) | Topic: `Strong Connectivity Graph Orientation and DFS Tree Back-Edge Directing` | Analysis: [`analysis/AtCoder-arc111_d.md`](analysis/AtCoder-arc111_d.md)
- `[problem:AtCoder-abc199_f]` — **Graph Smoothing** (Rating: 2065) | Topic: `Markov Chain Expected Value Transition via Matrix Exponentiation` | Analysis: [`analysis/AtCoder-abc199_f.md`](analysis/AtCoder-abc199_f.md)
- `[problem:AtCoder-abc299_g]` — **Minimum Permutation** (Rating: 2066) | Topic: `Monotonic Stack with Frequency/Last-Occurrence Tracking for Lexicographically Minimal Permutation` | Analysis: [`analysis/AtCoder-abc299_g.md`](analysis/AtCoder-abc299_g.md)
- `[problem:AtCoder-abc158_f]` — **Removing Robots** (Rating: 2067) | Topic: `Chain Reaction Interval Reachability via Segment Tree and Linear DP` | Analysis: [`analysis/AtCoder-abc158_f.md`](analysis/AtCoder-abc158_f.md)
- `[problem:AtCoder-abc195_f]` — **Coprime Present** (Rating: 2068) | Topic: `Prime Factor Bitmask DP over Bounded Interval Differences` | Analysis: [`analysis/AtCoder-abc195_f.md`](analysis/AtCoder-abc195_f.md)
- `[problem:AtCoder-arc214_c]` — **Divide into 4 Teams** (Rating: 2070) | Topic: `Basis Decoupling Sign DP and Subset Sum Reduction` | Analysis: [`analysis/AtCoder-arc214_c.md`](analysis/AtCoder-arc214_c.md)
- `[problem:AtCoder-arc226_c]` — **Square Corner Packing** (Rating: 2070) | Topic: `Grid Parity Lower Bound and Recursive Square Border Peeling Construction` | Analysis: [`analysis/AtCoder-arc226_c.md`](analysis/AtCoder-arc226_c.md)
- `[problem:AtCoder-arc168_c]` — **Swap Characters** (Rating: 2071) | Topic: `Permutation Cycle Decomposition and Multinomial Mismatch Counting` | Analysis: [`analysis/AtCoder-arc168_c.md`](analysis/AtCoder-arc168_c.md)
- `[problem:AtCoder-arc081_c]` — **Don't Be a Subsequence** (Rating: 2072) | Topic: `Automaton Transition DAG Shortest Non-Subsequence DP with Lexicographical Greedy Reconstruction` | Analysis: [`analysis/AtCoder-arc081_c.md`](analysis/AtCoder-arc081_c.md)
- `[problem:AtCoder-arc101_b]` — **Median of Medians** (Rating: 2073) | Topic: `Binary Search on Answer with +1/-1 Reduction and Fenwick Tree Prefix Sum Inversion Counting` | Analysis: [`analysis/AtCoder-arc101_b.md`](analysis/AtCoder-arc101_b.md)

### Batch 6 Part 2B: ABC / ARC Curated Ladder (2074 - 2099)
- `[problem:AtCoder-abc207_d]` — **Congruence Points** (Rating: 2074) | Topic: `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)` | Analysis: [`analysis/AtCoder-abc207_d.md`](analysis/AtCoder-abc207_d.md)
- `[problem:AtCoder-abc257_g]` — **Prefix Concatenation** (Rating: 2075) | Topic: `Knuth Morris Pratt (KMP) and Prefix Automaton` | Analysis: [`analysis/AtCoder-abc257_g.md`](analysis/AtCoder-abc257_g.md)
- `[problem:AtCoder-arc110_d]` — **Binomial Coefficient is Fun** (Rating: 2075) | Topic: `Stars and Bars` | Analysis: [`analysis/AtCoder-arc110_d.md`](analysis/AtCoder-arc110_d.md)
- `[problem:AtCoder-abc337_g]` — **Tree And LCS** (Rating: 2078) | Topic: `BIT / Fenwick Tree` | Analysis: [`analysis/AtCoder-abc337_g.md`](analysis/AtCoder-abc337_g.md)
- `[problem:AtCoder-arc152_c]` — **Pivot** (Rating: 2079) | Topic: `Euclidean Algorithm` | Analysis: [`analysis/AtCoder-arc152_c.md`](analysis/AtCoder-arc152_c.md)
- `[problem:AtCoder-arc138_d]` — **Differ by K bits** (Rating: 2080) | Topic: `Vector Space and XOR Basis` | Analysis: [`analysis/AtCoder-arc138_d.md`](analysis/AtCoder-arc138_d.md)
- `[problem:AtCoder-abc027_d]` — **Robot Movement** (Rating: 2081) | Topic: `Basic Greedy Algorithms` | Analysis: [`analysis/AtCoder-abc027_d.md`](analysis/AtCoder-abc027_d.md)
- `[problem:AtCoder-abc205_f]` — **Grid and Tokens** (Rating: 2082) | Topic: `Maximum Flow / Minimum Cut` | Analysis: [`analysis/AtCoder-abc205_f.md`](analysis/AtCoder-abc205_f.md)
- `[problem:AtCoder-abc237_g]` — **Range Sort Query** (Rating: 2085) | Topic: `Segment Tree with Lazy Propagation` | Analysis: [`analysis/AtCoder-abc237_g.md`](analysis/AtCoder-abc237_g.md)
- `[problem:AtCoder-abc295_g]` — **Minimum Path** (Rating: 2086) | Topic: `DSU / Union Find` | Analysis: [`analysis/AtCoder-abc295_g.md`](analysis/AtCoder-abc295_g.md)
- `[problem:AtCoder-arc016_3]` — **Gacha** (Rating: 2087) | Topic: `Bitmask DP` | Analysis: [`analysis/AtCoder-arc016_3.md`](analysis/AtCoder-arc016_3.md)
- `[problem:AtCoder-arc127_c]` — **Binary String** (Rating: 2087) | Topic: `Trie on Strings and Bits` | Analysis: [`analysis/AtCoder-arc127_c.md`](analysis/AtCoder-arc127_c.md)
- `[problem:AtCoder-abc411_g]` — **Count Cycles** (Rating: 2088) | Topic: `Cycle Detection` | Analysis: [`analysis/AtCoder-abc411_g.md`](analysis/AtCoder-abc411_g.md)
- `[problem:AtCoder-abc470_e]` — **Matching Game** (Rating: 2090) | Topic: `Probabilities and Expected Values` | Analysis: [`analysis/AtCoder-abc470_e.md`](analysis/AtCoder-abc470_e.md)
- `[problem:AtCoder-abc291_h]` — **Centroid Decomposition Tree** (Rating: 2090) | Topic: `Centroid Decomposition` | Analysis: [`analysis/AtCoder-abc291_h.md`](analysis/AtCoder-abc291_h.md)
- `[problem:AtCoder-abc470_g]` — **Range Mex Sum** (Rating: 2094) | Topic: `Segment Tree Beats` | Analysis: [`analysis/AtCoder-abc470_g.md`](analysis/AtCoder-abc470_g.md)
- `[problem:AtCoder-abc359_g]` — **Sum of Tree Distance** (Rating: 2095) | Topic: `Virtual Tree / Auxiliary Tree` | Analysis: [`analysis/AtCoder-abc359_g.md`](analysis/AtCoder-abc359_g.md)
- `[problem:AtCoder-arc107_d]` — **Number of Multisets** (Rating: 2096) | Topic: `x2 +1 Trick` | Analysis: [`analysis/AtCoder-arc107_d.md`](analysis/AtCoder-arc107_d.md)

### Batch 6 Part 3A: ABC / ARC Curated Ladder (2101 - 2125)
- `[problem:AtCoder-abc370_f]` — **Cake Division** (Rating: 2102) | Topic: `Sparse Table` | Analysis: [`analysis/AtCoder-abc370_f.md`](analysis/AtCoder-abc370_f.md)
- `[problem:AtCoder-agc029_c]` — **Lexicographic constraints** (Rating: 2103) | Topic: `Binary Search` | Analysis: [`analysis/AtCoder-agc029_c.md`](analysis/AtCoder-agc029_c.md)
- `[problem:AtCoder-abc140_f]` — **Many Slimes** (Rating: 2105) | Topic: `Basic Greedy Algorithms` | Analysis: [`analysis/AtCoder-abc140_f.md`](analysis/AtCoder-abc140_f.md)
- `[problem:AtCoder-abc342_g]` — **Retroactive Range Chmax** (Rating: 2107) | Topic: `Segment Tree (Point Update Range Query)` | Analysis: [`analysis/AtCoder-abc342_g.md`](analysis/AtCoder-abc342_g.md)
- `[problem:AtCoder-abc289_g]` — **Shopping in AtCoder store** (Rating: 2109) | Topic: `Convex Hull Trick (CHT) and Dynamic CHT` | Analysis: [`analysis/AtCoder-abc289_g.md`](analysis/AtCoder-abc289_g.md)
- `[problem:AtCoder-abc371_f]` — **Takahashi in Narrow Road** (Rating: 2109) | Topic: `Segment Tree with Lazy Propagation` | Analysis: [`analysis/AtCoder-abc371_f.md`](analysis/AtCoder-abc371_f.md)
- `[problem:AtCoder-arc100_c]` — **Or Plus Max** (Rating: 2111) | Topic: `Sum Over Subsets DP (SOS DP)` | Analysis: [`analysis/AtCoder-arc100_c.md`](analysis/AtCoder-arc100_c.md)
- `[problem:AtCoder-abc230_f]` — **Predilection** (Rating: 2113) | Topic: `Knapsack and Basic Dynamic Programming` | Analysis: [`analysis/AtCoder-abc230_f.md`](analysis/AtCoder-abc230_f.md)
- `[problem:AtCoder-abc343_g]` — **Compress Strings** (Rating: 2114) | Topic: `Bitmask DP` | Analysis: [`analysis/AtCoder-abc343_g.md`](analysis/AtCoder-abc343_g.md)
- `[problem:AtCoder-arc117_d]` — **Miracle Tree** (Rating: 2115) | Topic: `Tree Diameter` | Analysis: [`analysis/AtCoder-arc117_d.md`](analysis/AtCoder-arc117_d.md)
- `[problem:AtCoder-keyence2021_d]` — **Choosing Up Sides** (Rating: 2115) | Topic: `Basic Constructive Algorithms` | Analysis: [`analysis/AtCoder-keyence2021_d.md`](analysis/AtCoder-keyence2021_d.md)
- `[problem:AtCoder-abc145_f]` — **Laminate** (Rating: 2116) | Topic: `Knapsack and Basic Dynamic Programming` | Analysis: [`analysis/AtCoder-abc145_f.md`](analysis/AtCoder-abc145_f.md)
- `[problem:AtCoder-arc175_c]` — **Jumping Through Intervals** (Rating: 2116) | Topic: `Basic Greedy Algorithms` | Analysis: [`analysis/AtCoder-arc175_c.md`](analysis/AtCoder-arc175_c.md)
- `[problem:AtCoder-abc244_g]` — **Construct Good Path** (Rating: 2117) | Topic: `DFS Tree` | Analysis: [`analysis/AtCoder-abc244_g.md`](analysis/AtCoder-abc244_g.md)
- `[problem:AtCoder-arc077_c]` — **guruguru** (Rating: 2117) | Topic: `Difference Array` | Analysis: [`analysis/AtCoder-arc077_c.md`](analysis/AtCoder-arc077_c.md)
- `[problem:AtCoder-arc183_b]` — **Near Assignment** (Rating: 2118) | Topic: `Basic Constructive Algorithms` | Analysis: [`analysis/AtCoder-arc183_b.md`](analysis/AtCoder-arc183_b.md)
- `[problem:AtCoder-abc426_g]` — **Range Knapsack Query** (Rating: 2119) | Topic: `Divide and Conquer on Queries` | Analysis: [`analysis/AtCoder-abc426_g.md`](analysis/AtCoder-abc426_g.md)
- `[problem:AtCoder-agc048_c]` — **Penguin Skating** (Rating: 2120) | Topic: `Two Pointers` | Analysis: [`analysis/AtCoder-agc048_c.md`](analysis/AtCoder-agc048_c.md)

### Batch 6 Part 3B: ABC / ARC Curated Ladder (2121 - 2150)
- `[problem:AtCoder-abc182_f]` — **Valid payments** (Rating: 2121) | Topic: `Digit DP` | Analysis: [`analysis/AtCoder-abc182_f.md`](analysis/AtCoder-abc182_f.md)
- `[problem:AtCoder-abc229_g]` — **Longest Y** (Rating: 2121) | Topic: `Binary Search` | Analysis: [`analysis/AtCoder-abc229_g.md`](analysis/AtCoder-abc229_g.md)
- `[problem:AtCoder-abc243_f]` — **Lottery** (Rating: 2125) | Topic: `Knapsack and Basic Dynamic Programming` | Analysis: [`analysis/AtCoder-abc243_f.md`](analysis/AtCoder-abc243_f.md)
- `[problem:AtCoder-abc235_f]` — **Variety of Digits** (Rating: 2129) | Topic: `Digit DP` | Analysis: [`analysis/AtCoder-abc235_f.md`](analysis/AtCoder-abc235_f.md)
- `[problem:AtCoder-agc021_b]` — **Holes** (Rating: 2130) | Topic: `Convex Hull(2D)` | Analysis: [`analysis/AtCoder-agc021_b.md`](analysis/AtCoder-agc021_b.md)
- `[problem:AtCoder-agc046_c]` — **Shift** (Rating: 2130) | Topic: `Knapsack and Basic Dynamic Programming` | Analysis: [`analysis/AtCoder-agc046_c.md`](analysis/AtCoder-agc046_c.md)
- `[problem:AtCoder-code_festival_2017_qualc_d]` — **Yet Another Palindrome Partitioning** (Rating: 2132) | Topic: `Bitmask DP` | Analysis: [`analysis/AtCoder-code_festival_2017_qualc_d.md`](analysis/AtCoder-code_festival_2017_qualc_d.md)
- `[problem:AtCoder-aising2020_e]` — **Camel Train** (Rating: 2133) | Topic: `Basic Greedy Algorithms` | Analysis: [`analysis/AtCoder-aising2020_e.md`](analysis/AtCoder-aising2020_e.md)
- `[problem:AtCoder-abc286_g]` — **Unique Walk** (Rating: 2135) | Topic: `Eulerian Path and Cycle` | Analysis: [`analysis/AtCoder-abc286_g.md`](analysis/AtCoder-abc286_g.md)
- `[problem:AtCoder-nikkei2019_2_qual_c]` — **Swaps** (Rating: 2136) | Topic: `Basic Constructive Algorithms` | Analysis: [`analysis/AtCoder-nikkei2019_2_qual_c.md`](analysis/AtCoder-nikkei2019_2_qual_c.md)
- `[problem:AtCoder-arc136_c]` — **Circular Addition** (Rating: 2137) | Topic: `Basic Constructive Algorithms` | Analysis: [`analysis/AtCoder-arc136_c.md`](analysis/AtCoder-arc136_c.md)
- `[problem:AtCoder-abc307_f]` — **Virus 2** (Rating: 2139) | Topic: `Dijkstra's Algorithm` | Analysis: [`analysis/AtCoder-abc307_f.md`](analysis/AtCoder-abc307_f.md)
- `[problem:AtCoder-abc368_e]` — **Train Delay** (Rating: 2140) | Topic: `DP on Trees and DAGs` | Analysis: [`analysis/AtCoder-abc368_e.md`](analysis/AtCoder-abc368_e.md)
- `[problem:AtCoder-abc342_f]` — **Black Jack** (Rating: 2141) | Topic: `Probabilities and Expected Values` | Analysis: [`analysis/AtCoder-abc342_f.md`](analysis/AtCoder-abc342_f.md)
- `[problem:AtCoder-arc020_3]` — **A mod B Problem** (Rating: 2141) | Topic: `Matrix Exponentiation` | Analysis: [`analysis/AtCoder-arc020_3.md`](analysis/AtCoder-arc020_3.md)
- `[problem:AtCoder-abc132_f]` — **Small Products** (Rating: 2143) | Topic: `Knapsack and Basic Dynamic Programming` | Analysis: [`analysis/AtCoder-abc132_f.md`](analysis/AtCoder-abc132_f.md)
- `[problem:AtCoder-arc123_d]` — **Inc, Dec - Decomposition** (Rating: 2143) | Topic: `Slope Trick` | Analysis: [`analysis/AtCoder-arc123_d.md`](analysis/AtCoder-arc123_d.md)
- `[problem:AtCoder-abc212_g]` — **Power Pair** (Rating: 2150) | Topic: `Euler's Totient Function / Phi Function` | Analysis: [`analysis/AtCoder-abc212_g.md`](analysis/AtCoder-abc212_g.md)
- `[problem:AtCoder-abc356_f]` — **Distance Component Size Query** (Rating: 2152) | Topic: `BIT / Fenwick Tree` | Analysis: [analysis/AtCoder-abc356_f.md](analysis/AtCoder-abc356_f.md) | Category: [`categories/data_structures/gap_tracking_fenwick_component_count.md`](categories/data_structures/gap_tracking_fenwick_component_count.md)
- `[problem:AtCoder-abc209_e]` — **Shiritori** (Rating: 2153) | Topic: `Games on Arbitrary Graphs` | Analysis: [analysis/AtCoder-abc209_e.md](analysis/AtCoder-abc209_e.md) | Category: [`categories/game_theory/retrograde_analysis_directed_cyclic_graphs.md`](categories/game_theory/retrograde_analysis_directed_cyclic_graphs.md)
- `[problem:AtCoder-abc252_g]` — **Pre-Order** (Rating: 2153) | Topic: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | Analysis: [analysis/AtCoder-abc252_g.md](analysis/AtCoder-abc252_g.md) | Category: [`categories/dynamic_programming/interval_dp_preorder_tree_reconstruction.md`](categories/dynamic_programming/interval_dp_preorder_tree_reconstruction.md)
- `[problem:AtCoder-abc189_f]` — **Sugoroku2** (Rating: 2154) | Topic: `Probabilities and Expected Values` | Analysis: [analysis/AtCoder-abc189_f.md](analysis/AtCoder-abc189_f.md) | Category: [`categories/math/expected_value_dp_reset_squares_affine.md`](categories/math/expected_value_dp_reset_squares_affine.md)
- `[problem:AtCoder-arc060_c]` — **Tak and Hotels** (Rating: 2154) | Topic: `Binary Lifting and LCA` | Analysis: [analysis/AtCoder-arc060_c.md](analysis/AtCoder-arc060_c.md) | Category: [`categories/graph_theory/binary_lifting_interval_reachability.md`](categories/graph_theory/binary_lifting_interval_reachability.md)
- `[problem:AtCoder-arc156_c]` — **Tree and LCS** (Rating: 2155) | Topic: `Basic Constructive Algorithms` | Analysis: [analysis/AtCoder-arc156_c.md](analysis/AtCoder-arc156_c.md) | Category: [`categories/basics/leaf_peeling_inversion_matching_tree_lcs.md`](categories/basics/leaf_peeling_inversion_matching_tree_lcs.md)
- `[problem:AtCoder-agc017_d]` — **Game on Tree** (Rating: 2156) | Topic: `Green Hackenbush on Trees and Graphs` | Analysis: [analysis/AtCoder-agc017_d.md](analysis/AtCoder-agc017_d.md) | Category: [`categories/game_theory/green_hackenbush_trees_colon_principle.md`](categories/game_theory/green_hackenbush_trees_colon_principle.md)
- `[problem:AtCoder-abc295_e]` — **Kth Number** (Rating: 2157) | Topic: `Probabilities and Expected Values` | Analysis: [analysis/AtCoder-abc295_e.md](analysis/AtCoder-abc295_e.md) | Category: [`categories/math/tail_sum_expectation_binomial_order_statistics.md`](categories/math/tail_sum_expectation_binomial_order_statistics.md)
- `[problem:AtCoder-abc345_f]` — **Many Lamps** (Rating: 2157) | Topic: `DFS Tree` | Analysis: [analysis/AtCoder-abc345_f.md](analysis/AtCoder-abc345_f.md) | Category: [`categories/graph_theory/spanning_tree_leaf_root_parity_toggling.md`](categories/graph_theory/spanning_tree_leaf_root_parity_toggling.md)
- `[problem:AtCoder-arc192_c]` — **Range Sums 2** (Rating: 2158) | Topic: `Interactive Problems` | Analysis: [analysis/AtCoder-arc192_c.md](analysis/AtCoder-arc192_c.md) | Category: [`categories/miscellaneous/interactive_range_sums_extremal_reconstruction.md`](categories/miscellaneous/interactive_range_sums_extremal_reconstruction.md)
- `[problem:AtCoder-tokiomarine2020_d]` — **Knapsack Queries on a tree** (Rating: 2158) | Topic: `Meet in the Middle` | Analysis: [analysis/AtCoder-tokiomarine2020_d.md](analysis/AtCoder-tokiomarine2020_d.md) | Category: [`categories/miscellaneous/complete_binary_tree_depth_meet_in_the_middle.md`](categories/miscellaneous/complete_binary_tree_depth_meet_in_the_middle.md)
- `[problem:AtCoder-abc247_g]` — **Dream Team** (Rating: 2159) | Topic: `Min Cost Max Flow (MCMF)` | Analysis: [analysis/AtCoder-abc247_g.md](analysis/AtCoder-abc247_g.md) | Category: [`categories/graph_theory/mcmf_primal_dual_bipartite_matching_all_sizes.md`](categories/graph_theory/mcmf_primal_dual_bipartite_matching_all_sizes.md)
- `[problem:AtCoder-arc099_c]` — **Independence** (Rating: 2160) | Topic: `Maximum Clique` | Analysis: [analysis/AtCoder-arc099_c.md](analysis/AtCoder-arc099_c.md) | Category: [`categories/graph_theory/clique_partition_complement_bipartite_knapsack.md`](categories/graph_theory/clique_partition_complement_bipartite_knapsack.md)
- `[problem:AtCoder-abc404_f]` — **Lost and Pound** (Rating: 2162) | Topic: `Knapsack and Basic Dynamic Programming` | Analysis: [analysis/AtCoder-abc404_f.md](analysis/AtCoder-abc404_f.md) | Category: [`categories/dynamic_programming/integer_partition_knapsack_optimal_resource_game.md`](categories/dynamic_programming/integer_partition_knapsack_optimal_resource_game.md)
- `[problem:AtCoder-agc066_b]` — **Decreasing Digit Sums** (Rating: 2162) | Topic: `Basic Constructive Algorithms` | Analysis: [analysis/AtCoder-agc066_b.md](analysis/AtCoder-agc066_b.md) | Category: [`categories/basics/decreasing_digit_sums_doubling_powers_of_five.md`](categories/basics/decreasing_digit_sums_doubling_powers_of_five.md)
- `[problem:AtCoder-abc459_f]` — **-1, +1** (Rating: 2163) | Topic: `Basic Greedy Algorithms` | Analysis: [analysis/AtCoder-abc459_f.md](analysis/AtCoder-abc459_f.md) | Category: [`categories/basics/monotonic_block_merging_sequence_equalization.md`](categories/basics/monotonic_block_merging_sequence_equalization.md)
- `[problem:AtCoder-abc436_g]` — **Linear Inequation** (Rating: 2164) | Topic: `Generating Functions` | Analysis: [analysis/AtCoder-abc436_g.md](analysis/AtCoder-abc436_g.md) | Category: [`categories/math/bostan_mori_polynomial_transitions_linear_inequations.md`](categories/math/bostan_mori_polynomial_transitions_linear_inequations.md)
- `[problem:AtCoder-agc008_d]` — **K-th K** (Rating: 2164) | Topic: `Basic Greedy Algorithms` | Analysis: [analysis/AtCoder-agc008_d.md](analysis/AtCoder-agc008_d.md) | Category: [`categories/basics/earliest_deadline_first_multi_occurrence_scheduling.md`](categories/basics/earliest_deadline_first_multi_occurrence_scheduling.md)
| [`[problem:AtCoder-arc021_3]`](analysis/AtCoder-arc021_3.md) | C. 増築王高橋君 | 2164 | `Basics` | `Binary Search` | [`categories/basics/binary_search_marginal_cost_threshold.md`](categories/basics/binary_search_marginal_cost_threshold.md) |
| [`[problem:AtCoder-arc194_d]`](analysis/AtCoder-arc194_d.md) | D. Reverse Brackets | 2164 | `Miscellaneous` | `Tree Isomorphism` | [`categories/miscellaneous/tree_isomorphism_bracket_multinomial_counting.md`](categories/miscellaneous/tree_isomorphism_bracket_multinomial_counting.md) |
| [`[problem:AtCoder-arc219_e]`](analysis/AtCoder-arc219_e.md) | E. Equal Distribution | 2164 | `Graph Theory` | `Hamiltonian Path and Cycle` | [`categories/graph_theory/hamiltonian_snake_cycle_circular_discrete_ivt.md`](categories/graph_theory/hamiltonian_snake_cycle_circular_discrete_ivt.md) |
| [`[problem:AtCoder-soundhound2018_summer_qual_e]`](analysis/AtCoder-soundhound2018_summer_qual_e.md) | E. + Graph | 2164 | `Graph Theory` | `Depth First Search (DFS)` | [`categories/graph_theory/edge_sum_linear_system_bipartite_odd_cycle.md`](categories/graph_theory/edge_sum_linear_system_bipartite_odd_cycle.md) |
| [`[problem:AtCoder-abc346_g]`](analysis/AtCoder-abc346_g.md) | G. Alone | 2166 | `Data Structures (DS)` | `Segment Tree (Point Update Range Query)` | [`categories/data_structures/rectangle_union_sweep_line_segment_tree.md`](categories/data_structures/rectangle_union_sweep_line_segment_tree.md) |
| [`[problem:AtCoder-abc408_g]`](analysis/AtCoder-abc408_g.md) | G. A/B < p/q < C/D | 2167 | `Miscellaneous` | `Stern-Brocot Tree and Rational Approximation` | [`categories/miscellaneous/stern_brocot_simplest_fraction_euclidean_reduction.md`](categories/miscellaneous/stern_brocot_simplest_fraction_euclidean_reduction.md) |
| [`[problem:AtCoder-abc457_f]`](analysis/AtCoder-abc457_f.md) | F. Second Gap | 2167 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dp/permutation_insertion_dp_suffix_second_gap.md`](categories/dp/permutation_insertion_dp_suffix_second_gap.md) |
| [`[problem:AtCoder-apc001_e]`](analysis/AtCoder-apc001_e.md) | E. Antennas on Tree | 2167 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dp/metric_dimension_tree_dp_high_degree_root.md`](categories/dp/metric_dimension_tree_dp_high_degree_root.md) |
| [`[problem:AtCoder-abc349_f]`](analysis/AtCoder-abc349_f.md) | I. Subsequence LCM | 2169 | `Dynamic Programming (DP)` | `Sum Over Subsets DP (SOS DP)` | [`categories/dp/subsequence_lcm_sos_dp_inclusion_exclusion.md`](categories/dp/subsequence_lcm_sos_dp_inclusion_exclusion.md) |
| [`[problem:AtCoder-abc454_f]`](analysis/AtCoder-abc454_f.md) | I. Make it Palindrome 2 | 2169 | `Basics` | `Difference Array` | [`categories/basics/palindrome_modulo_difference_array_matching.md`](categories/basics/palindrome_modulo_difference_array_matching.md) |
| [`[problem:AtCoder-agc028_b]`](analysis/AtCoder-agc028_b.md) | B. Removing Blocks | 2172 | `Math` | `Probabilities and Expected Values` | [`categories/math/linearity_of_expectation_harmonic_prefix_sums.md`](categories/math/linearity_of_expectation_harmonic_prefix_sums.md) |
| [`[problem:AtCoder-abc283_g]`](analysis/AtCoder-abc283_g.md) | G. Partial Xor Enumeration | 2173 | `Math` | `[Technique] XOR Basis ft Reduced Row Echelon Form` | [`categories/math/xor_basis_reduced_row_echelon_kth_query.md`](categories/math/xor_basis_reduced_row_echelon_kth_query.md) |
| [`[problem:AtCoder-arc035_d]`](analysis/AtCoder-arc035_d.md) | D. 高橋くんとマラソンコース | 2173 | `Data Structures (DS)` | `Segment Tree (Point Update Range Query)` | [`categories/data_structures/grid_paths_log_binomial_fenwick_tree.md`](categories/data_structures/grid_paths_log_binomial_fenwick_tree.md) |
| [`[problem:AtCoder-arc217_c]`](analysis/AtCoder-arc217_c.md) | C. Greedy Customers 2 | 2173 | `Math` | `Probabilities and Expected Values` | [`categories/math/greedy_customers_hall_multinomial_prefix_dp.md`](categories/math/greedy_customers_hall_multinomial_prefix_dp.md) |
| [`[problem:AtCoder-abc291_g]`](analysis/AtCoder-abc291_g.md) | G. OR Sum | 2176 | `Math` | `Fast Fourier Transform (FFT)` | [`categories/math/cyclic_or_convolution_bitwise_ntt.md`](categories/math/cyclic_or_convolution_bitwise_ntt.md) |
| [`[problem:AtCoder-agc022_c]`](analysis/AtCoder-agc022_c.md) | C. Remainder Game | 2176 | `Miscellaneous` | `Exchange Arguments` | [`categories/miscellaneous/remainder_game_greedy_power_of_two_reachability.md`](categories/miscellaneous/remainder_game_greedy_power_of_two_reachability.md) |
| [`[problem:AtCoder-agc049_c]`](analysis/AtCoder-agc049_c.md) | C. Robots | 2177 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/robots_line_intervals_suffix_min_greedy.md`](categories/basics/robots_line_intervals_suffix_min_greedy.md) |
| [`[problem:AtCoder-mujin_pc_2017_b]`](analysis/AtCoder-mujin_pc_2017_b.md) | B. Row to Column | 2177 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/row_to_column_grid_operations_state_reduction.md`](categories/basics/row_to_column_grid_operations_state_reduction.md) |
| [`[problem:AtCoder-abc228_f]`](analysis/AtCoder-abc228_f.md) | I. Stamp Game | 2179 | `Data Structures (DS)` | `Monotonic Queue 2D` | [`categories/data_structures/monotonic_queue_2d_sliding_window_max.md`](categories/data_structures/monotonic_queue_2d_sliding_window_max.md) |
| [`[problem:AtCoder-abc347_f]`](analysis/AtCoder-abc347_f.md) | I. Non-overlapping Squares | 2179 | `Basics` | `2D Prefix Sum` | [`categories/basics/2d_prefix_sum_geometric_cut_decomposition.md`](categories/basics/2d_prefix_sum_geometric_cut_decomposition.md) |
| [`[problem:AtCoder-arc056_c]`](analysis/AtCoder-arc056_c.md) | C. 部門分け | 2179 | `Dynamic Programming (DP)` | `Bitmask DP` | [`categories/dynamic_programming/submask_dp_lowest_bit_department_partition.md`](categories/dynamic_programming/submask_dp_lowest_bit_department_partition.md) |
| [`[problem:AtCoder-digitalarts_3]`](analysis/AtCoder-digitalarts_3.md) | C. Chokutter | 2179 | `Basics` | `Prefix Sum` | [`categories/basics/event_snapshot_difference_timeline_aggregation.md`](categories/basics/event_snapshot_difference_timeline_aggregation.md) |
| [`[problem:AtCoder-abc287_g]`](analysis/AtCoder-abc287_g.md) | G. Balance Update Query | 2180 | `Data Structures (DS)` | `Segment Tree (Point Update Range Query)` | [`categories/data_structures/segment_tree_point_update_range_query_kth_walk.md`](categories/data_structures/segment_tree_point_update_range_query_kth_walk.md) |
| [`[problem:AtCoder-abc415_g]`](analysis/AtCoder-abc415_g.md) | G. Get Many Cola | 2180 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/unbounded_knapsack_pigeonhole_greedy_replacement.md`](categories/dynamic_programming/unbounded_knapsack_pigeonhole_greedy_replacement.md) |
| [`[problem:AtCoder-arc030_3]`](analysis/AtCoder-arc030_3.md) | C. 有向グラフ | 2180 | `Graph Theory` | `Strongly Connected Components (SCC)` | [`categories/graph_theory/scc_condensation_lexicographical_dag_dp.md`](categories/graph_theory/scc_condensation_lexicographical_dag_dp.md) |
| [`[problem:AtCoder-arc076_c]`](analysis/AtCoder-arc076_c.md) | E. Connected? | 2180 | `Basics` | `Stack` | [`categories/basics/perimeter_mapping_stack_bracket_matching.md`](categories/basics/perimeter_mapping_stack_bracket_matching.md) |
| [`[problem:AtCoder-abc319_g]`](analysis/AtCoder-abc319_g.md) | G. Counting Shortest Paths | 2185 | `Graph Theory` | `Breadth First Search (BFS)` | [`categories/graph_theory/complement_graph_bfs_layered_shortest_path_counting.md`](categories/graph_theory/complement_graph_bfs_layered_shortest_path_counting.md) |
| [`[problem:AtCoder-arc015_3]`](analysis/AtCoder-arc015_3.md) | C. 変わった単位 | 2185 | `Graph Theory` | `Depth First Search (DFS)` | [`categories/graph_theory/multiplicative_potential_tree_traversal.md`](categories/graph_theory/multiplicative_potential_tree_traversal.md) |
| [`[problem:AtCoder-arc185_e]`](analysis/AtCoder-arc185_e.md) | E. Adjacent GCD | 2185 | `Number Theory` | `Euler's Totient Function / Phi Function` | [`categories/number_theory/eulers_totient_expansion_online_gcd_subsequence_dp.md`](categories/number_theory/eulers_totient_expansion_online_gcd_subsequence_dp.md) |
| [`[problem:AtCoder-abc362_f]`](analysis/AtCoder-abc362_f.md) | I. Perfect Matching on a Tree | 2186 | `Data Structures (DS)` | `Centroid Decomposition` | [`categories/data_structures/tree_centroid_cyclic_pairing_max_matching.md`](categories/data_structures/tree_centroid_cyclic_pairing_max_matching.md) |
| [`[problem:AtCoder-abc272_g]`](analysis/AtCoder-abc272_g.md) | G. Yet Another mod M | 2187 | `Miscellaneous` | `Randomized Algorithms` | [`categories/miscellaneous/monte_carlo_majority_prime_factorization.md`](categories/miscellaneous/monte_carlo_majority_prime_factorization.md) |
| [`[problem:AtCoder-arc125_d]`](analysis/AtCoder-arc125_d.md) | D. Unique Subsequence | 2187 | `Data Structures (DS)` | `BIT / Fenwick Tree` | [`categories/data_structures/fenwick_tree_last_occurrence_unique_subsequences.md`](categories/data_structures/fenwick_tree_last_occurrence_unique_subsequences.md) |
| [`[problem:AtCoder-arc196_b]`](analysis/AtCoder-arc196_b.md) | B. Torus Loop | 2188 | `Data Structures (DS)` | `Augmented DSU / Weighted DSU` | [`categories/data_structures/bipartite_potential_dsu_torus_edge_loops.md`](categories/data_structures/bipartite_potential_dsu_torus_edge_loops.md) |
| [`[problem:AtCoder-abc144_f]`](analysis/AtCoder-abc144_f.md) | F. Fork in the Road | 2189 | `Math` | `Probabilities and Expected Values` | [`categories/math/expected_value_dag_dp_single_edge_perturbation.md`](categories/math/expected_value_dag_dp_single_edge_perturbation.md) |
| [`[problem:AtCoder-arc059_c]`](analysis/AtCoder-arc059_c.md) | E. Children and Candies | 2189 | `Math` | `Generating Functions` | [`categories/math/polynomial_generating_function_convolution_dp_power_sums.md`](categories/math/polynomial_generating_function_convolution_dp_power_sums.md) |
| [`[problem:AtCoder-abc407_g]`](analysis/AtCoder-abc407_g.md) | G. Domino Covering SUM | 2190 | `Graph Theory` | `Min Cost Max Flow (MCMF)` | [`categories/graph_theory/min_cost_max_flow_bipartite_matching.md`](categories/graph_theory/min_cost_max_flow_bipartite_matching.md) |
| [`[problem:AtCoder-arc067_c]`](analysis/AtCoder-arc067_c.md) | E. Grouping | 2190 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dp/group_size_partition_knapsack_dp.md`](categories/dp/group_size_partition_knapsack_dp.md) |
| [`[problem:AtCoder-arc137_d]`](analysis/AtCoder-arc137_d.md) | D. Prefix XORs | 2191 | `Dynamic Programming (DP)` | `Sum Over Subsets DP (SOS DP)` | [`categories/dp/subsequence_lcm_sos_dp_inclusion_exclusion.md`](categories/dp/subsequence_lcm_sos_dp_inclusion_exclusion.md) |
| [`[problem:AtCoder-arc166_d]`](analysis/AtCoder-arc166_d.md) | D. Interval Counts | 2192 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/interval_counts_difference_fifo_matching.md`](categories/basics/interval_counts_difference_fifo_matching.md) |
| [`[problem:AtCoder-abc328_g]`](analysis/AtCoder-abc328_g.md) | G. Cut and Reorder | 2193 | `Dynamic Programming (DP)` | `Bitmask DP` | [`categories/dynamic_programming/contiguous_subsegment_reordering_bitmask_dp.md`](categories/dynamic_programming/contiguous_subsegment_reordering_bitmask_dp.md) |
| [`[problem:AtCoder-agc065_b]`](analysis/AtCoder-agc065_b.md) | B. Erase and Insert | 2193 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dp/permutation_insertion_dp_suffix_second_gap.md`](categories/dp/permutation_insertion_dp_suffix_second_gap.md) |
| [`[problem:AtCoder-arc003_4]`](analysis/AtCoder-arc003_4.md) | D. シャッフル席替え | 2194 | `Miscellaneous` | `Randomized Algorithms` | [`categories/miscellaneous/monte_carlo_circular_table_seating_simulation.md`](categories/miscellaneous/monte_carlo_circular_table_seating_simulation.md) |
| [`[problem:AtCoder-abc396_g]`](analysis/AtCoder-abc396_g.md) | G. Flip Row or Col | 2195 | `Math` | `Fast Walsh Hadamard Transform (FWHT) and its Variations` | [`categories/math/fast_walsh_hadamard_transform_xor_convolution.md`](categories/math/fast_walsh_hadamard_transform_xor_convolution.md) |
| [`[problem:AtCoder-abc194_f]`](analysis/AtCoder-abc194_f.md) | F. Digits Paradise in Hexadecimal | 2197 | `Dynamic Programming (DP)` | `Digit DP` | [`categories/dynamic_programming/hexadecimal_distinct_digits_state_compression_digit_dp.md`](categories/dynamic_programming/hexadecimal_distinct_digits_state_compression_digit_dp.md) |
| [`[problem:AtCoder-zone2021_f]`](analysis/AtCoder-zone2021_f.md) | F. Encounter and Farewell | 2197 | `Math` | `[Technique] XOR Basis ft Reduced Row Echelon Form` | [`categories/math/xor_basis_hypercube_spanning_tree.md`](categories/math/xor_basis_hypercube_spanning_tree.md) |
| [`[problem:AtCoder-arc063_c]`](analysis/AtCoder-arc063_c.md) | E. Integers on a Tree | 2198 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dp/tree_integers_interval_parity_dp.md`](categories/dp/tree_integers_interval_parity_dp.md) |
| [`[problem:AtCoder-arc191_c]`](analysis/AtCoder-arc191_c.md) | C. A^n - 1 | 2198 | `Number Theory` | `Multiplicative Order and Carmichael's Lambda Function` | [`categories/number_theory/binomial_multiplicative_order_construction.md`](categories/number_theory/binomial_multiplicative_order_construction.md) |
| [`[problem:AtCoder-arc220_b]`](analysis/AtCoder-arc220_b.md) | B. Incomplete Shuffle | 2199 | `Graph Theory` | `Eulerian Path and Cycle` | [`categories/graph_theory/incomplete_shuffle_eulerian_trail_decomposition.md`](categories/graph_theory/incomplete_shuffle_eulerian_trail_decomposition.md) |
| [`[problem:AtCoder-abc353_f]`](analysis/AtCoder-abc353_f.md) | Tile Distance | 2201 | `Miscellaneous` | `Manhattan <> Chebyshev` | [`categories/miscellaneous/tile_distance_chebyshev_step_metric.md`](categories/miscellaneous/tile_distance_chebyshev_step_metric.md) |
| [`[problem:AtCoder-agc037_b]`](analysis/AtCoder-agc037_b.md) | RGB Balls | 2202 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/rgb_balls_3color_prefix_greedy_matching.md`](categories/basics/rgb_balls_3color_prefix_greedy_matching.md) |
| [`[problem:AtCoder-abc008_4]`](analysis/AtCoder-abc008_4.md) | 金塊ゲーム | 2203 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dp/gold_rush_2d_divide_and_conquer_range_dp.md`](categories/dp/gold_rush_2d_divide_and_conquer_range_dp.md) |
| [`[problem:AtCoder-abc425_g]`](analysis/AtCoder-abc425_g.md) | Sum of Min of XOR | 2205 | `Data Structures (DS)` | `Trie on Strings and Bits` | [`categories/data_structures/sum_of_min_of_xor_trie_canonical_subcube_dp.md`](categories/data_structures/sum_of_min_of_xor_trie_canonical_subcube_dp.md) |
| [`[problem:AtCoder-arc214_d]`](analysis/AtCoder-arc214_d.md) | Distinct Sum Grid Path | 2205 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/distinct_sum_grid_path_combinadics_diagonal_construction.md`](categories/basics/distinct_sum_grid_path_combinadics_diagonal_construction.md) |
| [`[problem:AtCoder-arc092_b]`](analysis/AtCoder-arc092_b.md) | Two Sequences | 2207 | `Basics` | `Binary Search` | [`categories/basics/two_sequences_bit_by_bit_modular_binary_search.md`](categories/basics/two_sequences_bit_by_bit_modular_binary_search.md) |
| [`[problem:AtCoder-abc227_g]`](analysis/AtCoder-abc227_g.md) | Divisors of Binomial Coefficient | 2207 | `Number Theory` | `Segmented Sieve` | [`categories/number_theory/divisors_of_binomial_coefficient_segmented_sieve.md`](categories/number_theory/divisors_of_binomial_coefficient_segmented_sieve.md) |
| [`[problem:AtCoder-abc149_f]`](analysis/AtCoder-abc149_f.md) | Surrounded Nodes | 2208 | `Math` | `Probabilities and Expected Values` | [`categories/math/surrounded_nodes_minimal_steiner_tree_expectation.md`](categories/math/surrounded_nodes_minimal_steiner_tree_expectation.md) |
| [`[problem:AtCoder-abc341_g]`](analysis/AtCoder-abc341_g.md) | Highest Ratio | 2208 | `Geometry` | `Convex Hull(2D)` | [`categories/geometry/highest_ratio_geometric_slope_lower_hull_monotonic_stack.md`](categories/geometry/highest_ratio_geometric_slope_lower_hull_monotonic_stack.md) |
| [`[problem:AtCoder-arc074_d]`](analysis/AtCoder-arc074_d.md) | Lotus Leaves | 2208 | `Graph Theory` | `Maximum Flow / Minimum Cut` | [`categories/graph_theory/lotus_leaves_bipartite_grid_lines_vertex_min_cut.md`](categories/graph_theory/lotus_leaves_bipartite_grid_lines_vertex_min_cut.md) |
| [`[problem:AtCoder-arc204_b]`](analysis/AtCoder-arc204_b.md) | Sort Permutation | 2210 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dp/sort_permutation_cyclic_chords_interval_dp.md`](categories/dp/sort_permutation_cyclic_chords_interval_dp.md) |
| [`[problem:AtCoder-abc274_f]`](analysis/AtCoder-abc274_f.md) | Fishing | 2212 | `Geometry` | `Sweep Line Algorithm and Radial Sweep` | [`categories/geometry/fishing_moving_points_interval_sweep_line.md`](categories/geometry/fishing_moving_points_interval_sweep_line.md) |
| [`[problem:AtCoder-abc009_4]`](analysis/AtCoder-abc009_4.md) | 漸化式 | 2213 | `Math` | `Matrix Exponentiation` | [`categories/math/recurrence_matrix_exponentiation_bitwise_and_xor_semiring.md`](categories/math/recurrence_matrix_exponentiation_bitwise_and_xor_semiring.md) |
| [`[problem:AtCoder-jsc2021_e]`](analysis/AtCoder-jsc2021_e.md) | Level K Palindrome | 2213 | `Data Structures (DS)` | `DSU / Union Find` | [`categories/data_structures/level_k_palindrome_dsu_recursive_halving_parity_break.md`](categories/data_structures/level_k_palindrome_dsu_recursive_halving_parity_break.md) |
| [`[problem:AtCoder-abc388_f]`](analysis/AtCoder-abc388_f.md) | Dangerous Sugoroku | 2214 | `Number Theory` | `Chicken McNugget Theorem` | [`categories/number_theory/chicken_mcnugget_dangerous_sugoroku_interval_compression.md`](categories/number_theory/chicken_mcnugget_dangerous_sugoroku_interval_compression.md) |
| [`[problem:AtCoder-abc213_f]`](analysis/AtCoder-abc213_f.md) | Common Prefixes | 2215 | `Strings` | `Suffix Array` | [`categories/strings/suffix_array_common_prefixes_lcp_monotonic_stack.md`](categories/strings/suffix_array_common_prefixes_lcp_monotonic_stack.md) |
| [`[problem:AtCoder-abc239_g]`](analysis/AtCoder-abc239_g.md) | Builder Takahashi | 2215 | `Graph Theory` | `Maximum Flow / Minimum Cut` | [`categories/graph_theory/dinic_min_vertex_cut_builder_takahashi.md`](categories/graph_theory/dinic_min_vertex_cut_builder_takahashi.md) |
| [`[problem:AtCoder-abc172_f]`](analysis/AtCoder-abc172_f.md) | Unfair Nim | 2216 | `Game Theory` | `Grundy Number and Basic Game Theory` | [`categories/game_theory/unfair_nim_bitwise_sum_xor_reduction.md`](categories/game_theory/unfair_nim_bitwise_sum_xor_reduction.md) |
| [`[problem:AtCoder-abc218_g]`](analysis/AtCoder-abc218_g.md) | Game on Tree 2 | 2217 | `Game Theory` | `Games on Arbitrary Graphs` | [`categories/game_theory/game_on_tree_2_minimax_bit_median.md`](categories/game_theory/game_on_tree_2_minimax_bit_median.md) |
| [`[problem:AtCoder-agc031_c]`](analysis/AtCoder-agc031_c.md) | Differ by 1 Bit | 2217 | `Graph Theory` | `Hamiltonian Path and Cycle` | [`categories/graph_theory/differ_by_1_bit_hypercube_hamiltonian_path.md`](categories/graph_theory/differ_by_1_bit_hypercube_hamiltonian_path.md) |
| [`[problem:AtCoder-abc284_g]`](analysis/AtCoder-abc284_g.md) | Only Once | 2218 | `Combinatorics` | `Contribution Technique` | [`categories/combinatorics/only_once_functional_graph_walk_falling_factorials.md`](categories/combinatorics/only_once_functional_graph_walk_falling_factorials.md) |
| [`[problem:AtCoder-abc250_g]`](analysis/AtCoder-abc250_g.md) | Stonks | 2219 | `Dynamic Programming (DP)` | `Slope Trick` | [`categories/dynamic_programming/stonks_buy_low_sell_high_priority_queue_slope_trick.md`](categories/dynamic_programming/stonks_buy_low_sell_high_priority_queue_slope_trick.md) |
| [`[problem:AtCoder-agc073_a]`](analysis/AtCoder-agc073_a.md) | Chords and Checkered | 2219 | `Math` | `Probabilities and Expected Values` | [`categories/math/chords_and_checkered_euler_characteristic_expectation.md`](categories/math/chords_and_checkered_euler_characteristic_expectation.md) |
| [`[problem:AtCoder-arc155_c]`](analysis/AtCoder-arc155_c.md) | Even Sum Triplet | 2219 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/even_sum_triplet_parity_invariant_permutations.md`](categories/basics/even_sum_triplet_parity_invariant_permutations.md) |
| [`[problem:AtCoder-abc270_g]`](analysis/AtCoder-abc270_g.md) | Sequence in mod P | 2220 | `Number Theory` | `Discrete Log / Baby Step Giant Step` | [`categories/number_theory/sequence_in_mod_p_affine_recurrence_bsgs.md`](categories/number_theory/sequence_in_mod_p_affine_recurrence_bsgs.md) |
| [`[problem:AtCoder-agc041_c]`](analysis/AtCoder-agc041_c.md) | Domino Quality | 2220 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/domino_quality_block_diagonal_tiling.md`](categories/basics/domino_quality_block_diagonal_tiling.md) |
| [`[problem:AtCoder-arc057_b]`](analysis/AtCoder-arc057_b.md) | 高橋君ゲーム | 2220 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/takahashi_game_state_inversion_win_rate_dp.md`](categories/dynamic_programming/takahashi_game_state_inversion_win_rate_dp.md) |
| [`[problem:AtCoder-abc206_f]`](analysis/AtCoder-abc206_f.md) | Interval Game 2 | 2221 | `Game Theory` | `Grundy Number and Basic Game Theory` | [`categories/game_theory/interval_game_2_sprague_grundy_range_dp.md`](categories/game_theory/interval_game_2_sprague_grundy_range_dp.md) |
| [`[problem:AtCoder-abc451_g]`](analysis/AtCoder-abc451_g.md) | Minimum XOR Walk | 2221 | `Math` | `[Technique] XOR Basis ft Reduced Row Echelon Form` | [`categories/math/minimum_xor_walk_rref_basis_trie.md`](categories/math/minimum_xor_walk_rref_basis_trie.md) |
| [`[problem:AtCoder-arc132_d]`](analysis/AtCoder-arc132_d.md) | Between Two Binary Strings | 2221 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/greedy_binary_strings_envelope_ray_tracing.md`](categories/basics/greedy_binary_strings_envelope_ray_tracing.md) |
| [`[problem:AtCoder-arc180_c]`](analysis/AtCoder-arc180_c.md) | Subsequence and Prefix Sum | 2221 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dp/subsequence_cumulative_sums_distinct_canonical_dp.md`](categories/dp/subsequence_cumulative_sums_distinct_canonical_dp.md) |
| [`[problem:AtCoder-abc464_f]`](analysis/AtCoder-abc464_f.md) | Random Vault Heist | 2225 | `Miscellaneous` | `Meet in the Middle` | [`categories/miscellaneous/meet_in_the_middle_random_vault_heist_prefix_expectation.md`](categories/miscellaneous/meet_in_the_middle_random_vault_heist_prefix_expectation.md) |
| [`[problem:AtCoder-abc477_g]`](analysis/AtCoder-abc477_g.md) | Frequency Query on Tree | 2226 | `Data Structures (DS)` | `Mo's on Tree` | [`categories/data_structures/mos_algorithm_on_tree_frequency_path_queries.md`](categories/data_structures/mos_algorithm_on_tree_frequency_path_queries.md) |
| [`[problem:AtCoder-abc450_g]`](analysis/AtCoder-abc450_g.md) | Random Subtraction | 2227 | `Math` | `Probabilities and Expected Values` | [`categories/math/expected_value_quadratic_forms_random_subtraction.md`](categories/math/expected_value_quadratic_forms_random_subtraction.md) |
| [`[problem:AtCoder-arc036_d]`](analysis/AtCoder-arc036_d.md) | 偶数メートル | 2227 | `Data Structures (DS)` | `Augmented DSU / Weighted DSU` | [`categories/data_structures/bipartite_dsu_parity_path_reachability.md`](categories/data_structures/bipartite_dsu_parity_path_reachability.md) |
| [`[problem:AtCoder-arc181_d]`](analysis/AtCoder-arc181_d.md) | Prefix Bubble Sort | 2227 | `Data Structures (DS)` | `BIT / Fenwick Tree` | [`categories/data_structures/prefix_bubble_sort_inversion_tracking_bit.md`](categories/data_structures/prefix_bubble_sort_inversion_tracking_bit.md) |
| [`[problem:AtCoder-arc143_d]`](analysis/AtCoder-arc143_d.md) | Bridges | 2229 | `Graph Theory` | `DFS Tree` | [`categories/graph_theory/dfs_tree_graph_orientation_bridge_minimization.md`](categories/graph_theory/dfs_tree_graph_orientation_bridge_minimization.md) |
| [`[problem:AtCoder-arc088_c]`](analysis/AtCoder-arc088_c.md) | Papple Sort | 2231 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/papple_sort_palindrome_adjacent_swaps_greedy_fenwick.md`](categories/basics/papple_sort_palindrome_adjacent_swaps_greedy_fenwick.md) |
| [`[problem:AtCoder-abc377_f]`](analysis/AtCoder-abc377_f.md) | Avoid Queen Attack | 2232 | `Combinatorics` | `Principle of Inclusion and Exclusion (PIE)` | [`categories/combinatorics/pie_queen_attack_avoidance_grid_intersections.md`](categories/combinatorics/pie_queen_attack_avoidance_grid_intersections.md) |
| [`[problem:AtCoder-abc462_g]`](analysis/AtCoder-abc462_g.md) | Completely Wrong | 2232 | `Math` | `Number Theoretic Transform (NTT)` | [`categories/math/ntt_divide_and_conquer_completely_wrong_derangements.md`](categories/math/ntt_divide_and_conquer_completely_wrong_derangements.md) |
| [`[problem:AtCoder-dwango2016qual_d]`](analysis/AtCoder-dwango2016qual_d.md) | 庭園 | 2233 | `Basics` | `2D Prefix Sum` | [`categories/basics/two_dimensional_prefix_sums_disjoint_rectangles_kadane.md`](categories/basics/two_dimensional_prefix_sums_disjoint_rectangles_kadane.md) |
| [`[problem:AtCoder-arc116_e]`](analysis/AtCoder-arc116_e.md) | Spread of Information | 2236 | `Graph Theory` | `Depth First Search (DFS)` | [`categories/graph_theory/tree_dominating_set_binary_search_dfs_spread.md`](categories/graph_theory/tree_dominating_set_binary_search_dfs_spread.md) |
| [`[problem:AtCoder-arc200_c]`](analysis/AtCoder-arc200_c.md) | Movie Theater | 2237 | `Graph Theory` | `Topological Sorting` | [`categories/graph_theory/interval_containment_poset_topological_sort_movie_theater.md`](categories/graph_theory/interval_containment_poset_topological_sort_movie_theater.md) |
| [`[problem:AtCoder-tenka1_2019_d]`](analysis/AtCoder-tenka1_2019_d.md) | Three Colors | 2237 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dp/knapsack_three_colors_triangle_inequality_complementary_counting.md`](categories/dp/knapsack_three_colors_triangle_inequality_complementary_counting.md) |
| [`[problem:AtCoder-abc272_f]`](analysis/AtCoder-abc272_f.md) | Two Strings | 2238 | `Strings` | `Suffix Array` | [`categories/strings/suffix_array_cyclic_shifts_comparison_two_strings.md`](categories/strings/suffix_array_cyclic_shifts_comparison_two_strings.md) |
| [`[problem:AtCoder-arc189_c]`](analysis/AtCoder-arc189_c.md) | Balls and Boxes | 2239 | `Miscellaneous` | `Permutations and Permutation Cycles` | [`categories/miscellaneous/permutations_cycles_balls_and_boxes_lis.md`](categories/miscellaneous/permutations_cycles_balls_and_boxes_lis.md) |
| [`[problem:AtCoder-abc130_f]`](analysis/AtCoder-abc130_f.md) | Minimum Bounding Box | 2240 | `Miscellaneous` | `Ternary Search` | [`categories/miscellaneous/ternary_search_minimum_bounding_box_envelope.md`](categories/miscellaneous/ternary_search_minimum_bounding_box_envelope.md) |
| [`[problem:AtCoder-abc296_g]`](analysis/AtCoder-abc296_g.md) | Polygon and Points | 2241 | `Geometry` | `Point in Convex Polygon in log(N)(2D)` | [`categories/geometry/point_in_convex_polygon_log_n_queries.md`](categories/geometry/point_in_convex_polygon_log_n_queries.md) |
| [`[problem:AtCoder-agc015_c]`](analysis/AtCoder-agc015_c.md) | Nuske vs Phantom Thnook | 2241 | `Basics` | `2D Prefix Sum` | [`categories/basics/2d_prefix_sum_grid_forest_connected_components.md`](categories/basics/2d_prefix_sum_grid_forest_connected_components.md) |
| [`[problem:AtCoder-abc222_g]`](analysis/AtCoder-abc222_g.md) | 222 | 2242 | `Number Theory` | `Multiplicative Order and Carmichael's Lambda Function` | [`categories/number_theory/multiplicative_order_repunit_divisibility.md`](categories/number_theory/multiplicative_order_repunit_divisibility.md) |
| [`[problem:AtCoder-abc334_g]`](analysis/AtCoder-abc334_g.md) | Christmas Color Grid 2 | 2242 | `Graph Theory` | `Articulation Points and Block Cut Tree` | [`categories/graph_theory/articulation_points_random_vertex_deletion_components.md`](categories/graph_theory/articulation_points_random_vertex_deletion_components.md) |
| [`[problem:AtCoder-abc410_g]`](analysis/AtCoder-abc410_g.md) | Longest Chord Chain | 2242 | `Dynamic Programming (DP)` | `Longest Increasing Subsequence (LIS)` | [`categories/dp/longest_chord_chain_nested_intervals_lis.md`](categories/dp/longest_chord_chain_nested_intervals_lis.md) |
| [`[problem:AtCoder-arc185_c]`](analysis/AtCoder-arc185_c.md) | Sum of Three Integers | 2242 | `Math` | `Number Theoretic Transform (NTT)` | [`categories/math/ntt_convolution_3_sum_integer_retrieval.md`](categories/math/ntt_convolution_3_sum_integer_retrieval.md) |
| [`[problem:AtCoder-arc017_4]`](analysis/AtCoder-arc017_4.md) | ARCたんクッキー | 2244 | `Data Structures (DS)` | `Segment Tree (Point Update Range Query)` | [`categories/data_structures/segment_tree_range_add_range_gcd_difference_array.md`](categories/data_structures/segment_tree_range_add_range_gcd_difference_array.md) |
| [`[problem:AtCoder-arc171_c]`](analysis/AtCoder-arc171_c.md) | Swap on Tree | 2244 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dp/tree_dp_swap_on_tree_degree_factorial_subgraphs.md`](categories/dp/tree_dp_swap_on_tree_degree_factorial_subgraphs.md) |
| [`[problem:AtCoder-abc391_g]`](analysis/AtCoder-abc391_g.md) | Many LCS | 2247 | `Strings` | `Bit LCS` | [`categories/strings/bit_lcs_automaton_dp_of_dp.md`](categories/strings/bit_lcs_automaton_dp_of_dp.md) |
| [`[problem:AtCoder-arc042_d]`](analysis/AtCoder-arc042_d.md) | あまり | 2247 | `Number Theory` | `Discrete Log / Baby Step Giant Step` | [`categories/number_theory/discrete_log_bsgs_interval_minimum_remainder.md`](categories/number_theory/discrete_log_bsgs_interval_minimum_remainder.md) |
| [`[problem:AtCoder-arc097_c]`](analysis/AtCoder-arc097_c.md) | Sorted and Sorted | 2247 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dp/sorted_and_sorted_adjacent_swaps_2d_dp.md`](categories/dp/sorted_and_sorted_adjacent_swaps_2d_dp.md) |
| [`[problem:AtCoder-abc033_d]`](analysis/AtCoder-abc033_d.md) | 三角形の分類 | 2248 | `Geometry` | `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)` | [`categories/geometry/polar_sort_triangle_classification_sweep.md`](categories/geometry/polar_sort_triangle_classification_sweep.md) |
| [`[problem:AtCoder-abc292_h]`](analysis/AtCoder-abc292_h.md) | Rating Estimator | 2248 | `Data Structures (DS)` | `Segment Tree (Point Update Range Query)` | [`categories/data_structures/walk_on_segment_tree_rating_estimator_prefix_average.md`](categories/data_structures/walk_on_segment_tree_rating_estimator_prefix_average.md) |
| [`[problem:AtCoder-arc203_c]`](analysis/AtCoder-arc203_c.md) | Destruction of Walls | 2248 | `Combinatorics` | `Large Factorials and Binomial Coefficients` | [`categories/combinatorics/destruction_of_walls_grid_shortest_paths_detours.md`](categories/combinatorics/destruction_of_walls_grid_shortest_paths_detours.md) |
| [`[problem:AtCoder-abc256_g]`](analysis/AtCoder-abc256_g.md) | G. Black and White Stones | 2250 | `Math` | `Matrix Exponentiation` | [`categories/math/matrix_exponentiation_circular_cycle_trace.md`](categories/math/matrix_exponentiation_circular_cycle_trace.md) |
| [`[problem:AtCoder-abc445_g]`](analysis/AtCoder-abc445_g.md) | G. Knight Placement | 2250 | `Graph Theory` | `Konig's Theorem and Maximum Independent Set in Bipartite Graphs` | [`categories/graph_theory/maximum_independent_set_bipartite_knight_flow.md`](categories/graph_theory/maximum_independent_set_bipartite_knight_flow.md) |
| [`[problem:AtCoder-arc104_d]`](analysis/AtCoder-arc104_d.md) | D. Multiset Mean | 2251 | `Dynamic Programming (DP)` | `Knapsack and Subset Sum Optimizations` | [`categories/dp/bounded_knapsack_average_deviation_sliding_window.md`](categories/dp/bounded_knapsack_average_deviation_sliding_window.md) |
| [`[problem:AtCoder-abc203_f]`](analysis/AtCoder-abc203_f.md) | F. Weed | 2252 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dp/logarithmic_halving_operations_greedy_dp.md`](categories/dp/logarithmic_halving_operations_greedy_dp.md) |
| [`[problem:AtCoder-abc454_g]`](analysis/AtCoder-abc454_g.md) | G. Mode in the Subtree | 2253 | `Data Structures (DS)` | `DSU on Tree and Small to Large Merging` | [`categories/data_structures/dsu_on_tree_subtree_mode_high_performance.md`](categories/data_structures/dsu_on_tree_subtree_mode_high_performance.md) |
| [`[problem:AtCoder-yahoo_procon2019_qual_f]`](analysis/AtCoder-yahoo_procon2019_qual_f.md) | F. Pass | 2253 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dp/boundary_constrained_prefix_ball_passing_dp.md`](categories/dp/boundary_constrained_prefix_ball_passing_dp.md) |
| [`[problem:AtCoder-abc238_g]`](analysis/AtCoder-abc238_g.md) | G. Cubic? | 2254 | `Miscellaneous` | `Randomized Algorithms` | [`categories/miscellaneous/parallel_trit_zobrist_hashing_range_cubes.md`](categories/miscellaneous/parallel_trit_zobrist_hashing_range_cubes.md) |
| [`[problem:AtCoder-abc365_g]`](analysis/AtCoder-abc365_g.md) | G. AtCoder Office | 2254 | `Data Structures (DS)` | `Splitting Objects into Light and Heavy / Case Processing` | [`categories/data_structures/sqrt_decomposition_light_heavy_interval_overlap.md`](categories/data_structures/sqrt_decomposition_light_heavy_interval_overlap.md) |
| [`[problem:AtCoder-abc452_g]`](analysis/AtCoder-abc452_g.md) | G. 221 Substring | 2255 | `Strings` | `Suffix Array` | [`categories/strings/rle_suffix_array_lcp_distinct_221_substrings.md`](categories/strings/rle_suffix_array_lcp_distinct_221_substrings.md) |
| [`[problem:AtCoder-nikkei2019_2_qual_e]`](analysis/AtCoder-nikkei2019_2_qual_e.md) | E. Non-triangular Triplets | 2257 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/constructive_triplets_parity_interleaving.md`](categories/basics/constructive_triplets_parity_interleaving.md) |
| [`[problem:AtCoder-arc037_d]`](analysis/AtCoder-arc037_d.md) | D. Chaotic Polygons | 2258 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dp/sierpinski_gasket_fractal_path_cycle_dp.md`](categories/dp/sierpinski_gasket_fractal_path_cycle_dp.md) |
| [`[problem:AtCoder-agc020_c]`](analysis/AtCoder-agc020_c.md) | C. Median Sum | 2259 | `Dynamic Programming (DP)` | `Knapsack and Subset Sum Optimizations` | [`categories/dp/subset_sum_complement_symmetry_bitset_median.md`](categories/dp/subset_sum_complement_symmetry_bitset_median.md) |
| [`[problem:AtCoder-abc318_g]`](analysis/AtCoder-abc318_g.md) | G. Typical Path Problem | 2260 | `Graph Theory` | `Maximum Flow / Minimum Cut` | [`categories/graph_theory/vertex_disjoint_paths_intermediate_node_flow.md`](categories/graph_theory/vertex_disjoint_paths_intermediate_node_flow.md) |
| [`[problem:AtCoder-abc263_g]`](analysis/AtCoder-abc263_g.md) | G. Erasing Prime Pairs | 2261 | `Graph Theory` | `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)` | [`categories/graph_theory/bipartite_matching_prime_pairs_ternary_search.md`](categories/graph_theory/bipartite_matching_prime_pairs_ternary_search.md) |
| [`[problem:AtCoder-arc060_b]`](analysis/AtCoder-arc060_b.md) | D. Digit Sum | 2261 | `Data Structures (DS)` | `Basic SQRT Decomposition` | [`categories/math/digit_sum_base_sqrt_decomposition_divisors.md`](categories/math/digit_sum_base_sqrt_decomposition_divisors.md) |
| [`[problem:AtCoder-m_solutions2019_e]`](analysis/AtCoder-m_solutions2019_e.md) | E. Product of Arithmetic Progression | 2261 | `Number Theory` | `Wilson's Theorem` | [`categories/number_theory/arithmetic_progression_product_factorial_mod_prime.md`](categories/number_theory/arithmetic_progression_product_factorial_mod_prime.md) |
| [`[problem:AtCoder-arc047_c]`](analysis/AtCoder-arc047_c.md) | C. N!÷K番目の単語 | 2262 | `Miscellaneous` | `Factorial Number System` | [`categories/miscellaneous/factorial_number_system_rank_fenwick.md`](categories/miscellaneous/factorial_number_system_rank_fenwick.md) |
| [`[problem:AtCoder-abc400_f]`](analysis/AtCoder-abc400_f.md) | F. Happy Birthday! 3 | 2263 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dynamic_programming_dp/interval_dp_circular_cake_coloring.md`](categories/dynamic_programming_dp/interval_dp_circular_cake_coloring.md) |
| [`[problem:AtCoder-abc311_g]`](analysis/AtCoder-abc311_g.md) | G. One More Grid Task | 2265 | `Data Structures (DS)` | `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum` | [`categories/data_structures_ds/monotonic_stack_2d_grid_min_sum.md`](categories/data_structures_ds/monotonic_stack_2d_grid_min_sum.md) |
| [`[problem:AtCoder-arc154_d]`](analysis/AtCoder-arc154_d.md) | D. A + B > C ? | 2265 | `Miscellaneous` | `Interactive Problems` | [`categories/miscellaneous/interactive_permutation_comparator_merge_sort.md`](categories/miscellaneous/interactive_permutation_comparator_merge_sort.md) |
| [`[problem:AtCoder-agc014_d]`](analysis/AtCoder-agc014_d.md) | D. Black and White Tree | 2266 | `Game Theory` | `[Problem] Matching Game On A Graph` | [`categories/game_theory/matching_game_on_tree_perfect_matching.md`](categories/game_theory/matching_game_on_tree_perfect_matching.md) |
| [`[problem:AtCoder-discovery_2016_final_c]`](analysis/AtCoder-discovery_2016_final_c.md) | C. 特別講演「括弧列と塗り分け」 | 2266 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming_dp/dp_on_trees_bracket_nesting_coloring.md`](categories/dynamic_programming_dp/dp_on_trees_bracket_nesting_coloring.md) |
| [`[problem:AtCoder-arc004_4]`](analysis/AtCoder-arc004_4.md) | D. 表現の自由 ( Freedom of expression ) | 2267 | `Basics` | `Stars and Bars` | [`categories/basics/stars_and_bars_signed_factor_partition.md`](categories/basics/stars_and_bars_signed_factor_partition.md) |
| [`[problem:AtCoder-arc231_c]`](analysis/AtCoder-arc231_c.md) | C. One Sky, Many Stars | 2267 | `Geometry` | `Euclidean Geometry` | [`categories/geometry/euclidean_geometry_1d_stargazing_intervals.md`](categories/geometry/euclidean_geometry_1d_stargazing_intervals.md) |
| [`[problem:AtCoder-abc242_f]`](analysis/AtCoder-abc242_f.md) | F. Black and White Rooks | 2268 | `Combinatorics` | `Principle of Inclusion and Exclusion (PIE)` | [`categories/combinatorics/pie_2d_chess_rook_placement.md`](categories/combinatorics/pie_2d_chess_rook_placement.md) |
| [`[problem:AtCoder-abc443_g]`](analysis/AtCoder-abc443_g.md) | G. Another Mod of Linear Problem | 2268 | `Number Theory` | `Floor Sum and Mod Sum of Arithmetic Progression` | [`categories/number_theory/floor_sum_linear_modulo_inequality.md`](categories/number_theory/floor_sum_linear_modulo_inequality.md) |
| [`[problem:AtCoder-m_solutions2020_e]`](analysis/AtCoder-m_solutions2020_e.md) | E. M's Solution | 2268 | `Dynamic Programming (DP)` | `Bitmask DP` | [`categories/dynamic_programming_dp/bitmask_dp_ternary_state_railway.md`](categories/dynamic_programming_dp/bitmask_dp_ternary_state_railway.md) |
| [`[problem:AtCoder-abc245_g]`](analysis/AtCoder-abc245_g.md) | G. Foreign Friends | 2270 | `Graph Theory` | `Dijkstra's Algorithm` | [`categories/graph_theory/dijkstra_top2_distinct_origin_countries.md`](categories/graph_theory/dijkstra_top2_distinct_origin_countries.md) |
| [`[problem:AtCoder-arc131_d]`](analysis/AtCoder-arc131_d.md) | D. AtArcher | 2271 | `Basics` | `Difference Array` | [`categories/basics/difference_array_concentric_score_bands.md`](categories/basics/difference_array_concentric_score_bands.md) |
| [`[problem:AtCoder-abc432_f]`](analysis/AtCoder-abc432_f.md) | F. Candy Redistribution | 2273 | `Dynamic Programming (DP)` | `Bitmask DP` | [`categories/dynamic_programming_dp/bitmask_dp_zero_sum_partition_reconstruction.md`](categories/dynamic_programming_dp/bitmask_dp_zero_sum_partition_reconstruction.md) |
| [`[problem:AtCoder-arc190_b]`](analysis/AtCoder-arc190_b.md) | B. L Partition | 2273 | `Combinatorics` | `Prefix Sum Queries of Binomial Coefficients` | [`categories/combinatorics/prefix_sum_binomial_l_partition_bijection.md`](categories/combinatorics/prefix_sum_binomial_l_partition_bijection.md) |
| [`[problem:AtCoder-abc196_f]`](analysis/AtCoder-abc196_f.md) | F. Substring 2 | 2274 | `Math` | `Number Theoretic Transform (NTT)` | [`categories/math/ntt_binary_string_hamming_distance.md`](categories/math/ntt_binary_string_hamming_distance.md) |
| [`[problem:AtCoder-arc202_c]`](analysis/AtCoder-arc202_c.md) | C. Repunits | 2274 | `Number Theory` | `Mobius Function and Mobius Inversion` | [`categories/number_theory/mobius_inversion_repunit_lcm.md`](categories/number_theory/mobius_inversion_repunit_lcm.md) |
| [`[problem:AtCoder-abc215_g]`](analysis/AtCoder-abc215_g.md) | G. Colorful Candies 2 | 2276 | `Math` | `Probabilities and Expected Values` | [`categories/math/expected_distinct_colors_hypergeometric_frequency_compression.md`](categories/math/expected_distinct_colors_hypergeometric_frequency_compression.md) |
| [`[problem:AtCoder-arc175_d]`](analysis/AtCoder-arc175_d.md) | D. LIS on Tree 2 | 2276 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/constructive_tree_permutation_target_lis_sum.md`](categories/basics/constructive_tree_permutation_target_lis_sum.md) |
| [`[problem:AtCoder-abc143_f]`](analysis/AtCoder-abc143_f.md) | F. Distinct Numbers | 2277 | `Basics` | `Binary Search` | [`categories/basics/binary_search_frequency_capped_subset_partition.md`](categories/basics/binary_search_frequency_capped_subset_partition.md) |
| [`[problem:AtCoder-abc273_f]`](analysis/AtCoder-abc273_f.md) | F. Hammer 2 | 2277 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dynamic_programming_dp/interval_dp_1d_coordinate_hammer_wall_reachability.md`](categories/dynamic_programming_dp/interval_dp_1d_coordinate_hammer_wall_reachability.md) |
| [`[problem:AtCoder-arc052_c]`](analysis/AtCoder-arc052_c.md) | C. 高橋くんと不思議な道 | 2277 | `Graph Theory` | `Dijkstra's Algorithm` | [`categories/graph_theory/dijkstra_quadratic_b_edge_state_pruning.md`](categories/graph_theory/dijkstra_quadratic_b_edge_state_pruning.md) |
| [`[problem:AtCoder-arc080_c]`](analysis/AtCoder-arc080_c.md) | E. Young Maids | 2277 | `Data Structures (DS)` | `Segment Tree (Point Update Range Query)` | [`categories/data_structures_ds/segment_tree_lexicographical_permutation_rmq_pair_peeling.md`](categories/data_structures_ds/segment_tree_lexicographical_permutation_rmq_pair_peeling.md) |
| [`[problem:AtCoder-arc227_d]`](analysis/AtCoder-arc227_d.md) | D. Median of Binary Strings | 2277 | `Graph Theory` | `2 SAT` | [`categories/graph_theory/two_sat_majority_polymorphism_pairwise_projection.md`](categories/graph_theory/two_sat_majority_polymorphism_pairwise_projection.md) |
| [`[problem:AtCoder-abc276_g]`](analysis/AtCoder-abc276_g.md) | G. Count Sequences | 2278 | `Basics` | `Stars and Bars` | [`categories/basics/stars_and_bars_modular_difference_hockey_stick.md`](categories/basics/stars_and_bars_modular_difference_hockey_stick.md) |
| [`[problem:AtCoder-arc170_d]`](analysis/AtCoder-arc170_d.md) | D. Triangle Card Game | 2279 | `Game Theory` | `Grundy Number and Basic Game Theory` | [`categories/game_theory/triangle_card_game_minimax_distance_gap_search.md`](categories/game_theory/triangle_card_game_minimax_distance_gap_search.md) |
| [`[problem:AtCoder-abc474_g]`](analysis/AtCoder-abc474_g.md) | G. LRUD Moving 2 | 2280 | `Graph Theory` | `Hamiltonian Path and Cycle` | [`categories/graph_theory/grid_hamiltonian_path_parity_serpentine_construction.md`](categories/graph_theory/grid_hamiltonian_path_parity_serpentine_construction.md) |
| [`[problem:AtCoder-abc150_f]`](analysis/AtCoder-abc150_f.md) | F. Xor Shift | 2281 | `Strings` | `Knuth Morris Pratt (KMP) and Prefix Automaton` | [`categories/strings/kmp_cyclic_xor_difference_matching.md`](categories/strings/kmp_cyclic_xor_difference_matching.md) |
| [`[problem:AtCoder-arc223_d]`](analysis/AtCoder-arc223_d.md) | D. Xpectation of Cards in Hand with Laboratory | 2281 | `Math` | `Gambler's Ruin` | [`categories/math/gamblers_ruin_reflection_principle_first_passage_expectation.md`](categories/math/gamblers_ruin_reflection_principle_first_passage_expectation.md) |
| [`[problem:AtCoder-arc151_d]`](analysis/AtCoder-arc151_d.md) | D. Binary Representations and Queries | 2282 | `Math` | `Fast Walsh Hadamard Transform (FWHT) and its Variations` | [`categories/math/fwht_tensor_product_independent_bit_transformations.md`](categories/math/fwht_tensor_product_independent_bit_transformations.md) |
| [`[problem:AtCoder-codefestival_2016_qualC_d]`](analysis/AtCoder-codefestival_2016_qualC_d.md) | D. Friction | 2283 | `Dynamic Programming (DP)` | `Edit Distance` | [`categories/dynamic_programming_dp/edit_distance_column_sinking_friction_alignment.md`](categories/dynamic_programming_dp/edit_distance_column_sinking_friction_alignment.md) |
| [`[problem:AtCoder-agc032_c]`](analysis/AtCoder-agc032_c.md) | C. Three Circuits | 2284 | `Graph Theory` | `Eulerian Path and Cycle` | [`categories/graph_theory/eulerian_three_circuit_degree_decomposition.md`](categories/graph_theory/eulerian_three_circuit_degree_decomposition.md) |
| [`[problem:AtCoder-arc199_a]`](analysis/AtCoder-arc199_a.md) | A. Graph Division | 2285 | `Basics` | `The XOR Trick` | [`categories/basics/xor_cycle_basis_bipartite.md`](categories/basics/xor_cycle_basis_bipartite.md) |
| [`[problem:AtCoder-abc219_g]`](analysis/AtCoder-abc219_g.md) | G. Propagation | 2287 | `Data Structures (DS)` | `Splitting Objects into Light and Heavy / Case Processing` | [`categories/data_structures/sqrt_decomp_heavy_light_lazy_propagation.md`](categories/data_structures/sqrt_decomp_heavy_light_lazy_propagation.md) |
| [`[problem:AtCoder-agc021_d]`](analysis/AtCoder-agc021_d.md) | D. Crossing | 2287 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dynamic_programming/interval_dp_longest_palindromic_subsequence_edits.md`](categories/dynamic_programming/interval_dp_longest_palindromic_subsequence_edits.md) |
| [`[problem:AtCoder-arc083_c]`](analysis/AtCoder-arc083_c.md) | C. Bichrome Tree | 2289 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming/tree_dp_knapsack_coloring.md`](categories/dynamic_programming/tree_dp_knapsack_coloring.md) |
| [`[problem:AtCoder-abc265_f]`](analysis/AtCoder-abc265_f.md) | F. Manhattan Cafe | 2290 | `Dynamic Programming (DP)` | `Knapsack and Subset Sum Optimizations` | [`categories/dynamic_programming/2d_knapsack_manhattan_prefix_sums.md`](categories/dynamic_programming/2d_knapsack_manhattan_prefix_sums.md) |
| [`[problem:AtCoder-abc177_f]`](analysis/AtCoder-abc177_f.md) | F. I hate Shortest Path Problem | 2291 | `Data Structures (DS)` | `Segment Tree with Lazy Propagation` | [`categories/data_structures/lazy_segment_tree_grid_path_chmin.md`](categories/data_structures/lazy_segment_tree_grid_path_chmin.md) |
| [`[problem:AtCoder-arc054_c]`](analysis/AtCoder-arc054_c.md) | C. Carnival | 2292 | `Math` | `Gaussian Elimination Modulo 2` | [`categories/math/gaussian_elimination_mod2_determinant.md`](categories/math/gaussian_elimination_mod2_determinant.md) |
| [`[problem:AtCoder-nikkei2019_qual_e]`](analysis/AtCoder-nikkei2019_qual_e.md) | E. Avoid Deletion | 2294 | `Data Structures (DS)` | `Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)` | [`categories/data_structures/kruskal_reconstruction_tree_weight_threshold.md`](categories/data_structures/kruskal_reconstruction_tree_weight_threshold.md) |
| [`[problem:AtCoder-arc026_4]`](analysis/AtCoder-arc026_4.md) | D. Highway Construction | 2297 | `Basics` | `Binary Search` | [`categories/basics/binary_search_01_fractional_programming_mst.md`](categories/basics/binary_search_01_fractional_programming_mst.md) |
| [`[problem:AtCoder-arc145_d]`](analysis/AtCoder-arc145_d.md) | D. Non Arithmetic Progression Set | 2297 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/constructive_3_free_set_ternary.md`](categories/basics/constructive_3_free_set_ternary.md) |
| [`[problem:AtCoder-abc355_e]`](analysis/AtCoder-abc355_e.md) | E. Guess the Sum | 2299 | `Graph Theory` | `Breadth First Search (BFS)` | [`categories/graph_theory/bfs_shortest_path_binary_interval_query.md`](categories/graph_theory/bfs_shortest_path_binary_interval_query.md) |
| [`[problem:AtCoder-arc177_d]`](analysis/AtCoder-arc177_d.md) | D. Earthquakes | 2299 | `Math` | `Probabilities and Expected Values` | [`categories/math/expected_values_domino_toppling_segment_tree.md`](categories/math/expected_values_domino_toppling_segment_tree.md) |
| [`[problem:AtCoder-arc198_d]`](analysis/AtCoder-arc198_d.md) | D. Tree Palindrome | 2299 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming/tree_dp_palindrome_paths_dsu.md`](categories/dynamic_programming/tree_dp_palindrome_paths_dsu.md) |
| [`[problem:AtCoder-abc290_f]`](analysis/AtCoder-abc290_f.md) | F. Maximum Diameter | 2300 | `Basics` | `Stars and Bars` | [`categories/basics/stars_and_bars_tree_diameter_degree_sequences.md`](categories/basics/stars_and_bars_tree_diameter_degree_sequences.md) |
| [`[problem:AtCoder-arc078_c]`](analysis/AtCoder-arc078_c.md) | E. Awkward Response | 2300 | `Miscellaneous` | `Interactive Problems` | [`categories/miscellaneous/interactive_lexicographical_binary_search.md`](categories/miscellaneous/interactive_lexicographical_binary_search.md) |
| [`[problem:AtCoder-arc129_d]`](analysis/AtCoder-arc129_d.md) | D. -1 +2 -1 | 2300 | `Basics` | `Difference Array` | [`categories/basics/difference_array_second_differences_circular.md`](categories/basics/difference_array_second_differences_circular.md) |
| [`[problem:AtCoder-abc314_g]`](analysis/AtCoder-abc314_g.md) | G. Amulets | 2301 | `Basics` | `Priority Queue / Heap` | [`categories/basics/prefix_immunity_dual_heap.md`](categories/basics/prefix_immunity_dual_heap.md) |
| [`[problem:AtCoder-arc211_d]`](analysis/AtCoder-arc211_d.md) | D. Two Signposts | 2301 | `Graph Theory` | `Topological Sorting` | [`categories/graph_theory/dual_dfs_signpost_orientation.md`](categories/graph_theory/dual_dfs_signpost_orientation.md) |
| [`[problem:AtCoder-arc229_f]`](analysis/AtCoder-arc229_f.md) | F. Card Game | 2302 | `Combinatorics` | `Contribution Technique` | [`categories/combinatorics/component_partitioning_edge_contribution.md`](categories/combinatorics/component_partitioning_edge_contribution.md) |
| [`[problem:AtCoder-abc281_g]`](analysis/AtCoder-abc281_g.md) | G. Farthest City | 2304 | `Graph Theory` | `Counting Labeled Graphs` | [`categories/graph_theory/layered_bfs_dag_graph_counting.md`](categories/graph_theory/layered_bfs_dag_graph_counting.md) |
| [`[problem:AtCoder-abc379_g]`](analysis/AtCoder-abc379_g.md) | G. Count Grid 3-coloring | 2304 | `Miscellaneous` | `Broken Profile DP / Plug DP` | [`categories/miscellaneous/broken_profile_grid_3coloring.md`](categories/miscellaneous/broken_profile_grid_3coloring.md) |
| [`[problem:AtCoder-arc159_c]`](analysis/AtCoder-arc159_c.md) | C. Permutation Addition | 2304 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/complementary_permutation_pair_transfer.md`](categories/basics/complementary_permutation_pair_transfer.md) |
| [`[problem:AtCoder-abc234_g]`](analysis/AtCoder-abc234_g.md) | G. Divide a Sequence | 2306 | `Data Structures (DS)` | `Segment Tree with Lazy Propagation` | [`categories/data_structures/dual_monotonic_stack_linear_dp.md`](categories/data_structures/dual_monotonic_stack_linear_dp.md) |
| [`[problem:AtCoder-abc258_f]`](analysis/AtCoder-abc258_f.md) | F. Main Street | 2306 | `Graph Theory` | `Dijkstra's Algorithm` | [`categories/graph_theory/grid_highway_projection_shortest_path.md`](categories/graph_theory/grid_highway_projection_shortest_path.md) |
| [`[problem:AtCoder-abc295_f]`](analysis/AtCoder-abc295_f.md) | F. substr = S | 2306 | `Dynamic Programming (DP)` | `Digit DP` | [`categories/dynamic_programming/digit_dp_substring_occurrence_linearity.md`](categories/dynamic_programming/digit_dp_substring_occurrence_linearity.md) |
| [`[problem:AtCoder-abc209_f]`](analysis/AtCoder-abc209_f.md) | F. Deforestation | 2307 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/permutation_relative_rank_insertion_dp.md`](categories/dynamic_programming/permutation_relative_rank_insertion_dp.md) |
| [`[problem:AtCoder-agc024_d]`](analysis/AtCoder-agc024_d.md) | D. Isomorphism Freak | 2307 | `Miscellaneous` | `Tree Isomorphism` | [`categories/miscellaneous/tree_isomorphism_center_leaf_minimization.md`](categories/miscellaneous/tree_isomorphism_center_leaf_minimization.md) |
| [`[problem:AtCoder-arc068_c]`](analysis/AtCoder-arc068_c.md) | E. Snuke Line | 2307 | `Data Structures (DS)` | `Splitting Objects into Light and Heavy / Case Processing` | [`categories/data_structures/harmonic_query_offline_fenwick_threshold.md`](categories/data_structures/harmonic_query_offline_fenwick_threshold.md) |
| [`[problem:AtCoder-arc049_c]`](analysis/AtCoder-arc049_c.md) | C. ぬりまーす | 2308 | `Graph Theory` | `Topological Sorting` | [`categories/graph_theory/branching_2sat_conflict_topological_cycle.md`](categories/graph_theory/branching_2sat_conflict_topological_cycle.md) |
| [`[problem:AtCoder-arc044_c]`](analysis/AtCoder-arc044_c.md) | C. ビーム | 2309 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/orthogonal_1d_beam_escape_interval_dp.md`](categories/dynamic_programming/orthogonal_1d_beam_escape_interval_dp.md) |
| [`[problem:AtCoder-exawizards2019_e]`](analysis/AtCoder-exawizards2019_e.md) | E. Black or White | 2309 | `Math` | `Gambler's Ruin` | [`categories/math/exhaustion_boundary_incremental_binomial_tails.md`](categories/math/exhaustion_boundary_incremental_binomial_tails.md) |
| [`[problem:AtCoder-panasonic2020_e]`](analysis/AtCoder-panasonic2020_e.md) | E. Three Substrings | 2309 | `Strings` | `String Matching using Bitsets` | [`categories/strings/pairwise_wildcard_alignment_filtering_span.md`](categories/strings/pairwise_wildcard_alignment_filtering_span.md) |
| [`[problem:AtCoder-abc268_g]`](analysis/AtCoder-abc268_g.md) | G. Random Student ID | 2311 | `Data Structures (DS)` | `Trie on Strings and Bits` | [`categories/data_structures/trie_random_alphabet_expected_rank.md`](categories/data_structures/trie_random_alphabet_expected_rank.md) |
| [`[problem:AtCoder-abc246_g]`](analysis/AtCoder-abc246_g.md) | G. Game on Tree 3 | 2313 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming/tree_game_binary_search_defense_dp.md`](categories/dynamic_programming/tree_game_binary_search_defense_dp.md) |
| [`[problem:AtCoder-arc167_d]`](analysis/AtCoder-arc167_d.md) | D. Good Permutation | 2313 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/functional_graph_cycle_merge_lexicographical_dsu.md`](categories/basics/functional_graph_cycle_merge_lexicographical_dsu.md) |
| [`[problem:AtCoder-arc213_b]`](analysis/AtCoder-arc213_b.md) | B. Hamming Distance is not 1 | 2313 | `Basics` | `Bitwise Operations and Bitmasks` | [`categories/basics/hypercube_interval_maximum_independent_set.md`](categories/basics/hypercube_interval_maximum_independent_set.md) |
| [`[problem:AtCoder-arc131_e]`](analysis/AtCoder-arc131_e.md) | E. Christmas Wreath | 2314 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/complete_graph_trichromatic_free_3partition.md`](categories/basics/complete_graph_trichromatic_free_3partition.md) |
| [`[problem:AtCoder-abc315_g]`](analysis/AtCoder-abc315_g.md) | G. Ai + Bj + Ck = X (1 <= i, j, k <= N) | 2315 | `Number Theory` | `Extended Euclid` | [`categories/number_theory/linear_diophantine_3var_bounded_solutions.md`](categories/number_theory/linear_diophantine_3var_bounded_solutions.md) |
| [`[problem:AtCoder-arc090_c]`](analysis/AtCoder-arc090_c.md) | E. Avoiding Collision | 2319 | `Graph Theory` | `Dijkstra's Algorithm` | [`categories/graph_theory/dijkstra_collision_avoidance_complementary_counting.md`](categories/graph_theory/dijkstra_collision_avoidance_complementary_counting.md) |
| [`[problem:AtCoder-agc062_c]`](analysis/AtCoder-agc062_c.md) | C. Mex of Subset Sum | 2320 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/subset_sum_bounded_holes_expansion.md`](categories/basics/subset_sum_bounded_holes_expansion.md) |
| [`[problem:AtCoder-abc227_f]`](analysis/AtCoder-abc227_f.md) | I. Treasure Hunting | 2323 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/grid_path_k_largest_sum_threshold_dp.md`](categories/dynamic_programming/grid_path_k_largest_sum_threshold_dp.md) |
| [`[problem:AtCoder-abc271_g]`](analysis/AtCoder-abc271_g.md) | G. Access Counter | 2323 | `Math` | `Matrix Exponentiation` | [`categories/math/markov_access_counter_matrix_exponentiation.md`](categories/math/markov_access_counter_matrix_exponentiation.md) |
| [`[problem:AtCoder-arc212_e]`](analysis/AtCoder-arc212_e.md) | E. Drop Min | 2324 | `Data Structures (DS)` | `Cartesian Tree` | [`categories/data_structures/drop_min_cartesian_tree_linear_extensions.md`](categories/data_structures/drop_min_cartesian_tree_linear_extensions.md) |
| [`[problem:AtCoder-arc115_d]`](analysis/AtCoder-arc115_d.md) | D. Odd Degree | 2325 | `Graph Theory` | `DFS Tree` | [`categories/graph_theory/spanning_forest_parity_handshaking_convolution.md`](categories/graph_theory/spanning_forest_parity_handshaking_convolution.md) |
| [`[problem:AtCoder-agc038_c]`](analysis/AtCoder-agc038_c.md) | C. LCMs | 2327 | `Number Theory` | `Mobius Function and Mobius Inversion` | [`categories/number_theory/lcm_sum_dirichlet_mobius_inversion.md`](categories/number_theory/lcm_sum_dirichlet_mobius_inversion.md) |
| [`[problem:AtCoder-caddi2018_c]`](analysis/AtCoder-caddi2018_c.md) | E. Negative Doubling | 2327 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/sign_partition_monotonic_stack_scaling_dp.md`](categories/dynamic_programming/sign_partition_monotonic_stack_scaling_dp.md) |
| [`[problem:AtCoder-abc133_f]`](analysis/AtCoder-abc133_f.md) | F. Colorful Tree | 2330 | `Graph Theory` | `Binary Lifting and LCA` | [`categories/graph_theory/tree_colored_edge_dynamic_length_offline_lca.md`](categories/graph_theory/tree_colored_edge_dynamic_length_offline_lca.md) |
| [`[problem:AtCoder-abc307_g]`](analysis/AtCoder-abc307_g.md) | G. Approximate Equalization | 2330 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/prefix_sum_approximate_equalization_dp.md`](categories/dynamic_programming/prefix_sum_approximate_equalization_dp.md) |
| [`[problem:AtCoder-arc122_d]`](analysis/AtCoder-arc122_d.md) | D. XOR Game | 2331 | `Data Structures (DS)` | `Trie on Strings and Bits` | [`categories/data_structures/trie_divide_and_conquer_xor_game.md`](categories/data_structures/trie_divide_and_conquer_xor_game.md) |
| [`[problem:AtCoder-arc232_a]`](analysis/AtCoder-arc232_a.md) | A. Permutation Journey | 2331 | `Dynamic Programming (DP)` | `1D1D DP Optimization` | [`categories/dynamic_programming/interval_reachability_monotone_dp.md`](categories/dynamic_programming/interval_reachability_monotone_dp.md) |
| [`[problem:AtCoder-abc212_f]`](analysis/AtCoder-abc212_f.md) | F. Greedy Takahashi | 2332 | `Graph Theory` | `Binary Lifting and LCA` | [`categories/graph_theory/functional_bus_graph_binary_lifting.md`](categories/graph_theory/functional_bus_graph_binary_lifting.md) |
| [`[problem:AtCoder-agc035_c]`](analysis/AtCoder-agc035_c.md) | C. Skolem XOR Tree | 2332 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/xor_tree_bichromatic_constructive.md`](categories/basics/xor_tree_bichromatic_constructive.md) |
| [`[problem:AtCoder-arc126_d]`](analysis/AtCoder-arc126_d.md) | D. Pure Permutation | 2332 | `Dynamic Programming (DP)` | `Bitmask DP` | [`categories/dynamic_programming/subsequence_permutation_clustering_bitmask_dp.md`](categories/dynamic_programming/subsequence_permutation_clustering_bitmask_dp.md) |
| [`[problem:AtCoder-abc191_f]`](analysis/AtCoder-abc191_f.md) | F. GCD or MIN | 2333 | `Number Theory` | `Sieve, Prime Factorization and Divisors` | [`categories/number_theory/gcd_divisor_closure_reachability.md`](categories/number_theory/gcd_divisor_closure_reachability.md) |
| [`[problem:AtCoder-abc136_f]`](analysis/AtCoder-abc136_f.md) | F. Enclosed Points | 2334 | `Data Structures (DS)` | `BIT / Fenwick Tree` | [`categories/data_structures/bounding_box_quadrant_inclusion_fenwick.md`](categories/data_structures/bounding_box_quadrant_inclusion_fenwick.md) |
| [`[problem:AtCoder-abc262_f]`](analysis/AtCoder-abc262_f.md) | F. Erase and Rotate | 2334 | `Data Structures (DS)` | `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum` | [`categories/data_structures/lexicographical_deletion_rotation_monotonic_stack.md`](categories/data_structures/lexicographical_deletion_rotation_monotonic_stack.md) |
| [`[problem:AtCoder-arc044_d]`](analysis/AtCoder-arc044_d.md) | D. suffix array | 2335 | `Strings` | `Suffix Array` | [`categories/strings/suffix_array_inverse_construction.md`](categories/strings/suffix_array_inverse_construction.md) |
| [`[problem:AtCoder-arc071_d]`](analysis/AtCoder-arc071_d.md) | F. Infinite Sequence | 2336 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/infinite_sequence_stabilization_dp.md`](categories/dynamic_programming/infinite_sequence_stabilization_dp.md) |
| [`[problem:AtCoder-arc174_e]`](analysis/AtCoder-arc174_e.md) | E. Existence Counting | 2336 | `Combinatorics` | `Contribution Technique` | [`categories/combinatorics/lexicographical_divergence_fenwick_existence_counting.md`](categories/combinatorics/lexicographical_divergence_fenwick_existence_counting.md) |
| [`[problem:AtCoder-abc260_g]`](analysis/AtCoder-abc260_g.md) | G. Scalene Triangle Area | 2339 | `Basics` | `2D Prefix Sum` | [`categories/basics/scalene_triangle_imos_2d_difference.md`](categories/basics/scalene_triangle_imos_2d_difference.md) |
| [`[problem:AtCoder-abc274_g]`](analysis/AtCoder-abc274_g.md) | G. Security Camera 3 | 2340 | `Graph Theory` | `Konig's Theorem and Maximum Independent Set in Bipartite Graphs` | [`categories/graph_theory/security_camera_bipartite_matching_konig.md`](categories/graph_theory/security_camera_bipartite_matching_konig.md) |
| [`[problem:AtCoder-abc292_g]`](analysis/AtCoder-abc292_g.md) | G. Count Substrings | 2340 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dynamic_programming/digit_partition_interval_dp.md`](categories/dynamic_programming/digit_partition_interval_dp.md) |
| [`[problem:AtCoder-arc202_b]`](analysis/AtCoder-arc202_b.md) | B. Tour | 2340 | `Combinatorics` | `Large Factorials and Binomial Coefficients` | [`categories/combinatorics/torus_knight_cycle_bipartite_gcd.md`](categories/combinatorics/torus_knight_cycle_bipartite_gcd.md) |
| [`[problem:AtCoder-keyence2020_e]`](analysis/AtCoder-keyence2020_e.md) | E. Bichromization | 2340 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/bichromization_distance_greedy_bfs.md`](categories/basics/bichromization_distance_greedy_bfs.md) |
| [`[problem:AtCoder-tenka1_2014_qualA_d]`](analysis/AtCoder-tenka1_2014_qualA_d.md) | D. 秘密結社 | 2341 | `Geometry` | `Sweep Line Algorithm and Radial Sweep` | [`categories/geometry/radial_sweep_circular_stabbing.md`](categories/geometry/radial_sweep_circular_stabbing.md) |
| [`[problem:AtCoder-abc141_f]`](analysis/AtCoder-abc141_f.md) | F. Xor Sum 3 | 2342 | `Math` | `Vector Space and XOR Basis` | [`categories/math/xor_basis_two_partition_maximization.md`](categories/math/xor_basis_two_partition_maximization.md) |
| [`[problem:AtCoder-agc030_b]`](analysis/AtCoder-agc030_b.md) | B. Tree Burning | 2342 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/alternating_circular_walk_burning.md`](categories/basics/alternating_circular_walk_burning.md) |
| [`[problem:AtCoder-arc141_c]`](analysis/AtCoder-arc141_c.md) | C. Bracket Manufacture | 2342 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/bracket_sequence_permutation_reconstruction.md`](categories/basics/bracket_sequence_permutation_reconstruction.md) |
| [`[problem:AtCoder-abc300_g]`](analysis/AtCoder-abc300_g.md) | G. P-smooth number | 2343 | `Miscellaneous` | `Meet in the Middle` | [`categories/miscellaneous/meet_in_the_middle_smooth_numbers.md`](categories/miscellaneous/meet_in_the_middle_smooth_numbers.md) |
| [`[problem:AtCoder-abc384_g]`](analysis/AtCoder-abc384_g.md) | G. Abs Sum | 2343 | `Data Structures (DS)` | `Mo's Algorithm` | [`categories/data_structures/mos_algorithm_prefix_abs_sum.md`](categories/data_structures/mos_algorithm_prefix_abs_sum.md) |
| [`[problem:AtCoder-agc004_d]`](analysis/AtCoder-agc004_d.md) | D. Teleporter | 2346 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/teleporter_tree_bottom_up_pruning.md`](categories/basics/teleporter_tree_bottom_up_pruning.md) |
| [`[problem:AtCoder-agc010_c]`](analysis/AtCoder-agc010_c.md) | C. Cleaning | 2346 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming/tree_path_capacity_pairing_dp.md`](categories/dynamic_programming/tree_path_capacity_pairing_dp.md) |
| [`[problem:AtCoder-arc216_c]`](analysis/AtCoder-arc216_c.md) | C. Count Power of 2 | 2346 | `Basics` | `Bit Manipulation` | [`categories/basics/power_of_two_subarray_divide_and_conquer.md`](categories/basics/power_of_two_subarray_divide_and_conquer.md) |
| [`[problem:AtCoder-abc442_g]`](analysis/AtCoder-abc442_g.md) | G. Lightweight Knapsack | 2347 | `Dynamic Programming (DP)` | `Knapsack and Subset Sum Optimizations` | [`categories/dynamic_programming/lightweight_knapsack_lcm_grouping.md`](categories/dynamic_programming/lightweight_knapsack_lcm_grouping.md) |
| [`[problem:AtCoder-abc264_g]`](analysis/AtCoder-abc264_g.md) | G. String Fair | 2348 | `Graph Theory` | `Bellman Ford` | [`categories/graph_theory/debruijn_spfa_negative_cycle_longest_path.md`](categories/graph_theory/debruijn_spfa_negative_cycle_longest_path.md) |
| [`[problem:AtCoder-abc371_g]`](analysis/AtCoder-abc371_g.md) | G. Lexicographically Smallest Permutation | 2348 | `Number Theory` | `Chinese Remainder Theorem (CRT)` | [`categories/number_theory/permutation_cycle_crt_minimization.md`](categories/number_theory/permutation_cycle_crt_minimization.md) |
| [`[problem:AtCoder-abc299_f]`](analysis/AtCoder-abc299_f.md) | F. Square Subsequence | 2349 | `Dynamic Programming (DP)` | `Substring DP` | [`categories/dynamic_programming/square_subsequence_automaton_dp.md`](categories/dynamic_programming/square_subsequence_automaton_dp.md) |
| [`[problem:AtCoder-abc211_f]`](analysis/AtCoder-abc211_f.md) | F. Rectilinear Polygons | 2350 | `Geometry` | `Sweep Line Algorithm and Radial Sweep` | [`categories/geometry/rectilinear_polygons_sweep_line.md`](categories/geometry/rectilinear_polygons_sweep_line.md) |
| [`[problem:AtCoder-arc221_b]`](analysis/AtCoder-arc221_b.md) | B. Two-Powered Sum | 2350 | `Combinatorics` | `Contribution Technique` | [`categories/combinatorics/two_powered_sum_dag_stirling_dp.md`](categories/combinatorics/two_powered_sum_dag_stirling_dp.md) |
| [`[problem:AtCoder-abc223_g]`](analysis/AtCoder-abc223_g.md) | G. Vertex Deletion | 2351 | `Graph Theory` | `Rerooting Technique` | [`categories/graph_theory/rerooting_tree_maximum_matching.md`](categories/graph_theory/rerooting_tree_maximum_matching.md) |
| [`[problem:AtCoder-abc405_g]`](analysis/AtCoder-abc405_g.md) | G. Range Shuffle Query | 2354 | `Data Structures (DS)` | `Mo's Algorithm` | [`categories/data_structures/mos_algorithm_multinomial_permutation.md`](categories/data_structures/mos_algorithm_multinomial_permutation.md) |
| [`[problem:AtCoder-agc011_c]`](analysis/AtCoder-agc011_c.md) | C. Squared Graph | 2355 | `Graph Theory` | `Depth First Search (DFS)` | [`categories/graph_theory/tensor_product_bipartite_components.md`](categories/graph_theory/tensor_product_bipartite_components.md) |
| [`[problem:AtCoder-abc345_e]`](analysis/AtCoder-abc345_e.md) | E. Colorful Subsequence | 2356 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/top2_color_linear_dp.md`](categories/dynamic_programming/top2_color_linear_dp.md) |
| [`[problem:AtCoder-abc414_f]`](analysis/AtCoder-abc414_f.md) | F. Jump Traveling | 2357 | `Graph Theory` | `Breadth First Search (BFS)` | [`categories/graph_theory/phase_bounded_tree_bfs.md`](categories/graph_theory/phase_bounded_tree_bfs.md) |
| [`[problem:AtCoder-agc036_c]`](analysis/AtCoder-agc036_c.md) | C. GP 2 | 2357 | `Basics` | `Stars and Bars` | [`categories/basics/gp2_stars_and_bars_parity.md`](categories/basics/gp2_stars_and_bars_parity.md) |
| [`[problem:AtCoder-arc172_e]`](analysis/AtCoder-arc172_e.md) | E. Last 9 Digits | 2358 | `Number Theory` | `Chinese Remainder Theorem (CRT)` | [`categories/number_theory/hensel_lifting_power_mod.md`](categories/number_theory/hensel_lifting_power_mod.md) |
| [`[problem:AtCoder-abc475_g]`](analysis/AtCoder-abc475_g.md) | G. Has Many Divisors | 2360 | `Number Theory` | `Number of Divisors / Sum of Divisors / Sigma Function` | [`categories/number_theory/highly_composite_avoiding_multiple.md`](categories/number_theory/highly_composite_avoiding_multiple.md) |
| [`[problem:AtCoder-arc232_c]`](analysis/AtCoder-arc232_c.md) | C. All Add or Single Negate | 2360 | `Graph Theory` | `Hungarian Algorithm / Bipartite Weighted Matching` | [`categories/graph_theory/hungarian_algorithm_parity_matching.md`](categories/graph_theory/hungarian_algorithm_parity_matching.md) |
| [`[problem:AtCoder-arc092_c]`](analysis/AtCoder-arc092_c.md) | E. Both Sides Merger | 2361 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/same_parity_merger_constructive.md`](categories/basics/same_parity_merger_constructive.md) |
| [`[problem:AtCoder-arc115_e]`](analysis/AtCoder-arc115_e.md) | E. LEQ and NEQ | 2363 | `Dynamic Programming (DP)` | `DP Optimization using Data Structures [Some Practice Problems]` | [`categories/dynamic_programming/monotonic_stack_pie_linear_dp.md`](categories/dynamic_programming/monotonic_stack_pie_linear_dp.md) |
| [`[problem:AtCoder-agc004_c]`](analysis/AtCoder-agc004_c.md) | C. AND Grid | 2367 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/dual_comb_grid_construction.md`](categories/basics/dual_comb_grid_construction.md) |
| [`[problem:AtCoder-abc430_g]`](analysis/AtCoder-abc430_g.md) | G. Range Set Modifying Query | 2371 | `Data Structures (DS)` | `Segment Tree with Lazy Propagation` | [`categories/data_structures/odt_lazy_segtree_cardinality.md`](categories/data_structures/odt_lazy_segtree_cardinality.md) |
| [`[problem:AtCoder-abc309_g]`](analysis/AtCoder-abc309_g.md) | G. Ban Permutation | 2372 | `Combinatorics` | `Principle of Inclusion and Exclusion (PIE)` | [`categories/combinatorics/pie_sliding_window_profile_dp.md`](categories/combinatorics/pie_sliding_window_profile_dp.md) |
| [`[problem:AtCoder-arc050_c]`](analysis/AtCoder-arc050_c.md) | C. LCM 111 | 2372 | `Math` | `Matrix Exponentiation` | [`categories/math/repunit_lcm_matrix_exponentiation.md`](categories/math/repunit_lcm_matrix_exponentiation.md) |
| [`[problem:AtCoder-abc226_g]`](analysis/AtCoder-abc226_g.md) | G. The baggage | 2373 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/greedy_bounded_knapsack_capacities.md`](categories/basics/greedy_bounded_knapsack_capacities.md) |
| [`[problem:AtCoder-abc224_g]`](analysis/AtCoder-abc224_g.md) | G. Roll or Increment | 2374 | `Math` | `Probabilities and Expected Values` | [`categories/math/threshold_reroll_expected_value.md`](categories/math/threshold_reroll_expected_value.md) |
| [`[problem:AtCoder-abc227_e]`](analysis/AtCoder-abc227_e.md) | E. Swap | 2377 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/multinomial_inversion_adjacent_swaps_dp.md`](categories/dynamic_programming/multinomial_inversion_adjacent_swaps_dp.md) |
| [`[problem:AtCoder-abc373_g]`](analysis/AtCoder-abc373_g.md) | G. No Cross Matching | 2377 | `Graph Theory` | `Min Cost Max Flow (MCMF)` | [`categories/graph_theory/euclidean_minimum_matching_no_cross.md`](categories/graph_theory/euclidean_minimum_matching_no_cross.md) |
| [`[problem:AtCoder-arc171_d]`](analysis/AtCoder-arc171_d.md) | D. Rolling Hash | 2377 | `Graph Theory` | `Chromatic Number` | [`categories/graph_theory/rolling_hash_difference_graph_chromatic_number.md`](categories/graph_theory/rolling_hash_difference_graph_chromatic_number.md) |
| [`[problem:AtCoder-arc188_c]`](analysis/AtCoder-arc188_c.md) | C. Honest or Liar or Confused | 2377 | `Graph Theory` | `2 SAT` | [`categories/graph_theory/villager_testimony_parity_consistency_2sat.md`](categories/graph_theory/villager_testimony_parity_consistency_2sat.md) |
| [`[problem:AtCoder-agc039_c]`](analysis/AtCoder-agc039_c.md) | C. Division by Two with Something | 2379 | `Combinatorics` | `Principle of Inclusion and Exclusion (PIE)` | [`categories/combinatorics/negated_cyclic_shift_mobius_periods.md`](categories/combinatorics/negated_cyclic_shift_mobius_periods.md) |
| [`[problem:AtCoder-abc303_f]`](analysis/AtCoder-abc303_f.md) | F. Damage over Time | 2381 | `Basics` | `Binary Search` | [`categories/basics/damage_over_time_binary_search_convex.md`](categories/basics/damage_over_time_binary_search_convex.md) |
| [`[problem:AtCoder-arc152_d]`](analysis/AtCoder-arc152_d.md) | D. Halftree | 2381 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/cyclic_shift_halftree_grid_construction.md`](categories/basics/cyclic_shift_halftree_grid_construction.md) |
| [`[problem:AtCoder-donuts_2015_4]`](analysis/AtCoder-donuts_2015_4.md) | D. ドーナツの箱詰め | 2383 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/nested_box_buffer_difference_multiset.md`](categories/basics/nested_box_buffer_difference_multiset.md) |
| [`[problem:AtCoder-dwango2016qual_c]`](analysis/AtCoder-dwango2016qual_c.md) | C. メンテナンス明け | 2384 | `Graph Theory` | `Dijkstra's Algorithm` | [`categories/graph_theory/sleep_risk_adversarial_dijkstra.md`](categories/graph_theory/sleep_risk_adversarial_dijkstra.md) |
| [`[problem:AtCoder-abc337_f]`](analysis/AtCoder-abc337_f.md) | F. Usual Color Ball Problems | 2386 | `Basics` | `Two Pointers` | [`categories/basics/cyclic_box_allocation_two_pointers.md`](categories/basics/cyclic_box_allocation_two_pointers.md) |
| [`[problem:AtCoder-abc479_g]`](analysis/AtCoder-abc479_g.md) | G. Tuning | 2386 | `Miscellaneous` | `Ternary Search` | [`categories/miscellaneous/collinear_manhattan_weighted_median.md`](categories/miscellaneous/collinear_manhattan_weighted_median.md) |
| [`[problem:AtCoder-abc135_f]`](analysis/AtCoder-abc135_f.md) | F. Strings of Eternity | 2388 | `Strings` | `Knuth Morris Pratt (KMP) and Prefix Automaton` | [`categories/strings/infinite_string_matching_functional_graph_kmp.md`](categories/strings/infinite_string_matching_functional_graph_kmp.md) |
| [`[problem:AtCoder-abc325_g]`](analysis/AtCoder-abc325_g.md) | G. offence | 2388 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dynamic_programming/interval_dp_of_elimination.md`](categories/dynamic_programming/interval_dp_of_elimination.md) |
| [`[problem:AtCoder-arc167_c]`](analysis/AtCoder-arc167_c.md) | C. MST on Line++ | 2388 | `Combinatorics` | `Contribution Technique` | [`categories/combinatorics/kruskal_mst_line_gap_stars_and_bars.md`](categories/combinatorics/kruskal_mst_line_gap_stars_and_bars.md) |
| [`[problem:AtCoder-arc201_d]`](analysis/AtCoder-arc201_d.md) | D. Match, Mod, Minimize | 2389 | `Basics` | `Binary Search` | [`categories/basics/modular_sum_split_reversal_matching.md`](categories/basics/modular_sum_split_reversal_matching.md) |
| [`[problem:AtCoder-arc048_c]`](analysis/AtCoder-arc048_c.md) | C. 足の多い高橋君 | 2390 | `Basics` | `Permutations, Combinations and Basic Counting Problems` | [`categories/basics/palindrome_leg_path_gcd_difference_components.md`](categories/basics/palindrome_leg_path_gcd_difference_components.md) |
| [`[problem:AtCoder-abc447_g]`](analysis/AtCoder-abc447_g.md) | G. Div. 1 & Div. 2 | 2391 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/distinct_genres_prefix_suffix_top_elements_segtree.md`](categories/dynamic_programming/distinct_genres_prefix_suffix_top_elements_segtree.md) |
| [`[problem:AtCoder-abc461_g]`](analysis/AtCoder-abc461_g.md) | G. Graph Problem 2026 | 2391 | `Graph Theory` | `Maximum Closure Problem` | [`categories/graph_theory/half_integral_independent_set_dinic_min_cut.md`](categories/graph_theory/half_integral_independent_set_dinic_min_cut.md) |
| [`[problem:AtCoder-arc055_c]`](analysis/AtCoder-arc055_c.md) | C. ABCAC | 2392 | `Strings` | `Z Algorithm` | [`categories/strings/abcac_decomposition_lcp_lcs_z_algorithm.md`](categories/strings/abcac_decomposition_lcp_lcs_z_algorithm.md) |
| [`[problem:AtCoder-abc147_f]`](analysis/AtCoder-abc147_f.md) | F. Sum Difference | 2393 | `Miscellaneous` | `Interval Set` | [`categories/miscellaneous/ap_subset_sums_coset_interval_union.md`](categories/miscellaneous/ap_subset_sums_coset_interval_union.md) |
| [`[problem:AtCoder-arc231_e]`](analysis/AtCoder-arc231_e.md) | E. Odd Inversion | 2393 | `Miscellaneous` | `Inversions` | [`categories/miscellaneous/odd_inversion_adjacent_sign_reversal_involution_dp.md`](categories/miscellaneous/odd_inversion_adjacent_sign_reversal_involution_dp.md) |
| [`[problem:AtCoder-arc109_d]`](analysis/AtCoder-arc109_d.md) | D. L | 2394 | `Geometry` | `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)` | [`categories/geometry/l_tromino_coordinate_transformation_chebyshev_distance.md`](categories/geometry/l_tromino_coordinate_transformation_chebyshev_distance.md) |
| [`[problem:AtCoder-arc091_d]`](analysis/AtCoder-arc091_d.md) | F. Strange Nim | 2395 | `Game Theory` | `Grundy Number and Basic Game Theory` | [`categories/game_theory/strange_nim_floor_subtraction_division_jumps.md`](categories/game_theory/strange_nim_floor_subtraction_division_jumps.md) |
| [`[problem:AtCoder-arc230_d]`](analysis/AtCoder-arc230_d.md) | D. Min Max Matrix | 2395 | `Combinatorics` | `Principle of Inclusion and Exclusion (PIE)` | [`categories/combinatorics/min_max_matrix_saddle_point_pie_lagrange.md`](categories/combinatorics/min_max_matrix_saddle_point_pie_lagrange.md) |
| [`[problem:AtCoder-abc207_f]`](analysis/AtCoder-abc207_f.md) | F. Tree Patrolling | 2398 | `Dynamic Programming (DP)` | `Combining Subtrees Technique` | [`categories/dynamic_programming/tree_guard_coverage_combining_subtrees_dp.md`](categories/dynamic_programming/tree_guard_coverage_combining_subtrees_dp.md) |
| [`[problem:AtCoder-abc277_f]`](analysis/AtCoder-abc277_f.md) | F. Sorting a Matrix | 2400 | `Graph Theory` | `Topological Sorting` | [`categories/graph_theory/matrix_row_column_sort_dummy_node_topological_sort.md`](categories/graph_theory/matrix_row_column_sort_dummy_node_topological_sort.md) |
| [`[problem:AtCoder-abc340_g]`](analysis/AtCoder-abc340_g.md) | G. Leaf Color | 2401 | `Graph Theory` | `Virtual Tree / Auxiliary Tree` | [`categories/graph_theory/virtual_tree_auxiliary_tree_leaf_color.md`](categories/graph_theory/virtual_tree_auxiliary_tree_leaf_color.md) |
| [`[problem:AtCoder-abc137_f]`](analysis/AtCoder-abc137_f.md) | F. Polynomial Construction | 2402 | `Math` | `Lagrange Interpolation` | [`categories/math/lagrange_interpolation_indicator_polynomial.md`](categories/math/lagrange_interpolation_indicator_polynomial.md) |
| [`[problem:AtCoder-mujin_pc_2016_d]`](analysis/AtCoder-mujin_pc_2016_d.md) | D. Parenthesis Sequence | 2404 | `Data Structures (DS)` | `Segment Tree (Point Update Range Query)` | [`categories/data_structures/segment_tree_parenthesis_prefix_balance.md`](categories/data_structures/segment_tree_parenthesis_prefix_balance.md) |
| [`[problem:AtCoder-abc298_g]`](analysis/AtCoder-abc298_g.md) | G. Strawberry War | 2405 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dynamic_programming/grid_range_mcm_subrectangle_split_dp.md`](categories/dynamic_programming/grid_range_mcm_subrectangle_split_dp.md) |
| [`[problem:AtCoder-abc259_h]`](analysis/AtCoder-abc259_h.md) | Ex. Yet Another Path Counting | 2406 | `Data Structures (DS)` | `Basic SQRT Decomposition` | [`categories/data_structures/sqrt_decomposition_frequency_grid_path_counting.md`](categories/data_structures/sqrt_decomposition_frequency_grid_path_counting.md) |
| [`[problem:AtCoder-arc139_c]`](analysis/AtCoder-arc139_c.md) | C. One Three Nine | 2406 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/constructive_grid_parity_linear_combination.md`](categories/basics/constructive_grid_parity_linear_combination.md) |
| [`[problem:AtCoder-abc290_g]`](analysis/AtCoder-abc290_g.md) | G. Edge Elimination | 2407 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming/perfect_kary_tree_subtree_cut_coin_greedy.md`](categories/dynamic_programming/perfect_kary_tree_subtree_cut_coin_greedy.md) |
| [`[problem:AtCoder-abc302_h]`](analysis/AtCoder-abc302_h.md) | Ex. Ball Collector | 2407 | `Data Structures (DS)` | `DSU with Rollbacks` | [`categories/data_structures/dsu_with_rollbacks_tree_dfs_bipartite_functional_graph.md`](categories/data_structures/dsu_with_rollbacks_tree_dfs_bipartite_functional_graph.md) |
| [`[problem:AtCoder-agc062_b]`](analysis/AtCoder-agc062_b.md) | B. Split and Insert | 2407 | `Dynamic Programming (DP)` | `Substring DP` | [`categories/dynamic_programming/radix_sort_inverse_permutation_trie_interval_dp.md`](categories/dynamic_programming/radix_sort_inverse_permutation_trie_interval_dp.md) |
| [`[problem:AtCoder-arc150_d]`](analysis/AtCoder-arc150_d.md) | D. Removing Gacha | 2407 | `Combinatorics` | `Contribution Technique` | [`categories/combinatorics/coupon_collector_tree_depth_harmonic_linearity_expectation.md`](categories/combinatorics/coupon_collector_tree_depth_harmonic_linearity_expectation.md) |
| [`[problem:AtCoder-arc224_f]`](analysis/AtCoder-arc224_f.md) | F. AND/OR | 2407 | `Basics` | `Bitwise Operations and Bitmasks` | [`categories/basics/bitwise_and_or_suffix_fixed_flag_pascal_dp.md`](categories/basics/bitwise_and_or_suffix_fixed_flag_pascal_dp.md) |
| [`[problem:AtCoder-arc182_c]`](analysis/AtCoder-arc182_c.md) | C. Sum of Number of Divisors of Product | 2408 | `Math` | `Matrix Exponentiation` | [`categories/math/prime_factor_subset_divisor_counting_matrix_expo.md`](categories/math/prime_factor_subset_divisor_counting_matrix_expo.md) |
| [`[problem:AtCoder-abc366_g]`](analysis/AtCoder-abc366_g.md) | G. XOR Neighbors | 2409 | `Math` | `Gaussian Elimination Modulo 2` | [`categories/math/f2_nullspace_gaussian_elimination_neighborhood_xor.md`](categories/math/f2_nullspace_gaussian_elimination_neighborhood_xor.md) |
| [`[problem:AtCoder-arc043_c]`](analysis/AtCoder-arc043_c.md) | C. 転倒距離 | 2409 | `Miscellaneous` | `Inversions` | [`categories/miscellaneous/inversion_distance_cayley_midpoint_fenwick.md`](categories/miscellaneous/inversion_distance_cayley_midpoint_fenwick.md) |
| [`[problem:AtCoder-abc421_g]`](analysis/AtCoder-abc421_g.md) | G. Increase to make it Increasing | 2410 | `Graph Theory` | `Min Cost Max Flow (MCMF)` | [`categories/graph_theory/min_cost_flow_difference_array_monotonicity.md`](categories/graph_theory/min_cost_flow_difference_array_monotonicity.md) |
| [`[problem:AtCoder-abc282_g]`](analysis/AtCoder-abc282_g.md) | Similar Permutation | 2412 | `Basics` | `2D Prefix Sum` | [`categories/basics/permutation_similarity_insertion_2d_prefix_sum_dp.md`](categories/basics/permutation_similarity_insertion_2d_prefix_sum_dp.md) |
| [`[problem:AtCoder-abc352_g]`](analysis/AtCoder-abc352_g.md) | Socks 3 | 2413 | `Math` | `Generating Functions` | [`categories/math/socks_distinct_draws_generating_functions_ntt.md`](categories/math/socks_distinct_draws_generating_functions_ntt.md) |
| [`[problem:AtCoder-abc180_f]`](analysis/AtCoder-abc180_f.md) | Unbranched | 2419 | `Combinatorics` | `Principle of Inclusion and Exclusion (PIE)` | [`categories/combinatorics/max_component_size_paths_cycles_pie.md`](categories/combinatorics/max_component_size_paths_cycles_pie.md) |
| [`[problem:AtCoder-abc241_g]`](analysis/AtCoder-abc241_g.md) | Round Robin | 2422 | `Graph Theory` | `Maximum Flow / Minimum Cut` | [`categories/graph_theory/round_robin_tournament_winner_max_flow.md`](categories/graph_theory/round_robin_tournament_winner_max_flow.md) |
| [`[problem:AtCoder-abc267_h]`](analysis/AtCoder-abc267_h.md) | Ex. Odd Sum | 2422 | `Math` | `Subset Sum Problem using Generating Functions` | [`categories/math/odd_cardinality_subset_sum_generating_functions_ntt.md`](categories/math/odd_cardinality_subset_sum_generating_functions_ntt.md) |
| [`[problem:AtCoder-diverta2019_e]`](analysis/AtCoder-diverta2019_e.md) | XOR Partitioning | 2423 | `Basics` | `Prefix XOR` | [`categories/basics/equal_xor_partitioning_prefix_xor_transition.md`](categories/basics/equal_xor_partitioning_prefix_xor_transition.md) |
| [`[problem:AtCoder-arc059_d]`](analysis/AtCoder-arc059_d.md) | Unhappy Hacking | 2427 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/editor_keystroke_random_walk_coordinate_dp.md`](categories/dynamic_programming/editor_keystroke_random_walk_coordinate_dp.md) |
| [`[problem:AtCoder-abc259_g]`](analysis/AtCoder-abc259_g.md) | Grid Card Game | 2428 | `Graph Theory` | `Maximum Closure Problem` | [`categories/graph_theory/grid_cards_row_col_selection_min_cut_closure.md`](categories/graph_theory/grid_cards_row_col_selection_min_cut_closure.md) |
| [`[problem:AtCoder-arc146_c]`](analysis/AtCoder-arc146_c.md) | Even XOR | 2428 | `Math` | `Vector Space and XOR Basis` | [`categories/math/even_xor_free_subsets_affine_basis_gf2.md`](categories/math/even_xor_free_subsets_affine_basis_gf2.md) |
| [`[problem:AtCoder-arc082_d]`](analysis/AtCoder-arc082_d.md) | Sandglass | 2429 | `Basics` | `Binary Search` | [`categories/basics/sandglass_piecewise_clamped_linear_binary_search.md`](categories/basics/sandglass_piecewise_clamped_linear_binary_search.md) |
| [`[problem:AtCoder-abc255_h]`](analysis/AtCoder-abc255_h.md) | Ex. Range Harvest Query | 2430 | `Miscellaneous` | `Interval Set` | [`categories/miscellaneous/range_harvest_tree_fruit_interval_set_odt.md`](categories/miscellaneous/range_harvest_tree_fruit_interval_set_odt.md) |
| [`[problem:AtCoder-arc008_4]`](analysis/AtCoder-arc008_4.md) | タコヤキオイシクナール | 2430 | `Data Structures (DS)` | `Dynamic Segment Tree` | [`categories/data_structures/affine_transformation_composition_dynamic_segment_tree.md`](categories/data_structures/affine_transformation_composition_dynamic_segment_tree.md) |
| [`[problem:AtCoder-abc138_f]`](analysis/AtCoder-abc138_f.md) | Coincidence | 2431 | `Dynamic Programming (DP)` | `Digit DP` | [`categories/dynamic_programming/mod_xor_submask_msb_digit_dp.md`](categories/dynamic_programming/mod_xor_submask_msb_digit_dp.md) |
| [`[problem:AtCoder-abc279_g]`](analysis/AtCoder-abc279_g.md) | At Most 2 Colors | 2431 | `Dynamic Programming (DP)` | `1D1D DP Optimization` | [`categories/dynamic_programming/at_most_two_colors_sliding_window_1d1d_dp.md`](categories/dynamic_programming/at_most_two_colors_sliding_window_1d1d_dp.md) |
| [`[problem:AtCoder-arc087_c]`](analysis/AtCoder-arc087_c.md) | Prefix-free Game | 2431 | `Game Theory` | `Grundy Number and Basic Game Theory` | [`categories/game_theory/prefix_free_trie_full_binary_tree_grundy_nim.md`](categories/game_theory/prefix_free_trie_full_binary_tree_grundy_nim.md) |
| [`[problem:AtCoder-arc073_c]`](analysis/AtCoder-arc073_c.md) | E. Ball Coloring | 2434 | `Basics` | `Two Pointers` | [`categories/basics/ball_coloring_extremal_two_pointers.md`](categories/basics/ball_coloring_extremal_two_pointers.md) |
| [`[problem:AtCoder-arc157_d]`](analysis/AtCoder-arc157_d.md) | D. YY Garden | 2435 | `Basics` | `2D Prefix Sum` | [`categories/basics/yy_garden_grid_partition_2d_prefix_sum.md`](categories/basics/yy_garden_grid_partition_2d_prefix_sum.md) |
| [`[problem:AtCoder-abc265_g]`](analysis/AtCoder-abc265_g.md) | G. 012 Inversion | 2436 | `Data Structures (DS)` | `Segment Tree with Lazy Propagation` | [`categories/data_structures/012_inversion_lazy_segment_tree.md`](categories/data_structures/012_inversion_lazy_segment_tree.md) |
| [`[problem:AtCoder-arc052_d]`](analysis/AtCoder-arc052_d.md) | D. 9 | 2436 | `Miscellaneous` | `Meet in the Middle` | [`categories/miscellaneous/digit_sum_modulo_meet_in_the_middle.md`](categories/miscellaneous/digit_sum_modulo_meet_in_the_middle.md) |
| [`[problem:AtCoder-agc009_c]`](analysis/AtCoder-agc009_c.md) | C. Division into Two | 2437 | `Dynamic Programming (DP)` | `DP Optimization using Data Structures [Some Practice Problems]` | [`categories/dynamic_programming/division_into_two_fenwick_dp.md`](categories/dynamic_programming/division_into_two_fenwick_dp.md) |
| [`[problem:AtCoder-arc130_d]`](analysis/AtCoder-arc130_d.md) | D. Zigzag Tree | 2437 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming/zigzag_tree_bipartite_linear_extensions_tree_dp.md`](categories/dynamic_programming/zigzag_tree_bipartite_linear_extensions_tree_dp.md) |
| [`[problem:AtCoder-abc233_g]`](analysis/AtCoder-abc233_g.md) | G. Strongest Takahashi | 2438 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dynamic_programming/strongest_takahashi_subgrid_interval_dp.md`](categories/dynamic_programming/strongest_takahashi_subgrid_interval_dp.md) |
| [`[problem:AtCoder-abc236_g]`](analysis/AtCoder-abc236_g.md) | G. Good Vertices | 2438 | `Math` | `Matrix Exponentiation` | [`categories/math/good_vertices_min_max_matrix_exponentiation.md`](categories/math/good_vertices_min_max_matrix_exponentiation.md) |
| [`[problem:AtCoder-abc220_g]`](analysis/AtCoder-abc220_g.md) | G. Isosceles Trapezium | 2439 | `Geometry` | `Polygons(2D)` | [`categories/geometry/isosceles_trapezium_perpendicular_bisectors.md`](categories/geometry/isosceles_trapezium_perpendicular_bisectors.md) |
| [`[problem:AtCoder-abc321_g]`](analysis/AtCoder-abc321_g.md) | G. Electric Circuit | 2439 | `Dynamic Programming (DP)` | `Bitmask DP` | [`categories/dynamic_programming/electric_circuit_random_connections_bitmask_dp.md`](categories/dynamic_programming/electric_circuit_random_connections_bitmask_dp.md) |
| [`[problem:AtCoder-abc269_g]`](analysis/AtCoder-abc269_g.md) | G. Reversible Cards 2 | 2440 | `Dynamic Programming (DP)` | `Knapsack and Subset Sum Optimizations` | [`categories/dynamic_programming/reversible_cards_bounded_knapsack.md`](categories/dynamic_programming/reversible_cards_bounded_knapsack.md) |
| [`[problem:AtCoder-arc095_c]`](analysis/AtCoder-arc095_c.md) | E. Symmetric Grid | 2441 | `Miscellaneous` | `Backtracking` | [`categories/miscellaneous/symmetric_grid_row_column_pairing_backtracking.md`](categories/miscellaneous/symmetric_grid_row_column_pairing_backtracking.md) |
| [`[problem:AtCoder-arc140_d]`](analysis/AtCoder-arc140_d.md) | D. One to One | 2443 | `Miscellaneous` | `Functional Graphs` | [`categories/miscellaneous/one_to_one_functional_graph_completion_dp.md`](categories/miscellaneous/one_to_one_functional_graph_completion_dp.md) |
| [`[problem:AtCoder-code_festival_2017_quala_d]`](analysis/AtCoder-code_festival_2017_quala_d.md) | D. Four Coloring | 2445 | `Miscellaneous` | `Manhattan <> Chebyshev` | [`categories/miscellaneous/four_coloring_manhattan_chebyshev_rotation.md`](categories/miscellaneous/four_coloring_manhattan_chebyshev_rotation.md) |
| [`[problem:AtCoder-abc364_g]`](analysis/AtCoder-abc364_g.md) | G. Last Major City | 2455 | `Graph Theory` | `Steiner Tree Problem` | [`categories/graph_theory/last_major_city_minimum_steiner_tree.md`](categories/graph_theory/last_major_city_minimum_steiner_tree.md) |
| [`[problem:AtCoder-arc084_b]`](analysis/AtCoder-arc084_b.md) | D. Small Multiple | 2457 | `Graph Theory` | `0/1 BFS` | [`categories/graph_theory/small_multiple_digit_sum_01_bfs.md`](categories/graph_theory/small_multiple_digit_sum_01_bfs.md) |
| [`[problem:AtCoder-tenka1_2018_e]`](analysis/AtCoder-tenka1_2018_e.md) | E. Equilateral | 2459 | `Miscellaneous` | `Manhattan <> Chebyshev` | [`categories/miscellaneous/equilateral_triangles_chebyshev_rotation.md`](categories/miscellaneous/equilateral_triangles_chebyshev_rotation.md) |
| [`[problem:AtCoder-abc240_g]`](analysis/AtCoder-abc240_g.md) | G. Teleporting Takahashi | 2462 | `Combinatorics` | `Large Factorials and Binomial Coefficients` | [`categories/combinatorics/teleporting_takahashi_3d_walk_combinatorics.md`](categories/combinatorics/teleporting_takahashi_3d_walk_combinatorics.md) |
| [`[problem:AtCoder-agc013_c]`](analysis/AtCoder-agc013_c.md) | C. Ants on a Circle | 2462 | `Miscellaneous` | `Permutations and Permutation Cycles` | [`categories/miscellaneous/ants_on_a_circle_cyclic_shift_invariant.md`](categories/miscellaneous/ants_on_a_circle_cyclic_shift_invariant.md) |
| [`[problem:AtCoder-agc028_c]`](analysis/AtCoder-agc028_c.md) | C. Min Cost Cycle | 2463 | `Graph Theory` | `Hamiltonian Path and Cycle` | [`categories/graph_theory/min_cost_cycle_hamiltonian_extremal.md`](categories/graph_theory/min_cost_cycle_hamiltonian_extremal.md) |
| [`[problem:AtCoder-abc128_f]`](analysis/AtCoder-abc128_f.md) | F. Frog Jump | 2464 | `Basics` | `Harmonic Number` | [`categories/basics/frog_jump_harmonic_number_pairs.md`](categories/basics/frog_jump_harmonic_number_pairs.md) |
| [`[problem:AtCoder-abc251_g]`](analysis/AtCoder-abc251_g.md) | G. Intersection of Polygons | 2468 | `Geometry` | `Polygons(2D)` | [`categories/geometry/intersection_of_polygons_halfplane_duality.md`](categories/geometry/intersection_of_polygons_halfplane_duality.md) |
| [`[problem:AtCoder-arc144_d]`](analysis/AtCoder-arc144_d.md) | D. AND OR Equation | 2468 | `Math` | `Vector Space and XOR Basis` | [`categories/math/and_or_affine_lattice_combinations.md`](categories/math/and_or_affine_lattice_combinations.md) |
| [`[problem:AtCoder-abc163_f]`](analysis/AtCoder-abc163_f.md) | F. path pass i | 2470 | `Graph Theory` | `Virtual Tree / Auxiliary Tree` | [`categories/graph_theory/path_pass_color_complement_tree_dfs.md`](categories/graph_theory/path_pass_color_complement_tree_dfs.md) |
| [`[problem:AtCoder-abc326_g]`](analysis/AtCoder-abc326_g.md) | G. Unlock Achievement | 2470 | `Graph Theory` | `Maximum Closure Problem` | [`categories/graph_theory/unlock_achievement_maximum_weight_closure.md`](categories/graph_theory/unlock_achievement_maximum_weight_closure.md) |
| [`[problem:AtCoder-arc033_4]`](analysis/AtCoder-arc033_4.md) | D. 見たことのない多項式 | 2470 | `Math` | `Lagrange Interpolation` | [`categories/math/polynomial_evaluation_lagrange_interpolation.md`](categories/math/polynomial_evaluation_lagrange_interpolation.md) |
| [`[problem:AtCoder-agc052_b]`](analysis/AtCoder-agc052_b.md) | B. Tree Edges XOR | 2473 | `Basics` | `Bitwise Operations and Bitmasks` | [`categories/basics/tree_edges_xor_potentials_permutation.md`](categories/basics/tree_edges_xor_potentials_permutation.md) |
| [`[problem:AtCoder-arc058_c]`](analysis/AtCoder-arc058_c.md) | E. Iroha and Haiku | 2473 | `Dynamic Programming (DP)` | `Bitmask DP` | [`categories/dynamic_programming/iroha_and_haiku_suffix_bitmask_dp.md`](categories/dynamic_programming/iroha_and_haiku_suffix_bitmask_dp.md) |
| [`[problem:AtCoder-abc193_f]`](analysis/AtCoder-abc193_f.md) | F. Zebraness | 2475 | `Graph Theory` | `Maximum Flow / Minimum Cut` | [`categories/graph_theory/zebraness_bipartite_grid_min_cut.md`](categories/graph_theory/zebraness_bipartite_grid_min_cut.md) |
| [`[problem:AtCoder-abc168_f]`](analysis/AtCoder-abc168_f.md) | F. . Single Dot | 2478 | `Miscellaneous` | `Coordinate Compression` | [`categories/miscellaneous/single_dot_grid_coordinate_compression_bfs.md`](categories/miscellaneous/single_dot_grid_coordinate_compression_bfs.md) |
| [`[problem:AtCoder-agc056_c]`](analysis/AtCoder-agc056_c.md) | C. 01 Balanced | 2481 | `Graph Theory` | `System Of Difference Constraints` | [`categories/graph_theory/01_balanced_difference_constraints_01_bfs.md`](categories/graph_theory/01_balanced_difference_constraints_01_bfs.md) |
| [`[problem:AtCoder-abc201_f]`](analysis/AtCoder-abc201_f.md) | F. Insertion Sort | 2484 | `Data Structures (DS)` | `Segment Tree (Point Update Range Query)` | [`categories/data_structures_ds/insertion_sort_unmoved_lis_segment_tree.md`](categories/data_structures_ds/insertion_sort_unmoved_lis_segment_tree.md) |
| [`[problem:AtCoder-arc102_c]`](analysis/AtCoder-arc102_c.md) | E. Stop. Otherwise... | 2484 | `Combinatorics` | `Principle of Inclusion and Exclusion (PIE)` | [`categories/combinatorics/stop_otherwise_pie_generating_functions.md`](categories/combinatorics/stop_otherwise_pie_generating_functions.md) |
| [`[problem:AtCoder-arc160_d]`](analysis/AtCoder-arc160_d.md) | D. Mahjong | 2485 | `Math` | `Generating Functions` | [`categories/math/mahjong_canonical_decomposition_generating_functions.md`](categories/math/mahjong_canonical_decomposition_generating_functions.md) |
| [`[problem:AtCoder-arc050_d]`](analysis/AtCoder-arc050_d.md) | D. Suffix Concat | 2487 | `Strings` | `Suffix Array` | [`categories/strings/suffix_concat_lcp_sparse_table_suffix_array.md`](categories/strings/suffix_concat_lcp_sparse_table_suffix_array.md) |
| [`[problem:AtCoder-abc277_g]`](analysis/AtCoder-abc277_g.md) | G. Random Walk to Millionaire | 2491 | `Math` | `Probabilities and Expected Values` | [`categories/math/random_walk_to_millionaire_level_transitions.md`](categories/math/random_walk_to_millionaire_level_transitions.md) |
| [`[problem:AtCoder-abc385_g]`](analysis/AtCoder-abc385_g.md) | G. Counting Buildings | 2492 | `Combinatorics` | `Stirling Number of the First Kind for Fixed N` | [`categories/combinatorics/counting_buildings_stirling_numbers_first_kind.md`](categories/combinatorics/counting_buildings_stirling_numbers_first_kind.md) |
| [`[problem:AtCoder-agc019_c]`](analysis/AtCoder-agc019_c.md) | C. Fountain Walk | 2495 | `Dynamic Programming (DP)` | `Longest Increasing Subsequence (LIS)` | [`categories/dynamic_programming_dp/fountain_walk_quarter_circle_savings_lis.md`](categories/dynamic_programming_dp/fountain_walk_quarter_circle_savings_lis.md) |
| [`[problem:AtCoder-agc047_c]`](analysis/AtCoder-agc047_c.md) | C. Product Modulo | 2496 | `Math` | `Number Theoretic Transform (NTT)` | [`categories/math/product_modulo_primitive_root_fft_convolution.md`](categories/math/product_modulo_primitive_root_fft_convolution.md) |
| [`[problem:AtCoder-agc034_c]`](analysis/AtCoder-agc034_c.md) | C. Tests | 2497 | `Basics` | `Binary Search` | [`categories/basics/tests_greedy_exam_hours_binary_search.md`](categories/basics/tests_greedy_exam_hours_binary_search.md) |
| [`[problem:AtCoder-abc254_h]`](analysis/AtCoder-abc254_h.md) | Ex. Multiply or Divide by 2 | 2499 | `Data Structures (DS)` | `Trie on Strings and Bits` | [`categories/data_structures_ds/multiply_or_divide_by_2_max_heap_trie.md`](categories/data_structures_ds/multiply_or_divide_by_2_max_heap_trie.md) |
| [`[problem:AtCoder-abc303_h]`](analysis/AtCoder-abc303_h.md) | Ex. Constrained Tree Degree | 2501 | `Graph Theory` | `Prufer Code` | [`categories/graph_theory/constrained_tree_degree_prufer_code_poly_exp.md`](categories/graph_theory/constrained_tree_degree_prufer_code_poly_exp.md) |
| [`[problem:AtCoder-arc061_c]`](analysis/AtCoder-arc061_c.md) | E. Snuke's Subway Trip | 2502 | `Graph Theory` | `Breadth First Search (BFS)` | [`categories/graph_theory/snukes_subway_trip_bipartite_01_bfs.md`](categories/graph_theory/snukes_subway_trip_bipartite_01_bfs.md) |
| [`[problem:AtCoder-cf17_final_d]`](analysis/AtCoder-cf17_final_d.md) | D. Zabuton | 2509 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming_dp/zabuton_cushion_stacking_exchange_argument_knapsack.md`](categories/dynamic_programming_dp/zabuton_cushion_stacking_exchange_argument_knapsack.md) |
| [`[problem:AtCoder-abc175_f]`](analysis/AtCoder-abc175_f.md) | F. Making Palindrome | 2512 | `Graph Theory` | `Dijkstra's Algorithm` | [`categories/graph_theory/making_palindrome_palindromic_residual_dijkstra.md`](categories/graph_theory/making_palindrome_palindromic_residual_dijkstra.md) |
| [`[problem:AtCoder-abc248_g]`](analysis/AtCoder-abc248_g.md) | G. GCD cost on the tree | 2514 | `Number Theory` | `Mobius Function and Mobius Inversion` | [`categories/number_theory/gcd_cost_on_the_tree_mobius_inversion.md`](categories/number_theory/gcd_cost_on_the_tree_mobius_inversion.md) |
| [`[problem:AtCoder-agc002_d]`](analysis/AtCoder-agc002_d.md) | D. Stamp Rally | 2514 | `Data Structures (DS)` | `Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)` | [`categories/data_structures_ds/stamp_rally_parallel_binary_search_dsu.md`](categories/data_structures_ds/stamp_rally_parallel_binary_search_dsu.md) |
| [`[problem:AtCoder-arc114_e]`](analysis/AtCoder-arc114_e.md) | E. Paper Cutting 2 | 2514 | `Math` | `Probabilities and Expected Values` | [`categories/math/paper_cutting_2_linearity_of_expectation.md`](categories/math/paper_cutting_2_linearity_of_expectation.md) |
| [`[problem:AtCoder-abc230_g]`](analysis/AtCoder-abc230_g.md) | G. GCD Permutation | 2516 | `Number Theory` | `Sieve, Prime Factorization and Divisors` | [`categories/number_theory/gcd_permutation_square_free_sieve.md`](categories/number_theory/gcd_permutation_square_free_sieve.md) |
| [`[problem:AtCoder-arc074_c]`](analysis/AtCoder-arc074_c.md) | E. RGB Sequence | 2519 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming_dp/rgb_sequence_prefix_color_dp.md`](categories/dynamic_programming_dp/rgb_sequence_prefix_color_dp.md) |
| [`[problem:AtCoder-abc273_g]`](analysis/AtCoder-abc273_g.md) | G. Row Column Sums 2 | 2521 | `Math` | `Generating Functions` | [`categories/math/row_column_sums_2_generating_functions_dp.md`](categories/math/row_column_sums_2_generating_functions_dp.md) |
| [`[problem:AtCoder-arc143_e]`](analysis/AtCoder-arc143_e.md) | E. Reversi | 2521 | `Graph Theory` | `Topological Sorting` | [`categories/graph_theory/reversi_tree_parity_topological_sort.md`](categories/graph_theory/reversi_tree_parity_topological_sort.md) |
| [`[problem:AtCoder-abc275_g]`](analysis/AtCoder-abc275_g.md) | G. Infinite Knapsack | 2522 | `Math` | `Linear Programming / Simplex Algorithm` | [`categories/math/infinite_knapsack_convex_hull_lp.md`](categories/math/infinite_knapsack_convex_hull_lp.md) |
| [`[problem:AtCoder-abc157_f]`](analysis/AtCoder-abc157_f.md) | F. Yakiniku Optimization Problem | 2525 | `Geometry` | `Circles, Circle Relations, Intersections, Inscribed Circles and Circumcircles(2D)` | [`categories/geometry/yakiniku_optimization_circle_intersections.md`](categories/geometry/yakiniku_optimization_circle_intersections.md) |
| [`[problem:AtCoder-abc286_h]`](analysis/AtCoder-abc286_h.md) | Ex. Don't Swim | 2526 | `Geometry` | `Tangents from Point to Convex and Convex to Convex(2D)` | [`categories/geometry/dont_swim_tangents_convex_polygon.md`](categories/geometry/dont_swim_tangents_convex_polygon.md) |
| [`[problem:AtCoder-abc233_h]`](analysis/AtCoder-abc233_h.md) | Ex. Manhattan Christmas Tree | 2530 | `Data Structures (DS)` | `Persistent Segment Tree` | [`categories/data_structures_ds/manhattan_christmas_tree_parallel_binary_search_fenwick.md`](categories/data_structures_ds/manhattan_christmas_tree_parallel_binary_search_fenwick.md) |
| [`[problem:AtCoder-abc256_h]`](analysis/AtCoder-abc256_h.md) | Ex. I like Query Problem | 2531 | `Data Structures (DS)` | `Segment Tree Beats` | [`categories/data_structures_ds/i_like_query_problem_segment_tree_beats.md`](categories/data_structures_ds/i_like_query_problem_segment_tree_beats.md) |
| [`[problem:AtCoder-abc261_h]`](analysis/AtCoder-abc261_h.md) | Ex. Game on Graph | 2531 | `Game Theory` | `Games on Arbitrary Graphs` | [`categories/game_theory/game_on_graph_retrograde_dijkstra.md`](categories/game_theory/game_on_graph_retrograde_dijkstra.md) |
| [`[problem:AtCoder-abc134_f]`](analysis/AtCoder-abc134_f.md) | F. Permutation Oddness | 2532 | `Dynamic Programming (DP)` | `Open and Close Interval Trick` | [`categories/dynamic_programming_dp/permutation_oddness_open_close_interval_trick.md`](categories/dynamic_programming_dp/permutation_oddness_open_close_interval_trick.md) |
| [`[problem:AtCoder-abc333_g]`](analysis/AtCoder-abc333_g.md) | G. Nearest Fraction | 2536 | `Miscellaneous` | `Stern-Brocot Tree and Rational Approximation` | [`categories/miscellaneous/nearest_fraction_stern_brocot_tree.md`](categories/miscellaneous/nearest_fraction_stern_brocot_tree.md) |
| [`[problem:AtCoder-arc111_e]`](analysis/AtCoder-arc111_e.md) | E. Simple Math 3 | 2541 | `Number Theory` | `Floor Sum and Mod Sum of Arithmetic Progression` | [`categories/number_theory/simple_math_3_floor_sum.md`](categories/number_theory/simple_math_3_floor_sum.md) |
| [`[problem:AtCoder-abl_f]`](analysis/AtCoder-abl_f.md) | F. Heights and Pairs | 2545 | `Combinatorics` | `Principle of Inclusion and Exclusion (PIE)` | [`categories/combinatorics/heights_and_pairs_dnc_ntt_pie.md`](categories/combinatorics/heights_and_pairs_dnc_ntt_pie.md) |
| [`[problem:AtCoder-hitachi2020_d]`](analysis/AtCoder-hitachi2020_d.md) | D. Manga Market | 2547 | `Miscellaneous` | `Exchange Arguments` | [`categories/miscellaneous/manga_market_exchange_argument_knapsack.md`](categories/miscellaneous/manga_market_exchange_argument_knapsack.md) |
| [`[problem:AtCoder-arc075_d]`](analysis/AtCoder-arc075_d.md) | F. Mirrored | 2549 | `Dynamic Programming (DP)` | `Digit DP` | [`categories/dynamic_programming_dp/mirrored_digit_differences_dfs.md`](categories/dynamic_programming_dp/mirrored_digit_differences_dfs.md) |
| [`[problem:AtCoder-abc232_g]`](analysis/AtCoder-abc232_g.md) | G. Modulo Shortest Path | 2550 | `Graph Theory` | `[Trick] Dijkstra on Segment Tree` | [`categories/graph_theory/modulo_shortest_path_cycle_graph_dijkstra.md`](categories/graph_theory/modulo_shortest_path_cycle_graph_dijkstra.md) |
| [`[problem:AtCoder-arc039_d]`](analysis/AtCoder-arc039_d.md) | D. 旅行会社高橋君 | 2550 | `Graph Theory` | `Articulation Bridges and Bridge Tree` | [`categories/graph_theory/travel_agency_bridge_block_tree_lca.md`](categories/graph_theory/travel_agency_bridge_block_tree_lca.md) |
| [`[problem:AtCoder-arc093_c]`](analysis/AtCoder-arc093_c.md) | E. Bichrome Spanning Tree | 2551 | `Graph Theory` | `Minimum Spanning Tree (MST) - Prim's and Kruskal's` | [`categories/graph_theory/bichrome_spanning_tree_kruskal_lca.md`](categories/graph_theory/bichrome_spanning_tree_kruskal_lca.md) |
| [`[problem:AtCoder-arc147_e]`](analysis/AtCoder-arc147_e.md) | E. Examination | 2553 | `Graph Theory` | `Halls Theorem` | [`categories/graph_theory/examination_halls_marriage_theorem_greedy.md`](categories/graph_theory/examination_halls_marriage_theorem_greedy.md) |
| [`[problem:AtCoder-arc128_d]`](analysis/AtCoder-arc128_d.md) | D. Neq Neq | 2554 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming_dp/neq_neq_linear_dp_alternating_runs.md`](categories/dynamic_programming_dp/neq_neq_linear_dp_alternating_runs.md) |
| [`[problem:AtCoder-abc200_f]`](analysis/AtCoder-abc200_f.md) | F. Minflip Summation | 2556 | `Math` | `Matrix Exponentiation` | [`categories/math/minflip_summation_cyclic_transitions_matrix_exp.md`](categories/math/minflip_summation_cyclic_transitions_matrix_exp.md) |
| [`[problem:AtCoder-abc348_g]`](analysis/AtCoder-abc348_g.md) | G. Max (Sum - Max) | 2559 | `Dynamic Programming (DP)` | `Divide and Conquer Optimization` | [`categories/dynamic_programming_dp/max_sum_minus_max_dnc_persistent_segtree.md`](categories/dynamic_programming_dp/max_sum_minus_max_dnc_persistent_segtree.md) |
| [`[problem:AtCoder-abc268_h]`](analysis/AtCoder-abc268_h.md) | Ex. Taboo | 2560 | `Strings` | `Aho Corasick` | [`categories/strings/taboo_aho_corasick_greedy_censoring.md`](categories/strings/taboo_aho_corasick_greedy_censoring.md) |
| [`[problem:AtCoder-keyence2021_e]`](analysis/AtCoder-keyence2021_e.md) | E. Greedy Ant | 2560 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dynamic_programming_dp/greedy_ant_interval_dp.md`](categories/dynamic_programming_dp/greedy_ant_interval_dp.md) |
| [`[problem:AtCoder-abc306_g]`](analysis/AtCoder-abc306_g.md) | G. Return to 1 | 2563 | `Graph Theory` | `Breadth First Search (BFS)` | [`categories/graph_theory/return_to_1_scc_bfs_cycle_gcd.md`](categories/graph_theory/return_to_1_scc_bfs_cycle_gcd.md) |
| [`[problem:AtCoder-abc225_g]`](analysis/AtCoder-abc225_g.md) | G. X | 2566 | `Graph Theory` | `Maximum Closure Problem` | [`categories/graph_theory/x_grid_project_selection_dinic_min_cut.md`](categories/graph_theory/x_grid_project_selection_dinic_min_cut.md) |
| [`[problem:AtCoder-abc285_g]`](analysis/AtCoder-abc285_g.md) | G. Tatami | 2566 | `Graph Theory` | `L-R Flow` | [`categories/graph_theory/tatami_lr_bounded_flow.md`](categories/graph_theory/tatami_lr_bounded_flow.md) |
| [`[problem:AtCoder-agc023_c]`](analysis/AtCoder-agc023_c.md) | C. Painting Machines | 2568 | `Combinatorics` | `Large Factorials and Binomial Coefficients` | [`categories/combinatorics/painting_machines_non_adjacent_subsets_factorial.md`](categories/combinatorics/painting_machines_non_adjacent_subsets_factorial.md) |
| [`[problem:AtCoder-arc156_d]`](analysis/AtCoder-arc156_d.md) | D. Xor Sum 5 | 2568 | `Combinatorics` | `Lucas Theorem` | [`categories/combinatorics/xor_sum_5_lucas_theorem_bitwise_dp.md`](categories/combinatorics/xor_sum_5_lucas_theorem_bitwise_dp.md) |
| [`[problem:AtCoder-arc162_d]`](analysis/AtCoder-arc162_d.md) | D. Smallest Vertices | 2568 | `Graph Theory` | `Prufer Code` | [`categories/graph_theory/smallest_vertices_prufer_tree_counting.md`](categories/graph_theory/smallest_vertices_prufer_tree_counting.md) |
| [`[problem:AtCoder-arc085_c]`](analysis/AtCoder-arc085_c.md) | E. MUL | 2571 | `Graph Theory` | `Maximum Closure Problem` | [`categories/graph_theory/mul_gemstones_divisibility_maximum_weight_closure.md`](categories/graph_theory/mul_gemstones_divisibility_maximum_weight_closure.md) |
| [`[problem:AtCoder-arc176_d]`](analysis/AtCoder-arc176_d.md) | D. Swap Permutation | 2572 | `Math` | `Probabilities and Expected Values` | [`categories/math/swap_permutation_markov_matrix_exponentiation.md`](categories/math/swap_permutation_markov_matrix_exponentiation.md) |
| [`[problem:AtCoder-abc338_g]`](analysis/AtCoder-abc338_g.md) | G. evall | 2573 | `Combinatorics` | `Contribution Technique` | [`categories/combinatorics/evall_arithmetic_substrings_contribution_technique.md`](categories/combinatorics/evall_arithmetic_substrings_contribution_technique.md) |
| [`[problem:AtCoder-arc187_c]`](analysis/AtCoder-arc187_c.md) | C. 1 Loop Bubble Sort | 2574 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming/one_loop_bubble_sort_prefix_maxima_dp.md`](categories/dynamic_programming/one_loop_bubble_sort_prefix_maxima_dp.md) |
| [`[problem:AtCoder-abc320_g]`](analysis/AtCoder-abc320_g.md) | G. Slot Strategy 2 (Hard) | 2575 | `Graph Theory` | `Halls Theorem` | [`categories/graph_theory/slot_strategy_2_bipartite_matching.md`](categories/graph_theory/slot_strategy_2_bipartite_matching.md) |
| [`[problem:AtCoder-codefestival_2016_qualB_e]`](analysis/AtCoder-codefestival_2016_qualB_e.md) | E. Lexicographical disorder | 2576 | `Data Structures (DS)` | `Trie on Strings and Bits` | [`categories/data_structures/lexicographical_disorder_trie_query_matrix.md`](categories/data_structures/lexicographical_disorder_trie_query_matrix.md) |
| [`[problem:AtCoder-arc163_d]`](analysis/AtCoder-arc163_d.md) | D. Sum of SCC | 2581 | `Graph Theory` | `Tournament Graph` | [`categories/graph_theory/tournament_graph_scc_condensation_inversion_dp.md`](categories/graph_theory/tournament_graph_scc_condensation_inversion_dp.md) |
| [`[problem:AtCoder-yahoo_procon2019_qual_e]`](analysis/AtCoder-yahoo_procon2019_qual_e.md) | E. Odd Subrectangles | 2585 | `Math` | `Gaussian Elimination Modulo 2` | [`categories/math/odd_subrectangles_f2_nullspace_gaussian_elimination.md`](categories/math/odd_subrectangles_f2_nullspace_gaussian_elimination.md) |
| [`[problem:AtCoder-arc165_d]`](analysis/AtCoder-arc165_d.md) | D. Substring Comparison | 2589 | `Graph Theory` | `Strongly Connected Components (SCC)` | [`categories/graph_theory/substring_comparison_iterative_scc_contraction.md`](categories/graph_theory/substring_comparison_iterative_scc_contraction.md) |
| [`[problem:AtCoder-arc127_d]`](analysis/AtCoder-arc127_d.md) | D. Sum of Min of Xor | 2593 | `Data Structures (DS)` | `Trie on Strings and Bits` | [`categories/data_structures/sum_of_min_of_xor_trie_canonical_subcube_dp.md`](categories/data_structures/sum_of_min_of_xor_trie_canonical_subcube_dp.md) |
| [`[problem:AtCoder-arc173_d]`](analysis/AtCoder-arc173_d.md) | D. Bracket Walk | 2598 | `Graph Theory` | `Cycle Detection` | [`categories/graph_theory/bracket_walk_bellman_ford_cycle_detection.md`](categories/graph_theory/bracket_walk_bellman_ford_cycle_detection.md) |
| [`[problem:AtCoder-arc168_d]`](analysis/AtCoder-arc168_d.md) | D. Maximize Update | 2440 | `Dynamic Programming (DP)` | `Interval DP / Range DP / Matrix Chain Multiplication (MCM)` | [`categories/dynamic_programming_dp/maximize_update_interval_dp.md`](categories/dynamic_programming_dp/maximize_update_interval_dp.md) |
| [`[problem:AtCoder-arc118_d]`](analysis/AtCoder-arc118_d.md) | D. Hamiltonian Cycle | 2448 | `Graph Theory` | `Hamiltonian Path and Cycle` | [`categories/graph_theory/hamiltonian_cycle_cayley_grid.md`](categories/graph_theory/hamiltonian_cycle_cayley_grid.md) |
| [`[problem:AtCoder-arc186_c]`](analysis/AtCoder-arc186_c.md) | C. Ball and Box | 2451 | `Miscellaneous` | `Exchange Arguments` | [`categories/miscellaneous/ball_and_box_exchange_arguments.md`](categories/miscellaneous/ball_and_box_exchange_arguments.md) |
| [`[problem:AtCoder-abc235_g]`](analysis/AtCoder-abc235_g.md) | G. Gardens | 2462 | `Combinatorics` | `Principle of Inclusion and Exclusion (PIE)` | [`categories/combinatorics/gardens_pie_prefix_binomial.md`](categories/combinatorics/gardens_pie_prefix_binomial.md) |
| [`[problem:AtCoder-abc312_h]`](analysis/AtCoder-abc312_h.md) | Ex. snukesnuke | 2477 | `Strings` | `Knuth Morris Pratt (KMP) and Prefix Automaton` | [`categories/strings/snukesnuke_kmp_primitive_root_harmonic.md`](categories/strings/snukesnuke_kmp_primitive_root_harmonic.md) |
| [`[problem:AtCoder-abc319_f]`](analysis/AtCoder-abc319_f.md) | F. Fighter Takahashi | 2480 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming_dp/fighter_takahashi_tree_bitmask_pq_dp.md`](categories/dynamic_programming_dp/fighter_takahashi_tree_bitmask_pq_dp.md) |
| [`[problem:AtCoder-arc178_d]`](analysis/AtCoder-arc178_d.md) | D. Delete Range Mex | 2498 | `Data Structures (DS)` | `Cartesian Tree` | [`categories/data_structures_ds/delete_range_mex_cartesian_tree_dp.md`](categories/data_structures_ds/delete_range_mex_cartesian_tree_dp.md) |
| [`[problem:AtCoder-agc063_c]`](analysis/AtCoder-agc063_c.md) | C. Add Mod Operations | 2500 | `Number Theory` | `Chinese Remainder Theorem (CRT)` | [`categories/number_theory/add_mod_operations_crt_cycle.md`](categories/number_theory/add_mod_operations_crt_cycle.md) |
| [`[problem:AtCoder-abc324_g]`](analysis/AtCoder-abc324_g.md) | G. Generate Arrays | 2501 | `Data Structures (DS)` | `Persistent Treap` | [`categories/data_structures_ds/generate_arrays_small_to_large_split_treap.md`](categories/data_structures_ds/generate_arrays_small_to_large_split_treap.md) |
| [`[problem:AtCoder-arc119_e]`](analysis/AtCoder-arc119_e.md) | E. Pancakes | 2502 | `Miscellaneous` | `Manhattan <> Chebyshev` | [`categories/miscellaneous/pancakes_interval_overlap_manhattan.md`](categories/miscellaneous/pancakes_interval_overlap_manhattan.md) |
| [`[problem:AtCoder-abc234_h]`](analysis/AtCoder-abc234_h.md) | Ex. Enumerate Pairs | 2505 | `Geometry` | `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)` | [`categories/geometry/enumerate_pairs_grid_hashing_2d.md`](categories/geometry/enumerate_pairs_grid_hashing_2d.md) |
| [`[problem:AtCoder-arc122_e]`](analysis/AtCoder-arc122_e.md) | E. Increasing LCMs | 2535 | `Number Theory` | `Sieve, Prime Factorization and Divisors` | [`categories/number_theory/increasing_lcms_greedy_backward_gcd.md`](categories/number_theory/increasing_lcms_greedy_backward_gcd.md) |
| [`[problem:AtCoder-abc219_f]`](analysis/AtCoder-abc219_f.md) | F. Cleaning Robot | 2542 | `Miscellaneous` | `Coordinate Compression` | [`categories/miscellaneous/cleaning_robot_1d_interval_merge.md`](categories/miscellaneous/cleaning_robot_1d_interval_merge.md) |
| [`[problem:AtCoder-abc301_f]`](analysis/AtCoder-abc301_f.md) | F. Anti-DDoS | 2548 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming_dp/anti_ddos_subsequence_counting_dp.md`](categories/dynamic_programming_dp/anti_ddos_subsequence_counting_dp.md) |
| [`[problem:AtCoder-abc395_g]`](analysis/AtCoder-abc395_g.md) | G. Minimum Steiner Tree 2 | 2561 | `Graph Theory` | `Steiner Tree Problem` | [`categories/graph_theory/minimum_steiner_tree_dreyfus_wagner.md`](categories/graph_theory/minimum_steiner_tree_dreyfus_wagner.md) |
| [`[problem:AtCoder-jsc2021_g]`](analysis/AtCoder-jsc2021_g.md) | G - Spanning Tree | 2451 | `Graph Theory` | `Kirchoffs Theorem ft Number of MSTs` | [`categories/graph_theory/spanning_tree_kirchhoffs_matrix_tree_theorem.md`](categories/graph_theory/spanning_tree_kirchhoffs_matrix_tree_theorem.md) |
| [`[problem:AtCoder-abc313_g]`](analysis/AtCoder-abc313_g.md) | G - Redistribution of Piles | 2454 | `Number Theory` | `Floor Sum and Mod Sum of Arithmetic Progression` | [`categories/number_theory/redistribution_of_piles_floor_sum.md`](categories/number_theory/redistribution_of_piles_floor_sum.md) |
| [`[problem:AtCoder-code_festival_2017_qualb_d]`](analysis/AtCoder-code_festival_2017_qualb_d.md) | D - 101 to 010 | 2499 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming_dp/101_to_010_interval_dp.md`](categories/dynamic_programming_dp/101_to_010_interval_dp.md) |
| [`[problem:AtCoder-abc390_g]`](analysis/AtCoder-abc390_g.md) | G - Permutation Concatenation | 2508 | `Math` | `Number Theoretic Transform (NTT)` | [`categories/math/permutation_concatenation_ntt_convolution.md`](categories/math/permutation_concatenation_ntt_convolution.md) |
| [`[problem:AtCoder-arc186_a]`](analysis/AtCoder-arc186_a.md) | A - Underclued | 2511 | `Combinatorics` | `Contribution Technique` | [`categories/combinatorics/underclued_tournament_bipartite_scc.md`](categories/combinatorics/underclued_tournament_bipartite_scc.md) |
| [`[problem:AtCoder-agc050_c]`](analysis/AtCoder-agc050_c.md) | C - Block Game | 2528 | `Dynamic Programming (DP)` | `Divide and Conquer Optimization` | [`categories/dynamic_programming_dp/block_game_doubling_dp.md`](categories/dynamic_programming_dp/block_game_doubling_dp.md) |
| [`[problem:AtCoder-codefestival_2016_final_f]`](analysis/AtCoder-codefestival_2016_final_f.md) | F - Road of the King | 2539 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming_dp/road_of_the_king_scc_walk_dp.md`](categories/dynamic_programming_dp/road_of_the_king_scc_walk_dp.md) |
| [`[problem:AtCoder-diverta2019_2_e]`](analysis/AtCoder-diverta2019_2_e.md) | E - Balanced Piles | 2543 | `Combinatorics` | `Principle of Inclusion and Exclusion (PIE)` | [`categories/combinatorics/balanced_piles_height_dag_pie.md`](categories/combinatorics/balanced_piles_height_dag_pie.md) |
| [`[problem:AtCoder-abc267_g]`](analysis/AtCoder-abc267_g.md) | G - Increasing K Times | 2561 | `Combinatorics` | `Product Trick` | [`categories/combinatorics/increasing_k_times_eulerian_multiset_dp.md`](categories/combinatorics/increasing_k_times_eulerian_multiset_dp.md) |
| [`[problem:AtCoder-abc365_f]`](analysis/AtCoder-abc365_f.md) | F - Takahashi on Grid | 2561 | `Data Structures (DS)` | `Iterative Segment Tree` | [`categories/data_structures_ds/takahashi_on_grid_iterative_segtree.md`](categories/data_structures_ds/takahashi_on_grid_iterative_segtree.md) |
| [`[problem:AtCoder-abc360_f]`](analysis/AtCoder-abc360_f.md) | F - InterSections | 2563 | `Geometry` | `Sweep Line Algorithm and Radial Sweep` | [`categories/geometry/intersections_sweep_line_lazy_segtree.md`](categories/geometry/intersections_sweep_line_lazy_segtree.md) |
| [`[problem:AtCoder-dwacon6th_prelims_d]`](analysis/AtCoder-dwacon6th_prelims_d.md) | D - Arrangement | 2589 | `Graph Theory` | `Halls Theorem` | [`categories/graph_theory/arrangement_halls_marriage_greedy.md`](categories/graph_theory/arrangement_halls_marriage_greedy.md) |
| [`[problem:AtCoder-aising2019_e]`](analysis/AtCoder-aising2019_e.md) | E - Attack to a Tree | 2595 | `Dynamic Programming (DP)` | `Combining Subtrees Technique` | [`categories/dynamic_programming_dp/attack_to_a_tree_knapsack_dp.md`](categories/dynamic_programming_dp/attack_to_a_tree_knapsack_dp.md) |
| [`[problem:AtCoder-arc193_b]`](analysis/AtCoder-arc193_b.md) | B - Broken Wheel | 2420 | `Graph Theory` | `Cycle Detection` | [`categories/graph_theory/broken_wheel_cycle_matrix_scan.md`](categories/graph_theory/broken_wheel_cycle_matrix_scan.md) |
| [`[problem:AtCoder-abc438_g]`](analysis/AtCoder-abc438_g.md) | G - Sum of Min | 2455 | `Number Theory` | `Extended Euclid` | [`categories/number_theory/sum_of_min_extended_euclid_fenwick.md`](categories/number_theory/sum_of_min_extended_euclid_fenwick.md) |
| [`[problem:AtCoder-agc065_c]`](analysis/AtCoder-agc065_c.md) | C - Avoid Half Sum | 2414 | `Game Theory` | `Grundy Number and Basic Game Theory` | [`categories/game_theory/avoid_half_sum_odd_partition_parity.md`](categories/game_theory/avoid_half_sum_odd_partition_parity.md) |
| [`[problem:AtCoder-abc420_f]`](analysis/AtCoder-abc420_f.md) | F - kirinuki | 2420 | `Data Structures (DS)` | `Cartesian Tree` | [`categories/data_structures_ds/kirinuki_cartesian_tree_histogram.md`](categories/data_structures_ds/kirinuki_cartesian_tree_histogram.md) |
| [`[problem:AtCoder-arc222_e]`](analysis/AtCoder-arc222_e.md) | E - XOR Matching | 2423 | `Math` | `Fast Walsh Hadamard Transform (FWHT) and its Variations` | [`categories/math/xor_matching_fwht_autocorrelation.md`](categories/math/xor_matching_fwht_autocorrelation.md) |
| [`[problem:AtCoder-abc463_g]`](analysis/AtCoder-abc463_g.md) | G - Random Walk Distance | 2452 | `Data Structures (DS)` | `Mo's Algorithm` | [`categories/data_structures_ds/random_walk_distance_mos_algorithm.md`](categories/data_structures_ds/random_walk_distance_mos_algorithm.md) |
| [`[problem:AtCoder-agc069_a]`](analysis/AtCoder-agc069_a.md) | A - Schedule Optimization | 2460 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming_dp/schedule_optimization_tournament_tree_dp.md`](categories/dynamic_programming_dp/schedule_optimization_tournament_tree_dp.md) |
| [`[problem:AtCoder-abc471_g]`](analysis/AtCoder-abc471_g.md) | G - Caeser Syllables | 2464 | `Basics` | `Difference Array` | [`categories/basics/caeser_syllables_cyclic_difference_ntt.md`](categories/basics/caeser_syllables_cyclic_difference_ntt.md) |
| [`[problem:AtCoder-arc195_d]`](analysis/AtCoder-arc195_d.md) | D - Swap and Erase | 2470 | `Dynamic Programming (DP)` | `Knapsack and Basic Dynamic Programming` | [`categories/dynamic_programming_dp/swap_and_erase_adjacent_swap_dp.md`](categories/dynamic_programming_dp/swap_and_erase_adjacent_swap_dp.md) |
| [`[problem:AtCoder-abc428_g]`](analysis/AtCoder-abc428_g.md) | G - Necklace | 2472 | `Number Theory` | `Dirichlet convolution` | [`categories/number_theory/necklace_dirichlet_convolution_polya.md`](categories/number_theory/necklace_dirichlet_convolution_polya.md) |
| [`[problem:AtCoder-arc200_d]`](analysis/AtCoder-arc200_d.md) | D - |A + A| | 2474 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/a_plus_a_additive_combinatorics_constructive.md`](categories/basics/a_plus_a_additive_combinatorics_constructive.md) |
| [`[problem:AtCoder-abc476_g]`](analysis/AtCoder-abc476_g.md) | G - Increasing Popcount | 2477 | `Graph Theory` | `POSET ft Dilworth's and Mirsky's Theorem` | [`categories/graph_theory/increasing_popcount_poset_dilworth.md`](categories/graph_theory/increasing_popcount_poset_dilworth.md) |
| [`[problem:AtCoder-abc456_g]`](analysis/AtCoder-abc456_g.md) | G - Count Holidays | 2488 | `Math` | `Number Theoretic Transform (NTT)` | [`categories/math/count_holidays_generating_function_ntt.md`](categories/math/count_holidays_generating_function_ntt.md) |
| [`[problem:AtCoder-arc207_c]`](analysis/AtCoder-arc207_c.md) | C - Combine to Make Non-decreasing | 2488 | `Basics` | `Bitwise Operations and Bitmasks` | [`categories/basics/combine_to_make_non_decreasing_bitwise_or.md`](categories/basics/combine_to_make_non_decreasing_bitwise_or.md) |
| [`[problem:AtCoder-abc431_g]`](analysis/AtCoder-abc431_g.md) | G - One Time Swap 2 | 2490 | `Data Structures (DS)` | `BIT / Fenwick Tree` | [`categories/data_structures_ds/one_time_swap_2_fenwick_inversions.md`](categories/data_structures_ds/one_time_swap_2_fenwick_inversions.md) |
| [`[problem:AtCoder-abc418_f]`](analysis/AtCoder-abc418_f.md) | F - We're teapots | 2496 | `Data Structures (DS)` | `Segment Tree (Point Update Range Query)` | [`categories/data_structures_ds/were_teapots_matrix_point_update_segtree.md`](categories/data_structures_ds/were_teapots_matrix_point_update_segtree.md) |
| [`[problem:AtCoder-abc435_g]`](analysis/AtCoder-abc435_g.md) | G - Domino Arrangement | 2519 | `Dynamic Programming (DP)` | `Open and Close Interval Trick` | [`categories/dynamic_programming_dp/domino_arrangement_interval_active_set_dp.md`](categories/dynamic_programming_dp/domino_arrangement_interval_active_set_dp.md) |
| [`[problem:AtCoder-arc215_e]`](analysis/AtCoder-arc215_e.md) | E - CNOT Party | 2418 | `Graph Theory` | `Breadth First Search (BFS)` | [`categories/graph_theory/cnot_party_bidirectional_bfs.md`](categories/graph_theory/cnot_party_bidirectional_bfs.md) |
| [`[problem:AtCoder-arc029_4]`](analysis/AtCoder-arc029_4.md) | D - 高橋君と木のおもちゃ | 2438 | `Dynamic Programming (DP)` | `DP on Trees and DAGs` | [`categories/dynamic_programming_dp/tree_toy_quadratic_tree_knapsack_dp.md`](categories/dynamic_programming_dp/tree_toy_quadratic_tree_knapsack_dp.md) |
| [`[problem:AtCoder-arc047_b]`](analysis/AtCoder-arc047_b.md) | B - 同一円周上 | 2455 | `Geometry` | `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)` | [`categories/geometry/equidistant_points_chebyshev_rotation.md`](categories/geometry/equidistant_points_chebyshev_rotation.md) |
| [`[problem:AtCoder-cf_2015_morning_hard_b]`](analysis/AtCoder-cf_2015_morning_hard_b.md) | D - 立方体とペンキ | 2456 | `Data Structures (DS)` | `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum` | [`categories/data_structures_ds/cubes_paint_monotonic_stack_peak_shaving.md`](categories/data_structures_ds/cubes_paint_monotonic_stack_peak_shaving.md) |
| [`[problem:AtCoder-arc027_4]`](analysis/AtCoder-arc027_4.md) | D - ぴょんぴょんトレーニング | 2474 | `Data Structures (DS)` | `Basic SQRT Decomposition` | [`categories/data_structures_ds/pyon_training_sqrt_matrix_decomposition.md`](categories/data_structures_ds/pyon_training_sqrt_matrix_decomposition.md) |
| [`[problem:AtCoder-arc010_4]`](analysis/AtCoder-arc010_4.md) | D - 情報伝播 | 2481 | `Graph Theory` | `Strongly Connected Components (SCC)` | [`categories/graph_theory/information_propagation_scc_indegree_zero.md`](categories/graph_theory/information_propagation_scc_indegree_zero.md) |
| [`[problem:AtCoder-arc005_4]`](analysis/AtCoder-arc005_4.md) | D - 連射王高橋君 | 2487 | `Dynamic Programming (DP)` | `Digit DP` | [`categories/dynamic_programming_dp/rensha_king_digit_dp_expression_reconstruction.md`](categories/dynamic_programming_dp/rensha_king_digit_dp_expression_reconstruction.md) |
| [`[problem:AtCoder-arc007_4]`](analysis/AtCoder-arc007_4.md) | D - 破れた宿題 | 2491 | `Miscellaneous` | `Heavy Implementation Problems` | [`categories/miscellaneous/torn_homework_ap_reconstruction.md`](categories/miscellaneous/torn_homework_ap_reconstruction.md) |
| [`[problem:AtCoder-dwango2015_prelims_4]`](analysis/AtCoder-dwango2015_prelims_4.md) | D - タクシー | 2495 | `Basics` | `Basic Greedy Algorithms` | [`categories/basics/taxi_circle_optimal_transport_weighted_median.md`](categories/basics/taxi_circle_optimal_transport_weighted_median.md) |
| [`[problem:AtCoder-arc024_4]`](analysis/AtCoder-arc024_4.md) | D - バス停 | 2496 | `Basics` | `Divide and Conquer` | [`categories/basics/bus_stops_divide_and_conquer_median_grid.md`](categories/basics/bus_stops_divide_and_conquer_median_grid.md) |
| [`[problem:AtCoder-tenka1_2013_qualA_d]`](analysis/AtCoder-tenka1_2013_qualA_d.md) | D - 天下一展開 | 2507 | `Miscellaneous` | `Expression Parsing` | [`categories/miscellaneous/tenka1_expansion_ast_range_extraction.md`](categories/miscellaneous/tenka1_expansion_ast_range_extraction.md) |
| [`[problem:AtCoder-arc023_4]`](analysis/AtCoder-arc023_4.md) | D - GCD区間 | 2511 | `Number Theory` | `Euclidean Algorithm` | [`categories/number_theory/gcd_intervals_distinct_values_map.md`](categories/number_theory/gcd_intervals_distinct_values_map.md) |
| [`[problem:AtCoder-agc077_a]`](analysis/AtCoder-agc077_a.md) | A - Reverse A…B | 2512 | `Basics` | `Basic Constructive Algorithms` | [`categories/basics/reverse_a_b_constructive_three_phase_inversion.md`](categories/basics/reverse_a_b_constructive_three_phase_inversion.md) |
| [`[problem:AtCoder-code_festival_morning_hard_c]`](analysis/AtCoder-code_festival_morning_hard_c.md) | C - 宝探し 2 | 2521 | `Data Structures (DS)` | `2D BIT` | [`categories/data_structures_ds/treasure_hunt_2d_bit_multitype_grid.md`](categories/data_structures_ds/treasure_hunt_2d_bit_multitype_grid.md) |
| [`[problem:AtCoder-discovery_2016_qual_c]`](analysis/AtCoder-discovery_2016_qual_c.md) | C - アメージングな文字列は、きみが作る！ | 2527 | `Strings` | `Suffix Array` | [`categories/strings/amazing_string_suffix_array_prefix_greedy.md`](categories/strings/amazing_string_suffix_array_prefix_greedy.md) |
