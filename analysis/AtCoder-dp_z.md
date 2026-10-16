# Problem Analysis: AtCoder-dp_z — Frog 3

**Problem ID**: `AtCoder-dp_z`  
**Contest**: `dp`  
**Rating**: 2200  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_z  
**VJudge Tag**: `[problem:AtCoder-dp_z]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Convex Hull Trick (CHT)`  
- **Topic (Skill)**: `Convex Hull Trick (CHT) and Dynamic CHT`  

---

## 1. Problem Statement & Key Idea
Jump between stones with quadratic cost (h_j - h_i)^2 + C where heights h_i are strictly increasing.

## 2. Core Observation & Invariant
Expanding (h_j - h_i)^2 + C gives h_j^2 + C + (h_i^2 + dp[i]) - 2 * h_j * h_i. This is a family of lines y = m_i * x + b_i where slope m_i = -2 * h_i is strictly decreasing. Slopes and query points x = h_j are both monotonic, allowing O(1) amortized deque maintenance.

## 3. Step-by-Step Algorithm
1. Maintain deque of lines forming the lower convex hull.
2. For stone j: pop lines from front while line[0].eval(h_j) >= line[1].eval(h_j).
3. dp[j] = best_line.eval(h_j) + h_j^2 + C.
4. Add new line (slope = -2*h_j, intercept = h_j^2 + dp[j]) to back, popping lines that violate convexity.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Editorial Comparison & Alignment
Canonical Convex Hull Trick with monotonic slopes and monotonic queries.

## 6. What This Problem Teaches
Geometric line lower envelope maintenance, convex hull deque operations, and linearizing quadratic DP costs.

## 7. Reusable Competitive Programming Pattern
`Monotonic Convex Hull Trick (CHT).`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)