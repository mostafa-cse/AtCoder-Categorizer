# Problem Analysis: AtCoder-abc281_g — G. Farthest City

**Problem ID**: `AtCoder-abc281_g`  
**Contest**: `abc281`  
**Rating / Difficulty**: 2304  
**URL**: https://atcoder.jp/contests/abc281/tasks/abc281_g  
**VJudge Tag**: `[problem:AtCoder-abc281_g]`  
**Category File**: [`../categories/graph_theory/layered_bfs_dag_graph_counting.md`](../categories/graph_theory/layered_bfs_dag_graph_counting.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Counting`  
- **Topic (Skill)**: `Counting Labeled Graphs`  

---

## 1. Problem Statement & Key Idea
Count the number of connected undirected graphs with $N$ labeled vertices where vertex $N$ has strictly greater shortest path distance from vertex 1 than any other vertex, modulo $M$.

## 2. Core Observation & Invariant
The condition that vertex $N$ has strictly greater distance from vertex 1 than all other vertices implies $N$ is the unique vertex in the final layer $D$ of the BFS DAG.

## 3. Step-by-Step Algorithm
1. Define $dp[i][j]$ as the number of valid graph structures formed by placing $i$ intermediate vertices with the last layer containing $j$ vertices.
2. Transition by adding a new layer of $k$ vertices from the remaining unplaced labeled vertices: choose vertices with $\binom{N-1-i}{k}$, choose internal edges with $2^{k(k-1)/2}$, and connect each new vertex to at least one vertex in the previous layer with $(2^j - 1)^k$.
3. Finally, connect vertex $N$ to the last layer using $(2^j - 1)$ choices in $O(N^3)$ total time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long MOD;
    if (!(cin >> N >> MOD)) return 0;

    vector<vector<long long>> C(N + 1, vector<long long>(N + 1, 0));
    for (int i = 0; i <= N; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    vector<long long> p2(N * N + 1, 1);
    for (int i = 1; i <= N * N; ++i) {
        p2[i] = (p2[i - 1] * 2) % MOD;
    }

    auto power = [&](long long base, long long exp) -> long long {
        long long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    };

    vector<vector<long long>> dp(N + 1, vector<long long>(N + 1, 0));
    dp[1][1] = 1;

    for (int i = 1; i < N - 1; ++i) {
        for (int j = 1; j <= i; ++j) {
            if (dp[i][j] == 0) continue;

            for (int k = 1; i + k <= N - 1; ++k) {
                long long ways_choose = C[N - 1 - i][k];
                long long ways_internal = p2[k * (k - 1) / 2];
                long long p_base = (p2[j] - 1 + MOD) % MOD;
                long long ways_cross = power(p_base, k);

                long long total_ways = ways_choose * ways_internal % MOD * ways_cross % MOD;
                dp[i + k][k] = (dp[i + k][k] + dp[i][j] * total_ways) % MOD;
            }
        }
    }

    long long ans = 0;
    for (int j = 1; j <= N - 1; ++j) {
        if (dp[N - 1][j] == 0) continue;
        long long ways_cross = (p2[j] - 1 + MOD) % MOD;
        ans = (ans + dp[N - 1][j] * ways_cross) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
