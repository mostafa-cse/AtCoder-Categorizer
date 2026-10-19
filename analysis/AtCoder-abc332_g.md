# Problem Analysis: AtCoder-abc332_g — G - Not Too Many Balls

**Problem ID**: `AtCoder-abc332_g`  
**Contest**: `abc332`  
**Rating / Difficulty**: 2775  
**URL**: https://atcoder.jp/contests/abc332/tasks/abc332_g  
**VJudge Tag**: `[problem:AtCoder-abc332_g]`  
**Category File**: [`../categories/graph_theory/bipartite_matching_min_cut_halls_marriage.md`](../categories/graph_theory/bipartite_matching_min_cut_halls_marriage.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Flow / Minimum Cut`  

---

## 1. Problem Statement & Key Idea
Given N ball types with supply A_i, and M box types with capacity B_j, at most i * j balls of type i can be placed into boxes of type j. Find the maximum total number of balls that can be placed.

## 2. Core Observation & Invariant
By the Max-Flow Min-Cut Theorem, maximum flow equals minimum s-t cut. In the bipartite flow network, let X_1 be the subset of left vertices cut to the source (paying sum_{i in X_1} A_i). If C = sum_{i in X_1} i, the residual capacity from X_1 to each right vertex j is C * j. Thus, each right vertex j contributes min(B_j, C * j) to the cut. The cut capacity for a chosen X_1 depends solely on C: Cut(X_1) = sum_{i in X_1} A_i + sum_{j=1}^M min(B_j, C * j). Since C <= N*(N+1)/2 <= 125,250, we can compute the minimum sum of A_i for each sum C using 0-1 knapsack DP, and precompute F(C) = sum_j min(B_j, C * j) using piecewise-linear prefix sum slopes.

## 3. Step-by-Step Algorithm
1. 1. Compute maximum possible sum C_max = N*(N+1)/2.
2. 2. Run 0-1 knapsack DP: dp[c] = min sum_{i in X_1} A_i for sum_{i in X_1} i = c.
3. 3. For F(C) = sum_{j=1}^M min(B_j, C * j), each term is linear with slope j for C <= floor(B_j / j), and constant B_j afterwards.
4. 4. Use slope difference arrays or prefix sums to compute F(C) for all C in 0..C_max in O(M + C_max) time.
5. 5. The minimum cut is min_{0 <= c <= C_max} (dp[c] + F(c)).

## 4. Complexity Analysis
- **Time Complexity**: `O(N * C_max + M + C_max) where C_max <= 125,250`
- **Space Complexity**: `O(C_max)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<long long> A(N + 1);
    long long sumA = 0;
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
        sumA += A[i];
    }

    vector<long long> B(M + 1);
    for (int j = 1; j <= M; ++j) {
        cin >> B[j];
    }

    int max_C = N * (N + 1) / 2;

    // dp[c] = max sum of A_i with sum of i = c
    vector<long long> dp(max_C + 1, -1);
    dp[0] = 0;
    int cur_max = 0;
    for (int i = 1; i <= N; ++i) {
        for (int c = cur_max; c >= 0; --c) {
            if (dp[c] != -1) {
                if (dp[c + i] < dp[c] + A[i]) {
                    dp[c + i] = dp[c] + A[i];
                }
            }
        }
        cur_max += i;
    }

    // F(C) = sum_{j=1}^M min(B_j, C * j)
    // For each box j: k_j = B_j / j, rem = B_j % j.
    // Step c from c-1 to c:
    // for 1 <= c <= k_j: delta is +j
    // for c = k_j + 1: delta is +rem
    // for c > k_j + 1: delta is 0
    vector<long long> diff(max_C + 5, 0);
    for (int j = 1; j <= M; ++j) {
        long long k_j = B[j] / j;
        long long rem = B[j] % j;

        diff[1] += j;
        if (k_j + 1 <= max_C + 3) {
            diff[k_j + 1] -= j;
            diff[k_j + 1] += rem;
        }
        if (k_j + 2 <= max_C + 3) {
            diff[k_j + 2] -= rem;
        }
    }

    vector<long long> F(max_C + 1, 0);
    long long cur_delta = 0;
    for (int c = 1; c <= max_C; ++c) {
        cur_delta += diff[c];
        F[c] = F[c - 1] + cur_delta;
    }

    long long min_cut = -1;
    for (int c = 0; c <= max_C; ++c) {
        if (dp[c] != -1) {
            long long cur_cut = (sumA - dp[c]) + F[c];
            if (min_cut == -1 || cur_cut < min_cut) {
                min_cut = cur_cut;
            }
        }
    }

    cout << min_cut << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
