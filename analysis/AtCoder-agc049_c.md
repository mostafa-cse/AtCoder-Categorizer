# Problem Analysis: AtCoder-agc049_c — C. Robots

**Problem ID**: `AtCoder-agc049_c`  
**Contest**: `agc049`  
**Rating / Difficulty**: 2177  
**URL**: https://atcoder.jp/contests/agc049/tasks/agc049_c  
**VJudge Tag**: `[problem:AtCoder-agc049_c]`  
**Category File**: [`../categories/basics/robots_line_intervals_suffix_min_greedy.md`](../categories/basics/robots_line_intervals_suffix_min_greedy.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Robots start at coordinates A_i and move B_i steps left, destroying encountered robots. Avoid destroying Robot 0 with minimum ball modifications. Robots with B_j < A_j can safely destroy other robots without reaching 0. Dangerous robots (B_i >= A_i) must either be destroyed by a safe robot to their right, or modified by deleting B_i - A_i + 1 balls (which sweeps and destroys all robots to its left).

## 2. Core Observation & Invariant
A safe robot j (B_j < A_j) covers coordinate range [A_j - B_j, A_j - 1]. Precomputing suffix minimums min_{j > k, B_j < A_j} (A_j - B_j) identifies which dangerous robots are automatically covered. If we delete B_i - A_i + 1 balls from the rightmost modified dangerous robot i, it safely destroys all robots < A_i. The optimal answer is min over all dangerous i of max(B_i - A_i + 1, suffix_uncovered_dangerous[i + 1]).

## 3. Step-by-Step Algorithm
1. Precompute suff_min[j] = min_{idx >= j, B < A} (A - B) from right to left.
2. Identify uncovered dangerous robots: bad[k] = 1 iff B_k >= A_k and suff_min[k + 1] > A_k.
3. Compute suffix sums suff_bad[k] of uncovered dangerous robots.
4. Initialize answer to suff_bad[0] (case with 0 deletions, purely fixing balls).
5. For each dangerous robot i (B_i >= A_i), evaluate cost max(B_i - A_i + 1, suff_bad[i + 1]) and take the minimum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    long long INF = 2e18;
    vector<long long> suff_min(N + 1, INF);
    for (int j = N - 1; j >= 0; --j) {
        suff_min[j] = suff_min[j + 1];
        if (B[j] < A[j]) {
            suff_min[j] = min(suff_min[j], A[j] - B[j]);
        }
    }

    vector<int> bad(N, 0);
    for (int k = 0; k < N; ++k) {
        if (B[k] >= A[k]) {
            if (suff_min[k + 1] > A[k]) {
                bad[k] = 1;
            }
        }
    }

    vector<int> suff_bad(N + 1, 0);
    for (int k = N - 1; k >= 0; --k) {
        suff_bad[k] = suff_bad[k + 1] + bad[k];
    }

    long long ans = suff_bad[0];
    for (int i = 0; i < N; ++i) {
        if (B[i] >= A[i]) {
            long long cost = max(B[i] - A[i] + 1LL, (long long)suff_bad[i + 1]);
            ans = min(ans, cost);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
