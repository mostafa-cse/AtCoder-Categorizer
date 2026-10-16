# AtCoder Quality Problems by Topic

A structured, topic-wise curriculum catalog of high-value AtCoder problems classified under the official Competitive Programming Curriculum.

### 3-Tier Taxonomy Structure:
1. **Tag** (Major Algorithmic Domain)
2. **Subtopic** (Conceptual Category)
3. **Topic / Skill** (Specific Algorithmic Technique)

---

# Basics

## Backtracking & Recursion

### Recursive Backtracking & Prefix Balance Invariant

- [problem:AtCoder-typical90_b] **Encyclopedia of Parentheses** (Rating: 800, ★3) — *Print all valid parentheses strings of length N in lexicographical order. N <= 16....*


## Binary Search

### Binary Search on Answer / Greedy Feasibility

- [problem:AtCoder-typical90_a] **Yokan Party** (Rating: 1200) — *Cut a stick of length L at K positions to maximize the minimum piece length.*

---

# Data Structures (DS)

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

## Impartial Games

### Sprague-Grundy / Combinatorial Game DP

- [problem:AtCoder-dp_k] **Stones** (Rating: 1100) — *Determine whether First or Second player wins an impartial subtract-a-stone game from pile of size K.*

---

# Graph Theory

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

## Angular Sweep / Polar Angles

### Polar Angle Sort + Binary Search for Opposite Vector

- [problem:AtCoder-typical90_i] **Three Point Angle** (Rating: 2100, ★6) — *Given N points in 2D plane (N <= 2000), choose three distinct points p_j, p_i, p_k to maximize the angle betwe...*

---


# Combinatorics

## Stars and Bars & Combinatorial Bounds

### Spacing Constraint Combinatorics + Harmonic Series O(N log N)

- [problem:AtCoder-typical90_o] **Don't be too close** (Rating: 2150, ★6) — *For each k from 1 to N, count non-empty subsets of {1, 2, ..., N} such that any two chosen elements have absol...*

---


# Math

## Search Space Invariants & Bounds

### Digit Product Value Compression & Inverse Search

- [problem:AtCoder-typical90_y] **Digit Product Equation** (Rating: 2400, ★7) — *Find the number of positive integers m <= N (N <= 10^11) satisfying m - f(m) = B, where f(m) is the product of...*

---


# Number Theory

## Prime Numbers & Sieve

### Modified Sieve of Eratosthenes / Prime Factor Multiplicity

- [problem:AtCoder-typical90_ad] **K Factors** (Rating: 1400, ★5) — *Count integers in the range [2, N] (N <= 10^7) that have at least K distinct prime factors....*

---
