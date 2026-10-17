# Problem Analysis: AtCoder-arc107_d — Number of Multisets

**Problem ID**: `AtCoder-arc107_d`  
**Contest**: `arc107`  
**Rating / Difficulty**: 2096  
**URL**: https://atcoder.jp/contests/arc107/tasks/arc107_d  
**VJudge Tag**: `[problem:AtCoder-arc107_d]`  
**Category File**: [`../categories/dynamic_programming/power_of_half_multiset_partition_dp.md`](../categories/dynamic_programming/power_of_half_multiset_partition_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `More Tricks`  
- **Topic (Skill)**: `x2 +1 Trick`  

---

## 1. Problem Statement & Key Idea
Find the number of multisets of size N consisting of powers of 1/2 (i.e. elements from {1, 1/2, 1/4, 1/8, ...}) such that the sum of the elements is K, modulo 998244353.

**Key Insight**: Let dp[n][k] be the number of multisets of size n summing to k. We can classify multisets based on whether they contain at least one element equal to 1. If it contains at least one 1: remove that 1, leaving a multiset of size n - 1 summing to k - 1, which gives dp[n - 1][k - 1]. If it contains NO 1s: every element in the multiset is <= 1/2. If we multiply every element by 2, we obtain a multiset of size n whose elements are powers of 1/2 summing to 2k! Thus, the second case gives dp[n][2k]. Putting these together gives the recurrence: dp[n][k] = dp[n - 1][k - 1] + dp[n][2k] (with base cases dp[0][0] = 1, and dp[n][k] = 0 for k > n).

## 2. Core Observation & Invariant
Multisets of powers of 1/2 can be partitioned into those containing 1 (subtract 1) and those containing only <= 1/2 (multiply all elements by 2, doubling the sum).

## 3. Step-by-Step Algorithm
1. Initialize dp table of size (N + 1) x (N + 1) with zeros, dp[0][0] = 1.
2. For n from 1 to N:
3.   For k from n down to 1:
4.     dp[n][k] = dp[n - 1][k - 1];
5.     if (2 * k <= n) dp[n][k] = (dp[n][k] + dp[n][2 * k]) % MOD;
6. Output dp[N][K].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Doubling transition and peeling the maximum element in multiset power partition DP.
- **Reusable Pattern**: Multiset partitions over negative powers of 2 reduce to dp[n][k] = dp[n-1][k-1] + dp[n][2k] by doubling all elements.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k > n || k <= 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
    dp[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = i; j >= 1; --j) {
            dp[i][j] = dp[i - 1][j - 1];
            if (2 * j <= i) {
                dp[i][j] = (dp[i][j] + dp[i][2 * j]) % MOD;
            }
        }
    }

    cout << dp[n][k] << "\n";
    return 0;
}
```
