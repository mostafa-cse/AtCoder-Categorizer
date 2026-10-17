# Problem Analysis: AtCoder-arc044_b — 最短路問題

**Problem ID**: `AtCoder-arc044_b`  
**Contest**: `arc044`  
**Rating / Difficulty**: 1744  
**URL**: https://atcoder.jp/contests/arc044/tasks/arc044_b  
**VJudge Tag**: `[problem:AtCoder-arc044_b]`  
**Category File**: [`../categories/combinatorics/layered_graph_counting_bfs_levels.md`](../categories/combinatorics/layered_graph_counting_bfs_levels.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Graph Counting`  
- **Topic (Skill)**: `Layered Graph Counting by BFS Distance Levels`  

---

## 1. Problem Statement & Key Idea
Given shortest path distances A_1, ..., A_N from vertex 1 to each vertex in a connected undirected graph. Count the number of valid graphs where the shortest path from vertex 1 to vertex i is exactly A_i, modulo 10^9 + 7.

**Key Insight**: The graph naturally decomposes into layers of nodes by distance d = A_i. For a node at layer d, it must have at least one edge to the nodes at layer d - 1, and can have any subset of edges to nodes in its own layer d.

## 2. Core Observation & Invariant
Let c[d] be the count of nodes at distance d. Valid conditions: A_1 == 0 and exactly one node has distance 0; distance levels must have no empty gaps. Number of ways: prod_{d=1}^{max_d} (2^{c[d-1]} - 1)^{c[d]} * 2^{C(c[d], 2)}.

## 3. Step-by-Step Algorithm
1. Check validity: A[0] must be 0, all other A[i] > 0, count[0] == 1.
2. Group nodes by distance: c[d] = count of nodes with A[i] = d.
3. If any intermediate level d in [1, max_d] has c[d] == 0, output 0.
4. ans = 1.
5. For d = 1 to max_d:
6.   ways_prev = (2^{c[d - 1]} - 1)^{c[d]} % MOD.
7.   ways_same = 2^{c[d] * (c[d] - 1) / 2} % MOD.
8.   ans = ans * ways_prev % MOD * ways_same % MOD.
9. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + max_d)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    int max_d = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_d = max(max_d, a[i]);
    }

    if (a[0] != 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> c(max_d + 1, 0);
    for (int i = 0; i < n; ++i) {
        c[a[i]]++;
    }

    if (c[0] != 1) {
        cout << 0 << "\n";
        return 0;
    }

    long long ans = 1;
    for (int d = 1; d <= max_d; ++d) {
        if (c[d] == 0) {
            cout << 0 << "\n";
            return 0;
        }

        long long ways_to_prev = (power(2, c[d - 1]) - 1 + MOD) % MOD;
        long long layer_edges = power(ways_to_prev, c[d]);

        long long same_pairs = c[d] * (c[d] - 1) / 2;
        long long same_layer_edges = power(2, same_pairs);

        ans = (ans * layer_edges) % MOD;
        ans = (ans * same_layer_edges) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting valid graph topologies partitioned by BFS distance level requirements.
- **Reusable Pattern**: `BFS Layered Graph Counting: (2^{c[d-1]} - 1)^{c[d]} * 2^{C(c[d], 2)}.`
