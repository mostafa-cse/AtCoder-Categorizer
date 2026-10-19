# Problem Analysis: AtCoder-abc351_g — G. Hash on Tree

**Problem ID**: `AtCoder-abc351_g`  
**Contest**: `abc351`  
**Rating / Difficulty**: 2920  
**URL**: https://atcoder.jp/contests/abc351/tasks/abc351_g  
**VJudge Tag**: `[problem:AtCoder-abc351_g]`  
**Category File**: [`../categories/data_structures/affine_tree_hash_dynamic_dp_hld.md`](../categories/data_structures/affine_tree_hash_dynamic_dp_hld.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Heavy Light Decomposition (HLD)`  
- **Topic (Skill)**: `Heavy Light Decomposition (HLD) ft Subtrees and Path Query`  

---

## 1. Problem Statement & Key Idea
Given a rooted tree with values A_v where each node's hash is recursively defined as an affine function of its children's hashes, process point value updates and query the root hash H(1).

## 2. Core Observation & Invariant
Each node's hash transition is an affine transformation x -> m * x + c of its heavy child's hash, with multiplier m given by the product of light children's hashes. Under Heavy-Light Decomposition (HLD), each heavy path is a sequence of affine functions whose composition is associative. A Segment Tree over each heavy chain maintains the composed affine transformation. Point updates modify a leaf and propagate up light edges in O(log^2 N) time.

## 3. Step-by-Step Algorithm
1. 1. Run DFS to compute tree sizes, heavy edges, and decompose into heavy chains.
2. 2. For each node, maintain product of light children hashes.
3. 3. Build Segment Trees over each heavy chain storing composed affine maps (a, b).
4. 4. When updating A_v: update v in its chain Segment Tree, query the new chain head hash, update the parent's light child product, and ascend to the root.
5. 5. Query the root hash directly from the top chain's Segment Tree.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

const int MAXN = 200005;
int P[MAXN];
long long A[MAXN];
vector<int> adj[MAXN];
int sz[MAXN], heavy[MAXN], head[MAXN], tail[MAXN], pos_in_tree[MAXN];
vector<int> order;

long long f_val[MAXN];
int zero_cnt[MAXN];
long long prod_nonzero[MAXN];

int tree_sz;
long long tree_a[1 << 19];
long long tree_b[1 << 19];

inline void combine(int node) {
    int l = 2 * node, r = 2 * node + 1;
    tree_a[node] = (tree_a[l] * tree_a[r]) % MOD;
    tree_b[node] = (tree_a[l] * tree_b[r] + tree_b[l]) % MOD;
}

long long get_light_prod(int u) {
    if (adj[u].empty()) return 0;
    if (zero_cnt[u] > 0) return 0;
    return prod_nonzero[u];
}

void set_leaf(int u) {
    int idx = tree_sz + pos_in_tree[u];
    tree_a[idx] = get_light_prod(u);
    tree_b[idx] = A[u];
    idx >>= 1;
    while (idx >= 1) {
        combine(idx);
        idx >>= 1;
    }
}

long long query_head(int h) {
    int L = tree_sz + pos_in_tree[h];
    int R = tree_sz + pos_in_tree[tail[h]];
    static int left_nodes[64], right_nodes[64];
    int ln = 0, rn = 0;

    while (L <= R) {
        if (L & 1) left_nodes[ln++] = L++;
        if (!(R & 1)) right_nodes[rn++] = R--;
        L >>= 1;
        R >>= 1;
    }

    long long cur_a = 1, cur_b = 0;
    for (int i = 0; i < ln; ++i) {
        int node = left_nodes[i];
        cur_b = (cur_a * tree_b[node] + cur_b) % MOD;
        cur_a = (cur_a * tree_a[node]) % MOD;
    }
    for (int i = rn - 1; i >= 0; --i) {
        int node = right_nodes[i];
        cur_b = (cur_a * tree_b[node] + cur_b) % MOD;
        cur_a = (cur_a * tree_a[node]) % MOD;
    }
    return cur_b;
}

void update_light(int p, long long old_val, long long new_val) {
    if (old_val == 0) {
        zero_cnt[p]--;
    } else {
        long long inv = modInverse(old_val);
        prod_nonzero[p] = (prod_nonzero[p] * inv) % MOD;
    }

    if (new_val == 0) {
        zero_cnt[p]++;
    } else {
        prod_nonzero[p] = (prod_nonzero[p] * new_val) % MOD;
    }
}

void dfs_hld(int u, int h) {
    head[u] = h;
    pos_in_tree[u] = order.size();
    order.push_back(u);
    if (heavy[u] != 0) {
        dfs_hld(heavy[u], h);
    }
    for (int v : adj[u]) {
        if (v != heavy[u]) {
            dfs_hld(v, v);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    if (!(cin >> N >> Q)) return 0;

    for (int i = 2; i <= N; ++i) {
        cin >> P[i];
        adj[P[i]].push_back(i);
    }
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }

    for (int u = N; u >= 1; --u) {
        sz[u] = 1;
        for (int v : adj[u]) {
            sz[u] += sz[v];
            if (heavy[u] == 0 || sz[v] > sz[heavy[u]]) {
                heavy[u] = v;
            }
        }
    }

    dfs_hld(1, 1);

    for (int u = 1; u <= N; ++u) {
        prod_nonzero[u] = 1;
        zero_cnt[u] = 0;
    }

    for (int u = N; u >= 1; --u) {
        if (adj[u].empty()) {
            f_val[u] = A[u];
        } else {
            long long cur_prod = 1;
            for (int v : adj[u]) {
                cur_prod = (cur_prod * f_val[v]) % MOD;
                if (v != heavy[u]) {
                    if (f_val[v] == 0) zero_cnt[u]++;
                    else prod_nonzero[u] = (prod_nonzero[u] * f_val[v]) % MOD;
                }
            }
            f_val[u] = (A[u] + cur_prod) % MOD;
        }
    }

    for (int u = 1; u <= N; ++u) {
        int curr = u;
        while (heavy[curr] != 0) curr = heavy[curr];
        tail[head[u]] = curr;
    }

    tree_sz = 1;
    while (tree_sz < N) tree_sz <<= 1;
    for (int i = 0; i < 2 * tree_sz; ++i) {
        tree_a[i] = 1;
        tree_b[i] = 0;
    }

    for (int u = 1; u <= N; ++u) {
        int idx = tree_sz + pos_in_tree[u];
        tree_a[idx] = get_light_prod(u);
        tree_b[idx] = A[u];
    }
    for (int idx = tree_sz - 1; idx >= 1; --idx) {
        combine(idx);
    }

    while (Q--) {
        int v;
        long long x;
        cin >> v >> x;
        A[v] = x;

        int curr = v;
        while (curr != 0) {
            int h = head[curr];
            int p = (h > 1 ? P[h] : 0);
            long long old_fh = query_head(h);
            set_leaf(curr);
            long long new_fh = query_head(h);
            if (p != 0) {
                update_light(p, old_fh, new_fh);
                set_leaf(p);
            }
            curr = p;
        }

        cout << query_head(1) << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
