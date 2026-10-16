# Problem Analysis: AtCoder-abc002_4 — Faction

**Problem ID**: `AtCoder-abc002_4`  
**Contest**: `abc002`  
**Rating / Difficulty**: 1418  
**URL**: https://atcoder.jp/contests/abc002/tasks/abc002_4  
**VJudge Tag**: `[problem:AtCoder-abc002_4]`  
**Category File**: [`../categories/basics/bitmask_maximum_clique.md`](../categories/basics/bitmask_maximum_clique.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Exhaustive Search`  
- **Topic (Skill)**: `Maximum Clique via Bitmask Verification`  

---

## 1. Problem Statement & Key Idea
Given N politicians (N <= 12) and M bilateral friendship relations. Find the maximum size of a faction such that every member in the faction knows every other member in the faction.

**Key Insight**: Since N <= 12 is very small, enumerate all 2^N subsets of politicians using bitmasks and verify pairwise mutual acquaintance in O(N^2).

## 2. Core Observation & Invariant
A faction is precisely a clique in the friendship graph. For N <= 12, 2^12 = 4096 subsets. Checking if a subset is a clique takes O(popcount^2) <= 144 operations. Total operations <= 6 * 10^5, running in under 5ms.

## 3. Step-by-Step Algorithm
1. Store friendships in an adjacency matrix adj[N][N].
2. Initialize max_size = 1.
3. Iterate mask from 1 to (1 << N) - 1:
4.   Check if all pairs (i, j) with bit i and bit j set in mask have adj[i][j] == true.
5.   If valid clique, update max_size = max(max_size, popcount(mask)).
6. Print max_size.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^N * N^2)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<bool>> adj(n, vector<bool>(n, false));
    for (int i = 0; i < n; ++i) adj[i][i] = true;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u][v] = adj[v][u] = true;
    }

    int max_clique = 1;
    int total_masks = 1 << n;

    for (int mask = 1; mask < total_masks; ++mask) {
        int size = __builtin_popcount(mask);
        if (size <= max_clique) continue;

        bool is_clique = true;
        for (int i = 0; i < n; ++i) {
            if (!(mask & (1 << i))) continue;
            for (int j = i + 1; j < n; ++j) {
                if (!(mask & (1 << j))) continue;
                if (!adj[i][j]) {
                    is_clique = false;
                    break;
                }
            }
            if (!is_clique) break;
        }

        if (is_clique) {
            max_clique = size;
        }
    }

    cout << max_clique << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitmask subset enumeration and clique validation on small graphs.
- **Reusable Pattern**: `Maximum Clique on N <= 16: iterate bitmasks 1..(1<<N)-1 and verify all pairs in subset.`
