# Problem Analysis: AtCoder-arc170_c — Prefix Mex Sequence

**Problem ID**: `AtCoder-arc170_c`  
**Contest**: `arc170`  
**Rating / Difficulty**: 2028  
**URL**: https://atcoder.jp/contests/arc170/tasks/arc170_c  
**VJudge Tag**: `[problem:AtCoder-arc170_c]`  
**Category File**: [`../categories/dynamic_programming/prefix_mex_sequence_cardinality_dp.md`](../categories/dynamic_programming/prefix_mex_sequence_cardinality_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Prefix MEX Sequence State Tracking via Cardinality DP`  

---

## 1. Problem Statement & Key Idea
Given a sequence S of length N where S_i in {0, 1}, and integer M. Count sequences A of length N with elements in [0, M] such that for each i, S_i = 1 iff A_i = MEX(A_1 ... A_{i-1}). Output mod 998244353.

**Key Idea**: The prefix MEX depends only on the cardinality j of distinct values from {0, ..., M} present so far. If j distinct values are present: when S_i = 1, A_i must equal the current MEX (exactly 1 choice), increasing the present set size to j + 1. When S_i = 0, A_i must not equal the current MEX: we can either choose one of the j already present values (j choices, size remains j), or choose one of the remaining non-MEX values in [0, M] (M + 1 - j - 1 = M - j choices, size increases to j + 1). DP state: dp[i][j] = ways for prefix i with j distinct elements.

## 2. Core Observation & Invariant
MEX dynamics depend purely on the number of occupied slots in the value alphabet rather than individual coordinates.

## 3. Step-by-Step Algorithm
1. Initialize dp[0][0] = 1.
2. For i from 0 to N - 1:
3.   For j from 0 to min(i, M + 1):
4.     if dp[i][j] == 0: continue;
5.     if S[i] == 1:
6.       // A_i must be MEX: 1 choice, j -> j + 1
7.       dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD;
8.     else:
9.       // S[i] == 0: A_i != MEX
10.       // 1. Choose from already present values: j choices
11.       dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * j) % MOD;
12.       // 2. Choose from unused values > MEX: max(0, M - j) choices
13.       if (j < M): dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j] * (M - j)) % MOD;
14. Print sum_{j} dp[N][j] mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * min(N, M))`
- **Space Complexity**: `O(min(N, M))`

## 5. Core Algorithmic Skill & Learning Takeaway
Prefix MEX tracking via state size cardinality representation.

**Reusable Pattern**: MEX Cardinality DP: Representing the seen prefix set by its size j, splitting transitions into seen (size j) vs unseen (size j + 1).

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }

    int max_j = min(n + 1, m + 1);
    vector<long long> dp(max_j + 1, 0);
    dp[0] = 1;

    for (int i = 0; i < n; ++i) {
        vector<long long> next_dp(max_j + 1, 0);

        for (int j = 0; j <= max_j; ++j) {
            if (dp[j] == 0) continue;

            if (s[i] == 1) {
                // Must pick MEX
                if (j + 1 <= max_j) {
                    next_dp[j + 1] = (next_dp[j + 1] + dp[j]) % MOD;
                }
            } else {
                // Must not pick MEX
                // 1. Pick from j already used numbers
                next_dp[j] = (next_dp[j] + dp[j] * j) % MOD;

                // 2. Pick an unused number != MEX: there are max(0, M - j) choices
                if (j < m && j + 1 <= max_j) {
                    next_dp[j + 1] = (next_dp[j + 1] + dp[j] * (m - j)) % MOD;
                }
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int j = 0; j <= max_j; ++j) {
        ans = (ans + dp[j]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
