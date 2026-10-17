# Problem Analysis: AtCoder-abc328_g — G. Cut and Reorder

**Problem ID**: `AtCoder-abc328_g`  
**Contest**: `abc328`  
**Rating / Difficulty**: 2193  
**URL**: https://atcoder.jp/contests/abc328/tasks/abc328_g  
**VJudge Tag**: `[problem:AtCoder-abc328_g]`  
**Category File**: [`../categories/dynamic_programming/contiguous_subsegment_reordering_bitmask_dp.md`](../categories/dynamic_programming/contiguous_subsegment_reordering_bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Partition sequence B into contiguous segments, each matching an unused contiguous subsegment A[l..r]. Mask S tracks elements of A already used; k = popcount(S) indicates the next prefix of B being filled. We iterate over unused contiguous ranges [l..r] in O(N * 2^N) total operations.

## 2. Core Observation & Invariant
Any partition of B into contiguous pieces of A can be achieved in a single cut-and-rearrange operation costing (X-1)C. Since segments [l..r] can be extended while bits r are not in S, the total number of transitions across all masks is sum_{L=1}^N (N - L + 1) 2^{N-L} = O(N * 2^N) approx 8.8e7 ops, easily running in 0.15s.

## 3. Step-by-Step Algorithm
1. Initialize dp[0] = 0, all other dp[S] = INF.
2. For S from 0 to 2^N - 1:
3.   If dp[S] == INF, continue. Let k = popcount(S).
4.   For each l from 0 to N - 1 with bit l not in S:
5.     cur_cost = dp[S] + (S == 0 ? 0 : C), mask = S.
6.     For r from l to N - 1:
7.       If S & (1 << r), break.
8.       cur_cost += abs(A[r] - B[k + (r - l)]), mask |= (1 << r).
9.       dp[mask] = min(dp[mask], cur_cost).
10. Output dp[2^N - 1].

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const long long INF = 4e18;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long C;
    if (!(cin >> N >> C)) return 0;

    vector<long long> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    int total_masks = 1 << N;
    vector<long long> dp(total_masks, INF);
    dp[0] = 0;

    for (int S = 0; S < total_masks; ++S) {
        if (dp[S] == INF) continue;
        int k = __builtin_popcount(S);
        for (int l = 0; l < N; ++l) {
            if (S & (1 << l)) continue;
            long long cur_cost = dp[S] + (S == 0 ? 0 : C);
            int mask = S;
            for (int r = l; r < N; ++r) {
                if (S & (1 << r)) break;
                cur_cost += abs(A[r] - B[k + (r - l)]);
                mask |= (1 << r);
                if (cur_cost < dp[mask]) {
                    dp[mask] = cur_cost;
                }
            }
        }
    }

    cout << dp[total_masks - 1] << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
