# Problem Analysis: AtCoder-abc454_g — G. Mode in the Subtree

**Problem ID**: `AtCoder-abc454_g`  
**Contest**: `abc454`  
**Rating / Difficulty**: 2253  
**URL**: https://atcoder.jp/contests/abc454/tasks/abc454_g  
**VJudge Tag**: `[problem:AtCoder-abc454_g]`  
**Category File**: [`../categories/data_structures/dsu_on_tree_subtree_mode_high_performance.md`](../categories/data_structures/dsu_on_tree_subtree_mode_high_performance.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `DSU on Tree and Small to Large Merging`  

---

## 1. Problem Statement & Key Idea
Given a rooted tree of $N$ colored vertices ($N \le 2.5 \times 10^6$), for each vertex $v$, find the maximum frequency $m_v$ of any color in $v$'s subtree and the count $k_v$ of colors achieving that maximum frequency. Output $\sum (m_i \oplus i)(k_i \oplus i) \bmod 998244353$.

## 2. Core Observation & Invariant
With $N = 2.5 \times 10^6$, map-based small-to-large merging is too slow due to pointer and dynamic allocation overhead. DSU on Tree (Sack) using a single flat frequency array $cnt$ allows $O(N \log N)$ total time with tiny constant factor.
Crucially, during the heavy-light traversal, when processing light children with `keep = false`, the entire subtree is wiped back to zero, allowing mode tracking without maintaining reverse frequency buckets.

## 3. Step-by-Step Algorithm
1. Generate tree and colors from the linear congruential generator pseudocode.
2. Run initial DFS to compute subtree sizes, Euler tour in/out times, and identify heavy children.
3. Run DSU on Tree DFS: recurse on light children with `keep = false`, recurse on heavy child with `keep = true`, insert light children subtrees and current node into $cnt$, answer queries for current node, and clear subtree if `keep = false`.
4. Compute the final XOR-sum modulo 998244353 and output.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int N, M, F;
long long seed;
vector<int> p, c;
vector<vector<int>> adj;
vector<int> sz, heavy, tin, tout, order;
int timer_dfs = 0;

void dfs_sz(int u) {
    sz[u] = 1;
    heavy[u] = 0;
    int max_c = 0;
    tin[u] = timer_dfs;
    order[timer_dfs++] = u;
    for (int v : adj[u]) {
        dfs_sz(v);
        sz[u] += sz[v];
        if (sz[v] > max_c) {
            max_c = sz[v];
            heavy[u] = v;
        }
    }
    tout[u] = timer_dfs;
}

vector<int> cnt;
int max_freq = 0;
int num_max = 0;
vector<int> ans_m, ans_k;

inline void add(int u) {
    int col = c[u];
    cnt[col]++;
    if (cnt[col] > max_freq) {
        max_freq = cnt[col];
        num_max = 1;
    } else if (cnt[col] == max_freq) {
        num_max++;
    }
}

void dfs_dsu(int u, bool keep) {
    for (int v : adj[u]) {
        if (v != heavy[u]) {
            dfs_dsu(v, false);
        }
    }
    if (heavy[u] != 0) {
        dfs_dsu(heavy[u], true);
    }
    for (int v : adj[u]) {
        if (v != heavy[u]) {
            for (int i = tin[v]; i < tout[v]; ++i) {
                add(order[i]);
            }
        }
    }
    add(u);
    ans_m[u] = max_freq;
    ans_k[u] = num_max;

    if (!keep) {
        for (int i = tin[u]; i < tout[u]; ++i) {
            cnt[c[order[i]]]--;
        }
        max_freq = 0;
        num_max = 0;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> seed >> M >> F)) return 0;

    vector<int> q(M + 1), d(M + 1);
    for (int i = 2; i <= M; ++i) cin >> q[i];
    for (int i = 1; i <= M; ++i) cin >> d[i];

    p.resize(N + 1);
    c.resize(N + 1);

    long long state = seed;
    const long long MOD_STATE = 2147483648LL; // 2^31

    for (int i = 2; i <= N; ++i) {
        if (i <= M) {
            p[i] = q[i];
        } else {
            p[i] = (state % (i - 1)) + 1;
            state = (state * 1103515245LL + 12345LL) % MOD_STATE;
        }
    }

    for (int i = 1; i <= N; ++i) {
        if (i <= M) {
            c[i] = d[i];
        } else {
            c[i] = (state % F) + 1;
            state = (state * 1103515245LL + 12345LL) % MOD_STATE;
        }
    }

    adj.resize(N + 1);
    for (int i = 2; i <= N; ++i) {
        adj[p[i]].push_back(i);
    }

    sz.resize(N + 1);
    heavy.resize(N + 1);
    tin.resize(N + 1);
    tout.resize(N + 1);
    order.resize(N + 1);
    dfs_sz(1);

    cnt.assign(N + 1, 0);
    ans_m.resize(N + 1);
    ans_k.resize(N + 1);
    dfs_dsu(1, true);

    long long total_ans = 0;
    for (int i = 1; i <= N; ++i) {
        long long term1 = (ans_m[i] ^ i);
        long long term2 = (ans_k[i] ^ i);
        long long prod = (term1 % MOD) * (term2 % MOD) % MOD;
        total_ans = (total_ans + prod) % MOD;
    }

    cout << total_ans << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
