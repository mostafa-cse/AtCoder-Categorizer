# Problem Analysis: AtCoder-abc201_e — Xor Distances

**Problem ID**: `AtCoder-abc201_e`  
**Contest**: `abc201`  
**Rating / Difficulty**: 1694  
**URL**: https://atcoder.jp/contests/abc201/tasks/abc201_e  
**VJudge Tag**: `[problem:AtCoder-abc201_e]`  
**Category File**: [`../categories/graph_theory/tree_xor_distances_bit_counting.md`](../categories/graph_theory/tree_xor_distances_bit_counting.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Tree XOR Distances Bit-by-Bit Counting via Root DFS`  

---

## 1. Problem Statement & Key Idea
Given a weighted tree with N vertices. The XOR distance between u and v is the XOR sum of edge weights on the simple path between them. Find the sum of XOR distances over all pairs 1 <= u < v <= N, modulo 10^9 + 7.

**Key Insight**: In any tree, the path from u to v can be routed through an arbitrary root (e.g. 1): dist(u, v) = dist(root, u) ^ dist(root, v), because edges on the common path to the LCA cancel out!

## 2. Core Observation & Invariant
Compute d[u] = dist(1, u) for all vertices using DFS. For each bit b from 0 to 59: count vertices with the b-th bit set (cnt1) and unset (cnt0). The b-th bit is set in dist(u, v) iff one endpoint has bit 1 and the other has bit 0: cnt1 * cnt0 pairs! Total sum = sum_{b=0}^{59} 2^b * cnt1 * cnt0 modulo 10^9 + 7.

## 3. Step-by-Step Algorithm
1. Root tree at 1 and compute d[u] = XOR distance from root 1 via DFS in O(N).
2. ans = 0.
3. For bit b from 0 to 59:
4.   cnt1 = count of u where (d[u] >> b) & 1.
5.   cnt0 = N - cnt1.
6.   pairs = (1LL * cnt1 * cnt0) % MOD.
7.   weight = (1LL << b) % MOD.
8.   ans = (ans + pairs * weight) % MOD.
9. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(60 * N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

struct Edge {
    int to;
    long long w;
};

vector<vector<Edge>> adj;
vector<long long> xor_dist;

void dfs(int u, int p, long long d) {
    xor_dist[u] = d;
    for (const auto& e : adj[u]) {
        if (e.to != p) {
            dfs(e.to, u, d ^ e.w);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    adj.resize(n + 1);
    xor_dist.resize(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    dfs(1, 0, 0);

    long long ans = 0;

    for (int b = 0; b < 60; ++b) {
        long long cnt1 = 0;
        for (int i = 1; i <= n; ++i) {
            if ((xor_dist[i] >> b) & 1) {
                cnt1++;
            }
        }
        long long cnt0 = n - cnt1;
        long long pairs = (cnt1 * cnt0) % MOD;
        long long bit_val = ((1LL << b) % MOD);
        ans = (ans + pairs * bit_val) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitwise independence and XOR path cancellation via root projection on trees.
- **Reusable Pattern**: `Tree Path XOR: dist(u, v) = d[u] ^ d[v]; count bit contributions independently.`
