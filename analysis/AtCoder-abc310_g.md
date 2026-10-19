# Problem Analysis: AtCoder-abc310_g — Takahashi Takahashi

**Problem ID**: `AtCoder-abc310_g`  
**Contest**: `abc310`  
**Rating / Difficulty**: 2696  
**URL**: https://atcoder.jp/contests/abc310/tasks/abc310_g  
**VJudge Tag**: `[problem:AtCoder-abc310_g]`  
**Category File**: [`../categories/graph_theory/takahashi_pass_ball_binary_lifting.md`](../categories/graph_theory/takahashi_pass_ball_binary_lifting.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Lowest Common Ancestor (LCA)`  
- **Topic (Skill)**: `Binary Lifting and LCA`  

---

## 1. Problem Statement & Key Idea
Ball passing game on functional graph where each ball at node j visits f^1(j), f^2(j), ..., f^K(j). By linearity of expectation, each node i receives B_j / K whenever f^x(j) = i. Decomposing paths of length K into dyadic power-of-two jump intervals allows assigning tags to binary lifting intervals and pushing them down from 2^d to 2^{d-1} in O(N log K) time.

## 2. Core Observation & Invariant
A jump of length 2^d from u splits into a jump of length 2^{d-1} from u and a jump of length 2^{d-1} from f^{2^{d-1}}(u). Thus, any interval update on tree/functional paths decomposes dyadically and propagates downwards like a segment tree on powers of two.

## 3. Step-by-Step Algorithm
1. 1. Precompute doubling table to[d][u] for d = 0..60 and u = 1..N.
2. 2. For each node j = 1..N, decompose K into powers of two: for each bit b of K, add B_j to tag[b][curr] and advance curr = to[b][curr].
3. 3. Push tags down for d = 60 down to 1: add tag[d][u] to tag[d-1][u] and tag[d-1][to[d-1][u]].
4. 4. At d = 0, tag[0][u] adds to ans[to[0][u]].
5. 5. Multiply ans[i] by K^{-1} mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log K)`
- **Space Complexity**: `O(N log K)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<int> A(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> A[i];
    }

    vector<long long> B(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> B[i];
    }

    const int MAX_D = 61;
    vector<vector<int>> to(MAX_D, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        to[0][i] = A[i];
    }
    for (int d = 1; d < MAX_D; ++d) {
        for (int i = 1; i <= n; ++i) {
            to[d][i] = to[d - 1][to[d - 1][i]];
        }
    }

    vector<vector<long long>> tag(MAX_D, vector<long long>(n + 1, 0));

    for (int j = 1; j <= n; ++j) {
        int curr = j;
        for (int b = 0; b < MAX_D; ++b) {
            if ((k >> b) & 1LL) {
                tag[b][curr] = (tag[b][curr] + B[j]) % MOD;
                curr = to[b][curr];
            }
        }
    }

    for (int d = MAX_D - 1; d > 0; --d) {
        for (int u = 1; u <= n; ++u) {
            long long val = tag[d][u];
            if (val != 0) {
                tag[d - 1][u] = (tag[d - 1][u] + val) % MOD;
                int v = to[d - 1][u];
                tag[d - 1][v] = (tag[d - 1][v] + val) % MOD;
            }
        }
    }

    vector<long long> ans(n + 1, 0);
    for (int u = 1; u <= n; ++u) {
        long long val = tag[0][u];
        if (val != 0) {
            int v = to[0][u];
            ans[v] = (ans[v] + val) % MOD;
        }
    }

    long long invK = modInverse(k % MOD);
    for (int i = 1; i <= n; ++i) {
        long long res = (ans[i] * invK) % MOD;
        cout << res << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
