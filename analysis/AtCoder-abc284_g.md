# Problem Analysis: AtCoder-abc284_g — Only Once

**Problem ID**: `AtCoder-abc284_g`  
**Contest**: `abc284`  
**Rating / Difficulty**: 2218  
**URL**: https://atcoder.jp/contests/abc284/tasks/abc284_g  
**VJudge Tag**: `[problem:AtCoder-abc284_g]`  
**Category File**: [`../categories/combinatorics/only_once_functional_graph_walk_falling_factorials.md`](../categories/combinatorics/only_once_functional_graph_walk_falling_factorials.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
Compute the sum over all N^N functional graphs f: [1, N] -> [1, N] of the number of elements that appear exactly once in the walk starting at each vertex i.

## 2. Core Observation & Invariant
By symmetry, every starting vertex i contributes identically to the total sum. For vertex 1, a walk v_1, ..., v_l repeats for the first time when f(v_l) loops back to some v_r (1 <= r <= l). Elements appearing exactly once are v_1, ..., v_{r-1}, totaling r - 1 elements. Summing r - 1 over all l loopback positions yields l(l - 1) / 2. Each path of length l has P(N - 1, l - 1) * N^{N - l} completions, leading to an O(N) closed summation.

## 3. Step-by-Step Algorithm
1. 1. Precompute powers N^k mod M for k in [0, N].
2. 2. Maintain falling factorial P(N - 1, l - 1) incrementally in O(1) per step.
3. 3. For each path length l from 1 to N, calculate ways = P(N - 1, l - 1) * N^{N - l} mod M and weight = l(l - 1) / 2 mod M.
4. 4. Accumulate ways * weight over all l, and multiply by N^2 mod M (or N * sum).

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> pw(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        pw[i] = (pw[i - 1] * (n % m)) % m;
    }

    long long total = 0;
    long long p = 1; // P(n - 1, l - 1)
    for (long long l = 1; l <= n; l++) {
        long long ways = (p * pw[n - l]) % m;
        long long weight = ((l * (l - 1) / 2) % m);
        total = (total + ways * weight) % m;
        p = (p * ((n - l) % m)) % m;
    }

    long long ans = (total * (n % m)) % m;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
