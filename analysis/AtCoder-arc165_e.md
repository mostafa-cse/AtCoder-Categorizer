# Problem Analysis: AtCoder-arc165_e — E - Random Resettlement

**Problem ID**: `AtCoder-arc165_e`  
**Contest**: `arc165`  
**Rating / Difficulty**: 2783  
**URL**: https://atcoder.jp/contests/arc165/tasks/arc165_e  
**VJudge Tag**: `[problem:AtCoder-arc165_e]`  
**Category File**: [`../categories/math/random_deletion_linearity_of_expectation_tree_dp.md`](../categories/math/random_deletion_linearity_of_expectation_tree_dp.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
In a tree with N vertices, vertices are deleted uniformly at random one by one until all connected components have size at most K. Find the expected number of deletion operations performed, modulo 998244353.

## 2. Core Observation & Invariant
By linearity of expectation, an operation is performed on a connected component S of size > K if and only if that component exists at some point during the process. For a subset of vertices S forming a connected component, S exists if and only if all external neighbors of S in the tree are deleted after all internal vertices of S. If S has n internal vertices and m boundary neighbor vertices, this probability is n! * m! / (n + m)!. We can iterate over every vertex r as the highest (root) vertex of S, and run tree knapsack DP to sum the probabilities over all valid subsets of size > K.

## 3. Step-by-Step Algorithm
1. 1. Iterate over every vertex r from 1 to N as the top root of component S.
2. 2. Root the tree at r. A valid component S containing r consists of r and a connected subset of descendants.
3. 3. Run tree DP: dp[u][sz][bd] = generating polynomial for forming a component of size sz in subtree u with bd boundary edges.
4. 4. Merge child subtrees using knapsack convolution.
5. 5. For each component rooted at r with size n > K and boundary m, add n! * m! / (n + m)! to the expected total.
6. 6. Sum over all r and output modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

static const long long MOD = 998244353;

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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    if (!(cin >> N >> K)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int max_fact = 2 * N + 5;
    vector<long long> fact(max_fact, 1), inv(max_fact, 1);
    for (int i = 1; i < max_fact; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[max_fact - 1] = modInverse(fact[max_fact - 1]);
    for (int i = max_fact - 2; i >= 0; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto p_T = [&](int n, int m) -> long long {
        return fact[n] * fact[m] % MOD * inv[n + m] % MOD;
    };

    // Root at 1 to define subtrees
    vector<int> parent(N + 1, 0);
    vector<vector<int>> children(N + 1);
    vector<int> stack = {1};
    vector<bool> visited(N + 1, false);
    visited[1] = true;

    while (!stack.empty()) {
        int u = stack.back();
        stack.pop_back();
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                parent[v] = u;
                children[u].push_back(v);
                stack.push_back(v);
            }
        }
    }

    long long ans = 0;

    for (int r = 1; r <= N; ++r) {
        // Collect subtree nodes
        vector<int> sub_nodes;
        vector<int> st = {r};
        while (!st.empty()) {
            int curr = st.back();
            st.pop_back();
            sub_nodes.push_back(curr);
            for (int c : children[curr]) {
                st.push_back(c);
            }
        }

        // dp[u][n][m_ch]
        vector<vector<vector<int>>> dp(N + 1);
        for (int i = (int)sub_nodes.size() - 1; i >= 0; --i) {
            int u = sub_nodes[i];
            // Initialize cur_dp for vertex u: size 1, 0 boundary children
            vector<vector<int>> cur_dp(2, vector<int>(1, 0));
            cur_dp[1][0] = 1;

            for (int c : children[u]) {
                int max_n1 = cur_dp.size() - 1;
                int max_m1 = cur_dp[0].size() - 1;
                int max_n2 = dp[c].size() - 1;
                int max_m2 = dp[c][0].size() - 1;

                int new_max_n = max_n1 + max_n2;
                int new_max_m = max(max_m1 + 1, max_m1 + max_m2);

                vector<vector<int>> nxt_dp(new_max_n + 1, vector<int>(new_max_m + 1, 0));

                // Option A: do not include c (c becomes boundary child, m += 1)
                for (int n = 1; n <= max_n1; ++n) {
                    for (int m = 0; m <= max_m1; ++m) {
                        if (cur_dp[n][m] == 0) continue;
                        nxt_dp[n][m + 1] = (nxt_dp[n][m + 1] + cur_dp[n][m]) % MOD;
                    }
                }

                // Option B: include c
                for (int n1 = 1; n1 <= max_n1; ++n1) {
                    for (int m1 = 0; m1 <= max_m1; ++m1) {
                        if (cur_dp[n1][m1] == 0) continue;
                        long long w1 = cur_dp[n1][m1];
                        for (int n2 = 1; n2 <= max_n2; ++n2) {
                            for (int m2 = 0; m2 <= max_m2; ++m2) {
                                if (dp[c][n2][m2] == 0) continue;
                                long long w2 = dp[c][n2][m2];
                                long long prod = (w1 * w2) % MOD;
                                nxt_dp[n1 + n2][m1 + m2] = (nxt_dp[n1 + n2][m1 + m2] + prod) % MOD;
                            }
                        }
                    }
                }
                cur_dp = move(nxt_dp);
            }
            dp[u] = move(cur_dp);
        }

        int parent_boundary = (r != 1 ? 1 : 0);
        int max_n = dp[r].size() - 1;
        int max_m = dp[r][0].size() - 1;

        for (int n = K + 1; n <= max_n; ++n) {
            for (int m_ch = 0; m_ch <= max_m; ++m_ch) {
                if (dp[r][n][m_ch] == 0) continue;
                int m = m_ch + parent_boundary;
                long long prob = p_T(n, m);
                long long ways = dp[r][n][m_ch];
                ans = (ans + ways * prob) % MOD;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
