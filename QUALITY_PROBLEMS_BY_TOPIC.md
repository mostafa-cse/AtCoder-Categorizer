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
