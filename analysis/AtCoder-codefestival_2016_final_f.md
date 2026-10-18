# Problem Analysis: AtCoder-codefestival_2016_final_f — F - Road of the King

**Problem ID**: `AtCoder-codefestival_2016_final_f`  
**Contest**: `codefestival_2016_final`  
**Rating / Difficulty**: 2539  
**URL**: https://atcoder.jp/contests/codefestival_2016_final/tasks/codefestival_2016_final_f  
**VJudge Tag**: `[problem:AtCoder-codefestival_2016_final_f]`  
**Category File**: [`../categories/dynamic_programming_dp/road_of_the_king_scc_walk_dp.md`](../categories/dynamic_programming_dp/road_of_the_king_scc_walk_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Count directed walks of length $M$ starting and ending at vertex 1 that visit all $N$ vertices and form a strongly connected graph.

## 2. Core Observation & Invariant
Maintain the state of the walk $(c, p)$ where $c$ is the number of vertices in the strongly connected component containing vertex 1, and $p$ is the length of the simple path extending outward from $C$ currently being traversed. When an edge returns to $C$, all $p$ path vertices merge into $C$, increasing $c$ to $c + p$. When an edge visits an unvisited vertex, $p$ increments to $p + 1$. When an edge visits an already traversed path vertex, a sub-cycle merges into the path.

## 3. Step-by-Step Algorithm
1. 1. Initialize $DP[0][1][0] = 1$ (at step 0, component of size 1, path length 0).
2. 2. For each step $t = 0 \dots M - 1$, and each state $(c, p)$:
3.    - Transition A (visit new unvisited vertex): choose from $N - c - p$ vertices, transition to $(c, p + 1)$.
4.    - Transition B (return to component $C$): choose from $c$ vertices, merge path: transition to $(c + p, 0)$.
5.    - Transition C (cycle within path): choose from $p$ vertices, path shrinks / stays: transition to $(c + k, p - k)$.
6. 3. The answer is $DP[M][N][0]$ modulo $10^9+7$.

## 4. Complexity Analysis
- **Time Complexity**: `O(M \cdot N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    // dp[c][p]: c in SCC, p in pending path
    vector<vector<int>> dp(N + 1, vector<int>(N + 1, 0));
    dp[1][0] = 1;

    for (int day = 0; day < M; ++day) {
        vector<vector<int>> next_dp(N + 1, vector<int>(N + 1, 0));
        for (int c = 1; c <= N; ++c) {
            for (int p = 0; c + p <= N; ++p) {
                long long val = dp[c][p];
                if (!val) continue;

                int unvisited = N - c - p;
                // 1. Move to unvisited
                if (unvisited > 0) {
                    next_dp[c][p + 1] = (next_dp[c][p + 1] + val * unvisited) % MOD;
                }
                // 2. Move to C
                next_dp[c + p][0] = (next_dp[c + p][0] + val * c) % MOD;
                // 3. Move to pending path
                if (p > 0) {
                    next_dp[c][p] = (next_dp[c][p] + val * p) % MOD;
                }
            }
        }
        dp = move(next_dp);
    }

    cout << dp[N][0] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
