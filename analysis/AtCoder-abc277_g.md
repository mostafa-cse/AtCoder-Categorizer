# Problem Analysis: AtCoder-abc277_g — G. Random Walk to Millionaire

**Problem ID**: `AtCoder-abc277_g`  
**Contest**: `abc277`  
**Rating / Difficulty**: 2491  
**URL**: https://atcoder.jp/contests/abc277/tasks/abc277_g  
**VJudge Tag**: `[problem:AtCoder-abc277_g]`  
**Category File**: [`../categories/math/random_walk_to_millionaire_level_transitions.md`](../categories/math/random_walk_to_millionaire_level_transitions.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
A token starts at vertex 1 with level $X = 0$. At each step, it moves uniformly at random to an adjacent vertex $v$. If $C_v = 0$, $X \leftarrow X + 1$. If $C_v = 1$, level is unchanged and you receive $X^2$ money. Track the state vector of expected values $(E[1], E[X], E[X^2])$ at each vertex across $K$ steps. When moving to a vertex with $C_v = 0$, expanding $(X + 1)^2 = X^2 + 2X + 1$ linearly transforms the expected values. Accumulate expected money reward whenever visiting $C_v = 1$ vertices.

## 2. Core Observation & Invariant
Because expectation is linear, knowing $E[1], E[X], E[X^2]$ at each vertex at step $t$ completely determines $E[1], E[X], E[X^2]$ at step $t + 1$. The transitions from all incoming edges average the state vectors, and applying the local level increment $(X + 1)$ shifts $E[X^2] \leftarrow E[X^2] + 2E[X] + E[1]$.

## 3. Step-by-Step Algorithm
1. 1. Precompute degrees and inverted degrees $deg[u]^{-1} \pmod{998244353}$.
2. 2. Maintain arrays $dp_0[u], dp_1[u], dp_2[u]$ for expected values $E[1], E[X], E[X^2]$ at vertex $u$. Initialize $dp_0[1] = 1$ and all other entries 0.
3. 3. For step $t = 1 \dots K$:
4.    a. For each vertex $u$, distribute its state scaled by $deg[u]^{-1}$ to all its neighbors.
5.    b. For each vertex $v$, if $C_v = 0$, update $dp_2[v] \leftarrow dp_2[v] + 2dp_1[v] + dp_0[v]$ and $dp_1[v] \leftarrow dp_1[v] + dp_0[v]$.
6.    c. If $C_v = 1$, add $dp_2[v]$ to the total expected reward.
7. 4. Output the accumulated expected money modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(K(N + M))`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

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

    int N, M, K;
    if (!(cin >> N >> M >> K)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> C(N + 1);
    for (int i = 1; i <= N; ++i) cin >> C[i];

    vector<long long> inv_deg(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        if (!adj[i].empty()) inv_deg[i] = modInverse(adj[i].size());
    }

    vector<long long> dp0(N + 1, 0), dp1(N + 1, 0), dp2(N + 1, 0);
    dp0[1] = 1;

    long long total_ans = 0;

    for (int step = 1; step <= K; ++step) {
        vector<long long> send0(N + 1), send1(N + 1), send2(N + 1);
        for (int u = 1; u <= N; ++u) {
            send0[u] = dp0[u] * inv_deg[u] % MOD;
            send1[u] = dp1[u] * inv_deg[u] % MOD;
            send2[u] = dp2[u] * inv_deg[u] % MOD;
        }

        vector<long long> P0(N + 1, 0), P1(N + 1, 0), P2(N + 1, 0);
        for (int u = 1; u <= N; ++u) {
            if (adj[u].empty()) continue;
            long long s0 = send0[u], s1 = send1[u], s2 = send2[u];
            for (int v : adj[u]) {
                P0[v] = (P0[v] + s0) % MOD;
                P1[v] = (P1[v] + s1) % MOD;
                P2[v] = (P2[v] + s2) % MOD;
            }
        }

        for (int v = 1; v <= N; ++v) {
            if (C[v] == 0) {
                dp0[v] = P0[v];
                dp1[v] = (P1[v] + P0[v]) % MOD;
                dp2[v] = (P2[v] + 2 * P1[v] + P0[v]) % MOD;
            } else {
                dp0[v] = P0[v];
                dp1[v] = P1[v];
                dp2[v] = P2[v];
                total_ans = (total_ans + dp2[v]) % MOD;
            }
        }
    }

    cout << total_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
