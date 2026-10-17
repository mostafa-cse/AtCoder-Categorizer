# Problem Analysis: AtCoder-abc425_g — Sum of Min of XOR

**Problem ID**: `AtCoder-abc425_g`  
**Contest**: `abc425`  
**Rating / Difficulty**: 2205  
**URL**: https://atcoder.jp/contests/abc425/tasks/abc425_g  
**VJudge Tag**: `[problem:AtCoder-abc425_g]`  
**Category File**: [`../categories/data_structures/sum_of_min_of_xor_trie_canonical_subcube_dp.md`](../categories/data_structures/sum_of_min_of_xor_trie_canonical_subcube_dp.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Trie`  
- **Topic (Skill)**: `Trie on Strings and Bits`  

---

## 1. Problem Statement & Key Idea
Binary Trie DP precalculating subtree minimum XOR sums over complete subcubes combined with canonical prefix decomposition of [0, M-1].

## 2. Core Observation & Invariant
For any subtree u at bit level b, the sum of min_{y in u} (z ^ y) as z ranges freely over all 2^b values is purely a structural property of subtree u: F(u, b) = F(L, b-1) + F(R, b-1) if both exist, or 2*F(child, b-1) + 2^(2b-2) if only one child exists.

## 3. Step-by-Step Algorithm
1. 1. Insert all A_i into a binary trie of depth 30.
2. 2. Post-order DFS computes F(u, b) for every trie node in O(N * 30).
3. 3. Decompose [0, M-1] into at most 30 canonical subcubes matching the binary digits of M.
4. 4. When bit b of M is 1, branch x = 0 gives a complete subcube of size 2^b, adding V * 2^b + F(child) to answer; then proceed with bit b of x set to 1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max A) + log M)`
- **Space Complexity**: `O(N log(max A))`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAX_NODES = 200000 * 32;
int ch[MAX_NODES][2];
ll F[MAX_NODES];
int node_cnt = 1;

void insert(int val) {
    int u = 1;
    for (int b = 29; b >= 0; --b) {
        int bit = (val >> b) & 1;
        if (!ch[u][bit]) {
            ch[u][bit] = ++node_cnt;
        }
        u = ch[u][bit];
    }
}

// Compute F(u, b) bottom-up
void dfs_f(int u, int b) {
    if (b == 0) {
        F[u] = 0;
        return;
    }
    int l = ch[u][0], r = ch[u][1];
    if (l) dfs_f(l, b - 1);
    if (r) dfs_f(r, b - 1);

    if (l && r) {
        F[u] = F[l] + F[r];
    } else if (l) {
        F[u] = 2 * F[l] + (1LL << (2 * (b - 1)));
    } else if (r) {
        F[u] = 2 * F[r] + (1LL << (2 * (b - 1)));
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    ll M;
    if (!(cin >> N >> M)) return 0;

    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a;
        insert(a);
    }

    dfs_f(1, 30);

    ll ans = 0;
    int u = 1;
    ll V = 0;

    for (int b = 29; b >= 0; --b) {
        int m_bit = (M >> b) & 1;
        if (m_bit == 1) {
            // Branch 1: set bit b of x to 0
            if (ch[u][0]) {
                ans += V * (1LL << b) + F[ch[u][0]];
            } else {
                ans += (V + (1LL << b)) * (1LL << b) + F[ch[u][1]];
            }

            // Branch 2: set bit b of x to 1, continue down
            if (ch[u][1]) {
                u = ch[u][1];
            } else {
                u = ch[u][0];
                V += (1LL << b);
            }
        } else {
            // Must set bit b of x to 0, continue down
            if (ch[u][0]) {
                u = ch[u][0];
            } else {
                u = ch[u][1];
                V += (1LL << b);
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
