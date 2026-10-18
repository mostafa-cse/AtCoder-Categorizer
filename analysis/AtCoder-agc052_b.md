# Problem Analysis: AtCoder-agc052_b — B. Tree Edges XOR

**Problem ID**: `AtCoder-agc052_b`  
**Contest**: `agc052`  
**Rating / Difficulty**: 2473  
**URL**: https://atcoder.jp/contests/agc052/tasks/agc052_b  
**VJudge Tag**: `[problem:AtCoder-agc052_b]`  
**Category File**: [`../categories/basics/tree_edges_xor_potentials_permutation.md`](../categories/basics/tree_edges_xor_potentials_permutation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitwise Thinking`  
- **Topic (Skill)**: `Bitwise Operations and Bitmasks`  

---

## 1. Problem Statement & Key Idea
Determine whether initial edge weights $w^1_i$ on a tree with $N$ vertices ($N$ odd) can be transformed to target weights $w^2_i$ by XORing incident edges of an edge $(u, v)$ with its weight $w$. Represent edge weights as differences of vertex potentials $w(u, v) = P_u \oplus P_v$. An operation on edge $(u, v)$ is identical to swapping potentials $P_u$ and $P_v$. Because the tree is connected, potentials can be permuted arbitrarily. Since $N$ is odd, the root potential shift $z$ is uniquely determined.

## 2. Core Observation & Invariant
Assigning potential $P_v = x \oplus dist^1_\oplus(1, v)$ preserves edge weights under vertex potential swaps. The multiset of potentials must match $\{y \oplus dist^2_\oplus(1, v)\}$. Summing potentials under XOR when $N$ is odd reveals $z = x \oplus y = (\bigoplus dist^1_v) \oplus (\bigoplus dist^2_v)$, eliminating all degrees of freedom.

## 3. Step-by-Step Algorithm
1. 1. Run DFS from vertex 1 on tree 1 to compute path XOR distances $d^1_v$ from root.
2. 2. Run DFS from vertex 1 on tree 2 to compute path XOR distances $d^2_v$ from root.
3. 3. Compute total XOR sums $X_1 = \bigoplus_{v=1}^N d^1_v$ and $X_2 = \bigoplus_{v=1}^N d^2_v$.
4. 4. Compute shift $z = X_1 \oplus X_2$.
5. 5. Transform tree 1 potentials: $d^1_v \leftarrow d^1_v \oplus z$.
6. 6. Sort both potential multisets. If they are identical, output 'YES', otherwise 'NO'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    long long w;
};

int n;
vector<vector<Edge>> adj1, adj2;
vector<long long> d1, d2;

void dfs1(int u, int p, long long cur) {
    d1[u] = cur;
    for (auto& edge : adj1[u]) {
        if (edge.to != p) {
            dfs1(edge.to, u, cur ^ edge.w);
        }
    }
}

void dfs2(int u, int p, long long cur) {
    d2[u] = cur;
    for (auto& edge : adj2[u]) {
        if (edge.to != p) {
            dfs2(edge.to, u, cur ^ edge.w);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n)) return 0;

    adj1.assign(n + 1, vector<Edge>());
    adj2.assign(n + 1, vector<Edge>());

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        long long w1, w2;
        cin >> u >> v >> w1 >> w2;
        adj1[u].push_back({v, w1});
        adj1[v].push_back({u, w1});
        adj2[u].push_back({v, w2});
        adj2[v].push_back({u, w2});
    }

    d1.assign(n + 1, 0);
    d2.assign(n + 1, 0);

    dfs1(1, 0, 0);
    dfs2(1, 0, 0);

    long long xor1 = 0, xor2 = 0;
    vector<long long> vals1(n), vals2(n);
    for (int i = 1; i <= n; ++i) {
        vals1[i - 1] = d1[i];
        vals2[i - 1] = d2[i];
        xor1 ^= d1[i];
        xor2 ^= d2[i];
    }

    long long z = xor1 ^ xor2;
    for (int i = 0; i < n; ++i) {
        vals1[i] ^= z;
    }

    sort(vals1.begin(), vals1.end());
    sort(vals2.begin(), vals2.end());

    if (vals1 == vals2) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
