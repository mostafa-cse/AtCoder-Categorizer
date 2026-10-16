# Problem Analysis: AtCoder-abc073_d — joisino's travel

**Problem ID**: `AtCoder-abc073_d`  
**Contest**: `abc073`  
**Rating / Difficulty**: 1345  
**URL**: https://atcoder.jp/contests/abc073/tasks/abc073_d  
**VJudge Tag**: `[problem:AtCoder-abc073_d]`  
**Category File**: [`../categories/graph_theory/floyd_warshall_permutation_subsets.md`](../categories/graph_theory/floyd_warshall_permutation_subsets.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `All-Pairs Shortest Paths`  
- **Topic (Skill)**: `Floyd-Warshall + Permutation Search on Target Subsets`  

---

## 1. Problem Statement & Key Idea
An undirected weighted graph with N towns and M roads. Joisino must visit R specific towns r_1, ..., r_R (R <= 8) in any order. Find the minimum total distance traveled.

**Key Idea**: Precompute all-pairs shortest paths using Floyd-Warshall in O(N^3). Then test all R! permutations of visiting the R specified towns.

## 2. Core Observation & Invariant
Because R <= 8, R! <= 8! = 40,320 permutations. For each permutation p of {r_1, ..., r_R}, the travel cost is sum_{i=0}^{R-2} dist[p[i]][p[i+1]]. The minimum over all R! permutations is the exact answer.

## 3. Step-by-Step Algorithm
1. Compute all-pairs shortest paths dist[u][v] using Floyd-Warshall in O(N^3).
2. Sort the array r of target towns.
3. Initialize min_dist = INF.
4. Iterate through all permutations of r using std::next_permutation:
5.   cost = sum_{i=0}^{R-2} dist[r[i]][r[i+1]]; min_dist = min(min_dist, cost).
6. Print min_dist.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 + R! * R)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

const long long INF = 1e15;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, R;
    if (!(cin >> n >> m >> R)) return 0;

    vector<int> r(R);
    for (int i = 0; i < R; ++i) {
        cin >> r[i];
    }

    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        dist[u][v] = min(dist[u][v], c);
        dist[v][u] = min(dist[v][u], c);
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    sort(r.begin(), r.end());
    long long ans = INF;

    do {
        long long cur = 0;
        for (int i = 0; i < R - 1; ++i) {
            cur += dist[r[i]][r[i + 1]];
        }
        ans = min(ans, cur);
    } while (next_permutation(r.begin(), r.end()));

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: All-pairs shortest path precomputation combined with small subset factorial order optimization.
- **Reusable Pattern**: `Visit subset of R nodes in any order: Floyd-Warshall + next_permutation(targets).`
