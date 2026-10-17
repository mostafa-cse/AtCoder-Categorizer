# Problem Analysis: AtCoder-arc187_b — Sum of CC

**Problem ID**: `AtCoder-arc187_b`  
**Contest**: `arc187`  
**Rating / Difficulty**: 2026  
**URL**: https://atcoder.jp/contests/arc187/tasks/arc187_b  
**VJudge Tag**: `[problem:AtCoder-arc187_b]`  
**Category File**: [`../categories/combinatorics/connected_component_boundary_independence_expectation.md`](../categories/combinatorics/connected_component_boundary_independence_expectation.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Linearity of Expectation`  
- **Topic (Skill)**: `Connected Component Boundary Independence and Linearity of Expectation`  

---

## 1. Problem Statement & Key Idea
Given array B of length N with elements in [1, M] or -1. Replace -1s with integers in [1, M] uniformly at random. Build graph with directed edges i -> j for i < j iff A_i <= A_j. Find sum of connected components f(A) over all M^(count -1) sequences, mod 998244353.

**Key Idea**: In this graph, no edges exist between prefix 1 ... i and suffix i+1 ... N if and only if min_{x <= i} A_x > max_{y > i} A_y. Each such boundary cleanly separates components! By Linearity of Expectation, the total number of connected components is 1 + sum_{i=1}^{N-1} [min(A_1 ... A_i) > max(A_{i+1} ... A_N)]. For each boundary i, the event min(prefix) > max(suffix) decouples: iterating over value v in [1, M], count ways where min(prefix) >= v and max(suffix) < v. Prefix choices (>= v) and suffix choices (< v) are completely independent and precomputed in O(N M).

## 2. Core Observation & Invariant
Graph component cut boundaries are equivalent to min(prefix) > max(suffix), decoupling across the boundary for independent polynomial counting.

## 3. Step-by-Step Algorithm
1. Precompute pref_ways[i][v]: number of completions of B[1 .. i] such that min >= v.
2.   For each position i, if B[i] == -1, choices is M - v + 1; if B[i] != -1, choices is (B[i] >= v ? 1 : 0).
3. Precompute suff_ways[i][v]: number of completions of B[i .. N] such that max < v.
4.   For each position i, if B[i] == -1, choices is v - 1; if B[i] != -1, choices is (B[i] < v ? 1 : 0).
5. Total ways = M^(count of -1 in B).
6. ans = total_ways (the 1st component for every sequence).
7. For each boundary i from 1 to N - 1:
8.   For each v from 2 to M:
9.     ans = (ans + (pref_ways[i][v] - pref_ways[i][v + 1]) * suff_ways[i + 1][v]) % MOD (where min(prefix) == v and max(suffix) < v).
10. Print ans mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(N * M)`

## 5. Core Algorithmic Skill & Learning Takeaway
Linearity of expectation on component boundaries with decoupled prefix-suffix conditions.

**Reusable Pattern**: Boundary Cut Linearity: Components = 1 + sum_{i=1}^{N-1} I(min(pref) > max(suff)), calculated via value sweep.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> b(n + 1);
    int total_wildcards = 0;
    for (int i = 1; i <= n; ++i) {
        cin >> b[i];
        if (b[i] == -1) total_wildcards++;
    }

    // pref[i][v]: completions of 1..i where all elements >= v
    vector<vector<long long>> pref(n + 1, vector<long long>(m + 2, 0));
    for (int v = 1; v <= m + 1; ++v) pref[0][v] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int v = 1; v <= m + 1; ++v) {
            long long choices = 0;
            if (b[i] == -1) {
                choices = max(0, m - v + 1);
            } else {
                choices = (b[i] >= v ? 1 : 0);
            }
            pref[i][v] = (pref[i - 1][v] * choices) % MOD;
        }
    }

    // suff[i][v]: completions of i..n where all elements < v
    vector<vector<long long>> suff(n + 2, vector<long long>(m + 2, 0));
    for (int v = 1; v <= m + 1; ++v) suff[n + 1][v] = 1;

    for (int i = n; i >= 1; --i) {
        for (int v = 1; v <= m + 1; ++v) {
            long long choices = 0;
            if (b[i] == -1) {
                choices = max(0, v - 1);
            } else {
                choices = (b[i] < v ? 1 : 0);
            }
            suff[i][v] = (suff[i + 1][v] * choices) % MOD;
        }
    }

    long long total_sequences = pref[n][1];
    long long ans = total_sequences;

    // For each boundary i in 1 .. n - 1:
    // A cut occurs if min(pref) >= v and max(suff) < v for some v
    // Equivalently: sum over v from 2 to m of (pref[i][v] - pref[i][v+1]) * suff[i+1][v]
    for (int i = 1; i < n; ++i) {
        for (int v = 2; v <= m; ++v) {
            long long min_is_v = (pref[i][v] - pref[i][v + 1] + MOD) % MOD;
            long long max_less_v = suff[i + 1][v];
            long long ways = (min_is_v * max_less_v) % MOD;
            ans = (ans + ways) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
