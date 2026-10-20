# Problem Analysis: AtCoder-agc006_c — C - Rabbit Exercise

**Problem ID**: `AtCoder-agc006_c`  
**Contest**: `agc006`  
**Rating / Difficulty**: 2996  
**URL**: https://atcoder.jp/contests/agc006/tasks/agc006_c  
**VJudge Tag**: `[problem:AtCoder-agc006_c]`  
**Category File**: [`../categories/math/rabbit_jump_expectation_linearity_permutation_cycle_power.md`](../categories/math/rabbit_jump_expectation_linearity_permutation_cycle_power.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Matrices`  
- **Topic (Skill)**: `Matrix Exponentiation`  

---

## 1. Problem Statement & Key Idea
N rabbits start at positions x_1 < ... < x_N. At each step, a chosen rabbit jumps across one of its neighbors with equal probability. Find expected final positions after repeating a pattern of M jumps K times.

## 2. Core Observation & Invariant
By linearity of expectation, jumping across a neighbor updates expected coordinate to x'_i = x_{i-1} + x_{i+1} - x_i. Considering differences d_i = x_{i+1} - x_i, this jump simply swaps d_{i-1} and d_i! The entire sequence of M jumps is therefore a single permutation sigma on the difference array. Computing sigma^K via cycle decomposition in O(N) yields the exact final differences and positions.

## 3. Step-by-Step Algorithm
1. 1. Compute initial difference array d_i = x_{i+1} - x_i for i = 1 to N-1.
2. 2. Represent the sequence of M jumps as a permutation sigma on indices 1 to N-1, where jump a_j swaps adjacent elements.
3. 3. Compute sigma^K in O(N) using disjoint cycle decomposition and cycle length modulo.
4. 4. Apply sigma^K to the initial difference array.
5. 5. Recover expected coordinates via prefix sums: x_i = x_1 + \sum_{j=1}^{i-1} d'_j.
6. 6. Output coordinates with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> x(N);
    for (int i = 0; i < N; ++i) {
        cin >> x[i];
    }

    int M;
    long long K;
    cin >> M >> K;

    vector<int> p(N - 1);
    for (int i = 0; i < N - 1; ++i) {
        p[i] = i;
    }

    for (int j = 0; j < M; ++j) {
        int a;
        cin >> a;
        --a; // a is 1-indexed, rabbit a jumps, swapping difference a-1 and a
        int idx = a - 1;
        swap(p[idx], p[idx + 1]);
    }

    // p maps current position in diff array to original position
    // After 1 set: d_new[i] = d_old[p[i]]
    // Decompose permutation p into cycles to compute p^K
    vector<int> p_final(N - 1);
    vector<bool> vis(N - 1, false);

    for (int i = 0; i < N - 1; ++i) {
        if (!vis[i]) {
            vector<int> cycle;
            int cur = i;
            while (!vis[cur]) {
                vis[cur] = true;
                cycle.push_back(cur);
                cur = p[cur];
            }
            int L = cycle.size();
            int shift = K % L;
            for (int k = 0; k < L; ++k) {
                p_final[cycle[k]] = cycle[(k + shift) % L];
            }
        }
    }

    vector<long long> d(N - 1);
    for (int i = 0; i < N - 1; ++i) {
        d[i] = x[i + 1] - x[i];
    }

    vector<long long> d_final(N - 1);
    for (int i = 0; i < N - 1; ++i) {
        d_final[i] = d[p_final[i]];
    }

    vector<long long> ans(N);
    ans[0] = x[0];
    for (int i = 1; i < N; ++i) {
        ans[i] = ans[i - 1] + d_final[i - 1];
    }

    cout << fixed << setprecision(1);
    for (int i = 0; i < N; ++i) {
        cout << (double)ans[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
