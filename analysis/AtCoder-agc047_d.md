# Problem Analysis: AtCoder-agc047_d — D. Twin Binary Trees

**Problem ID**: `AtCoder-agc047_d`  
**Contest**: `agc047`  
**Rating / Difficulty**: 2910  
**URL**: https://atcoder.jp/contests/agc047/tasks/agc047_d  
**VJudge Tag**: `[problem:AtCoder-agc047_d]`  
**Category File**: [`../categories/graph_theory/twin_binary_tree_dual_lca_cycle_convolution.md`](../categories/graph_theory/twin_binary_tree_dual_lca_cycle_convolution.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Lowest Common Ancestor (LCA)`  
- **Topic (Skill)**: `Binary Lifting and LCA`  

---

## 1. Problem Statement & Key Idea
Two perfect binary trees of depth H share the same 2^{H-1} leaves via a leaf permutation P. Compute the sum of weights over all pairs of leaves (u, v), where weight depends on the depths of LCA_1(u, v) and LCA_2(P(u), P(v)).

## 2. Core Observation & Invariant
Iterate over each internal node a in T_1. The node a is the LCA in T_1 for all pairs (u, v) where u is in the left subtree L(a) and v is in the right subtree R(a). For a fixed a, LCA_1 is constant. For each u in L(a), trace up T_2 from P(u) to the root, adding path weights to ancestor counters. Then for each v in R(a), trace up T_2 from P(v), accumulating contributions where the meeting node in T_2 is the exact LCA_2. Clearing the table keeps the total complexity proportional to subtree sizes.

## 3. Step-by-Step Algorithm
1. 1. Iterate over every internal node a in T_1.
2. 2. For each leaf u in L(a), traverse the H ancestors of P(u) in T_2, adding path multipliers to an ancestor weight table.
3. 3. For each leaf v in R(a), traverse the H ancestors of P(v) in T_2; at each ancestor anc, multiply by (H - depth(a)) * (H - depth(anc)) * product of path weights, and accumulate.
4. 4. Clear the ancestor table for all u in L(a).
5. 5. Sum contributions across all internal nodes modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(H^2 * 2^H) = O(N log^2 N)`
- **Space Complexity**: `O(2^H)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 1000000007;

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

const int MAX_NODES = (1 << 19);
long long up_prod[MAX_NODES];
long long G[MAX_NODES];
long long tree2_sum[MAX_NODES];
int P[MAX_NODES];
int H, L;
long long ans = 0;
vector<int> modified_nodes;

void rec(int u, int l, int r) {
    if (r - l <= 1) return;
    int mid = (l + r) / 2;
    rec(2 * u, l, mid);
    rec(2 * u + 1, mid, r);

    modified_nodes.clear();
    for (int i = l; i < mid; ++i) {
        int curr = L + i;
        long long w1 = 1;
        while (curr != u) {
            w1 = (w1 * curr) % MOD;
            curr /= 2;
        }

        int leaf2 = L + P[i] - 1;
        long long f_val = up_prod[leaf2];
        long long X_a = (w1 * f_val) % MOD;

        int curr2 = leaf2;
        while (curr2 >= 1) {
            tree2_sum[curr2] = (tree2_sum[curr2] + X_a);
            if (tree2_sum[curr2] >= MOD) tree2_sum[curr2] -= MOD;
            modified_nodes.push_back(curr2);
            curr2 /= 2;
        }
    }

    long long cur_sum = 0;
    for (int i = mid; i < r; ++i) {
        int curr = L + i;
        long long w1 = 1;
        while (curr != u) {
            w1 = (w1 * curr) % MOD;
            curr /= 2;
        }

        int leaf2 = L + P[i] - 1;
        long long f_val = up_prod[leaf2];
        long long Y_b = (w1 * f_val) % MOD;

        int curr2 = leaf2;
        while (curr2 > 1) {
            int p = curr2 / 2;
            int sib = curr2 ^ 1;
            if (tree2_sum[sib] > 0) {
                long long term = (Y_b * G[p]) % MOD * tree2_sum[sib] % MOD;
                cur_sum = (cur_sum + term);
                if (cur_sum >= MOD) cur_sum -= MOD;
            }
            curr2 = p;
        }
    }

    ans = (ans + cur_sum % MOD * u) % MOD;

    for (int node : modified_nodes) {
        tree2_sum[node] = 0;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> H)) return 0;
    L = 1 << (H - 1);
    for (int i = 0; i < L; ++i) {
        cin >> P[i];
    }

    int total_nodes = 1 << H;
    up_prod[0] = 1;
    up_prod[1] = 1;
    for (int i = 2; i < total_nodes; ++i) {
        up_prod[i] = (up_prod[i / 2] * i) % MOD;
    }

    for (int v = 1; v < total_nodes; ++v) {
        int p = v / 2;
        long long denom = (1LL * v * (up_prod[p] * up_prod[p] % MOD)) % MOD;
        G[v] = modInverse(denom);
    }

    rec(1, 0, L);

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
