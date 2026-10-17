# Problem Analysis: AtCoder-abc451_g — Minimum XOR Walk

**Problem ID**: `AtCoder-abc451_g`  
**Contest**: `abc451`  
**Rating / Difficulty**: 2221  
**URL**: https://atcoder.jp/contests/abc451/tasks/abc451_g  
**VJudge Tag**: `[problem:AtCoder-abc451_g]`  
**Category File**: [`../categories/math/minimum_xor_walk_rref_basis_trie.md`](../categories/math/minimum_xor_walk_rref_basis_trie.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `[Technique] XOR Basis ft Reduced Row Echelon Form`  

---

## 1. Problem Statement & Key Idea
Given connected undirected graph with edge weights W_i < 2^30, count pairs of vertices (x, y) (x < y) whose minimum XOR walk weight is <= K.

## 2. Core Observation & Invariant
Any walk XOR between x and y equals (D[x] ^ D[y]) ^ c where D[v] is spanning tree path XOR and c is in the linear span of fundamental cycles. Putting the cycle XOR basis into Reduced Row Echelon Form (RREF) allows projecting each D[v] into a canonical representative D~[v] where all pivot bits are cleared. The minimum walk XOR between x and y is identically D~[x] ^ D~[y], allowing pair counting via a 0-1 Trie.

## 3. Step-by-Step Algorithm
1. 1. Construct a spanning tree via BFS, computing XOR distances D[v] from root.
2. 2. For each non-tree edge (u, v, w), insert cycle XOR D[u] ^ D[v] ^ w into an XOR linear basis.
3. 3. Transform the basis into Reduced Row Echelon Form (RREF).
4. 4. Reduce each vertex distance D[v] against the RREF basis to produce canonical D~[v].
5. 5. Use a 0-1 Trie to count pairs with D~[x] ^ D~[y] <= K in O(N log(max W)) time.

## 4. Complexity Analysis
- **Time Complexity**: `O(M + N log(max W))`
- **Space Complexity**: `O(N log(max W) + M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

// 0-1 Trie node
struct TrieNode {
    int next[2];
    int count;
    TrieNode() {
        next[0] = next[1] = -1;
        count = 0;
    }
};

struct Trie {
    vector<TrieNode> nodes;
    Trie() {
        nodes.emplace_back();
    }

    void insert(unsigned int val) {
        int u = 0;
        nodes[u].count++;
        for (int b = 29; b >= 0; b--) {
            int bit = (val >> b) & 1;
            if (nodes[u].next[bit] == -1) {
                nodes[u].next[bit] = nodes.size();
                nodes.emplace_back();
            }
            u = nodes[u].next[bit];
            nodes[u].count++;
        }
    }

    // count how many elements x in trie satisfy (x ^ val) <= K
    long long count_le(unsigned int val, unsigned int K) {
        int u = 0;
        long long res = 0;
        for (int b = 29; b >= 0; b--) {
            if (u == -1) break;
            int bit_v = (val >> b) & 1;
            int bit_k = (K >> b) & 1;

            if (bit_k == 1) {
                // If we match bit_v, the XOR bit is 0 < 1, so all elements in this subtree are strictly < K
                int child0 = nodes[u].next[bit_v];
                if (child0 != -1) {
                    res += nodes[child0].count;
                }
                // Then follow the branch that gives XOR bit 1 == bit_k
                u = nodes[u].next[bit_v ^ 1];
            } else {
                // bit_k == 0, so XOR bit MUST be 0, which means we must follow bit_v
                u = nodes[u].next[bit_v];
            }
        }
        if (u != -1) {
            // value exactly equals K
            res += nodes[u].count;
        }
        return res;
    }
};

struct Basis {
    unsigned int basis[30];
    Basis() {
        memset(basis, 0, sizeof(basis));
    }

    void insert(unsigned int val) {
        for (int b = 29; b >= 0; b--) {
            if ((val >> b) & 1) {
                if (!basis[b]) {
                    basis[b] = val;
                    return;
                }
                val ^= basis[b];
            }
        }
    }

    void make_rref() {
        for (int b = 0; b < 30; b++) {
            if (basis[b]) {
                for (int higher = b + 1; higher < 30; higher++) {
                    if ((basis[higher] >> b) & 1) {
                        basis[higher] ^= basis[b];
                    }
                }
            }
        }
    }

    unsigned int reduce(unsigned int val) {
        for (int b = 29; b >= 0; b--) {
            if (basis[b] && ((val >> b) & 1)) {
                val ^= basis[b];
            }
        }
        return val;
    }
};

void solve() {
    int n, m;
    unsigned int K;
    if (!(cin >> n >> m >> K)) return;

    struct Edge {
        int to;
        unsigned int w;
        int id;
    };
    vector<vector<Edge>> adj(n);
    vector<pair<pair<int, int>, unsigned int>> all_edges(m);
    for (int i = 0; i < m; i++) {
        int u, v;
        unsigned int w;
        cin >> u >> v >> w;
        u--; v--;
        adj[u].push_back({v, w, i});
        adj[v].push_back({u, w, i});
        all_edges[i] = {{u, v}, w};
    }

    // Spanning tree via BFS
    vector<unsigned int> D(n, 0);
    vector<bool> vis(n, false);
    vector<bool> is_tree_edge(m, false);

    queue<int> q;
    q.push(0);
    vis[0] = true;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (auto& e : adj[u]) {
            if (!vis[e.to]) {
                vis[e.to] = true;
                is_tree_edge[e.id] = true;
                D[e.to] = D[u] ^ e.w;
                q.push(e.to);
            }
        }
    }

    // Insert all fundamental cycles into Basis
    Basis basis;
    for (int i = 0; i < m; i++) {
        if (!is_tree_edge[i]) {
            int u = all_edges[i].first.first;
            int v = all_edges[i].first.second;
            unsigned int w = all_edges[i].second;
            unsigned int cycle_xor = D[u] ^ D[v] ^ w;
            basis.insert(cycle_xor);
        }
    }

    basis.make_rref();

    vector<unsigned int> reduced_D(n);
    for (int i = 0; i < n; i++) {
        reduced_D[i] = basis.reduce(D[i]);
    }

    Trie trie;
    long long total_pairs = 0;
    for (int i = 0; i < n; i++) {
        total_pairs += trie.count_le(reduced_D[i], K);
        trie.insert(reduced_D[i]);
    }

    cout << total_pairs << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
