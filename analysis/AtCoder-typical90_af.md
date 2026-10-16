# Problem Analysis: AtCoder-typical90_af — AtCoder Ekiden

**Problem ID**: `AtCoder-typical90_af`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 032)  
**Rating / Difficulty**: 850 (★3)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_af  
**VJudge Tag**: `[problem:AtCoder-typical90_af]`  
**Category File**: [`../categories/basics/permutation_enumeration.md`](../categories/basics/permutation_enumeration.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Permutations & Brute Force`  
- **Topic (Skill)**: `Permutation Enumeration with Adjacency Graph Pruning`  

---

## 1. Problem Statement & Key Idea
N runners (N <= 10) run N sections. Runner i takes A_{i, j} time for section j. M pairs of runners (X_k, Y_k) cannot pass the sash directly to each other. Find minimum total time, or -1 if impossible.

**Core Idea**: With N <= 10, total permutations of runner ordering is N! <= 3,628,800. Enumerate all permutations and validate adjacency.

## 2. Core Observation & Invariant
Store forbidden handoffs in a 2D boolean adjacency matrix bad[u][v]. Check bad[p_k][p_{k+1}] in O(1) during permutation traversal.

## 3. Step-by-Step Algorithm
1. Initialize p = {0, 1, ..., N - 1}.
2. bad[X_k][Y_k] = bad[Y_k][X_k] = true.
3. Loop permutations with std::next_permutation:
   - Check if any adjacent pair has bad[p_k][p_{k+1}] == true.
   - If valid, sum A[p_k][k] and update minimum total time.
4. Output min time or -1.

## 4. Complexity Analysis
Time: O(N! * N), Space: O(N^2).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> a[i][j];
    }

    int m;
    cin >> m;
    vector<vector<bool>> bad(n, vector<bool>(n, false));
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        bad[u][v] = bad[v][u] = true;
    }

    vector<int> p(n);
    iota(p.begin(), p.end(), 0);

    int min_time = INF;

    do {
        bool ok = true;
        for (int i = 0; i < n - 1; ++i) {
            if (bad[p[i]][p[i + 1]]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            int cur_time = 0;
            for (int i = 0; i < n; ++i) {
                cur_time += a[p[i]][i];
            }
            min_time = min(min_time, cur_time);
        }
    } while (next_permutation(p.begin(), p.end()));

    if (min_time == INF) cout << -1 << "\n";
    else cout << min_time << "\n";

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Full permutation traversal with O(1) graph adjacency verification.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Permutation generation with std::next_permutation and Hamiltonian path filtering on small graphs.
- **Reusable Pattern**: `Permutation Generation with Adjacency Graph Validation.`

---
Back to [Permutation Enumeration with Adjacency Graph Pruning](../categories/basics/permutation_enumeration.md) | [Categories Directory](../categories/README.md)