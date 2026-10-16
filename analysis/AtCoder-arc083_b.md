# Problem Analysis: AtCoder-arc083_b — Restoring Road Network

**Problem ID**: `AtCoder-arc083_b`  
**Contest**: `abc074`  
**Rating / Difficulty**: 1563  
**URL**: https://atcoder.jp/contests/abc074/tasks/arc083_b  
**VJudge Tag**: `[problem:AtCoder-arc083_b]`  
**Category File**: [`../categories/graph_theory/reverse_floyd_warshall_edge_minimality.md`](../categories/graph_theory/reverse_floyd_warshall_edge_minimality.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `All-Pairs Shortest Paths`  
- **Topic (Skill)**: `Reverse Floyd-Warshall Strict Triangle Inequality Edge Minimality`  

---

## 1. Problem Statement & Key Idea
Given an N x N matrix A of all-pairs shortest path distances. Verify whether a valid graph exists whose shortest path matrix equals A. If yes, output the minimum total weight of edges.

**Key Insight**: Reverse Floyd-Warshall! If A[i][j] > A[i][k] + A[k][j] for any k, the triangle inequality is violated (output -1). If A[i][j] == A[i][k] + A[k][j] for some k != i, j, edge (i, j) is redundant and can be omitted. Otherwise, edge (i, j) is strictly required.

## 2. Core Observation & Invariant
Any edge (i, j) whose weight equals the sum of two other paths can be safely removed without altering any shortest path. Edges that strictly cannot be bypassed must be kept, and their sum is the minimum possible total weight.

## 3. Step-by-Step Algorithm
1. For all triples (i, j, k) with k != i and k != j:
2.   If A[i][j] > A[i][k] + A[k][j], return -1.
3. Initialize total_weight = 0.
4. For each pair (i, j) with i < j:
5.   necessary = true.
6.   For each k != i, j:
7.     If A[i][j] == A[i][k] + A[k][j]: necessary = false, break.
8.   If necessary: total_weight += A[i][j].
9. Print total_weight.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> A(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> A[i][j];
        }
    }

    // Check triangle inequality
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (A[i][j] > A[i][k] + A[k][j]) {
                    cout << -1 << "\n";
                    return 0;
                }
            }
        }
    }

    long long total_weight = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            bool redundant = false;
            for (int k = 0; k < n; ++k) {
                if (k != i && k != j) {
                    if (A[i][j] == A[i][k] + A[k][j]) {
                        redundant = true;
                        break;
                    }
                }
            }
            if (!redundant) {
                total_weight += A[i][j];
            }
        }
    }

    cout << total_weight << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Reverse triangle inequality verification and minimal transitively irreducible subgraph extraction.
- **Reusable Pattern**: `Shortest Path Matrix Reducibility: check strict triangle violation, omit edges with equality bypass.`
