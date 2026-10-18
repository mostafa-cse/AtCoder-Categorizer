# Problem Analysis: AtCoder-agc032_d — D. Rotation Sort

**Problem ID**: `AtCoder-agc032_d`  
**Contest**: `agc032`  
**Rating / Difficulty**: 2602  
**URL**: https://atcoder.jp/contests/agc032/tasks/agc032_d  
**VJudge Tag**: `[problem:AtCoder-agc032_d]`  
**Category File**: [`../categories/dynamic_programming_dp/rotation_sort_weighted_lis.md`](../categories/dynamic_programming_dp/rotation_sort_weighted_lis.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Longest Increasing Subsequence (LIS)`  

---

## 1. Problem Statement & Key Idea
Given a permutation P of 1 to N, pay A to cyclic shift any subarray [l, r] left (moving p_l to the right), or pay B to shift [l, r] right (moving p_r to the left). Find the minimum cost to sort P.

## 2. Core Observation & Invariant
The elements that never move must form an increasing subsequence. For any element between two preserved elements P_j < P_i: if P_k < P_j, it must move left (cost B); if P_k > P_i, it must move right (cost A); otherwise, it moves at cost min(A, B). This cost decomposes into (i - 1 - j) * min(A, B) plus |A - B| times the count of elements on the heavier side.

## 3. Step-by-Step Algorithm
1. Add sentinels P_0 = 0 and P_{N+1} = N+1. Maintain DP[i] as the minimum cost to sort the prefix such that P_i is unmoved.
2. If A >= B: for each i, decrement j from i-1 down to 0, maintaining count of P_k > P_i in O(1) per step.
3. If B > A: push DP transitions from j to all i > j, maintaining count of P_k < P_j in O(1) per step.
4. Output DP[N+1].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long A, B;
    if (!(cin >> N >> A >> B)) return 0;

    vector<int> P(N + 2);
    P[0] = 0;
    for (int i = 1; i <= N; ++i) {
        cin >> P[i];
    }
    P[N + 1] = N + 1;

    const long long INF = 1e18;
    vector<long long> dp(N + 2, INF);
    dp[0] = 0;

    if (A >= B) {
        for (int i = 1; i <= N + 1; ++i) {
            long long cnt_greater = 0;
            for (int j = i - 1; j >= 0; --j) {
                if (P[j] < P[i]) {
                    long long cost = (long long)(i - 1 - j) * B + (A - B) * cnt_greater;
                    dp[i] = min(dp[i], dp[j] + cost);
                }
                if (P[j] > P[i]) {
                    cnt_greater++;
                }
            }
        }
    } else {
        for (int j = 0; j <= N; ++j) {
            if (dp[j] == INF) continue;
            long long cnt_smaller = 0;
            for (int i = j + 1; i <= N + 1; ++i) {
                if (P[j] < P[i]) {
                    long long cost = (long long)(i - 1 - j) * A + (B - A) * cnt_smaller;
                    dp[i] = min(dp[i], dp[j] + cost);
                }
                if (P[i] < P[j]) {
                    cnt_smaller++;
                }
            }
        }
    }

    cout << dp[N + 1] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
