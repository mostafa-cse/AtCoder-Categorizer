# Problem Analysis: AtCoder-abc210_e — Ring MST

**Problem ID**: `AtCoder-abc210_e`  
**Contest**: `abc210`  
**Rating / Difficulty**: 1618  
**URL**: https://atcoder.jp/contests/abc210/tasks/abc210_e  
**VJudge Tag**: `[problem:AtCoder-abc210_e]`  
**Category File**: [`../categories/graph_theory/ring_mst_gcd_reduction.md`](../categories/graph_theory/ring_mst_gcd_reduction.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Minimum Spanning Tree`  
- **Topic (Skill)**: `Kruskal MST on Ring via Modular GCD Component Reduction`  

---

## 1. Problem Statement & Key Idea
A graph with N vertices on a ring. M operations: operation j connects all pairs (i, (i + A_j) % N) with edge cost C_j. Find the minimum cost to make the graph connected, or -1 if impossible.

**Key Insight**: Kruskal's greedy paradigm! Sort operations by cost C_j ascending. Adding ring edges of step A_j reduces the number of connected components from current g to gcd(g, A_j).

## 2. Core Observation & Invariant
Each operation reduces the number of components from g to g' = gcd(g, A_j), adding exactly g - g' edges at cost C_j. If the final component count is 1, the total accumulated cost is minimal. If final count > 1, the graph cannot be connected.

## 3. Step-by-Step Algorithm
1. Sort operations by cost C_j in ascending order.
2. Initialize current components g = N, total_cost = 0.
3. For each operation (A_j, C_j):
4.   g_next = gcd(g, A_j).
5.   If g_next < g:
6.     total_cost += 1LL * (g - g_next) * C_j.
7.     g = g_next.
8. If g == 1 print total_cost; else print -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long gcd_ll(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

struct Op {
    long long a, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int m;
    if (!(cin >> n >> m)) return 0;

    vector<Op> ops(m);
    for (int i = 0; i < m; ++i) {
        cin >> ops[i].a >> ops[i].c;
    }

    sort(ops.begin(), ops.end(), [](const Op& x, const Op& y) {
        return x.c < y.c;
    });

    long long g = n;
    long long total_cost = 0;

    for (const auto& op : ops) {
        long long g_next = gcd_ll(g, op.a);
        if (g_next < g) {
            total_cost += (g - g_next) * op.c;
            g = g_next;
        }
    }

    if (g == 1) {
        cout << total_cost << "\n";
    } else {
        cout << -1 << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Algebraic component reduction using Bezout's identity / GCD in Kruskal's algorithm.
- **Reusable Pattern**: `Ring Cycle MST: sort by cost, reduce components via g = gcd(g, A), add (g - g')*C.`
